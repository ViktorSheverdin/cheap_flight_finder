import data_manager
import flight_data
from flight_search import FlightSearch
import notification_manager


def main():
    ticket = FlightSearch()
    print(ticket.make_request_to_tequila().json())


main()
