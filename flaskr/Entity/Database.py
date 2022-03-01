from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative.api import DeclarativeMeta
from sqlalchemy.pool import NullPool
from sqlalchemy.pool import QueuePool
from flaskr.Model.Status import DBType
from flaskr.Config import Config

class Database:
    def __init__(self, dbFile: str, tableBase :DeclarativeMeta, dbType: int = DBType.Mysql, autoConnection: bool = True):
        self.session = None
        self.connect = None
        if dbType == DBType.Sqlite:
            self._engine = create_engine('sqlite:///' + dbFile + '?check_same_thread=false', poolclass = NullPool)
        elif dbType == DBType.Mysql:
            if not Config.TESTING:
                self._engine = create_engine('mysql+mysqldb://' + dbFile + '?charset=utf8', poolclass = QueuePool, pool_size = 30, pool_recycle = 300)#, pool_timeout = 90)
            else:
                self._engine = create_engine('mysql+mysqldb://' + dbFile + '?charset=utf8', poolclass = NullPool)
        else:
            raise Exception('DB type unknown')
        if tableBase != None:
            tableBase.metadata.create_all(self._engine, checkfirst = True)
        if autoConnection:
            self.connection()

    def connection(self):
        if self.connect is None or self.connect.closed is True:
            self.connect = self._engine.connect()
        self.session = scoped_session(sessionmaker(bind = self.connect, autocommit = False))#()
    
    def close(self):
        self.connect.close()
        self.session.close()
    
    def __del__(self):
        self._engine.dispose()