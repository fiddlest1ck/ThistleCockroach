from drawSvg.elements import DrawingBasicElement


class TylkoRectangle(DrawingBasicElement):
    # Your's rectangle have = y1 = y1 factor, but
    # drawSvg library have y1 = - y1 - height, so it's
    # seems to be weird, so I hacked this.

    TAG_NAME = 'rect'

    def __init__(self, x, y, width, height, **kwargs):
        super().__init__(x=x, y=y, width=width, height=height,
                         **kwargs)


def get_width_height(x1, x2, y1, y2):
    width = x2 - x1
    height = y2 - y1
    return width, height
