from django.urls import reverse
from rest_framework.status import HTTP_200_OK
from utils import default_geometry, get_rect_as_dictionary


def test_XY_projection(client):
    response = client.post(reverse('projection'), data=default_geometry('XY'),
                           content_type='application/json')
    dict_response = get_rect_as_dictionary(response.content.decode('utf-8'))
    assert dict_response['x'] == -207
    assert dict_response['y'] == 9
    assert dict_response['width'] == -125
    assert dict_response['height'] == 182
    assert response.status_code == HTTP_200_OK


def test_XZ_projection(client):
    response = client.post(reverse('projection'), data=default_geometry('XZ'),
                           content_type='application/json')
    dict_response = get_rect_as_dictionary(response.content.decode('utf-8'))
    assert dict_response['x'] == -207
    assert dict_response['y'] == 0
    assert dict_response['width'] == -125
    assert dict_response['height'] == 18
    assert response.status_code == HTTP_200_OK


def test_YZ_projection(client):
    response = client.post(reverse('projection'), data=default_geometry('YZ'),
                           content_type='application/json')
    dict_response = get_rect_as_dictionary(response.content.decode('utf-8'))
    assert dict_response['x'] == 9
    assert dict_response['y'] == 0
    assert dict_response['width'] == 182
    assert dict_response['height'] == 18
    assert response.status_code == HTTP_200_OK
