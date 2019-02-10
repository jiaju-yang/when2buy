from operator import itemgetter

from parsers.parselib import jmespath_search


def parse_flights(data: dict):
    extract_expression = """
            data.routeList[?routeType=='Flight'].legs[0].
            {
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
                stop_times: flight.stopTimes | to_int(@),
                prices: cabins[*].{
                    cabin_class_code: cabinClass,
                    lowest_price: price.price,
                    lowest_price_discount: price.rate,
                    cancellation_fee: refundEndorse.minRefundFee,
                    changing_seat_fee: refundEndorse.minEndorseFee
                }
            }
            """
    result = jmespath_search(extract_expression, data)
    for item in result:
        prices = item.pop('prices', None)
        if prices:
            item.update(min(prices, key=itemgetter('lowest_price')))
    return result
