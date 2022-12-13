import pytest
from triangle import Point
from triangle import Line
from triangle import Triangle


def test_point_creation_getting_setting_values():
    p1 = Point(1, 2)
    assert isinstance(p1, Point), 'object is not an instance of a Point'
    assert p1.x == 1 and p1.y == 2, 'right values are not accessible via attributes'

    p2 = Point(2.0, 1.0)
    assert isinstance(p2, Point), 'object is not an instance of a Point'
    assert p2.x == 2.0 and p2.y == 1.0, 'right values are not accessible via attributes'

    p1.x, p1.y = 2.0, 3.0
    assert p1.x == 2.0 and p1.y == 3.0, 'values setting does not work properly, got wrong values'

    p2.x, p2.y = 3, 4
    assert p2.x == 3 and p2.y == 4, 'values setting does not work properly, got wrong values'

    with pytest.raises(TypeError):
        p3 = Point('1', 2)

    with pytest.raises(TypeError):
        p4 = Point(1.0, 2.0)
        p4.x = '2'


def test_point_str():
    p1 = Point(1, 2)
    assert str(p1) == '1,2', 'not expected result'


def test_point_comparison():
    """
    Only __eq__ is supported for Points
    """
    p1 = Point(1, 2)
    p2 = Point(1.0, 2.0)
    p3 = Point(3, 4)
    assert p1 == p1, 'not expected result'
    assert p1 == p2, 'not expected result'
    assert p2 != p3, 'not expected result'
    assert p3 != p1, 'not expected result'

    with pytest.raises(TypeError):
        assert p1 == 2


def test_adding_points():
    p1 = Point(1, 2)
    p2 = Point(2, 3)
    p3 = Point(3, 4)
    p4 = Point(4, 5)

    line1 = p1 + p2
    triangle1 = p1 + p2 + p3
    triangle2 = line1 + p3
    triangle3 = p3 + line1

    assert isinstance(line1, Line), 'not expected result'
    assert isinstance(triangle1, Triangle), 'not expected result'
    assert isinstance(triangle2, Triangle), 'not expected result'
    assert isinstance(triangle3, Triangle), 'not expected result'

    with pytest.raises(NotImplementedError):
        quadrilateral1 = p4 + triangle1

    with pytest.raises(TypeError):
        line1 = p1 + 2


def test_line_creation():
    p1 = Point(1, 2)
    p2 = Point(1.0, 2.0)
    p3 = Point(2, 3)

    line1 = Line(p1, p3)
    line2 = Line(p2, p3)

    assert isinstance(line1, Line), 'not expected result'
    assert isinstance(line2, Line), 'not expected result'

    with pytest.raises(ValueError):
        line3 = Line(p1, p2)


def test_line_getting_setting():
    p1 = Point(1, 2)
    p2 = Point(2, 3)
    p3 = Point(3, 4)

    line1 = Line(p1, p2)

    assert (line1.begin.x, line1.end.x, line1.begin.y, line1.end.y) == (1, 2, 2, 3), 'not expected result'

    line1.begin.x, line1.end.x, line1.begin.y, line1.end.y = 2, 1, 3, 2
    assert (line1.begin.x, line1.end.x, line1.begin.y, line1.end.y) == (2, 1, 3, 2), \
        'right values are not accessible'

    line1.begin = p3
    line1.end = p1
    assert line1.begin == p3, 'not expected result'
    assert line1.end == p1, 'not expected result'
    assert isinstance(line1.begin, Point), 'not expected result'
    assert isinstance(line1.end, Point), 'not expected result'

    with pytest.raises(TypeError):
        line1.begin = 1

    with pytest.raises(TypeError):
        line1.end = 1


def test_line_str():
    p1 = Point(1, 2)
    p2 = Point(2, 3)

    line1 = Line(p1, p2)

    assert str(line1) == '1,2 -- 2,3', 'not expected result'


def test_adding_to_line():
    p1 = Point(1, 2)
    p2 = Point(2, 3)
    p3 = Point(3, 4)
    p4 = Point(4, 5)

    line1 = p1 + p2
    line2 = p3 + p4

    triangle1 = line1 + p3
    assert isinstance(triangle1, Triangle), 'not expected result'

    with pytest.raises(NotImplementedError):
        quadrilateral1 = line1 + line2

    with pytest.raises(TypeError):
        triangle1 = line1 + 2


