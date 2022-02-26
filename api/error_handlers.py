from flask import Response
import json
import logging


def error_response(msg):
    logging.error(msg, exc_info=True)
    data = json.dumps({"error": msg})
    return Response(data, status=500, mimetype='application/json')


def mbta_error_handler(e):
    msg = 'MBTA API error!'
    return error_response(msg)


def app_error_handler(e):
    msg = f'App error: {e}'
    return error_response(msg)