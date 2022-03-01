import json
import traceback
import flaskr.Model.Card as Card
import flaskr.Utility.ResponseTemplate as ResponseTemplate
import flaskr.Entity.GlobalDataBase as GlobalDataBase
from flaskr.Config import Config
from flask import Blueprint, Response, request
from flaskr.Model.JException import *
from google.auth import jwt

cardAPI = Blueprint('cardAPI', __name__)

def init_app(app):
    app.register_blueprint(cardAPI, url_prefix='/api/card')

@cardAPI.route('/all/<pool_id>', methods=['GET'])
def getAllCards(pool_id):
    database = GlobalDataBase.database(Config.databaseUser)
    try:
        return Response(json.dumps(Card.getAllCards(database, pool_id)))
    except (
        JException
    ) as e:
        print(traceback.format_exc())
        response = ResponseTemplate.fail(e.__str__())
        response.status_code = e.code
        return response
    except (
        Exception
    ) as e:
        print(traceback.format_exc())
        response = ResponseTemplate.fail(e.__str__())
        response.status_code = 490
        return response
    finally:
        database.close()

@cardAPI.route('/<card_id>', methods=['GET'])
def getCard(card_id):
    database = GlobalDataBase.database(Config.databaseUser)
    try:
        return Response(json.dumps(Card.getCard(database, card_id)))
    except (
        JException
    ) as e:
        print(traceback.format_exc())
        response = ResponseTemplate.fail(e.__str__())
        response.status_code = e.code
        return response
    except (
        Exception
    ) as e:
        print(traceback.format_exc())
        response = ResponseTemplate.fail(e.__str__())
        response.status_code = 490
        return response
    finally:
        database.close()

@cardAPI.route('/create', methods=['PUT'])
def putCard():
    database = GlobalDataBase.database(Config.databaseUser)
    try:
        name = request.form['name'] if 'name' in request.form else ''
        image = request.form['image'] if 'image' in request.form else ''
        weight = request.form['weight'] if 'weight' in request.form else 10
        cardPoolId = request.form['cardPoolId'] if 'cardPoolId' in request.form else ''

        token = request.headers['user-token'] if 'user-token' in request.headers else None

        if token == None:
            raise JException('缺少 user-token')

        userId = jwt.decode(token, verify=False)['sub']
        result = Card.putCard(database, name, image, weight, cardPoolId, userId)
        database.session.commit()
        return ResponseTemplate.success(result.id)
    except (
        JException
    ) as e:
        print(traceback.format_exc())
        response = ResponseTemplate.fail(e.__str__())
        response.status_code = e.code
        return response
    except (
        Exception
    ) as e:
        print(traceback.format_exc())
        response = ResponseTemplate.fail(e.__str__())
        response.status_code = 490
        return response
    finally:
        database.close()

@cardAPI.route('/<card_id>', methods=['POST'])
def updateCard(card_id):
    database = GlobalDataBase.database(Config.databaseUser)
    try:
        name = request.form['name'] if 'name' in request.form else ''
        image = request.form['image'] if 'image' in request.form else ''
        weight = request.form['weight'] if 'weight' in request.form else 10

        token = request.headers['user-token'] if 'user-token' in request.headers else None

        if token == None:
            raise JException('缺少 user-token')

        userId = jwt.decode(token, verify=False)['sub']
        Card.updateCard(database, name, image, weight, card_id, userId)
        database.session.commit()
        return ResponseTemplate.success()
    except (
        JException
    ) as e:
        print(traceback.format_exc())
        response = ResponseTemplate.fail(e.__str__())
        response.status_code = e.code
        return response
    except (
        Exception
    ) as e:
        print(traceback.format_exc())
        response = ResponseTemplate.fail(e.__str__())
        response.status_code = 490
        return response
    finally:
        database.close()

@cardAPI.route('/<card_id>', methods=['DELETE'])
def deleteCard(card_id):
    database = GlobalDataBase.database(Config.databaseUser)
    try:
        token = request.headers['user-token'] if 'user-token' in request.headers else None

        if token == None:
            raise JException('缺少 user-token')

        userId = jwt.decode(token, verify=False)['sub']
        Card.deleteCard(database, card_id, userId)
        database.session.commit()
        return ResponseTemplate.success()
    except (
        JException
    ) as e:
        print(traceback.format_exc())
        response = ResponseTemplate.fail(e.__str__())
        response.status_code = e.code
        return response
    except (
        Exception
    ) as e:
        print(traceback.format_exc())
        response = ResponseTemplate.fail(e.__str__())
        response.status_code = 490
        return response
    finally:
        database.close()