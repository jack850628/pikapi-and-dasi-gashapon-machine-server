from flaskr.Entity.Table import getTableBase
from flaskr.Entity.Database import Database
from flaskr.Config import Path
from flaskr.Model.Status import DBType

def database(appRootPath: str) -> Database:
    return Database(
        dbFile = appRootPath + Path.dataBase,
        tableBase = getTableBase(),
        dbType = DBType.Mysql,
        autoConnection = True
    )