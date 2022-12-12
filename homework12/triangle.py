# 1. Доопрацюйте класс Point так, щоб в атрибути x та y обʼєктів цього класу можна було записати тільки обʼєкти класу
# int або float
# 2. Доопрацюйте класс Line так, щоб в атрибути begin та end обʼєктів цього класу можна було записати
# тільки обʼєкти класу Point
# 3. Створіть класс Triangle (трикутник), який задається трьома точками (обʼєкти классу
# Point).
# 4. Реалізуйте перевірку даних, аналогічно до класу Line. Визначет метод, що містить площу трикутника. Для
# обчислень можна використати формулу Герона (https://en.wikipedia.org/wiki/Heron%27s_formula)

from abc import ABC, abstractmethod


class Point:
    x = 0
    y = 0

    def __init__(self, x, y):
        if not type(x) in {int, float} or not type(y) in {int, float}:
            print('Error: only int and float parameters are allowed')
            raise TypeError

        self.x = x
        self.y = y

    def __str__(self):
        return f'Object of class {self.__class__.__name__} with coordinates: x = {self.x}, y = {self.y}'

    def __add__(self, other):
        """
        Creates new object by adding vertices of summed objects
        Point + Point = Line
        Point + Line = Triangle
        (not implemented yet) Point + Triangle =  Quadrilateral
        """
        supported_figure_classes = (Point, Line, Triangle)

        if not isinstance(other, supported_figure_classes):
            print(f'addition supported only for classes {supported_figure_classes} for other')
            raise TypeError

        if isinstance(other, Point):
            return Line(self, other)

        if isinstance(other, Line):
            return Triangle(self, other.begin, other.end)

        if isinstance(other, Triangle):
            raise NotImplementedError

    def __eq__(self, other):
        """
        Compares Point objects. They are equal if their both coordinates are equal
        """
        if not isinstance(other, Point):
            print('equality supported only for two objects of Point class')
            raise TypeError

        return self.x == other.x and self.y == other.y


