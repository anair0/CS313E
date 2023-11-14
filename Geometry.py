#  File: Geometry.py

#  Description: Various classes and functions for Solid Geometry calculations

#  Student Name: Arjun Nair

#  Student UT EID: asn922

#  Course Name: CS 313E

#  Unique Number: 51120

#  Date Created: 2/6/2022

#  Date Last Modified: 2/7/2022

import math
import sys

class Point (object):
    # constructor with default values
    def __init__ (self, x = 0, y = 0, z = 0):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    # create a string representation of a Point
    # returns a string of the form (x, y, z)
    def __str__ (self):
        return '(' + str(self.x) + ', ' + str(self.y) + ', ' + str(self.z) + ')'

    # get distance to another Point object
    # other is a Point object
    # returns the distance as a floating point number
    def distance (self, other):
        return float(math.sqrt(((float(self.x) - float(other.x))**2) + ((float(self.y) - float(other.y))**2)
                               + ((float(self.z) - float(other.z))**2)))

    # test for equality between two points
    # other is a Point object
    # returns a Boolean
    def __eq__ (self, other):
        tol = 1.0e-6
        return (abs(self.x - other.x) < tol) and (abs(self.y - other.y) < tol) and (abs(self.z - other.z) < tol)

class Sphere (object):
    # constructor with default values
    def __init__ (self, x = 0, y = 0, z = 0, radius = 1):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
        self.radius = float(radius)
        self.center = Point(x,y,z)

    # returns string representation of a Sphere of the form:
    # Center: (x, y, z), Radius: value
    def __str__ (self):
        return 'Center: (' + str(self.x) + ', ' + str(self.y) + ', ' + str(self.z) + '), Radius: ' + str(self.radius)

    # compute surface area of Sphere
    # returns a floating point number
    def area (self):
        return float(4 * math.pi * (self.radius ** 2))

    # compute volume of a Sphere
    # returns a floating point number
    def volume (self):
        return float((4 / 3) * math.pi * (self.radius ** 3))

    # determines if a Point is strictly inside the Sphere
    # p is Point object
    # returns a Boolean
    def is_inside_point (self, p):
        return self.center.distance(p) < self.radius

    # determine if another Sphere is strictly inside this Sphere
    # other is a Sphere object
    # returns a Boolean
    def is_inside_sphere (self, other):
        return (self.center.distance(other.center) + other.radius) < self.radius

    #determine if another Sphere is strictly outside this Sphere
    # other is a Sphere object
    # returns a Boolean
    def is_outside_sphere (self, other):
        return self.center.distance(other.center) > other.radius + self.radius

    # determine if a Cube is strictly inside this Sphere
    # determine if the eight corners of the Cube are strictly
    # inside the Sphere
    # a_cube is a Cube object
    # returns a Boolean
    def is_inside_cube (self, a_cube):
        #Takes all of the points of a cube and checks if they are in the Sphere
        x = a_cube.x
        y = a_cube.y
        z = a_cube.z
        side = a_cube.side / 2
        cor_one = Point(x + side, y + side, z + side)
        cor_two = Point(x - side, y - side, z - side)
        cor_three = Point(x + side, y - side, z + side)
        cor_four = Point(x + side, y - side, z - side)
        cor_five = Point(x + side, y + side, z - side)
        cor_six = Point(x - side, y + side, z + side)
        cor_seven = Point(x - side, y - side, z + side)
        cor_eight = Point(x - side, y + side, z - side)
        if(
            self.is_inside_point(cor_one) and
            self.is_inside_point(cor_two) and
            self.is_inside_point(cor_three) and
            self.is_inside_point(cor_four) and
            self.is_inside_point(cor_five) and
            self.is_inside_point(cor_six) and
            self.is_inside_point(cor_seven) and
            self.is_inside_point(cor_eight)
        ):
            return True
        else:
            return False

    # determine if a Cube is strictly outside this Sphere
    # determine if the eight corners of the Cube are strictly
    # outside the Sphere
    # a_cube is a Cube object
    # returns a Boolean
    def is_outside_cube(self, a_cube):
        #Use the 8 vertices of the cube to check if it is outside sphere
        x = a_cube.x
        y = a_cube.y
        z = a_cube.z
        side = a_cube.side / 2
        cor_one = Point(x + side, y + side, z + side)
        cor_two = Point(x - side, y - side, z - side)
        cor_three = Point(x + side, y - side, z + side)
        cor_four = Point(x + side, y - side, z - side)
        cor_five = Point(x + side, y + side, z - side)
        cor_six = Point(x - side, y + side, z + side)
        cor_seven = Point(x - side, y - side, z + side)
        cor_eight = Point(x - side, y + side, z - side)
        if (
                self.is_inside_point(cor_one) == False and
                self.is_inside_point(cor_two) == False and
                self.is_inside_point(cor_three) == False and
                self.is_inside_point(cor_four) == False and
                self.is_inside_point(cor_five) == False and
                self.is_inside_point(cor_six) == False and
                self.is_inside_point(cor_seven) == False and
                self.is_inside_point(cor_eight) == False
        ):
            return True
        else:
            return False

    # determine if a Cylinder is strictly inside this Sphere
    # a_cyl is a Cylinder object
    # returns a Boolean
    def is_inside_cyl (self, a_cyl):
        #Look at Cylinder and Sphere from 2 angles in 2D
        #Top look to see if circle is in circle
        #On the side see if rectangle is inside rectangle
        x = a_cyl.x
        y = a_cyl.y
        z = a_cyl.z
        radius = a_cyl.radius
        height = a_cyl.height / 2
        if(self.center.distance(a_cyl.center) + a_cyl.radius > self.radius):
            return False
        cor_one = Point(x + radius, y, z + height)
        cor_two = Point(x - radius, y, z - height)
        cor_three = Point(x - radius, y, z + height)
        cor_four = Point(x + radius, y, z - height)
        if(
            self.is_inside_point(cor_one) and
            self.is_inside_point(cor_two) and
            self.is_inside_point(cor_three) and
            self.is_inside_point(cor_four)
        ):
            return True
        else:
            return False

    # determine if a Cylinder is strictly outside this Sphere
    # a_cyl is a Cylinder object
    # returns a Boolean
    def is_outside_cyl(self, a_cyl):
        #Uses 2 2D angles to check if cyl is outside sphere
        x = a_cyl.x
        y = a_cyl.y
        z = a_cyl.z
        radius = a_cyl.radius
        height = a_cyl.height / 2
        cor_one = Point(x + radius, y, z + height)
        cor_two = Point(x - radius, y, z - height)
        cor_three = Point(x - radius, y, z + height)
        cor_four = Point(x + radius, y, z - height)
        if (
                self.is_inside_point(cor_one) == False and
                self.is_inside_point(cor_two) == False and
                self.is_inside_point(cor_three) == False and
                self.is_inside_point(cor_four) == False and
                self.center.distance(a_cyl.center) > self.radius + a_cyl.radius
        ):
            return True
        else:
            return False

    # determine if another Sphere intersects this Sphere
    # other is a Sphere object
    # two spheres intersect if they are not strictly inside
    # or not strictly outside each other
    # returns a Boolean
    def does_intersect_sphere (self, other):
        if(self.is_inside_sphere(other) == False and self.is_outside_sphere(other) == False):
            return True
        else:
            return False

    # determine if a Cube intersects this Sphere
    # the Cube and Sphere intersect if they are not
    # strictly inside or not strictly outside the other
    # a_cube is a Cube object
    # returns a Boolean
    def does_intersect_cube (self, a_cube):
        if(self.is_inside_cube(a_cube) == False and self.is_outside_cube(a_cube) == False):
            return True
        else:
            return False

    # return the largest Cube object that is circumscribed
    # by this Sphere
    # all eight corners of the Cube are on the Sphere
    # returns a Cube object
    def circumscribe_cube (self):
        side = (2 * self.radius) / math.sqrt(3)
        x = self.x
        y = self.y
        z = self.z
        return Cube(x,y,z,side)

