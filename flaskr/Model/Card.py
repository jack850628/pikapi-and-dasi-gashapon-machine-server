import flaskr.Model.CardPool as CardPool
from flaskr.Entity.Table import CardEntity, CardPoolEntity
from flaskr.Entity.Database import Database
from flaskr.Model.JException import *
from flaskr.Entity.Table import *
from flaskr.Values import Locales as Locales
from flaskr.Model.JException import *
from sqlalchemy import or_, and_

def getAllCards(database: Database, poolId) -> list:
    cardEntitys = database.session.query(
        CardEntity.id,
        CardEntity.name,
        CardEntity.image,
        CardEntity.weight,
        CardEntity.userId
    ).filter(
        CardEntity.cardPoolId == poolId
    ).all()
    cardList = []
    for i in cardEntitys:
        cardList.append(i._asdict())
    return cardList

def getCard(database: Database, cardId: int) -> dict:
    cardEntity = database.session.query(
        CardEntity.name,
        CardEntity.image,
        CardEntity.weight,
        CardEntity.userId,
        CardEntity.cardPoolId
    ).filter(
        CardEntity.id == cardId
    ).first()
    
    if cardEntity == None :
        raise JException('卡片不存在')

    return cardEntity._asdict()

def putCard(database: Database, name: str, image: str, weight: int, cardPoolId: int, userId: str) -> CardEntity:
    cardPool = CardPool.getPool(database, cardPoolId)

    if cardPool['userId'] != userId and not cardPool['isPublic']:
        raise JException('沒有權限', 403)

    cardEntity = CardEntity(
        name = name,
        image = image,
        weight = weight,
        cardPoolId = cardPoolId,
        userId = userId
    )
    database.session.add(cardEntity)

    return cardEntity

def updateCard(database: Database, name: str, image: str, weight: int, cardId: int, userId: str):
    cardEntity = database.session.query(
        CardEntity
    ).join(
        CardPoolEntity,
        CardPoolEntity.id == CardEntity.cardPoolId
    ).filter(
        CardEntity.id == cardId,
        or_(
            CardEntity.userId == userId,
            CardPoolEntity.userId == userId
        )
    ).first()

    if cardEntity == None :
        raise JException('卡片不存在或沒有權限')

    cardEntity.name = name
    cardEntity.image = image
    cardEntity.weight = weight

def deleteCard(database: Database, cardId: int, userId: str) -> int:
    cardEntity = database.session.query(
        CardEntity
    ).join(
        CardPoolEntity,
        CardPoolEntity.id == CardEntity.cardPoolId
    ).filter(
        CardEntity.id == cardId,
        or_(
            CardEntity.userId == userId,
            CardPoolEntity.userId == userId
        )
    ).first()

    if cardEntity == None :
        raise JException('卡片不存在或沒有權限')

    database.session.delete(cardEntity)
    