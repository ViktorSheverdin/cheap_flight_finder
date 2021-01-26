import credentials
import requests


class DataManager:
    def __init__(self):
        self.google_sheet_endpoint = "https://api.sheety.co/3033aaca49063d28ad1fce51d6ed3b21/flightDealsPython/prices"

    def get_cities_from_google_sheet(self):
        headers = {
            "Authorization": credentials.sheety_auth_token
        }
        response = requests.get(
            url=self.google_sheet_endpoint, headers=headers)
        return response

    def add_iata_to_google_sheet(self, city_id, iata):
        print(city_id, iata)
        body = {
            "price": {
                "iataCode": iata,
            }
        }
        headers = {
            "Authorization": credentials.sheety_auth_token
        }
        response = requests.put(url=f"{self.google_sheet_endpoint}/{city_id}",
                                json=body, headers=headers)
        print(response)
        return response


# dm = DataManager()
# print(dm.add_iata_to_google_sheet("Paris", "PAR").json())
