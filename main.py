from data_manager import DataManager
import flight_data
from flight_search import FlightSearch
import notification_manager


def main():
    data_manager = DataManager()
    flight_search = FlightSearch()
    list_of_cities = data_manager.get_cities_from_google_sheet().json()[
        "prices"]
    for city in list_of_cities:
        # print(city["city"])
        iata = flight_search.get_iata_for_cities(city["city"]).json()[
            "locations"][0]["code"]
        # print(iata)
        data_manager.add_iata_to_google_sheet(city["id"], iata)


main()
