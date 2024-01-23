import hashlib
import hmac
import json
import time
from typing import Any, Dict, List, Optional

from hummingbot.connector.exchange.pibase import pibase_constants as CONSTANTS
from hummingbot.connector.time_synchronizer import TimeSynchronizer
from hummingbot.core.web_assistant.auth import AuthBase
from hummingbot.core.web_assistant.connections.data_types import RESTRequest, WSRequest
from hummingbot.core.web_assistant.connections.data_types import RESTMethod
from hummingbot.core.web_assistant.web_assistants_factory import WebAssistantsFactory
import requests


class PibaseAuth(AuthBase):
    """Auth Class for PiBase

    """
    is_new_session = True
    def __init__(self, api_key: str, secret_key: str, time_provider: TimeSynchronizer):
        self.api_key = api_key
        self.secret_key = secret_key
        self.time_provider: time_provider
        
    
    async def rest_authenticate(self, request: RESTRequest) -> RESTRequest:
        
        """
        Adds the server time and the signature to the request, required for authenticated interactions. It also adds
        the required parameter in the request header.

        :param request: the request to be configured for authenticated interaction

        :return: The RESTRequest with auth information included
        """
        path = request.throttler_limit_id
        headers_auth = await self.get_auth_headers(path)
        headers ={}
        if request.headers is not None:
            headers.update(request.headers)
        headers.update(headers_auth)
        request.headers = headers
        
        return request


    async def ws_authenticate(self, request: WSRequest) -> WSRequest:
        """
        This method is intended to configure a websocket request to be authenticated.  use this
        functionality
        """
        return request  # pass-through

    async def get_auth_headers(self, path_url: str, data: Dict[str, Any] = None):
        """
        Generates authentication signature and return it in a dictionary along with other inputs
        :param path_url: URL of the auth API endpoint
        :param data: data to be included in the headers
        :return: a dictionary of request info including the request signature
        """
        # if self.is_new_session:
        #    secret_new_key = await self.get_new_key()
        #    self.secret_key = secret_new_key
        #    self.is_new_session = False

        
        
        
        if path_url == CONSTANTS.SYMBOL_PATH_URL:
              return {
            "Authorization": self.api_key,
        }

        return {
            "Authorization": self.secret_key,
        }


    def _time(self) -> float:
        return time.time()
    
    
    # async def get_new_key(self):

        
    #     result =  requests.post( url="http://staging-api-trader-gateway.pibase.io/users/login/email",
    #                                  headers= {"Content-Type": "application/json",
    #                                            "Accept": "application/json","x-device-info": CONSTANTS.X_DEVICE_INFO},
                                                               
    #                                                           json={"email" : "raghul+19@pibase.info", "password" : "Qwerty@123"}, 
                                                              
    #                                                            )
    #     result_json = result.json()["data"]
    #     token = result_json["token"]
    #     secret_key = token.split(" ")[1]
    #     return secret_key
    
