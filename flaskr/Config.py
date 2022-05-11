import os
from datetime import timedelta 

class Config:
    APP_NAME = 'pikapi-and-dasi-gashapon-machine-server'

    DEBUG = False
    TESTING = False

    secretKey = 'xssCIE8lNz4Q1L6DYTd4bDNhEeKcMOV0yBF2uuWtu0s='

    database = '/PikapiAndDasiGashaponMachine'
    databaseUser = '%s:%s@localhost' % (os.environ.get('DATABASE_USER_NAME'), os.environ.get('DATABASE_USER_PASSWORD'))

class Path:
    dataBase = Config.database#'/../{}/{}'.format(Config.dataFolder, Config.globalDatabase)