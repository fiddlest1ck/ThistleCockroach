from drawSvg.elements import Rectangle
from cockroach.utils import TylkoRectangle, return_width_height
from utils import get_rect_as_dictionary


def test_tylko_rectangle():
    t_rectangle = TylkoRectangle(1, 2, 3, 4).args
    d_rectangle = Rectangle(1, 2, 3, 4).args

    assert d_rectangle['y'] == -t_rectangle['y'] - t_rectangle['height']
    assert t_rectangle['y'] == 2


def test_return_width_height():
    assert return_width_height(2, 1, 2, 1) == (1, 1)


def test_get_rect_as_dictionary():
    svg_text = '''<?xml version="1.0" encoding="UTF-8"?>
                    <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
                    width="1000" height="1000" viewBox="-500.0 -500.0 1000 1000">
                    <defs>
                    </defs>
                    <rect x="-207" y="-191" width="-125" height="182" fill="gray" />
                    </svg>'''
    assert get_rect_as_dictionary(svg_text) == {'x': -207, 'y': -191, 'height': 182, 'width': -125}
