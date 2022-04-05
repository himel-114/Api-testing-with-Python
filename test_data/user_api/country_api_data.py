from test_data.api_end_point import *
from test_data.common_data import data_from_server
from test_data.headers import headers_post


# from test_data.payloads import *


def response_get_bd_data():
    res = data_from_server("GET", bangladesh_all_data)
    return res.json(), res.status_code


def response_get_all_data():
    res = data_from_server("GET", all_country_data)
    return res.json(), res.status_code
