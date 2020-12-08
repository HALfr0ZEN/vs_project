"""Calculate triangle."""
import math


class Triangle:
    """
    Class of the triangle.

    :ivar
        point_a, point_b, point_c:
            used for storing the points inserted by user
        a, b, c:
            used for storing the calculated sides
    >>> 'There is no reason to test this'
    'There is no reason to test this'
    """

    def __init__(self, point_a, point_b, point_c):
        """
        Define points and sides of the triangle.

        :param
            point_a, point_b, point_c:
                used for transfer points to self.points
        >>> 'There is no reason to test this'
        'There is no reason to test this'
        """
        self.point_a = point_a
        self.point_b = point_b
        self.point_c = point_c
        self.a, self.b, self.c = self.side_lenght()

    def side_lenght(self):
        """
        Take inserted points and calculate sides.

        :return: [float, float, float] -> list
        >>> tr = Triangle([1,0], [0,1], [1,1])
        >>> tr.c
        1.0
        """
        sides = (self.point_a, self.point_b), \
                (self.point_a, self.point_c), \
                (self.point_b, self.point_c)

        return [
            math.sqrt(pow(i[0][0] - i[1][0], 2) + pow(i[0][1] - i[1][1], 2))
            for i in sides]

    def is_able(self):
        """
        Check if the triangle is able to construct.

        :return: True | False
        >>> tr = Triangle([1,0], [0,1], [1,1])
        >>> tr.is_able()
        True
        """
        a, b, c = self.a, self.b, self.c

        if a + b > c and a + c > b and c + b > a:
            return True
        else:
            return False

    def is_rectangular(self):
        """
        Check if there is 90 degrees corner in the triangle.

        :return: True | False
        >>> tr = Triangle([1,0], [0,1], [1,1])
        >>> tr.is_rectangular()
        True
        """
        sides: list[float] = [self.a, self.b, self.c]
        sides.sort(reverse=True)

        if round(sides[0] * sides[0]) == sides[1] * sides[1] + sides[2] * \
                sides[2]:
            return True
        else:
            return False

    def perimeter(self):
        """
        Calculate the other contour of the triangle.

        :return: perimeter of the triangle (float)
        >>> tr = Triangle([1,0], [0,1], [1,1])
        >>> round(tr.perimeter(), 2)
        3.41
        """
        return self.a + self.b + self.c

    def area(self) -> float:
        """
        Calculate the inner area of the triangle.

        :return: Area of the triangle (float)
        >>> tr = Triangle([1,0], [0,1], [1,1])
        >>> round(tr.area(), 2)
        0.5
        """
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))


def input_values(point_name):
    """
    User input method. Split user input into list.

    :param point_name: name of the point (char)
    :return: True, user input (list[int, int]) -> (tuple) | False
    >>> 'There is no way of testing this'
    'There is no way of testing this'
    """
    point = str_list_to_int(
        input(f"Zadejte souřadnice bodu {point_name}: ").split(","))
    if point:
        return point
    else:
        print("Zadejte souřadnice ve správném formátu! například: 1,1")
        return input_values(point_name)


def str_list_to_int(list_to_convert):
    """
    Check if user input is in the right format.

    :param list_to_convert: user input converted to list (list[str])
    :return: True & User input converted to (int) -> (tuple) | False
    >>> str_list_to_int(["1", "1"])[1]
    (1, 1)
    """
    try:
        return True, (int(list_to_convert[0]), int(list_to_convert[1]))
    except ValueError or NameError:
        return False
