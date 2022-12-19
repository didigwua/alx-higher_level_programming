#!/usr/bin/python3
class Rectangle:
    """ class that defines a rectangle """
    number_of_instances = 0
    """ Incremented during each new instance instantiation
    Decremented during each instance deletion """
    print_symbol = '#'
    def __init__(self, width=0, height=0):
        """ constructor """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ setter """
        if type(value) not in [int]:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ setter """
        if type(value) not in [int]:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """ Public instance method that returns the rectangle area """
        return self.width * self.height

    def perimeter(self):
        """ Public instance method that returns the rectangle perimeter """
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """ return a string for print """
        string = ''
        if self.width == 0 or self.height == 0:
            return string
        else:
            iterable = []
            for i in range(self.height):
                iterable.append('#' * self.width)
                if i < (self.height - 1):
                    iterable.append('\n')
            return string.join(iterable)

    def __repr__(self):
        """ return a string representation of the rectangle
        to be able to recreate a new instance by using eval() """
        return 'Rectangle({:d}, {:d})'.format(self.width, self.height)

    def __del__(self):
        """ Instance method called when an instance is delete  """
        Rectangle.number_of_instances -= 1
        print('Bye rectangle...')
