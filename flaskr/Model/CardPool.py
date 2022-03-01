from flaskr.Entity.Table import CardPoolEntity, CardEntity
from flaskr.Entity.Database import Database
from flaskr.Model.JException import *
from flaskr.Entity.Table import *
from flaskr.Values import Locales as Locales
from flaskr.Model.JException import *

def getAllPools(database: Database) -> list:
    cardPoolEntitys = database.session.query(
        CardPoolEntity.id,
        CardPoolEntity.name,
        CardPoolEntity.describe,
        CardPoolEntity.userId,
        CardPoolEntity.isPublic
    ).all()
    poolList = []
    for i in cardPoolEntitys:
        poolList.append(i._asdict())
    return poolList

def getPool(database: Database, poolId: int) -> dict:
    cardPoolEntity = database.session.query(
        CardPoolEntity.name,
        CardPoolEntity.describe,
        CardPoolEntity.userId,
        CardPoolEntity.isPublic
    ).filter(
        CardPoolEntity.id == poolId
    ).first()
    
    if cardPoolEntity == None :
        raise JException('卡池不存在')

    return cardPoolEntity._asdict()

def putPool(database: Database, name: str, describe: str, isPublic: bool, userId: str) -> CardPoolEntity:
    cardPoolEntity = CardPoolEntity(
        name = name,
        describe = describe,
        userId = userId,
        isPublic = isPublic
    )
    database.session.add(cardPoolEntity)

    return cardPoolEntity

def updatePool(database: Database, poolId: int, name: str, describe: str, isPublic: bool, userId: str):
    cardPoolEntity = database.session.query(
        CardPoolEntity
    ).filter(
        CardPoolEntity.id == poolId,
        CardPoolEntity.userId == userId
    ).first()

    if cardPoolEntity == None :
        raise JException('卡池不存在')

    cardPoolEntity.name = name
    cardPoolEntity.describe = describe
    cardPoolEntity.isPublic = isPublic

def deletePool(database: Database, poolId: int, userId: str) -> int:
    cardPoolEntity = database.session.query(
        CardPoolEntity
    ).filter(
        CardPoolEntity.id == poolId,
        CardPoolEntity.userId == userId
    ).first()

    if cardPoolEntity == None :
        raise JException('卡池不存在')

    database.session.query(
        CardEntity
    ).filter(
        CardEntity.cardPoolId == poolId
    ).delete()

    database.session.delete(cardPoolEntity)
    