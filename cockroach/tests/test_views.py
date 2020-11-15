import pytest

from rest_framework.status import HTTP_200_OK
from cockroach.utils import return_width_height
from utils import get_rect_as_dictionary

FIRST_CASE = {"geometry": [{"x1": -207, "x2": -332, "y1": 9, "y2": 191, "z1": 0, "z2": 18}],
              "projection_plane": "XY"}
SECOND_CASE = {"geometry": [{"x1": -207, "x2": -332, "y1": 209, "y2": 391, "z1": 0, "z2": 18}],
               "projection_plane": "XZ"}
THIRD_CASE = {"geometry": [{"x1": 207, "x2": 332, "y1": 9, "y2": 191, "z1": 0, "z2": 18}],
              "projection_plane": "YZ"}


@pytest.mark.parametrize("test_input", [FIRST_CASE, SECOND_CASE, THIRD_CASE])
def test_projection(api_client, test_input):
    response = api_client.post('/api/v1/cockroach/projection', data=test_input, format='json')
    response_as_text = response.content.decode('utf-8')

    dict_response = get_rect_as_dictionary(response_as_text)
    geometry_element = test_input['geometry'][0]

    projection_plane = test_input['projection_plane']
    x_factor = projection_plane[0].lower()
    y_factor = projection_plane[1].lower()

    x1 = int(geometry_element[f'{x_factor}1'])
    x2 = int(geometry_element[f'{x_factor}2'])
    y1 = int(geometry_element[f'{y_factor}1'])
    y2 = int(geometry_element[f'{y_factor}2'])

    width, height = return_width_height(x2, x1, y2, y1)

    assert dict_response['x'] == x1
    assert dict_response['y'] == y1
    assert dict_response['width'] == width
    assert dict_response['height'] == height
    assert response.status_code == HTTP_200_OK
