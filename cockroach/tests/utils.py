def get_rect_as_dictionary(svg):
    rect_dict = {}
    for x in svg.split("<rect ")[1].split(' />')[0].split(' '):
        key, value = x.split('=')
        if key not in ['fill', 'stroke']:
            value = value.split('"')[1]
            rect_dict[key] = int(value)
    return rect_dict
