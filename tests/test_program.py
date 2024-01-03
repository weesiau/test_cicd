import os
import sys
import pytest
from main import program

def test_default():
    result = program.func(3)
    assert result == 4

def test_1():
    assert True == False