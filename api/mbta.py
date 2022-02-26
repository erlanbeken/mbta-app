import logging
import requests
import json

import exceptions

logger = logging.getLogger()

API_BASE_URL = 'https://api-v3.mbta.com/'

carrier = {
  'MBTA': "MBTA",
  'AMTRAK': "AMTRAK"
}

stations = {
  'SOUTH_STATION': "place-sstat",
  'NORTH_STATION': "place-north"
}

transportation = {
  'LIGHT_RAIL': 0,
  'HEAVY_RAIL': 1,
  'COMMUTER_RAIL': 2,
  'BUS': 3,
  'FERRY': 4
}

directions = {
  'OUTBOUND': 0,
  'INBOUND': 1
}


def make_api_request(url, params):
    '''
    Base method that makes a GET call to the MBTA API.
    Returns json, raises exception on non-200 response.
    '''
    response = requests.get(API_BASE_URL + url, params)
    try:
        response.raise_for_status()
        return response.json()['data']
    except (requests.exceptions.HTTPError, json.JSONDecodeError, KeyError) as e:
        raise exceptions.MBTAError(e)


def fetch_routes(station: str, type: str):
    params = {
        'filter[stop]': station,
        'filter[type]': type
    }
    return make_api_request('routes', params)


def fetch_predictions(station: str, direction: str, routes=None):
    params = {
        'filter[stop]': station,
        'filter[direction_id]': direction,
        'sort': 'departure_time',
        'include': 'schedule,vehicle,trip,stop'
    }
    if routes is not None:
        params['filter[route]'] = ','.join([route['id'] for route in routes]),
    return make_api_request('predictions', params)


def fetch_departure_board():
    station = stations['NORTH_STATION']
    direction = directions['OUTBOUND']

    # 2DO: get rid of mock data and use the actual API instead
    # predictions = fetch_predictions(station, direction)

    predictions = [
        {
            'carrier': 'AMTRACK',
            'time': '6:45pm',
            'destination': 'Portland, ME',
            'train': '697',
            'track': 'TBD',
            'status': 'ON TIME'
        },
        {
            'carrier': 'MBTA',
            'time': '7:15pm',
            'destination': 'Newburyport',
            'train': '2169',
            'track': 'TBD',
            'status': 'ON TIME'
        },
        {
            'carrier': 'MBTA',
            'time': '8:15pm',
            'destination': 'Lowell',
            'train': '2314',
            'track': 'TBD',
            'status': 'ON TIME'
        }
    ]
    return predictions