class Figure(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def __eq__(self, other):
        pass

    def area(self):
        pass

    def length(self):
        pass


class Line(Figure):
    begin = Point(0, 0)
    end = Point(0, 0)

    def __init__(self, begin, end):
        if not isinstance(begin, Point) or not isinstance(end, Point):
            print('Please pass as parameters only objects of Point class')
            raise TypeError
        self.begin = begin
        self.end = end

    def __str__(self):
        return f'Object of class {self.__class__.__name__} with points coordinates: ' \
               f'begin = ({self.begin.x}, {self.begin.y}), end = ({self.end.x}, {self.end.y})'

    def __add__(self, other):
        """
        Creates new object by adding vertices of summed objects
        LIne + Point = Triangle
        (not implemented yet) Line + Line =  Quadrilateral
        """
        supported_figure_classes = (Point, Line)

        if not isinstance(other, supported_figure_classes):
            print(f'addition supported only for classes {supported_figure_classes} for other')
            raise TypeError

        if isinstance(other, Point):
            return Triangle(self.begin, self.end, other)

        if isinstance(other, Line):
            raise NotImplementedError

    def __eq__(self, other):
        """
        Considers two lines equal if their lengths are equal
        """
        if not isinstance(other, Line):
            print('Comparison supported only for two objects of Line class')
            raise TypeError
        return self.length == other.length

    def __gt__(self, other):
        """
        Compares lengths of two lines when Line objects are compared
        """
        if not isinstance(other, Line):
            print('Comparison supported only for two objects of Line class')
            raise TypeError
        return self.length > other.length

    def __ge__(self, other):
        """
        Compares lengths of two lines when Line objects are compared
        """
        if not isinstance(other, Line):
            print('Comparison supported only for two objects of Line class')
            raise TypeError
        return self.length >= other.length

    # commented because __eq__, __gt__ and __ge__ is enough to work. There is no other specific logic in lt and le
    # def __lt__(self, other):
    #     """
    #     Compares lengths of two lines when Line objects are compared
    #     """
    #     if not isinstance(other, Line):
    #         print('Comparison supported only for two objects of Line class')
    #         raise TypeError
    #     return self.length < other.length

    # def __le__(self, other):
    #     """
    #     Compares lengths of two lines when Line objects are compared
    #     """
    #     if not isinstance(other, Line):
    #         print('Comparison supported only for two objects of Line class')
    #         raise TypeError
    #     return self.length <= other.length

    @property
    def length(self) -> float:
        res = ((self.begin.x - self.end.x)**2 + (self.begin.y - self.end.y)**2)**0.5
        return res


class Triangle(Figure):
    vertex_coord_1 = Point(0, 0)
    vertex_coord_2 = Point(0, 0)
    vertex_coord_3 = Point(0, 0)
    vertices_tuple = (vertex_coord_1, vertex_coord_2, vertex_coord_3)

    def __init__(self, point1, point2, point3):
        if not isinstance(point1, Point) or not isinstance(point2, Point) or not isinstance(point3, Point):
            print('Please pass as parameters only objects of Point class')
            raise TypeError

        if point1 == point2 or point2 == point3 or point3 == point1:
            print('Please pass 3 different points into the Triangle class')
            raise ValueError

        self.vertex_coord_1 = point1
        self.vertex_coord_2 = point2
        self.vertex_coord_3 = point3

    def __str__(self):
        return f'Object of class {self.__class__.__name__} with vertices coordinates: ' \
               f'vertex_coord_1 = ({self.vertex_coord_1.x}, {self.vertex_coord_1.y}), ' \
               f'vertex_coord_2 = ({self.vertex_coord_2.x}, {self.vertex_coord_2.y}), ' \
               f'vertex_coord_3 = ({self.vertex_coord_3.x}, {self.vertex_coord_3.y})'

    def __eq__(self, other):
        """
        Considers two Triangles equal if the set of length of their sides are equal
        """
        if not isinstance(other, Triangle):
            print('equality supported only for two objects of Triangle class')
            raise TypeError

        return set(self.side_lengths_tuple) == set(other.side_lengths_tuple)

    @property
    def sides_tuple(self) -> tuple:
        """
        Creates a tuple with sides of triangles - objects of Line class
        """
        side_triangle_1 = Line(self.vertex_coord_1, self.vertex_coord_2)
        side_triangle_2 = Line(self.vertex_coord_2, self.vertex_coord_3)
        side_triangle_3 = Line(self.vertex_coord_3, self.vertex_coord_1)
        return side_triangle_1, side_triangle_2, side_triangle_3

    @property
    def side_lengths_tuple(self) -> tuple:
        return tuple(map(lambda x: x.length, self.sides_tuple))

    @property
    def perimetr_triangle(self) -> float:
        return sum(self.side_lengths_tuple)

    @property
    def semiperimetr_triangle(self) -> float:
        return self.perimetr_triangle / 2

    @property
    def area(self) -> float:
        """
        Returns area of a triangle using Heron's formula
        """
        sem_per = self.semiperimetr_triangle
        sides = self.side_lengths_tuple
        area_res = (sem_per * (sem_per - sides[0]) * (sem_per - sides[1]) * (sem_per - sides[2]))**0.5

        return area_res


p1 = Point(0, 0)
p2 = Point(0, 4)
p3 = Point(3, 0)
print(f'Point1: {p1}')
print(f'Point2: {p2}')
print(f'Point3: {p3}')

my_new_triangle = Triangle(p1, p2, p3)
print(f'my_new_triangle: {my_new_triangle}')
print(f'my_new_triangle has an area of -->  {my_new_triangle.area}')

# changing some random vertex
my_new_triangle.vertex_coord_1.x, my_new_triangle.vertex_coord_1.y = 10, 11
print(f'my_new_triangle: {my_new_triangle}')
print(f'my_new_triangle has an area of -->  {my_new_triangle.area}')

# changing it back
my_new_triangle.vertex_coord_1.x, my_new_triangle.vertex_coord_1.y = 0, 0


# Custom addition and comparison methods for lulz

line_with_params = Line(p1, p2)
print(f'line_with_params: {line_with_params}')

# Here the line is created by adding two points
line_by_addition = p2 + p1
print(f'line_by_addition: {line_by_addition}')

# Different Lines instances created with the same points are equal (because we compare their lengths)
print(f'line_with_params == line_by_addition: {line_with_params == line_by_addition}')
print(f'line_with_params >= line_by_addition: {line_with_params >= line_by_addition}')
print(f'line_with_params <= line_by_addition: {line_with_params <= line_by_addition}')
print(f'line_with_params < line_by_addition: {line_with_params < line_by_addition}')
print(f'line_with_params > line_by_addition: {line_with_params > line_by_addition}')


# But when we compare different lines (with different lengths) - they are not equal:
line_bigger = Line(p1, p2)
line_smaller = Line(p3, p1)
print(f'line_bigger == line_smaller: {line_bigger == line_smaller}')
print(f'line_bigger != line_smaller: {line_bigger != line_smaller}')
print(f'line_bigger > line_smaller: {line_bigger > line_smaller}')
print(f'line_bigger >= line_smaller: {line_bigger >= line_smaller}')
print(f'line_bigger < line_smaller: {line_bigger < line_smaller}')
print(f'line_bigger <= line_smaller: {line_bigger <= line_smaller}')

print('Here the triangle is created by adding Line(p2, p1) and a point p3')
triangle_by_addition1 = line_by_addition + p3
print(triangle_by_addition1)

print('Here the triangle is created by adding 3 points p1 p2 p3')
triangle_by_addition2 = p1 + p2 + p3
print(triangle_by_addition2)

print(f'triangle_by_addition1 == triangle_by_addition2: {triangle_by_addition1 == triangle_by_addition2}')