def test_line_length():
    p1 = Point(0, 0)
    p2 = Point(3, 4)
    p3 = Point(9, 12)

    line1 = Line(p1, p2)
    line2 = Line(p1, p3)

    assert line1.length == 5.0, 'not expected result'
    assert isinstance(line1.length, float), 'not expected result'


def test_line_comparison():
    p1 = Point(1, 2)
    p2 = Point(2.0, 3.0)
    p3 = Point(3, 4)
    p4 = Point(4, 6)

    line1 = Line(p1, p2)
    line2 = Line(p2, p3)
    line3 = Line(p3, p4)

    assert line1 == line2, 'not expected result'
    assert not line1 != line2, 'not expected result'
    assert line1 >= line2, 'not expected result'
    assert line1 <= line2, 'not expected result'
    assert not line1 > line2, 'not expected result'
    assert not line1 < line2, 'not expected result'

    assert not line3 == line2, 'not expected result'
    assert line3 != line2, 'not expected result'
    assert line3 >= line2, 'not expected result'
    assert not line3 <= line2, 'not expected result'
    assert line3 > line2, 'not expected result'
    assert not line3 < line2, 'not expected result'

    with pytest.raises(TypeError):
        assert line1 == 2


def test_triangle_creation():
    p1 = Point(1, 2)
    p2 = Point(2, 3)
    p3 = Point(4, 5)
    p4 = Point(1, 2)

    triangle1 = Triangle(p1, p2, p3)

    assert isinstance(triangle1, Triangle), 'not expected result'

    with pytest.raises(ValueError):
        line3 = Triangle(p1, p2, p4)


def test_triangle_getting_setting():
    p1 = Point(1, 2)
    p2 = Point(2, 3)
    p3 = Point(4, 3)
    p4 = Point(10, 10)

    triangle1 = Triangle(p1, p2, p3)

    assert (triangle1.vertex_coord_1, triangle1.vertex_coord_2, triangle1.vertex_coord_3) == (p1, p2, p3), \
        'not expected result'
    assert (triangle1.vertex_coord_1.x, triangle1.vertex_coord_1.y) == (1, 2), 'not expected result'

    triangle1.vertex_coord_1 = p4
    assert isinstance(triangle1.vertex_coord_1, Point), 'not expected result'
    assert triangle1.vertex_coord_1 == p4, 'not expected result'
    assert (triangle1.vertex_coord_1.x, triangle1.vertex_coord_1.y) == (10, 10), 'not expected result'

    with pytest.raises(TypeError):
        triangle1.vertex_coord_1 = 1


def test_triangle_str():
    p1 = Point(1, 2)
    p2 = Point(2, 3)
    p3 = Point(4, 5)

    triangle1 = Triangle(p1, p2, p3)

    assert str(triangle1) == '1,2 -- 2,3 -- 4,5'


def test_triangle_area():
    p1 = Point(0, 0)
    p2 = Point(0, 3)
    p3 = Point(4, 0)
    p4 = Point(9, 0)
    p5 = Point(0, 12)

    triangle1 = Triangle(p1, p2, p3)
    triangle2 = Triangle(p1, p4, p5)

    assert triangle1.area == 6.0
    assert isinstance(triangle1.area, float)

    assert triangle2.area == 54.0
    assert isinstance(triangle2.area, float)


def test_triangle_comparison():
    p1 = Point(0, 0)
    p2 = Point(0, 3)
    p3 = Point(4, 0)
    p4 = Point(4, 3)
    p5 = Point(10, 10)

    triangle1 = Triangle(p1, p2, p3)
    triangle2 = Triangle(p4, p2, p3)
    triangle3 = Triangle(p5, p2, p3)

    assert triangle1.area == triangle2.area
    assert triangle3.area > triangle2.area

    assert triangle1 == triangle2, 'not expected result'
    assert not triangle1 != triangle2, 'not expected result'
    assert triangle1 >= triangle2, 'not expected result'
    assert triangle1 <= triangle2, 'not expected result'
    assert not triangle1 > triangle2, 'not expected result'
    assert not triangle1 < triangle2, 'not expected result'

    assert not triangle3 == triangle2, 'not expected result'
    assert triangle3 != triangle2, 'not expected result'
    assert triangle3 >= triangle2, 'not expected result'
    assert not triangle3 <= triangle2, 'not expected result'
    assert triangle3 > triangle2, 'not expected result'
    assert not triangle3 < triangle2, 'not expected result'

    with pytest.raises(TypeError):
        assert triangle3 == 2

    with pytest.raises(TypeError):
        assert triangle3 > p4
