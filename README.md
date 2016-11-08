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
