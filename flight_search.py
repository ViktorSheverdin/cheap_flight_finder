import requests
import datetime as dt
from dateutil.relativedelta import relativedelta
import credentials


class FlightSearch:
    def __init__(self):
        self.tequila_endpoint = "https://tequila-api.kiwi.com/v2"

    def make_request_to_tequila(self):
        tequila_headers = {
            "apikey": credentials.tequila_api_key,
        }
        tequila_params = {
            "fly_from": "FRA",
            "fly_to": "PRG",
            "date_from": "01/22/2021",
            # "date_from": str(dt.datetime.today().strftime("%d/%m/%Y")),
            "date_to": "06/22/2021"
            # "date_to": str((dt.datetime.today() + relativedelta(months=+6)).strftime("%d/%m/%Y")),
        }
        print(self.tequila_endpoint)
        response = requests.get(
            url=self.tequila_endpoint, params=tequila_params, headers=tequila_headers)
        return response
