from lib.order_confirmation import *
from lib.takeaway import *
from unittest.mock import Mock

def test_order_confirmation():
    fake_takeaway = Mock()
    fake_takeaway.order = ('Chicken Katsu Curry', 2)
    fake_takeaway.calculate_total.return_value = {'Chicken Katsu Curry': 8.40}
    order_confirmation = OrderConfirmation(fake_takeaway, '07340415483')
    result = order_confirmation.send_confirmation()
    assert result == True