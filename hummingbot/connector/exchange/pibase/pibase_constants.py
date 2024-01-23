# A single source of truth for constant variables related to the exchange

from hummingbot.core.api_throttler.data_types import RateLimit
from hummingbot.core.data_type.in_flight_order import OrderState



WS_PING_TIMEOUT = 20 * 0.8

DEFAULT_DOMAIN = ""
MAX_ORDER_ID_LEN = 32
HBOT_ORDER_ID_PREFIX = ""
BROKER_ID = "hummingbotfound"
USER_SECRET_KEY = ""
X_DEVICE_INFO = "PMRGG33VNZ2HE6JCHIRESTRCFQRGS4C7MFSGI4TFONZSEORCGEYTKLRZHEXDIMZOGEZDQIRMEJWG6Y3BORUW63RCHIRDCMROHA4TAMBMHAYC4MRTGEZSELBCOVZWK4S7MFTWK3TUEI5CETLPPJUWY3DBF42S4MBAFBMDCMJ3EBGGS3TVPAQHQOBWL43DIKJAIFYHA3DFK5SWES3JOQXTKMZXFYZTMIBIJNEFITKMFQQGY2LLMUQEOZLDNNXSSICDNBZG63LFF4YTCNZOGAXDALRQEBJWCZTBOJUS6NJTG4XDGNRCFQRGIZLWNFRWKX3OMFWWKIR2EJBWQ4TPNVSSAVRRGE3S4MBOGAXDAIBIJRUW45LYFERCYITDNRUWK3TUL52HS4DFEI5CE53FMIRH2==="

PUBLIC_AUTH_KEY = "a68d1a18-717f-4a2f-a376-3488bf5c0024"
PUBLIC_TRADE_CHANNEL_NAME = "public/spot_orders"
PUBLIC_DEPTH_CHANNEL_NAME = "public/spot_orders"
PRIVATE_ORDER_PROGRESS_CHANNEL_NAME = "spot_orders"

# REST API ENDPOINTS

GET_TRADING_RULES_PATH_URL = "assets/all?type=CRYPTO"
GET_LAST_TRADING_PRICES_PATH_URL = "tickers"
GET_ORDER_BOOK_PATH_URL = "public/spot_orders/order_book"
CREATE_ORDER_PATH_URL = "spot_orders/create"
CANCEL_ORDER_PATH_URL = "spot_orders/cancel"
GET_ACCOUNT_SUMMARY_PATH_URL = "wallets/estimated_balance"
GET_ORDER_DETAIL_PATH_URL = "spot_orders"
GET_TRADE_DETAIL_PATH_URL = "spot_trades"
SERVER_TIME_PATH = "system/time"

# WS API ENDPOINTS
WS_CONNECT = "feeder-"
WS_SUBSCRIBE = "feeder-"

# BitMart has a per method API limit

ORDER_STATE = {
    "OPEN": OrderState.OPEN,
    "FAILED": OrderState.FAILED,
    "OPEN": OrderState.OPEN,
    "PARTIALLY_FILLED": OrderState.PARTIALLY_FILLED,
    "FILLED": OrderState.FILLED,
    "PENDING_CANCEL": OrderState.PENDING_CANCEL,
    "CANCELED": OrderState.CANCELED,
}




# A single source of truth for constant variables related to the exchange
from hummingbot.core.api_throttler.data_types import LinkedLimitWeightPair, RateLimit

EXCHANGE_NAME = "pibase"
DEFAULT_DOMAIN = ""
HBOT_BROKER_ID = "hummingbot"
HBOT_ORDER_ID = "t-HBOT"
MAX_ID_LEN = 30

REST_URL = "https://staging-api-exchange-gateway.pibase.io/pix"
REST_URL_AUTH = "http://staging-api-trader-gateway.pibase.io"
TOKEN_ENDPOINT = "users/login/email"
WS_URL = "wss://staging-websocket.pibase.io/"
NETWORK_CHECK_PATH_URL = "wallets/wallet_assets"
SYMBOL_PATH_URL = "symbols/all"
ORDER_CREATE_PATH_URL = "spot/orders"
ORDER_DELETE_PATH_URL = "spot/orders/{order_id}"
USER_BALANCES_PATH_URL = "wallets/wallet_assets"
ORDER_STATUS_PATH_URL = "spot/orders/{order_id}"
USER_ORDERS_PATH_URL = "spot/open_orders"
TICKER_PATH_URL = "spot/tickers"
ORDER_BOOK_PATH_URL = "spot/order_book"
MY_TRADES_PATH_URL = "spot/my_trades"

