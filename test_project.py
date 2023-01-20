from project import *

def test_orderFood():
    assert orderFood("1") == print("\nMa ma mia!")
    assert orderFood("v") == print("Invalid")

def test_bookRoom():
    assert bookRoom(1,2) == True

def test_hotelService():
    assert hotelService(4,5) == print("Too busy!")
