from polynomials import Polynomial

def test_values():
    p = Polynomial([2,4,1]) # 2 + 4x + x**2
    assert  p(-2) == -2 and p(0) == 2 and p(1) == 7
    
def test_add():
    a = Polynomial([1,0,3,-4])
    b = Polynomial([-1,2,0])
    assert a+b == [0,2,3,-4]
    
def test_sub():
    a = Polynomial([5,0,-2])
    b = Polynomial([-3,2,1,4])
    assert a-b == [8,-2,-3,-4]

def test_degree():
    q = Polynomial([0,1,0,3])
    assert q.degree() == 3
    
test_values()
test_add()
test_sub()
test_degree()