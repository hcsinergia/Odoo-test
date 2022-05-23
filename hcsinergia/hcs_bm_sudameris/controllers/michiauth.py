# -*- coding: utf-8 -*-
import requests
import json
from odoo import http
from odoo.http import request

import logging
_logger = logging.getLogger(__name__)

baseUrl = 'https://dev.sudameris.com.py/api-ext/michi-auth-sudameris'
deviceIdRequestUrl = baseUrl + '/devices/new-from-ua'
authRequestUrlUser = baseUrl + '/auth/session'
authRequestUrlOperator = baseUrl + '/operator-auth/session'


class BM_OfficialSalary_MichiAuth(http.Controller):
    @http.route('/michi_auth_request_device_id', type="json", auth='public')
    def michi_auth_request_device_id(self, **kwargs):
        try:
            d = json.dumps(kwargs)
            h = request.httprequest.headers
            #r = requests.post(deviceIdRequestUrl, data=d, headers=h, verify=False, timeout=3)
            #response = json.loads(r.content)
            response = {
                "deviceId": "1cdd6a6f-f93b-4413-b1ab-a1f63f5ce1ea"
            }
            _logger.debug(['device_id', response])
            # return {'status': r.status_code, 'response': response, 'message': 'Success'}
            return {'status': 200, 'response': response, 'message': 'Success'}
        except:
            return {'status': 500, 'response': False, 'message': 'Success'}

    @http.route('/michi_auth_user_login', type="json", auth='public')
    def michi_auth_user_login(self, **kwargs):
        try:
            d = json.dumps(kwargs)
            h = request.httprequest.headers
            #r = requests.post(authRequestUrlUser, data=d, headers=h, verify=False, timeout=3)
            #response = json.loads(r.content)
            response = {
                "accessToken": "393b0f09be053f90f05c@f2fd9d8b-7d54-4ae8-9b81-1bcd0128e12f@700f69c488261c8b08c8",
                "session": {
                    "status": "VALID",
                    "userInfo": {
                        "additionalInfo": {
                            "UserOperators": [
                                {
                                    "externalId": "58603801078008"

                                }
                            ]
                        }
                    }
                }
            }
            _logger.debug(['user_login', response])
            # return {'status': r.status_code, 'response': response, 'message': 'Success'}
            return {'status': 200, 'response': response, 'message': 'Success'}
        except:
            return {'status': 500, 'response': False, 'message': 'Success'}

    @http.route('/michi_auth_operator_login', type="json", auth='public')
    def michi_auth_operator_login(self, **kwargs):
        try:
            d = json.dumps(kwargs)
            h = request.httprequest.headers
            #r = requests.post(authRequestUrlOperator, data=d, headers=h, verify=False, timeout=3)
            #response = json.loads(r.content)
            response = {
                "accessToken": "3db63ef17973057c4b71@b160b9d3-cd74-4db3-b731-d4a08fb269a8@b1eb10ffd2cdb1f47a02",
                "session": {
                    "status": "VALID",
                    "userInfo": {
                        "subjectId": "58603801078008",
                        "login": "4332768",
                        "fullName": "Nombre1 Nombre2 Apellido1 4332768 4332768",
                        "additionalInfo": {
                        "BantotalAccountsLimits": {
                            "3564267": {}
                        }
                        }
                    }
                }
            }
            _logger.debug(['operator_login', response])
            # return {'status': r.status_code, 'response': response, 'message': 'Success'}
            return {'status': 200, 'response': response, 'message': 'Success'}
        except:
            return {'status': 500, 'response': False, 'message': 'Success'}
