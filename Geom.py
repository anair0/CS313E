import math

class Point (object):
    # constructor
    def __init__ (self, x = 0, y = 0):
        self.x = x
        self.y = y

    # get the distance to another Point object
    def dist (self, other):
        return math.hypot (self.x - other.x, self.y - other.y)

    # string representation of a Point object
    def __str__ (self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'

    # test for equality of two Point objects
    #def __eq__ (self, other):
    #    tol = 1.0e-6
    #    return (abs(self.x - other.x) < tol) and (abs(self.y - other.y) < tol)

class Circle (object):
    # constructor
    def __init__ (self, radius = 1, x = 0, y = 0):
        self.radius = radius
        self.center = Point (x, y)

    # compute the circumference
    def circumference (self):
        return 2 * math.pi * self.radius

    # compute the area
    def area (self):
        return math.pi * self.radius * self.radius

    # determine if a Point is strictly inside the Circle
    def point_inside (self, p):
        return self.center.dist(p) < self.radius

    # determine if a Circle c is strictly inside the Circle
    def circle_inside (self, c):
        return self.center.dist(c.center) + c.radius < self.radius

    # determine if a Circle c is strictly outside the Circle
    def circle_outside (self, c):
        dist_centers = self.center.dist(c.center)
        return dist_centers > self.radius + c.radius 

    # determines if a Circle c intersects the Circle
    def circle_intersect (self, c):
        if(self.circle_outside(c) == False and self.circle_inside(c) == False):
            return True
        else:
            return False

def main():
    # create Point objects
    a = Point(3,8)
    b = Point (3,8)
    c = a
    d = b

    x = (c==d)
    y = (b==d)

    print(x)
    print(y)

    #print the Point objects
    print(a)
    print(b)

    #test for equality of Point objects
    if (b == c):
        print ('Point objects are equal')
    else:
        print ('Point objects are not equal')

    cir = Circle(3, 0, 0)
    cir2 = Circle(2, 1, 1)
    print(cir.circle_outside(cir2))
    print(cir.circle_intersect(cir2))

main()
