from discogs_wrapper.dv import DV
from pytest import fixture

@fixture
def dv_keys():
    # Responsible only for returning the test data
    return ['id', 'status', 'year', 'resource_url',
              'uri', 'artists', 'artists_sort',
              'label']

def test_release():
    dv_instance = DV("FooBarApp/3.0")
    response = dv_instance.get_release(249504)

    assert isinstance(response, dict)
    # assert set(dv_keys).issubset(response.keys()), "All keys should be in the response"
    # assert response['id'] == 1396, "The ID should be in the response"

def test_masters_release():
    dv_instance = DV("FooBarApp/3.0")
    response = dv_instance.get_masters_release(1000)
    assert isinstance(response, dict)

def test_artist():
    dv_instance = DV("FooBarApp/3.0")
    response = dv_instance.get_artist(108713)
    assert isinstance(response, dict)



    