from integrator import integrate
from numpy_integrator import numpy_integrator

def test_integral_of_linear_function():
    f = lambda x: 2*x
    computed_for = integrate(f,0,1,1e7)
    computed_numpy = numpy_integrator(f,0,1,1e7)
    expected = 1.
    success = abs(computed_for - expected) < 1e-4 and abs(computed_numpy - expected) < 1e-4 
    assert success
    
def test_integral_of_constant_function():
    f = lambda x: 2
    computed_for = integrate(f,0,1,100)
    computed_numpy = numpy_integrator(f,0,1,100)
    expected = 2
    success = computed_for == expected and (computed_numpy - expected) < 1e-16
    assert success 
    

test_integral_of_constant_function()
test_integral_of_linear_function()

"""
runfile('C:/Users/simen/INF3331-Simehaa/assignment4/test_integrator.py', wdir='C:/Users/simen/INF3331-Simehaa/assignment4')
Reloaded modules: integrator, numpy_integrator
"""