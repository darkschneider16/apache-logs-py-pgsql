#!/usr/bin/python
# -*- coding: utf-8 -*-

from sqlalchemy import DateTime, Column, Integer, BigInteger
from sqlalchemy import String, Sequence
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class ApacheLog(Base):
    __tablename__ = 'apache_log'

    id_apache_log = Column(
        Integer, Sequence('apache_log_id_seq'), primary_key=True)
    server_name = Column(String)
    port = Column(Integer)
    original_deflate = Column(Integer)
    final_deflate = Column(Integer)
    ratio_deflate = Column(Integer)
    remote_address = Column(BigInteger)
    timestamp = Column(DateTime)
    request_method = Column(String)
    url_path_requested = Column(String)
    query_string = Column(String)
    request_protocol = Column(String)
    status = Column(Integer)
    response_size = Column(Integer)
    header_referer = Column(String)
    header_user_agent = Column(String)
    header_cookie = Column(String)
    header_accept_lang = Column(String)
    reply_content_lang = Column(String)
    header_accept_enc = Column(String)
    reply_content_enc = Column(String)
    reply_content_location = Column(String)
    reply_vary = Column(String)
    reply_content_type = Column(String)
    # Added for back apache proxy extra configuration
    balancer_session_sticky = Column(String)
    balancer_session_route = Column(String)
    my_cookie = Column(String)
    balancer_worker_route = Column(String)
    balancer_route_changed = Column(String)
    request_duration = Column(Integer)


#class ApacheLogsSQLite():
    #db = None
    #session = None

    #def __init__(self):
        #super(ApacheLogsSQLite, self).__init__()
        #self.db = create_engine('sqlite://')
        #Base.metadata.create_all(self.db)
        #Base.metadata.bind = self.db
        #DBSession = sessionmaker(bind=self.db)
        #self.session = DBSession()

    ## To check if an ip address is valid
    #def _valid_ip(self, address=None):
        #try:
            #ipaddress.ip_address(address)
            #return True
        #except:
            #return False

    #def add_record(self, line=None):
        #record = line.split('\t')
        #new_log = ApacheLog()
        #new_log.server_name = record[0]
        #new_log.port = record[1]
        #deflate = record[2][1:-1].split('/')
        #if deflate[0] != '-':
            #new_log.final_deflate = deflate[0]
        #instream = deflate[1].split('(')
        #if instream[0] != '-':
            #new_log.original_deflate = instream[0]
        #ratio = instream[1][0:-2]
        #if ratio != '-':
            #new_log.ratio_deflate = ratio
        #if self._valid_ip(record[3]):
        ##if record[3] != '-' and record[3] != 'unknown':
            #new_log.remote_address = record[3]
        #new_log.timestamp = datetime.strptime(
            #record[4], "[%d/%b/%Y:%H:%M:%S %z]")
        #if record[5] != '-':
            #new_log.request_method = record[5]
        #if record[6] != '-':
            #new_log.url_path_requested = record[6]
        #new_log.query_string = record[7]
        #if record[8] != '-':
            #new_log.request_protocol = record[8]
        #new_log.status = record[9]
        #new_log.response_size = record[10]
        #if record[11] != '-':
            #new_log.header_referer = record[11]
        #if record[12] != '-':
            #new_log.header_user_agent = record[12]
        #if record[13] != '-':
            #new_log.header_cookie = record[13]
        #if record[14] != '-':
            #new_log.header_accept_lang = record[14]
        #if record[15] != '-':
            #new_log.reply_content_lang = record[15]
        #if record[16] != '-':
            #new_log.header_accept_enc = record[16]
        #if record[17] != '-':
            #new_log.reply_content_enc = record[17]
        #if record[18] != '-':
            #new_log.reply_content_location = record[18]
        #if record[19] != '-':
            #new_log.reply_vary = record[19]
        #if record[20] != '-':
            #new_log.reply_content_type = record[20]
        #new_log.request_duration = record[21]

        #self.session.add(new_log)
        #self.session.commit()

    #def status_all(self):
        #return self.session.query(ApacheLog.status, ApacheLog.timestamp,
            #ApacheLog.remote_address).all()

    #def status_200(self):
        #return self.session.query(
            #ApacheLog).filter(ApacheLog.status == 200).count()

    #def close(self):
        #self.session.close()
