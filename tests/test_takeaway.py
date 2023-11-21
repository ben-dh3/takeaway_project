from lib.takeaway import *

def test_takeaway_menu():
    takeaway = Takeaway()
    assert takeaway.menu == [
        {'Chicken Katsu Curry': 8.40}, 
        {'Vegetable Yakisoba': 7.80}
        ]

def test_takeaway_order():
    takeaway = Takeaway()
    order1 = takeaway.order('Chicken Katsu Curry', 2)
    assert order1 == [
        {'Chicken Katsu Curry': 16.8}
    ]
    order2 = takeaway.order('Vegetable Yakisoba', 3)
    assert order2 == [ 
        {'Chicken Katsu Curry': 16.8},
        {'Vegetable Yakisoba': 23.4}
    ]

def test_calculate_total():
    takeaway = Takeaway()
    order1 = takeaway.order('Chicken Katsu Curry', 2)
    order2 = takeaway.order('Vegetable Yakisoba', 3)
    result = takeaway.calculate_total()
    assert result == [ 
        {'Chicken Katsu Curry': 16.8},
        {'Vegetable Yakisoba': 23.4},
        {'Total Cost': 40.2}
    ] 

