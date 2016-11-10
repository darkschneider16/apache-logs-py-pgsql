# apache-logs-py-pgsql
A way to dump apache logs with python sqlalchemy into a postgresql server
## Pre-requisites
The script is tested with python 3.5. I recommend the use of a virtual environment. If you have a debian sytem you can do the next:
```
# apt install python-virtualenv
```
And, in order to create this isolated zone you have to do this, as a regular user:
```
$ virtualenv -p /usr/bin/python3.5 venvpy35
```
After that you can activate the cage and control the packages inside it without the need of being root:
```
$ source venvpy35/bin/activate
(venvpy35) $ pip install sqlalchemy psycopg2
```
With these packages we can use our scripts.
## Creation of the Database Schema
First of all we have to create the schema in the database. Of course you must have created the database, with a fresh postgresql installation you only have to do this:
```
# su - postgres
$ createdb apache_logs
```
With an empty database we can create the table which stores the data from our logs:
```
(venvpy35) $ python create_apache_logs_schema.py -database apache_logs
```
If you connect to your database will see the table *apache_log* created:
```
$ psql -U postgres apache_logs
psql (9.6.1)
Digite «help» para obtener ayuda.

apache_logs=# \d apache_log
                       Tabla «public.apache_log»
         Columna         |            Tipo             | Modificadores 
-------------------------+-----------------------------+---------------
 id_apache_log           | integer                     | not null
 server_name             | character varying           | 
 port                    | integer                     | 
[...]
```
## Adding some data
In the project we have an example file with 50 lines from a real apache log, with changed information, of course. We can add this line to our database with the next command and consult it:
```
(venvpy35) $ python add_logs_apache.py -database apache_logs -log access_reduced.log.bz2
(venvpy35) $ psql -U postgres apache_logs
psql (9.6.1)
Digite «help» para obtener ayuda.

apache_logs=# select count(*) from apache_log where status = 200;
 count 
-------
    48
(1 fila)
```
## Notes
The scripts are based on the python class *ApacheLog* defined in the file *apachelog.py*. In the same file you can find another class, commented out, which uses *SQLite3* instead *PostgreSQL*. You can explore this class as well.

In terms of performance i must admit that with a file with four million lines, one day in the life of my company's main apache the queries suffer from a serious delay. You can create an index over the table and the performance improves, but when you load a bunch of days we fall in the same kind of delays.

I have a script to break the files in several parts and launch the *add_logs_apache.py* script *n* times simultaneosly when *n* is the number of cores which the host running the database has.

If you explore the apache log example and the python class that we are using, you've come to the conclusion that the python class and the format of the log are extremely bonded and you're right. I've not developed a more flexible approach because the project is served well to me as is. The configuration of the log in apache is shown below:
```
# LogFormats
LogFormat "%V\t%p\t[%{outstream}n/%{instream}n(%{ratio}n%%)]\t%a\t%t\t%m\t%U\t%q\t%H\t%s\t%B\t\"%{Referer}i\"\t\"%{User-agent}i\"\t%{Cookie}i\t%{Accept-Language}i\t%{Content-Language}o\t%{Accept-Encoding}i\t%{Content-Encoding}o\t%{Content-Location}o\t%{Vary}o\t%{Content-Type}o\t%{BALANCER_SESSION_STICKY}e\t%{BALANCER_SESSION_ROUTE}e\t%{MYCOOKIE}C\t%{BALANCER_WORKER_ROUTE}e\t%{BALANCER_ROUTE_CHANGED}e\t%D" combined
```
## Future
I'd like to explore the possibility of using the modern jsonb tuples in the Python class in order to see if i can improve the performance and the manageability of the queries.

Talking of performance i'd like to test the new parallel capabilities of *PostgreSQL 9.6* too.
