import pytest
from utils import get_rect_as_dictionary

from cockroach.utils import get_width_height


@pytest.mark.parametrize('x1,x2,y1,y2', [(1, 2, 1, 2), (2, 3, 2, 3), (1, 4, 6, 8)])
def test_get_width_height(x1, x2, y1, y2):
    assert get_width_height(x1, x2, y1, y2) == (x2 - x1, y2 - y1)


def test_get_rect_as_dictionary():
    svg_text = '''<?xml version="1.0" encoding="UTF-8"?>
                    <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
                    width="1000" height="1000" viewBox="-500.0 -500.0 1000 1000">
                    <defs>
                    </defs>
                    <rect x="-207" y="-191" width="-125" height="182" fill="gray" />
                    </svg>'''
    assert get_rect_as_dictionary(svg_text) == {'x': -207, 'y': -191, 'height': 182, 'width': -125}
