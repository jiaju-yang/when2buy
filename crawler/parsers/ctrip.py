from parsers.parselib import jmespath_search


def parse_flights(data: dict):
    extract_expression = """
            data.routeList[?routeType=='Flight'].legs[0].
            {
                lowest_price: characteristic.lowestPrice | to_int(@),
                flight_number: flight.flightNumber | to_str(@),
                plane_type_code: flight.craftTypeCode | to_str(@),
                airline_code: flight.airlineCode | to_str(@),
                departure_city_code: flight.departureAirportInfo.cityTlc | to_str(@),
                departure_airport_code: flight.departureAirportInfo.airportTlc | to_str(@),
                departure_terminal_id: flight.departureAirportInfo.terminal.id | to_int(@),
                arrival_city_code: flight.arrivalAirportInfo.cityTlc | to_str(@),
                arrival_airport_code: flight.arrivalAirportInfo.airportTlc | to_str(@),
                arrival_terminal_id: flight.arrivalAirportInfo.terminal.id | to_int(@),
                depart_at: flight.departureDate | to_datetime(@, ''),
                arrive_at: flight.arrivalDate | to_datetime(@, ''),
                punctual_rate: flight.punctualityRate | to_percent(@),
                stop_times: flight.stopTimes | to_int(@)
            }
            """
    return jmespath_search(extract_expression, data)
