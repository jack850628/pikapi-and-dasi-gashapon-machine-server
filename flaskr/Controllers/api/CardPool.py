import json
import traceback
import flaskr.Model.CardPool as CardPool
import flaskr.Utility.ResponseTemplate as ResponseTemplate
import flaskr.Entity.GlobalDataBase as GlobalDataBase
from flaskr.Config import Config
from flask import Blueprint, Response, request
from flaskr.Model.JException import *
from flaskr.Utility.Auth import check_identity

cardPoolAPI = Blueprint('cardPoolAPI', __name__)

def init_app(app):
    app.register_blueprint(cardPoolAPI, url_prefix='/api/cardPool')

@cardPoolAPI.route('/', methods=['GET'])
def getAllPools():
    database = GlobalDataBase.database(Config.databaseUser)
    try:
        return Response(json.dumps(CardPool.getAllPools(database)))
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

@cardPoolAPI.route('/<pool_id>', methods=['GET'])
def getPool(pool_id):
    database = GlobalDataBase.database(Config.databaseUser)
    try:
        return Response(json.dumps(CardPool.getPool(database, pool_id)))
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

@cardPoolAPI.route('/create', methods=['PUT'])
@check_identity
def putPool(userInfo):
    database = GlobalDataBase.database(Config.databaseUser)
    try:
        name = request.form['name'] if 'name' in request.form else ''
        describe = request.form['describe'] if 'describe' in request.form else ''
        image = request.form['image'] if 'image' in request.form else ''
        isPublic = request.form['isPublic'] == 'true' if 'isPublic' in request.form else False

        userId = userInfo['sub']
        result = CardPool.putPool(database, name, describe, image, isPublic, userId)
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

@cardPoolAPI.route('/<pool_id>', methods=['POST'])
@check_identity
def updatePool(pool_id, userInfo):
    database = GlobalDataBase.database(Config.databaseUser)
    try:
        name = request.form['name'] if 'name' in request.form else ''
        describe = request.form['describe'] if 'describe' in request.form else ''
        image = request.form['image'] if 'image' in request.form else ''
        isPublic = request.form['isPublic'] == 'true' if 'isPublic' in request.form else False

        userId = userInfo['sub']
        CardPool.updatePool(database, pool_id, name, describe, image, isPublic, userId)
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

@cardPoolAPI.route('/<pool_id>', methods=['DELETE'])
@check_identity
def deletePool(pool_id, userInfo):
    database = GlobalDataBase.database(Config.databaseUser)
    try:
        token = request.headers['user-token'] if 'user-token' in request.headers else None

        if token == None:
            raise JException('缺少 user-token')

        userId = userInfo['sub']
        CardPool.deletePool(database, pool_id, userId)
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