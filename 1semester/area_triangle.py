x1 = float(0)              # All coordinates of the triangle
y1 = float(0)
x2 = float(1)
y2 = float(0)
x3 = float(0)
y3 = float(2)

def triangle_area(x1, y1, x2, y2, x3, y3):
    A = 1./2*(x2*y3 - x3*y2 - x1*y3 + x3*y1 + x1*y2 + x2*y1)  # function for area of a triangle in a coordinate system
    return A      # Returning area value, A

print 'the area of the triangle (%i, %i) (%i, %i) (%i, %i) is' \
       % (x1, y1, x2, y2, x3, y3), triangle_area(x1, y1, x2, y2, x3, y3)

def test_triangle_area():        # funtion test from the exercise
    """
    Verify the area of a triangle with vertex coordinates
    (0,0), (1,0), and (0,2).
    """
    v1 = (0,0); v2 = (1,0); v3 = (0,2)
    vertices = [v1, v2, v3]
    expected = 1
    computed = triangle_area(x1, y1, x2, y2, x3, y3)
    tol = 1E-14
    success = abs(expected - computed) < tol
    msg = 'computed area=%g != %g (expected)' % \
          (computed, expected)
    assert success, msg

test_triangle_area()

"""
simen@simen-VirtualBox:~/python/uke3$ python area_triangle.py
the area of the triangle (0, 0) (1, 0) (0, 2) is 1.0
"""
