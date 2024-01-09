from decimal import Decimal
import logging
from hummingbot.core.event.events import OrderType
from hummingbot.strategy.market_trading_pair_tuple import MarketTradingPairTuple
from hummingbot.strategy.strategy_py_base import StrategyPyBase
from hummingbot.logger import HummingbotLogger

hws_logger = None

class LimitOrder(StrategyPyBase):
    """
    This strategy places limit orders on the market.
    """


    @classmethod
    def logger(cls) -> HummingbotLogger:
        global hws_logger
        if hws_logger is None:
            hws_logger = logging.getLogger(__name__)
        return hws_logger
    
    def __init__(self,
                 market_info: MarketTradingPairTuple,):
        super().__init__()
        self._market_info = market_info
        self._connector_ready = False
        self._order_completed = False
        self.add_markets([self._market_info.market])
        
    def tick(self, timestamp: float):
        if not self._connector_ready:
            self._connector_ready = self._market_info.market.ready
            if not self._connector_ready:
                self.logger().warning("Connector is not ready. Waiting...")
                return
            else:
                self.logger().warning("Connector is ready. trading started!")
                
        if not self._order_completed:
            # The get_mid_price method gets the mid price of the coin and
            # stores it. This method is derived from the MarketTradingPairTuple class.
            mid_price = self._market_info.get_mid_price() 

            # The buy_with_specific_market method executes the trade for you. This     
            # method is derived from the Strategy_base class. 
            order_id = self.buy_with_specific_market(
                self._market_info,  # market_trading_pair_tuple
                Decimal("0.005"),   # amount
                OrderType.LIMIT,    # order_type
                mid_price           # price
            )
            self.logger().info(f"Submitted limit buy order {order_id}")
            self._order_completed = True
            if not self._order_completed:
            # The get_mid_price method gets the mid price of the coin and
            # stores it. This method is derived from the MarketTradingPairTuple class.
                 mid_price = self._market_info.get_mid_price() 

            # The buy_with_specific_market method executes the trade for you. This     
            # method is derived from the Strategy_base class. 
                 order_id = self.buy_with_specific_market(
                self._market_info,  # market_trading_pair_tuple
                Decimal("0.005"),   # amount
                OrderType.LIMIT,    # order_type
                mid_price           # price
            )
                 self.logger().info(f"Submitted limit buy order {order_id}")
                 self._order_completed = True



    def did_complete_buy_order(self, order_completed_event):
        self.logger().info(f"Your limit buy order {order_completed_event.order_id} has been executed")
        self.logger().info(order_completed_event)