TRADES_ENDPOINT_NAME = "spot.trades"
ORDER_SNAPSHOT_ENDPOINT_NAME = "spot.order_book"
ORDERS_UPDATE_ENDPOINT_NAME = "spot.order_book_update"
USER_TRADES_ENDPOINT_NAME = "spot.usertrades"
USER_ORDERS_ENDPOINT_NAME = "spot.orders"
USER_BALANCE_ENDPOINT_NAME = "spot.balances"
PONG_CHANNEL_NAME = "spot.pong"

# Timeouts
MESSAGE_TIMEOUT = 30.0
PING_TIMEOUT = 10.0
API_CALL_TIMEOUT = 10.0
API_MAX_RETRIES = 4

# Intervals
# Only used when nothing is received from WS
SHORT_POLL_INTERVAL = 5.0
# 45 seconds should be fine since we get trades, orders and balances via WS
LONG_POLL_INTERVAL = 45.0
# One minute should be fine since we get trades, orders and balances via WS
UPDATE_ORDER_STATUS_INTERVAL = 60.0
# 10 minute interval to update trading rules, these would likely never change whilst running.
INTERVAL_TRADING_RULES = 600

PUBLIC_URL_POINTS_LIMIT_ID = "PublicPoints"
PRIVATE_URL_POINTS_LIMIT_ID = "PrivatePoints"  # includes place-orders
CANCEL_ORDERS_LIMITS_ID = "CancelOrders"
ORDER_DELETE_LIMIT_ID = "OrderDelete"
ORDER_STATUS_LIMIT_ID = "OrderStatus"
RATE_LIMITS = [
    RateLimit(limit_id=PUBLIC_URL_POINTS_LIMIT_ID, limit=900, time_interval=1),
    RateLimit(limit_id=PRIVATE_URL_POINTS_LIMIT_ID, limit=900, time_interval=1),
    RateLimit(limit_id=CANCEL_ORDERS_LIMITS_ID, limit=5_000, time_interval=1),
    RateLimit(limit_id=NETWORK_CHECK_PATH_URL, limit=900, time_interval=1, linked_limits=[LinkedLimitWeightPair(PUBLIC_URL_POINTS_LIMIT_ID)]),
    RateLimit(limit_id=SYMBOL_PATH_URL, limit=900, time_interval=1, linked_limits=[LinkedLimitWeightPair(PUBLIC_URL_POINTS_LIMIT_ID)]),
    RateLimit(limit_id=ORDER_CREATE_PATH_URL, limit=900, time_interval=1, linked_limits=[LinkedLimitWeightPair(PRIVATE_URL_POINTS_LIMIT_ID)]),
    RateLimit(limit_id=ORDER_DELETE_LIMIT_ID, limit=5_000, time_interval=1, linked_limits=[LinkedLimitWeightPair(CANCEL_ORDERS_LIMITS_ID)]),
    RateLimit(limit_id=USER_BALANCES_PATH_URL, limit=900, time_interval=1, linked_limits=[LinkedLimitWeightPair(PRIVATE_URL_POINTS_LIMIT_ID)]),
    RateLimit(limit_id=ORDER_STATUS_LIMIT_ID, limit=900, time_interval=1, linked_limits=[LinkedLimitWeightPair(PRIVATE_URL_POINTS_LIMIT_ID)]),
    RateLimit(limit_id=USER_ORDERS_PATH_URL, limit=900, time_interval=1, linked_limits=[LinkedLimitWeightPair(PRIVATE_URL_POINTS_LIMIT_ID)]),
    RateLimit(limit_id=TICKER_PATH_URL, limit=900, time_interval=1, linked_limits=[LinkedLimitWeightPair(PUBLIC_URL_POINTS_LIMIT_ID)]),
    RateLimit(limit_id=ORDER_BOOK_PATH_URL, limit=900, time_interval=1, linked_limits=[LinkedLimitWeightPair(PUBLIC_URL_POINTS_LIMIT_ID)]),
    RateLimit(limit_id=MY_TRADES_PATH_URL, limit=900, time_interval=1, linked_limits=[LinkedLimitWeightPair(PRIVATE_URL_POINTS_LIMIT_ID)]),
]


class UserInfo:
    email = "raghul+19@pibase.info"
    password = "Qwerty@123"
    
        