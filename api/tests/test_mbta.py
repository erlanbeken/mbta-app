import mbta
import requests_mock
import pytest

import exceptions

def test_fetch_predictions():
    with requests_mock.Mocker() as m:
        m.get(f'{mbta.API_BASE_URL}predictions', json={'data': 'HERE'})
        res = mbta.fetch_predictions('station', 'type')
    assert res == 'HERE'
    assert m.last_request.url == f'{mbta.API_BASE_URL}predictions?filter%5Bstop%5D=station&filter%5Bdirection_id%5D=type&sort=departure_time&include=schedule%2Cvehicle%2Ctrip%2Cstop'


def test_fetch_predictions_exception():
    with requests_mock.Mocker() as m:
        m.get(f'{mbta.API_BASE_URL}predictions', json={'wrong_key': 'HERE'})
        with pytest.raises(exceptions.MBTAError):
            mbta.fetch_predictions('station', 'type')


# 2DO: add more unit tests