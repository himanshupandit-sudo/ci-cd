from src.math_operations import add,sub

def test_add():
    assert add(2,3)==5
    assert add(0,0)==0
    assert add(9,0)==9

def test_sub():
    assert sub(-1,-9)== 8
    assert sub(0,0)== 0
    assert sub(5,1)==4
