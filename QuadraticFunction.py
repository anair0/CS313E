import math


class QuadraticFunction (object):

    # Construct an object to represent an equation of the form f(x) = ax^2 + bx + c.
    # For simplicity, the a, b, and c coefficients will be given as ints.
    def __init__(self, a: int, b: int, c: int):
        self.a = a
        self.b = b
        self.c = c

    # Return a list containing the x-coordinates of the root(s) of this quadratic equation.
    # If there are multiple roots, return them sorted in ascending order.
    def roots(self):
        roots = []
        if(self.a != 0 and (self.b ** 2) >= (4*self.a*self.c)):
            root = (-self.b + math.sqrt((self.b ** 2) - 4 * self.a * self.c)) / (2 * self.a)
            roots.append(root)
            root = (- self.b - math.sqrt((self.b ** 2) - 4 * self.a * self.c)) / (2 * self.a)
            if (root != roots[0]):
                roots.append(root)
            roots = sorted(roots)

        return roots

    # Return the location of the vertex as a tuple (x,y).
    def vertex(self):
        x = (-self.b) / (2 * self.a)
        y = self.a * (x ** 2) + self.b * x + self.c
        vertex = (x, y)

        return vertex

    # Return the y-coordinate of the graph at the given x-coordinate.
    def evaluate(self, x):
        y = self.a * (x ** 2) + self.b * x + self.c

        return y

    # Return a string that represents this equation in the form: "f(x) = ax^2 + bx + c"
    # *If the coefficient for a term is 0, the term should not be included.
    def __str__(self):
        if(self.a == 0):
            return "f(x) = " + str(self.b) + 'x + ' + str(self.c)
        if(self.b == 0):
            return "f(x) = " + str(self.a) + 'x^2 + '  + str(self.c)
        if(self.c == 0):
            return "f(x) = " + str(self.a) + 'x^2 + ' + str(self.b) + 'x'
        else:
            return "f(x) = " + str(self.a) + 'x^2 + ' + str(self.b) + 'x + ' + str(self.c)
