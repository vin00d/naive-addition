from src.add import add
import numpy as np

def test_add():
    assert add(1) == 101

def test_add_np():
    assert (add(np.array([1, 2])) == [101, 102]).all()

def test_add_np2():
    assert (add(np.array([1]), np.array([3])) == [4]).all()