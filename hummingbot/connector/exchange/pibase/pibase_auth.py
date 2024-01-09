import hashlib
import hmac
import json
import time
from typing import Any, Dict, List, Optional

from hummingbot.connector.exchange.bitmart import bitmart_constants as CONSTANTS
from hummingbot.connector.time_synchronizer import TimeSynchronizer
from hummingbot.core.web_assistant.auth import AuthBase
from hummingbot.core.web_assistant.connections.data_types import RESTRequest, WSRequest

class PibaseAuth(AuthBase):
    """Auth Class for PiBase

    """
    
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
        headers_auth = self.get_auth_headers(path)
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

    def get_auth_headers(self, path_url: str, data: Dict[str, Any] = None):
        """
        Generates authentication signature and return it in a dictionary along with other inputs
        :param path_url: URL of the auth API endpoint
        :param data: data to be included in the headers
        :return: a dictionary of request info including the request signature
        """

        timestamp = str(int(self._time() * 1e3))
        message = timestamp + path_url
        signature = hmac.new(self.secret_key.encode("utf-8"), message.encode("utf-8"), hashlib.sha256).hexdigest()

        return {
            "Authorization": self.secret_key,
        }

    def _time(self) -> float:
        return time.time()
