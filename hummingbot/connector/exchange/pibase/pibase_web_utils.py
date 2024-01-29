import time
from typing import Any, Dict, Optional

import hummingbot.connector.exchange.pibase.pibase_constants as CONSTANTS
from hummingbot.core.api_throttler.async_throttler import AsyncThrottler
from hummingbot.core.web_assistant.auth import AuthBase
from hummingbot.core.web_assistant.connections.data_types import RESTMethod
from hummingbot.core.web_assistant.web_assistants_factory import WebAssistantsFactory


def public_rest_url(endpoint: str, domain: str = CONSTANTS.DEFAULT_DOMAIN) -> str:
    """
    Creates a full URL for provided public REST endpoint

    :param endpoint: a public REST endpoint
    :param domain: unused

    :return: the full URL to the endpoint
    """
    if CONSTANTS.REST_URL[-1] != "/" and endpoint[0] != "/":
        endpoint = "/" + endpoint
    return CONSTANTS.REST_URL + endpoint


def private_rest_url(endpoint: str, domain: str = CONSTANTS.DEFAULT_DOMAIN) -> str:
    return public_rest_url(endpoint, domain)


def build_api_factory(
        throttler: Optional[AsyncThrottler] = None,
        auth: Optional[AuthBase] = None) -> WebAssistantsFactory:
    throttler = throttler or create_throttler()
    api_factory = WebAssistantsFactory(
        throttler=throttler,
        auth=auth)
    return api_factory


def create_throttler() -> AsyncThrottler:
    return AsyncThrottler(CONSTANTS.RATE_LIMITS)


async def get_current_server_time(
        throttler: Optional[AsyncThrottler] = None,
        domain: str = CONSTANTS.DEFAULT_DOMAIN,
) -> float:
    throttler = throttler or create_throttler()
    api_factory = build_api_factory_without_time_synchronizer_pre_processor(throttler=throttler)
    rest_assistant = await api_factory.get_rest_assistant()
    response = await rest_assistant.execute_request(
        url=public_rest_url(path_url=CONSTANTS.SERVER_TIME_PATH, domain=domain),
        method=RESTMethod.GET,
        throttler_limit_id=CONSTANTS.SERVER_TIME_PATH,
    )
    server_time = response["server_time"]
    print(server_time)
    return server_time



def is_exchange_information_valid(exchange_info: Dict[str, Any]) -> bool:
    """
    Verifies if a trading pair is enabled to operate with based on its exchange information
    :param exchange_info: the exchange information for a trading pair
    :return: True if the trading pair is enabled, False otherwise
    """
    return exchange_info.get("trade_status", None) == "tradable"

def build_api_factory_without_time_synchronizer_pre_processor(throttler: AsyncThrottler) -> WebAssistantsFactory:
    api_factory = WebAssistantsFactory(throttler=throttler)
    return api_factory



async def checkTime() -> None:
    throttler = create_throttler()
    servertime = await get_current_server_time()


checkTime()