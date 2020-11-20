# Processing
def road_trip(distance, speed, departure):
    durationMinutes = int((distance / speed) * 60)
    durationHours = durationMinutes // 60
    durationMinutes -= durationHours * 60

    # Generate the text for the departure time
    if departure[1] < 10:
        departureResult = "Départ à {}h0{}".format(departure[0], departure[1])
    else:
        departureResult = "Départ à {}h{}".format(departure[0], departure[1])

    # Generate the text for the duration of the travel
    durationResult = "Trajet de "

    if durationHours > 0:
        durationResult += "{} heure".format(durationHours)

        if durationHours > 1:
            durationResult += 's'

        durationResult += " et "

    durationResult += "{} minute".format(durationMinutes)
    if durationMinutes != 1:
        durationResult += 's'

    arrival = [0, 0]  # [hours, minutes]
    arrival[1] = (departure[1] + durationMinutes) % 60
    arrival[0] = (departure[0] + durationHours + (departure[1] + durationMinutes) // 60) % 24

    # Generate the text for the arrival time
    if arrival[1] < 10:
        arrivalResult = "Arrivée prévue à {}h0{}".format(arrival[0], arrival[1])
    else:
        arrivalResult = "Arrivée prévue à {}h{}".format(arrival[0], arrival[1])

    return departureResult + '\n' + durationResult + '\n' + arrivalResult


# Unit Tests API Input
# print(road_trip(lines[0], lines[1], lines[2]))

# Tests
print(road_trip(45, 95, [7, 10]))       # Must return "Départ à 7h10\nTrajet de 28 minutes\nArrivée prévue à 7h38"
print(road_trip(600, 115, [23, 10]))    # Must return "Départ à 23h10\nTrajet de 5 heures et 13 minutes\nArrivée prévue à 4h23"
print(road_trip(200, 75, [23, 55]))     # Must return "Départ à 23h55\nTrajet de 2 heures et 40 minutes\nArrivée prévue à 2h35"
print(road_trip(15, 45, [15, 3]))       # Must return "Départ à 15h03\nTrajet de 20 minutes\nArrivée prévue à 15h23"
print(road_trip(0.1, 6, [15, 3]))       # Must return "Départ à 15h03\nTrajet de 1 minute\nArrivée prévue à 15h04"
print(road_trip(1, 0.97, [15, 3]))      # Must return "Départ à 15h03\nTrajet de 1 heure et 1 minute\nArrivée prévue à 16h04"
print(road_trip(1, 0.99, [15, 3]))      # Must return "Départ à 15h03\nTrajet de 1 heure et 0 minutes\nArrivée prévue à 16h03"
print(road_trip(143, 140, [18, 30]))    # Must return "Départ à 18h30\nTrajet de 1 heure et 1 minute\nArrivée prévue à 19h31"
