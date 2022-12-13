# 1. Доопрацюйте всі реревірки на типи даних (x, y в Point, begin, end в Line, etc) - зробіть перевірки за допомогою property або класса-дескриптора.
# 2. Доопрацюйте класс Triangle з попередньої домашки наступним чином:
# обʼєкти классу Triangle можна порівнювати між собою (==, !=, >, >=, <, <=) за площею.
# перетворення обʼєкту классу Triangle на стрінг показує координати його вершин у форматі x1, y1 -- x2, y2 -- x3, y3

# print(str(triangle1))
# > (1,0 -- 5,9 -- 3,3)


from abc import ABC, abstractmethod


class OnlyCertainClassesDescriptor:
    """
    Controls that set value of attribute is an instance of class passed to a class during init
    """
    def __init__(self, attr_name, class_to_check):
        """
        Args:
            attr_name (str): object's name to be represented as f'_{attr_name}'
            class_to_check (object): Object of class. Descriptor allows to set value of class_to_check classes only
        """
        self.attr_name = f'_{attr_name}'
        self.class_to_check = class_to_check

    def __get__(self, instance, owner):
        return getattr(instance, self.attr_name, None)

    def __set__(self, instance, value):
        if not isinstance(value, self.class_to_check):
            print(f'Error: Allowed classes of parameters are only: {self.class_to_check}')
            raise TypeError

        setattr(instance, self.attr_name, value)


class Point:
    x = OnlyCertainClassesDescriptor('x', (int, float))
    y = OnlyCertainClassesDescriptor('y', (int, float))

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'{self.x},{self.y}'

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
    begin = OnlyCertainClassesDescriptor('begin', Point)
    end = OnlyCertainClassesDescriptor('end', Point)

    def __init__(self, begin, end):
        if begin == end:
            print('Error: points are equal, must be different')
            raise ValueError

        self.begin = begin
        self.end = end

    def __str__(self):
        return f'{self.begin.x},{self.begin.y} -- {self.end.x},{self.end.y}'

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

    def __ne__(self, other):
        """
        Considers two lines not equal if their lengths are not equal
        """
        if not isinstance(other, Line):
            print('Comparison supported only for two objects of Line class')
            raise TypeError
        return self.length != other.length

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

    def __lt__(self, other):
        """
        Compares lengths of two lines when Line objects are compared
        """
        if not isinstance(other, Line):
            print('Comparison supported only for two objects of Line class')
            raise TypeError
        return self.length < other.length

    def __le__(self, other):
        """
        Compares lengths of two lines when Line objects are compared
        """
        if not isinstance(other, Line):
            print('Comparison supported only for two objects of Line class')
            raise TypeError
        return self.length <= other.length

    @property
    def length(self) -> float:
        res = ((self.begin.x - self.end.x)**2 + (self.begin.y - self.end.y)**2)**0.5
        return res


class Triangle(Figure):
    vertex_coord_1 = OnlyCertainClassesDescriptor('vertex_coord_1', Point)
    vertex_coord_2 = OnlyCertainClassesDescriptor('vertex_coord_2', Point)
    vertex_coord_3 = OnlyCertainClassesDescriptor('vertex_coord_3', Point)
    vertices_tuple = (vertex_coord_1, vertex_coord_2, vertex_coord_3)

    def __init__(self, point1, point2, point3):
        if point1 == point2 or point2 == point3 or point3 == point1:
            print('Please pass 3 different points into the Triangle class')
            raise ValueError

        self.vertex_coord_1 = point1
        self.vertex_coord_2 = point2
        self.vertex_coord_3 = point3

    def __str__(self):
        return f'{self.vertex_coord_1.x},{self.vertex_coord_1.y} -- ' \
               f'{self.vertex_coord_2.x},{self.vertex_coord_2.y} -- ' \
               f'{self.vertex_coord_3.x},{self.vertex_coord_3.y}'

    def __eq__(self, other):
        if not isinstance(other, Triangle):
            print('Comparison supported only for two objects of Triangle class')
            raise TypeError
        return self.area == other.area

    def __ne__(self, other):
        if not isinstance(other, Triangle):
            print('Comparison supported only for two objects of Triangle class')
            raise TypeError
        return self.area != other.area

    def __gt__(self, other):
        if not isinstance(other, Triangle):
            print('Comparison supported only for two objects of Triangle class')
            raise TypeError
        return self.area > other.area

    def __ge__(self, other):
        if not isinstance(other, Triangle):
            print('Comparison supported only for two objects of Triangle class')
            raise TypeError
        return self.area >= other.area

    def __lt__(self, other):
        if not isinstance(other, Triangle):
            print('Comparison supported only for two objects of Triangle class')
            raise TypeError
        return self.area < other.area

    def __le__(self, other):
        if not isinstance(other, Triangle):
            print('Comparison supported only for two objects of Triangle class')
            raise TypeError
        return self.area <= other.area

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