class Cube (object):
    # Cube is defined by its center (which is a Point object)
    # and side. The faces of the Cube are parallel to x-y, y-z,
    # and x-z planes.
    def __init__ (self, x = 0, y = 0, z = 0, side = 1):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
        self.center = Point(x,y,z)
        self.side = float(side)

    # string representation of a Cube of the form:
    # Center: (x, y, z), Side: value
    def __str__ (self):
        return 'Center: (' + str(self.x) + ', ' + str(self.y) + ', ' + str(self.z) + '), Side: ' + str(self.side)

    # compute the total surface area of Cube (all 6 sides)
    # returns a floating point number
    def area (self):
        return 6 * (self.side ** 2)

    # compute volume of a Cube
    # returns a floating point number
    def volume (self):
        return self.side ** 3

    # determines if a Point is strictly inside this Cube
    # p is a point object
    # returns a Boolean
    def is_inside_point (self, p):
        x = self.x
        y = self.y
        z = self.z
        side = self.side / 2
        cor_one = Point(x + side, y + side, z)
        cor_two = Point(x - side, y - side, z)
        cor_three = Point(x + side, y, z + side)
        cor_four = Point(x - side, y, z - side)
        if(
            p.x < cor_one.x and
            p.x > cor_two.x and
            p.y < cor_one.y and
            p.y > cor_two.y and
            p.z < cor_three.z and
            p.z > cor_four.z
        ):
            return True
        else:
            return False


    # determine if a Sphere is strictly inside this Cube
    # a_sphere is a Sphere object
    # returns a Boolean
    def is_inside_sphere (self, a_sphere):
        x = self.x
        y = self.y
        z = self.z
        side = self.side / 2
        cor_one = Point(x + side, y + side, z)
        cor_two = Point(x - side, y - side, z)
        cor_three = Point(x + side, y, z + side)
        cor_four = Point(x - side, y, z - side)
        x = a_sphere.x
        y = a_sphere.y
        z = a_sphere.z
        radius = a_sphere.radius
        circle_one = Point(x, y + radius, z)
        circle_two = Point(x, y - radius, z)
        circle_three = Point(x - radius, y, z)
        circle_four = Point(x + radius, y, z)
        circle_five = Point(x, y, z + radius)
        circle_six = Point(x, y, z - radius)
        if(
            circle_one.y < cor_one.y and
            circle_two.y > cor_two.y and
            circle_three.x > cor_two.x and
            circle_four.x < cor_one.x and
            circle_five.z < cor_three.z and
            circle_six.z > cor_four.z
        ):
            return True
        else:
            return False

    # determine if another Cube is strictly inside this Cube
    # other is a Cube object
    # returns a Boolean
    def is_inside_cube (self, other):
        x = self.x
        y = self.y
        z = self.z
        side = self.side / 2
        cor_one = Point(x + side, y + side, z)
        cor_two = Point(x - side, y - side, z)
        cor_three = Point(x + side, y, z + side)
        cor_four = Point(x - side, y, z - side)
        x = other.x
        y = other.y
        z = other.z
        side = other.side / 2
        cube_one = Point(x + side, y + side, z)
        cube_two = Point(x - side, y - side, z)
        cube_three = Point(x + side, y, z + side)
        cube_four = Point(x - side, y, z - side)
        if(
            cube_one.x < cor_one.x and
            cube_two.x > cor_two.x and
            cube_one.y < cor_one.y and
            cube_two.y > cor_two.y and
            cube_three.z < cor_three.z and
            cube_four.z > cor_four.z
        ):
            return True
        else:
            return False

    # determine if another Cube is strictly outside this Cube
    # other is a Cube object
    # returns a Boolean
    def is_outside_cube(self, other):
        x = self.x
        y = self.y
        z = self.z
        side = self.side / 2
        cor_one = Point(x + side, y + side, z)
        cor_two = Point(x - side, y - side, z)
        cor_three = Point(x + side, y, z + side)
        cor_four = Point(x - side, y, z - side)
        x = other.x
        y = other.y
        z = other.z
        side = other.side / 2
        cube_one = Point(x + side, y + side, z)
        cube_two = Point(x - side, y - side, z)
        cube_three = Point(x + side, y, z + side)
        cube_four = Point(x - side, y, z - side)
        if (
                ((cube_one.x > cor_one.x and cube_two.x > cor_one.x) or
                 (cube_one.x < cor_two.x and cube_two.x < cor_two.x)) and
                ((cube_one.y > cor_one.y and cube_two.y > cor_one.y) or
                 (cube_one.y < cor_two.y and cube_two.y < cor_two.y)) and
                ((cube_three.z > cor_three.z and cube_four.z > cor_three.z) or
                 (cube_three.z < cor_four.z and cube_four.z < cor_four.z))
        ):
            return True
        else:
            return False

    # determine if a Cylinder is strictly inside this Cube
    # a_cyl is a Cylinder object
    # returns a Boolean
    def is_inside_cylinder (self, a_cyl):
        x = self.x
        y = self.y
        z = self.z
        side = self.side / 2
        cor_one = Point(x + side, y + side, z)
        cor_two = Point(x - side, y - side, z)
        cor_three = Point(x + side, y, z + side)
        cor_four = Point(x - side, y, z - side)
        x = a_cyl.x
        y = a_cyl.y
        z = a_cyl.z
        radius = a_cyl.radius
        height = a_cyl.height / 2
        cyl_one = Point(x, y + radius, z)
        cyl_two = Point(x, y - radius, z)
        cyl_three = Point(x - radius, y, z)
        cyl_four = Point(x + radius, y, z)
        cyl_five = Point(x, y, z + height)
        cyl_six = Point(x, y, z - height)
        if(
            cyl_one.y < cor_one.y and
            cyl_two.y > cor_two.y and
            cyl_three.x > cor_two.x and
            cyl_four.x < cor_one.x and
            cyl_five.z < cor_three.z and
            cyl_six.z > cor_four.z
        ):
            return True
        else:
            return False

    # determine if another Cube intersects this Cube
    # two Cube objects intersect if they are not strictly
    # inside and not strictly outside each other
    # other is a Cube object
    # returns a Boolean
    def does_intersect_cube (self, other):
        if(self.is_inside_cube(other) == False and self.is_outside_cube(other) == False):
            return True
        else:
            return False

    # determine the volume of intersection if this Cube
    # intersects with another Cube
    # other is a Cube object
    # returns a floating point number
    def intersection_volume (self, other):
        x = self.x
        y = self.y
        z = self.z
        side = self.side / 2
        cor_one = Point(x + side, y + side, z)
        cor_two = Point(x - side, y - side, z)
        cor_three = Point(x + side, y, z + side)
        cor_four = Point(x - side, y, z - side)
        x = other.x
        y = other.y
        z = other.z
        side = other.side / 2
        other_one = Point(x + side, y + side, z)
        other_two = Point(x - side, y - side, z)
        other_three = Point(x + side, y, z + side)
        other_four = Point(x - side, y, z - side)
        side_one = 1
        side_two = 1
        side_three = 1
        if(self.does_intersect_cube(other)):
            if(other_one.x < cor_one.x and other_one.x > cor_two.x and other_two.x < cor_two.x):
                side_one = other_one.x - cor_two.x
            if(other_one.x > cor_one.x and other_two.x > cor_two.x and other_two.x < cor_one.x):
                side_one = cor_one.x - other_two.x
            if(other_one.x < cor_one.x and other_one.x > cor_two.x and other_two.x > cor_two.x):
                side_one = other_one.x - other_two.x
            if (other_one.y < cor_one.y and other_one.y > cor_two.y and other_two.y < cor_two.y):
                side_two = other_one.y - cor_two.y
            if (other_one.y > cor_one.y and other_two.y > cor_two.y and other_two.y < cor_one.y):
                side_two = cor_one.y - other_two.y
            if (other_one.y < cor_one.y and other_one.y > cor_two.y and other_two.y > cor_two.y):
                side_two = other_one.y - other_two.y
            if (other_three.z < cor_three.z and other_three.z > cor_four.z and other_four.z < cor_four.z):
                side_three = other_three.z - cor_four.z
            if (other_three.z > cor_three.z and other_four.z > cor_four.z and other_four.z < cor_three.z):
                side_three = cor_three.z - other_four.z
            if (other_three.z < cor_three.z and other_three.z > cor_four.z and other_four.z > cor_four.z):
                side_three = other_three.z - other_four.z
            return float(side_one) * float(side_two) * float(side_three)
    # return the largest Sphere object that is inscribed
    # by this Cube
    # Sphere object is inside the Cube and the faces of the
    # Cube are tangential planes of the Sphere
    # returns a Sphere object
    def inscribe_sphere (self):
        x = self.x
        y = self.y
        z = self.z
        radius = self.side / 2
        return Sphere(x,y,z,radius)

