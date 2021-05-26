import pytest
from src.shoe import Shoe

def test_create_shoe():
    assert Shoe() is not None