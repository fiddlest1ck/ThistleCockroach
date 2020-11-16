from rest_framework.status import HTTP_200_OK

from utils import get_rect_as_dictionary, default_geometry


PROJECTION_URL = '/api/v1/cockroach/projection'


def test_XY_projection(api_client):
    response = api_client.post(PROJECTION_URL,
                               data=default_geometry('XY'), format='json')
    dict_response = get_rect_as_dictionary(response.content.decode('utf-8'))
    assert dict_response['x'] == -207
    assert dict_response['y'] == 9
    assert dict_response['width'] == -125
    assert dict_response['height'] == 182
    assert response.status_code == HTTP_200_OK


def test_XZ_projection(api_client):
    response = api_client.post(PROJECTION_URL,
                               data=default_geometry('XZ'), format='json')
    dict_response = get_rect_as_dictionary(response.content.decode('utf-8'))
    assert dict_response['x'] == -207
    assert dict_response['y'] == 0
    assert dict_response['width'] == -125
    assert dict_response['height'] == 18
    assert response.status_code == HTTP_200_OK


def test_YZ_projection(api_client):
    response = api_client.post(PROJECTION_URL,
                               data=default_geometry('YZ'), format='json')
    dict_response = get_rect_as_dictionary(response.content.decode('utf-8'))
    assert dict_response['x'] == 9
    assert dict_response['y'] == 0
    assert dict_response['width'] == 182
    assert dict_response['height'] == 18
    assert response.status_code == HTTP_200_OK