class Cylinder (object):
    # Cylinder is defined by its center (which is a Point object),
    # radius and height. The main axis of the Cylinder is along the
    # z-axis and height is measured along this axis
    def __init__ (self, x = 0, y = 0, z = 0, radius = 1, height = 1):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
        self.radius = float(radius)
        self.height = float(height)
        self.center = Point(x,y,z)

    # returns a string representation of a Cylinder of the form:
    # Center: (x, y, z), Radius: value, Height: value
    def __str__ (self):
        return 'Center: (' + str(self.x) + ', ' + str(self.y) + ', ' + str(self.z) + '), Radius: ' + str(self.radius) \
               + ', Height: ' + str(self.height)

    # compute surface area of Cylinder
    # returns a floating point number
    def area (self):
        return (2 * math.pi * self.radius * self.height) + (2 * math.pi * (self.radius ** 2))

    # compute volume of a Cylinder
    # returns a floating point number
    def volume (self):
        return math.pi * (self.radius ** 2) * self.height

    # determine if a Point is strictly inside this Cylinder
    # p is a Point object
    # returns a Boolean
    def is_inside_point (self, p):
        x = self.x
        y = self.y
        z = self.z
        radius = self.radius
        height = self.height / 2
        cyl_one = Point(x, y + radius, z)
        cyl_two = Point(x, y - radius, z)
        cyl_three = Point(x - radius, y, z)
        cyl_four = Point(x + radius, y, z)
        cyl_five = Point(x, y, z + height)
        cyl_six = Point(x, y, z - height)
        if(
            p.y < cyl_one.y and
            p.y > cyl_two.y and
            p.x > cyl_three.x and
            p.x < cyl_four.x and
            p.z < cyl_five.z and
            p.z > cyl_six.z
        ):
            return True
        else:
            return False

    # determine if a Sphere is strictly inside this Cylinder
    # a_sphere is a Sphere object
    # returns a Boolean
    def is_inside_sphere (self, a_sphere):
        x = self.x
        y = self.y
        z = self.z
        radius = self.radius
        height = self.height / 2
        cyl_one = Point(x, y + radius, z)
        cyl_two = Point(x, y - radius, z)
        cyl_three = Point(x - radius, y, z)
        cyl_four = Point(x + radius, y, z)
        cyl_five = Point(x, y, z + height)
        cyl_six = Point(x, y, z - height)
        x = a_sphere.x
        y = a_sphere.y
        z = a_sphere.z
        radius = a_sphere.radius
        circle_one = Point(x, y + radius, z)
        circle_two = Point(x, y - radius, z)
        circle_three = Point(x - radius, y, z)
        circle_four = Point(x + radius, y, z)
        circle_five = Point(x, y, z + radius)
        circle_six = Point(x, y, z - radius)
        if(
            circle_one.y < cyl_one.y and
            circle_two.y > cyl_two.y and
            circle_three.x > cyl_three.x and
            circle_four.x < cyl_four.x and
            circle_five.z < cyl_five.z and
            circle_six.z > cyl_six.z
        ):
            return True
        else:
            return False

    # determine if a Cube is strictly inside this Cylinder
    # determine if all eight corners of the Cube are inside
    # the Cylinder
    # a_cube is a Cube object
    # returns a Boolean
    def is_inside_cube (self, a_cube):
        x = self.x
        y = self.y
        z = self.z
        radius = self.radius
        height = self.height / 2
        cyl_one = Point(x, y + radius, z)
        cyl_two = Point(x, y - radius, z)
        cyl_three = Point(x - radius, y, z)
        cyl_four = Point(x + radius, y, z)
        cyl_five = Point(x, y, z + height)
        cyl_six = Point(x, y, z - height)
        x = a_cube.x
        y = a_cube.y
        z = a_cube.z
        side = a_cube.side / 2
        cube_one = Point(x + side, y + side, z)
        cube_two = Point(x - side, y - side, z)
        cube_three = Point(x + side, y, z + side)
        cube_four = Point(x - side, y, z - side)
        if(
            cube_one.y < cyl_one.y and
            cube_two.y > cyl_two.y and
            cube_two.x > cyl_three.x and
            cube_one.x < cyl_four.x and
            cube_three.z < cyl_five.z and
            cube_four.z > cyl_six.z
        ):
            return True
        else:
            return False


    # determine if another Cylinder is strictly inside this Cylinder
    # other is Cylinder object
    # returns a Boolean
    def is_inside_cylinder (self, other):
        # Same method of using 2 2D angles to see if circle and rectangle are inside cylinder
        x = self.x
        y = self.y
        z = self.z
        radius = self.radius
        height = self.height / 2
        cyl_five = Point(x, y, z + height)
        cyl_six = Point(x, y, z - height)
        x = other.x
        y = other.y
        z = other.z
        radius = other.radius
        height = other.height / 2
        other_five = Point(x, y, z + height)
        other_six = Point(x, y, z - height)
        if(
            self.center.distance(other.center) + other.radius < self.radius and
            other_five.z < cyl_five.z and
            other_five.z > cyl_six.z and
            other_six.z > cyl_six.z and
            other_six.z < cyl_five.z
        ):
            return True
        else:
            return False

    # determine if another Cylinder is strictly outside this Cylinder
    # other is Cylinder object
    # returns a Boolean
    def is_outside_cylinder(self, other):
        #Same method of using 2 2D angles to see if circle and rectangle are outside cylinder
        x = self.x
        y = self.y
        z = self.z
        height = self.height / 2
        cyl_five = Point(x, y, z + height)
        cyl_six = Point(x, y, z - height)
        x = other.x
        y = other.y
        z = other.z
        height = other.height / 2
        other_five = Point(x, y, z + height)
        other_six = Point(x, y, z - height)
        cond_one = False
        cond_two = False
        cond_three = False
        if(self.center.distance(other.center) > self.radius + other.radius):
            cond_one = True
            cond_two = True
        if(other_five.z > cyl_five.z and other_six.z > cyl_five.z):
            cond_three = True
        if(other_five.z < cyl_six.z and other_six.z < cyl_six.z):
            cond_three = True
        if(cond_three == True):
            cond_one = True
            cond_two = True

        if(cond_one and cond_two and cond_three):
            return True
        else:
            return False

    # determine if another Cylinder intersects this Cylinder
    # two Cylinder object intersect if they are not strictly
    # inside and not strictly outside each other
    # other is a Cylinder object
    # returns a Boolean
    def does_intersect_cylinder (self, other):
        if (self.is_inside_cylinder(other) == False and self.is_outside_cylinder(other) == False):
            return True
        else:
            return False

