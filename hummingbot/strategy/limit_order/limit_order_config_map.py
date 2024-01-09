from hummingbot.client.config.config_var import ConfigVar


def market_prompt() -> str:
    connector = limit_order_config_map.get("connector").value
    return f'Enter the Trading Pair you would like to trade on {connector}. (e.g. BTC-USDT) >>> '

limit_order_config_map = {
    "strategy":
        ConfigVar(key="strategy",
                  prompt="",
                  default="limit_order",
        ),
    "connector":
        ConfigVar(key="connector",
                  prompt="Enter the Name of the exchange  >>> ",
                  prompt_on_new=True,
        ),
    "market":
        ConfigVar(key="market",
                  prompt=market_prompt,
                  prompt_on_new=True,
                  is_connect_key=True,
        )
        
        }