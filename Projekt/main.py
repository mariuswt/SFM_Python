from Projekt.Airport import Airport


def menu():
    selection = ""
    try:
        selection = int(input("\n0. END\n"
                              "1. Register new Flight\n"
                              "2. Show Flights\n"
                              "3. Edit Fight\n"
                              "4. Remove Flight\n\n"))
    except:
        print("*" * 5, "SELECTION MUST BE INTEGER", "*" * 5)
    return selection


def main():
    selection = 22
    airport = Airport()
    while selection != 0:
        selection = menu()
        if selection == 1:
            airport.register_new_flight()
        if selection == 2:
            airport.show_flights()
        if selection == 3:
            airport.edit_flights()
        if selection == 4:
            airport.remove_flight()


if __name__ == "__main__":
    main()
