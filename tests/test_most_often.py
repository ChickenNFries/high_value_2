# File: tests/test_most_often.py

from lib.most_often import MostOften

def test_most_often_instantiates_list_parameter():
    my_list = [1, 1, 2, 3, 4]
    mo = MostOften(my_list)
    assert mo.starting_list == my_list

def test_most_often_can_add_new_item_to_list():
    mo = MostOften([1, 1, 2, 3, 4])
    mo.add_new(9)
    assert mo.starting_list == [1, 1, 2, 3, 4, 9]

def test_most_often_returns_most_often():
    mo = MostOften([1, 1, 2, 3, 4, 9])
    assert mo.get_most_often() == 1

def test_most_often_only_one_parameter():
    mo = MostOften([1, 2])
    assert mo.get_most_often() == "no clear winner"