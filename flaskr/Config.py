import os
from datetime import timedelta 

class Config:
    APP_NAME = 'pikapi-and-dasi-gashapon-machine-server'

    DEBUG = False
    TESTING = False

    database = '/PikapiAndDasiGashaponMachine'
    databaseUser = '%s:%s@localhost' % (os.environ.get('DATABASE_USER_NAME'), os.environ.get('DATABASE_USER_PASSWORD'))

    googleClientId = os.environ.get('GOOGLE_CLIENT_ID')

class Path:
    dataBase = Config.database#'/../{}/{}'.format(Config.dataFolder, Config.globalDatabase)