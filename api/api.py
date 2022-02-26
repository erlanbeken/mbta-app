from flask import Flask

from exceptions import AppError, MBTAError
from error_handlers import mbta_error_handler, app_error_handler
import mbta

app = Flask(__name__)

app.register_error_handler(MBTAError, mbta_error_handler)
app.register_error_handler(AppError, app_error_handler)


@app.route('/api/mbta_departure_board')
def mbta_departure_board():
    res = mbta.fetch_departure_board()
    return {'result': res}