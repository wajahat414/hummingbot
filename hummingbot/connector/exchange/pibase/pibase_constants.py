# A single source of truth for constant variables related to the exchange

from hummingbot.core.api_throttler.data_types import RateLimit

from hummingbot.core.api_throttler.data_types import LinkedLimitWeightPair, RateLimit

REST_URL = "https://staging-api-exchange-gateway.pibase.io/pix"
REST_URL_AUTH = "http://staging-api-trader-gateway.pibase.io" # not using but may need in future


DEFAULT_DOMAIN = ""
USER_SECRET_KEY = ""
X_DEVICE_INFO = "PMRGG33VNZ2HE6JCHIRESTRCFQRGS4C7MFSGI4TFONZSEORCGEYTKLRZHEXDIMZOGEZDQIRMEJWG6Y3BORUW63RCHIRDCMROHA4TAMBMHAYC4MRTGEZSELBCOVZWK4S7MFTWK3TUEI5CETLPPJUWY3DBF42S4MBAFBMDCMJ3EBGGS3TVPAQHQOBWL43DIKJAIFYHA3DFK5SWES3JOQXTKMZXFYZTMIBIJNEFITKMFQQGY2LLMUQEOZLDNNXSSICDNBZG63LFF4YTCNZOGAXDALRQEBJWCZTBOJUS6NJTG4XDGNRCFQRGIZLWNFRWKX3OMFWWKIR2EJBWQ4TPNVSSAVRRGE3S4MBOGAXDAIBIJRUW45LYFERCYITDNRUWK3TUL52HS4DFEI5CE53FMIRH2==="

PUBLIC_AUTH_KEY = "a68d1a18-717f-4a2f-a376-3488bf5c0024"
# REST API ENDPOINTS  ACTIVE


SERVER_TIME_PATH = "time"
USER_BALANCES_PATH_URL = "wallets/wallet_assets"
SYMBOL_PATH_URL = "symbols/all"
NETWORK_CHECK_PATH_URL = SERVER_TIME_PATH


# WS API ENDPOINTS YET TO BE IMPLEMENTED
WS_CONNECT = "feeder-"
WS_SUBSCRIBE = "feeder-"



HBOT_ORDER_ID = "t-HBOT"
MAX_ID_LEN = 30


WS_URL = "wss://staging-websocket.pibase.io/"

ORDER_CREATE_PATH_URL = "spot/orders"
ORDER_DELETE_PATH_URL = "spot/orders/{order_id}"

ORDER_STATUS_PATH_URL = "spot/orders/{order_id}"
USER_ORDERS_PATH_URL = "spot/open_orders"
TICKER_PATH_URL = "spot/tickers"
ORDER_BOOK_PATH_URL = "spot/order_book"
MY_TRADES_PATH_URL = "spot/my_trades"

TRADES_ENDPOINT_NAME = "spot.trades"
ORDERS_UPDATE_ENDPOINT_NAME = "spot.order_book_update"
USER_TRADES_ENDPOINT_NAME = "spot.usertrades"
USER_ORDERS_ENDPOINT_NAME = "spot.orders"
USER_BALANCE_ENDPOINT_NAME = "spot.balances"
PONG_CHANNEL_NAME = "spot.pong"

# Timeouts
PING_TIMEOUT = 10.0

# Intervals
# Only used when nothing is received from WS
# 45 seconds should be fine since we get trades, orders and balances via WS



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
