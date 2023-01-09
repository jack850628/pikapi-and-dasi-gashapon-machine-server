import flaskr.Utility.ResponseTemplate as ResponseTemplate
import traceback
from functools import wraps
from flask import request
from google.oauth2 import id_token
from google.auth.transport import requests as googleRequests
from flaskr.Config import Config
from flaskr.Model.JException import *


def check_identity(func):
    @wraps(func)#缺少這行將導致錯誤AssertionError: View function mapping is overwriting an existing endpoint function
    def check(*args, **keys):
        try:
            if 'user-token' in request.headers:
                token = request.headers['user-token']
            else:
                raise JException('缺少 user-token')
            
            keys['userInfo'] = id_token.verify_oauth2_token(token, googleRequests.Request(), Config.googleClientId)

            return func(*args, **keys)
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

    # check.__name__ = func.__name__#已經用wraps取代
    return check