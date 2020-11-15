import drawSvg as draw
from cockroach.utils import return_width_height, TylkoRectangle


class SvgCreator:

    def __init__(self, geometry, plane):
        self.geometry = geometry
        self.x_factor, self.y_factor = self.get_plane_factors(plane)
        self.drawing_place = draw.Drawing(1000, 1000, origin='center')

    def get_plane_factors(self, plane):
        return plane[0].lower(), plane[1].lower()

    def draw_rectangles(self):
        for entry in self.geometry:
            width, height = return_width_height(entry[f'{self.x_factor}2'], entry[f'{self.x_factor}1'],
                                                entry[f'{self.y_factor}2'], entry[f'{self.y_factor}1'])
            x = entry[f'{self.x_factor}1']
            y = entry[f'{self.y_factor}1']
            rect = TylkoRectangle(x, y, width, height, fill='gray', stroke='black')
            self.drawing_place.append(rect)

    def generate_svg(self):
        self.draw_rectangles()
        return self.drawing_place.asSvg()
