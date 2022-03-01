from datetime import timedelta

class Config:
    APP_NAME = 'pikapi-and-dasi-gashapon-machine-server'

    DEBUG = False
    TESTING = False

    defaultDataServerId = 0

    secretKey = 'TJX6sre1I3RTJLP9uX+A/Vi+zHao0E6B'
    apiKey = 'gCt9v1RlkCCBjK2npm2HryV+S8sth6ULcpes5Igpqs8='

    database = '/PikapiAndDasiGashaponMachine'
    databaseUser = 'pdgm:pdgm2022@localhost'

    http = 'http'
    serverDomain = 'localhost' if DEBUG else 'code.origthatone.com'

class Path:
    dataBase = Config.database#'/../{}/{}'.format(Config.dataFolder, Config.globalDatabase)