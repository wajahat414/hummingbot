from decimal import Decimal

from pydantic import Field, SecretStr

from hummingbot.client.config.config_data_types import BaseConnectorConfigMap, ClientFieldData
from hummingbot.connector.exchange.pibase import pibase_constants as CONSTANTS
from hummingbot.core.data_type.trade_fee import TradeFeeSchema
from hummingbot.core.api_throttler.async_throttler import AsyncThrottler
from hummingbot.core.api_throttler.data_types import RateLimit
from hummingbot.connector.exchange.pibase import pibase_constants as CONSTANTS, pibase_web_utils as web_utils

CENTRALIZED = True
EXAMPLE_PAIR = "BTC-USDT"
DEFAULT_FEES = TradeFeeSchema(
    maker_percent_fee_decimal=Decimal("0.000"),
    taker_percent_fee_decimal=Decimal("0.000"),
)


class PibaseConfigMap(BaseConnectorConfigMap):
    connector: str = Field(default="pibase",const=True, client_data=None )
    pibase_api_key: SecretStr = Field(
        default=CONSTANTS.PUBLIC_AUTH_KEY,
        client_data=ClientFieldData(
            prompt=lambda cm: "Enter your Pibase API key",
            is_secure=False,
            is_connect_key=True,
            prompt_on_new=True,
        )  
    )
    pibase_secret_key: SecretStr = Field(
        default=CONSTANTS.USER_SECRET_KEY,
        client_data=ClientFieldData(
            prompt=lambda cm: "Enter your PiBase API secret",
            is_secure=False,
            is_connect_key=True,
            prompt_on_new=True,
        )     
    )



KEYS = PibaseConfigMap.construct()