def main():
    # read data from standard input

    # read the coordinates of the first Point p
    p = sys.stdin.readline()
    p = p.strip()
    p = p.split()
    x = p[0]
    y = p[1]
    z = p[2]
    # create a Point object
    p = Point(x,y,z)
    # read the coordinates of the second Point q
    q = sys.stdin.readline()
    q = q.strip()
    q = q.split()
    x = q[0]
    y = q[1]
    z = q[2]
    # create a Point object
    q = Point(x,y,z)
    # read the coordinates of the center and radius of sphereA
    sphereA = sys.stdin.readline()
    sphereA = sphereA.strip()
    sphereA = sphereA.split()
    x = sphereA[0]
    y = sphereA[1]
    z = sphereA[2]
    radius = sphereA[3]
    # create a Sphere object
    sphereA = Sphere(x,y,z,radius)
    # read the coordinates of the center and radius of sphereB
    sphereB = sys.stdin.readline()
    sphereB = sphereB.strip()
    sphereB = sphereB.split()
    x = sphereB[0]
    y = sphereB[1]
    z = sphereB[2]
    radius = sphereB[3]
    # create a Sphere object
    sphereB = Sphere(x,y,z,radius)
    # read the coordinates of the center and side of cubeA
    cubeA = sys.stdin.readline()
    cubeA = cubeA.strip()
    cubeA = cubeA.split()
    x = cubeA[0]
    y = cubeA[1]
    z = cubeA[2]
    side = cubeA[3]
    # create a Cube object
    cubeA = Cube(x,y,z,side)
    # read the coordinates of the center and side of cubeB
    cubeB = sys.stdin.readline()
    cubeB = cubeB.strip()
    cubeB = cubeB.split()
    x = cubeB[0]
    y = cubeB[1]
    z = cubeB[2]
    side = cubeB[3]
    # create a Cube object
    cubeB = Cube(x,y,z,side)
    # read the coordinates of the center, radius and height of cylA
    cylA = sys.stdin.readline()
    cylA = cylA.strip()
    cylA = cylA.split()
    x = cylA[0]
    y = cylA[1]
    z = cylA[2]
    radius = cylA[3]
    height = cylA[4]
    # create a Cylinder object
    cylA = Cylinder(x,y,z,radius,height)
    # read the coordinates of the center, radius and height of cylB
    cylB = sys.stdin.readline()
    cylB = cylB.strip()
    cylB = cylB.split()
    x = cylB[0]
    y = cylB[1]
    z = cylB[2]
    radius = cylB[3]
    height = cylB[4]
    # create a Cylinder object
    cylB = Cylinder(x,y,z,radius,height)
    # print if the distance of p from the origin is greater
    # than the distance of q from the origin
    strng = 'is not'
    origin = Point(0,0,0)
    if(p.distance(origin) > q.distance(origin)):
        strng = 'is'
    print("Distance of Point p from the origin " + str(strng) + " greater than the distance of Point q from the origin")
    # print if Point p is inside sphereA
    strng = 'is not'
    if(sphereA.is_inside_point(p)):
        strng = 'is'
    print("Point p " + str(strng) + " inside sphereA")
    # print if sphereB is inside sphereA
    strng = 'is not'
    if(sphereA.is_inside_sphere(sphereB)):
        strng = 'is'
    print("sphereB " + str(strng) + " inside sphereA")
    # print if cubeA is inside sphereA
    strng = 'is not'
    if(sphereA.is_inside_cube(cubeA)):
        strng = 'is'
    print("cubeA " + str(strng) + " inside sphereA")
    # print if cylA is inside sphereA
    strng = 'is not'
    if (sphereA.is_inside_cyl(cylA)):
        strng = 'is'
    print("cylA " + str(strng) + " inside sphereA")
    # print if sphereA intersects with sphereB
    strng = 'does not'
    if (sphereB.does_intersect_sphere(sphereA)):
        strng = 'does'
    print("sphereA " + str(strng) + " intersect sphereB")
    # print if cubeB intersects with sphereB
    strng = 'does not'
    if (sphereB.does_intersect_cube(cubeB)):
        strng = 'does'
    print("cubeB " + str(strng) + " intersect sphereB")
    # print if the volume of the largest Cube that is circumscribed
    # by sphereA is greater than the volume of cylA
    strng = 'is not'
    circum_cube = sphereA.circumscribe_cube()
    cube_vol = circum_cube.volume()
    cyl_vol = cylA.volume()
    if (cube_vol > cyl_vol):
        strng = 'is'
    print("Volume of the largest Cube that is circumscribed by sphereA " + str(strng)
          + " greater than the volume of cylA")
    # print if Point p is inside cubeA
    strng = 'is not'
    if (cubeA.is_inside_point(p)):
        strng = 'is'
    print("Point p " + str(strng) + " inside cubeA")
    # print if sphereA is inside cubeA
    strng = 'is not'
    if (cubeA.is_inside_sphere(sphereA)):
        strng = 'is'
    print("sphereA " + str(strng) + " inside cubeA")
    # print if cubeB is inside cubeA
    strng = 'is not'
    if (cubeA.is_inside_cube(cubeB)):
        strng = 'is'
    print("cubeB " + str(strng) + " inside cubeA")
    # print if cylA is inside cubeA
    strng = 'is not'
    if (cubeA.is_inside_cylinder(cylA)):
        strng = 'is'
    print("cylA " + str(strng) + " inside cubeA")
    # print if cubeA intersects with cubeB
    strng = 'does not'
    if (cubeB.does_intersect_cube(cubeA)):
        strng = 'does'
    print("cubeA " + str(strng) + " intersect cubeB")
    # print if the intersection volume of cubeA and cubeB
    # is greater than the volume of sphereA
    strng = 'is not'
    intersection = cubeA.intersection_volume(cubeB)
    if (intersection > sphereA.volume()):
        strng = 'is'
    print("Intersection volume of cubeA and cubeB " + str(strng) + " greater than the volume of sphereA")
    # print if the surface area of the largest Sphere object inscribed
    # by cubeA is greater than the surface area of cylA
    strng = 'is not'
    sphere = cubeA.inscribe_sphere()
    if (sphere.area() > cylA.area()):
        strng = 'is'
    print("Surface area of the largest Sphere object inscribed by cubeA " + str(strng) + " greater than the surface area of cylA")
    # print if Point p is inside cylA
    strng = 'is not'
    if (cylA.is_inside_point(p)):
        strng = 'is'
    print("Point p " + str(strng) + " inside cylA")
    # print if sphereA is inside cylA
    strng = 'is not'
    if (cylA.is_inside_sphere(sphereA)):
        strng = 'is'
    print("sphereA " + str(strng) + " inside cylA")
    # print if cubeA is inside cylA
    strng = 'is not'
    if (cylA.is_inside_cube(cubeA)):
        strng = 'is'
    print("cubeA " + str(strng) + " inside cylA")
    # print if cylB is inside cylA
    strng = 'is not'
    if (cylA.is_inside_cylinder(cylB)):
        strng = 'is'
    print("cylB " + str(strng) + " inside cylA")
    # print if cylB intersects with cylA
    strng = 'does not'
    if (cylA.does_intersect_cylinder(cylB)):
        strng = 'does'
    print("cylB " + str(strng) + " intersect cylA")

if __name__ == "__main__":
    main()
