import xml.etree.ElementTree as ET


def get_rect_as_dictionary(svg):
    root = ET.fromstring(svg)
    return {key: int(value) for key, value in root[1].items() if key not in ['fill', 'stroke']}


def default_geometry(projection_plane):
    return {"geometry": [{"x1": -207, "x2": -332, "y1": 9, "y2": 191, "z1": 0, "z2": 18}],
            "projection_plane": projection_plane}
