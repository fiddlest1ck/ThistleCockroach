import drawSvg as draw

from cockroach.utils import get_width_height, TylkoRectangle


class SvgCreator:

    def __init__(self, geometry, plane):
        self.geometry = geometry
        self.x_factor, self.y_factor = self.get_plane_factors(plane)
        self.drawing_place = draw.Drawing(1000, 1000, origin='center')

    def get_plane_factors(self, plane):
        return plane[0].lower(), plane[1].lower()

    def draw_rectangles(self):
        for entry in self.geometry:
            x1 = entry[f'{self.x_factor}1']
            x2 = entry[f'{self.x_factor}2']
            y1 = entry[f'{self.y_factor}1']
            y2 = entry[f'{self.y_factor}2']
            width, height = get_width_height(x1, x2, y1, y2)
            rect = TylkoRectangle(x1, y1, width, height, fill='gray', stroke='black')
            self.drawing_place.append(rect)

    def generate_svg(self):
        self.draw_rectangles()
        return self.drawing_place.asSvg()
