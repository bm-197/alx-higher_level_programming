#!/usr/bin/python3
"""Define a class Rectangle inheriting from base class."""


class Rectangle(Base):
    """Represents the Rectangle.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize the rectangle.
        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
            x (int): The x coordinate of the new Rectangle.
            y (int): The y coordinate of the new Rectangle.
            id (int): The identity of the new Rectangle.
        """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """Accessing the width."""
        return self.__width

    @width.setter
    def width(self, value):
        """setting the width."""
        if type(value) != int:
            raise TyepError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Set/get the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Set/get the x coordinate of the Rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Set/get the y coordinate of the Rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """The area of the rectangle."""
        return self.__width * self.__height
    def display(self):
        """Prints in stdout the Rectangle with # character."""
        [print(" ") for m in range(self.__y)]
        for i in range(self.__height):
            [print(" ", end="") for n in range(self.__x)]
            [print("#", end="") for j in range(self.__width)]
            print("")
    def __str__(self):
        """Return the str() representation of the rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)

    def update(self, *args, **kwargs):
        """Assignes an argument to each attribute."""
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a = 0:
                    if arg == None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                else if a == 1:
                    self.width = arg
                elif a == 2:
                    self.height = arg
                elif a == 3:
                    self.x = arg
                elif a == 4:
                    self.y = arg
                a += 1
        if kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k = "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v
