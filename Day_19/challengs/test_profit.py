import pytest

from profit_calu import profit  # Replace 'your_module' with the actual module name


@pytest.mark.parametrize(
    "info, expected",
    [
        ({"cost_price": 32.67, "sell_price": 45.00, "inventory": 1200}, 14796),
        ({"cost_price": 0.1, "sell_price": 0.18, "inventory": 259800}, 20784),
        ({"cost_price": 185.00, "sell_price": 299.99, "inventory": 300}, 34497),
        ({"cost_price": 378.11, "sell_price": 990.00, "inventory": 99}, 60577),
        ({"cost_price": 4.67, "sell_price": 5.00, "inventory": 78000}, 25740),
        ({"cost_price": 19.87, "sell_price": 110.00, "inventory": 350}, 31546),
        ({"cost_price": 2.91, "sell_price": 4.50, "inventory": 6000}, 9540),
        ({"cost_price": 68.01, "sell_price": 149.99, "inventory": 500}, 40990),
        ({"cost_price": 1.45, "sell_price": 8.50, "inventory": 10000}, 70500),
        ({"cost_price": 10780, "sell_price": 34999, "inventory": 10}, 242190),
    ],
)
def test_profit(info, expected):
    assert profit(info) == expected
