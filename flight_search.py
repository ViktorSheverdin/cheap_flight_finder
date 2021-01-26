import requests
import datetime as dt
from dateutil.relativedelta import relativedelta
import credentials


class FlightSearch:
    def __init__(self):
        self.tequila_endpoint = "https://tequila-api.kiwi.com/"

    def get_iata_for_cities(self, city_name):
        tequila_headers = {
            "apikey": credentials.tequila_api_key
        }
        tequila_params = {
            # "fly_from": "FRA",
            # "fly_to": "PRG",
            # "date_from": "01/22/2021",
            # # "date_from": str(dt.datetime.today().strftime("%d/%m/%Y")),
            # "date_to": "06/22/2021"
            # # "date_to": str((dt.datetime.today() + relativedelta(months=+6)).strftime("%d/%m/%Y")),
            "term": city_name,
            "location_types": "city"
        }
        # print(f"{self.tequila_endpoint}locations/query")

        response = requests.get(
            url=f"{self.tequila_endpoint}locations/query", headers=tequila_headers, params=tequila_params)
        # print(response)
        return response


# fs = FlightSearch()
# fs.get_iata_for_cities()
