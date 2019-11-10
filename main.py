import logging
from flask import Flask, request
import json


app = Flask(__name__)


@app.route('/moneyanlz/ping', methods=['GET'])
def ping():
    return 'pong'


if __name__ == '__main__':
    logging.info('Start')

    logging.info('Starting Flask')
    app.run(host='0.0.0.0', debug=False, port=5001, threaded=True)

