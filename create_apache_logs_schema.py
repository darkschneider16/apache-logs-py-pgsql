#!/usr/bin/python
# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from apachelogs import Base
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('-host', help='Database host')
parser.add_argument('-user', help='Databse user')
parser.add_argument('-port', help='Database port')
parser.add_argument('-database', required=True, help='Database name')
parser.set_defaults(host='localhost', user='postgres', port='5432')
args = parser.parse_args()

# We open the connection with the main ddbb
db = create_engine('postgresql://' + args.user + '@' + args.host + ':' +
    args.port + '/' + args.database)
Base.metadata.bind = db
Base.metadata.create_all(db)
DBSession = sessionmaker(bind=db)
session = DBSession()

# Commit the session
session.commit()
