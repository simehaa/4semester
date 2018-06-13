def H(x):         # my heaviside function
    if x < 0:     # simply formated with an if/else test
        x = 0
    else:
        x = 1
    return x

def test_H():
    print "test function called"
    expected_0 = 0      # expected is calculated by hand to make sure
    expected_1 = 1      # that the program computes correctly
    tol = 1E-14
    success = abs(expected_0 - H(-10)) < tol and \
              abs(expected_0 - H(-10e-15)) < tol and \
              abs(expected_1 - H(0)) < tol and \
              abs(expected_1 - H(10e-15)) < tol and \
              abs(expected_1 - H(10)) < tol
    msg = 'one or more of the funtions failed'
    assert success, msg

print H(-10), H(-10e-15), H(0), H(10e-15), H(10)  # printing the heaviside function for all values
test_H()   # running the test function

"""
simen@simen-VirtualBox:~/python/uke3$ python Heaviside.py
0 0 1 1 1
test function called
"""
