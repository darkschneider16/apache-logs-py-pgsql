# apache-logs-py-pgsql
A way to dump apache logs with python sqlalchemy into a postgresql server

## Creation of the Database Schema

First of all we have to create the schema in the database. Of course you must have created the database:

```
# su - postgres
$ createdb apache_logs
```
