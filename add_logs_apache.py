#!/usr/bin/python
# -*- coding: utf-8 -*-

import bz2
import argparse
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from apachelogs import ApacheLog, Base
import ipaddress


# To check if an ip address is valid
def valid_ip(address):
    try:
        int(ipaddress.ip_address(address))
        return True
    except:
        return False

# We parse the arguments from the command line
parser = argparse.ArgumentParser()
parser.add_argument('-host', help='Database host')
parser.add_argument('-user', help='Databse user')
parser.add_argument('-port', help='Database port')
parser.add_argument('-database', required=True, help='Database name')
parser.add_argument('-log', required=True, help='Log file to parse')
parser.set_defaults(host='localhost', user='postgres', port='5432')
args = parser.parse_args()
log_file = args.log

# We open the connection with the main ddbb
db = create_engine('postgresql://' + args.user + '@' + args.host + ':' +
    args.port + '/' + args.database)
Base.metadata.bind = db
DBSession = sessionmaker(bind=db)
session = DBSession()

# We open the file to introduce the data into the ddbb
step = 0
for line in bz2.open(log_file, mode='rt', compresslevel=9):
    data = line.split('\t')
    new_log = ApacheLog()
    new_log.server_name = data[0]
    new_log.port = data[1]
    deflate = data[2][1:-1].split('/')
    if deflate[0] != '-':
        new_log.final_deflate = deflate[0]
    instream = deflate[1].split('(')
    if instream[0] != '-':
        new_log.original_deflate = instream[0]
    ratio = instream[1][0:-2]
    if ratio != '-':
        new_log.ratio_deflate = ratio
    if valid_ip(data[3]):
    #if data[3] != '-' and data[3] != 'unknown':
        new_log.remote_address = int(ipaddress.ip_address(data[3]))
    new_log.timestamp = data[4][1:-1]
    if data[5] != '-':
        new_log.request_method = data[5]
    if data[6] != '-':
        new_log.url_path_requested = data[6]
    new_log.query_string = data[7]
    if data[8] != '-':
        new_log.request_protocol = data[8]
    new_log.status = data[9]
    new_log.response_size = data[10]
    if data[11] != '-':
        new_log.header_referer = data[11]
    if data[12] != '-':
        new_log.header_user_agent = data[12]
    if data[13] != '-':
        new_log.header_cookie = data[13]
    if data[14] != '-':
        new_log.header_accept_lang = data[14]
    if data[15] != '-':
        new_log.reply_content_lang = data[15]
    if data[16] != '-':
        new_log.header_accept_enc = data[16]
    if data[17] != '-':
        new_log.reply_content_enc = data[17]
    if data[18] != '-':
        new_log.reply_content_location = data[18]
    if data[19] != '-':
        new_log.reply_vary = data[19]
    if data[20] != '-':
        new_log.reply_content_type = data[20]
    if data[21] != '-':
        new_log.balancer_session_sticky = data[21]
    if data[22] != '-':
        new_log.balancer_session_route = data[22]
    if data[23] != '-':
        new_log.my_cookie = data[23]
    if data[24] != '-':
        new_log.balancer_worker_route = data[24]
    if data[25] != '-':
        new_log.balancer_route_changed = data[25]
    new_log.request_duration = data[26]

    session.add(new_log)
    step = step + 1
    if step == 10000:
        session.commit()
        step = 0

# Commit the session for the rest of the log below 10000
session.commit()
