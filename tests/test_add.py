from src.add import add
import numpy as np

def test_add():
    assert add(1) == 101

def test_add_np():
    assert add(np.array([1])) == np.array([101])