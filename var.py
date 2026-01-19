country_data = {}


def get_yes_no(prompt):
    """
    Takes Y/N input from user.
    Allows lowercase and uppercase.
    Keeps asking until valid input is given.
    """
    while True:
        choice = input(prompt).strip().upper()
        if choice in ("Y", "N"):
            return choice
        print("Invalid input. Please enter Y or N only.")


def create_data():
    """
    Handles creation of countries, states, and cities.
    """
    # -------- Create Countries --------
    while True:
        country_name = input("Enter country name: ").strip()
        if not country_name:
            print("Country cannot be blank")
            continue

        if country_name not in country_data:
            country_data[country_name] = {}
        else:
            print("Country already exists")

        if get_yes_no("Add another country? (Y/N): ") == "N":
            break

    # -------- Create States --------
    while country_data:
        state_name = input("Enter state name: ").strip()
        if not state_name:
            print("State cannot be blank")
            continue

        print("Available Countries:", list(country_data.keys()))
        selected_country = input("Select country for this state: ")

        if selected_country in country_data:
            country_data[selected_country][state_name] = []
        else:
            print("Invalid country")

        if get_yes_no("Add another state? (Y/N): ") == "N":
            break

    # -------- Create Cities --------
    while True:
        city_name = input("Enter city name: ").strip()
        if not city_name:
            print("City cannot be blank")
            continue

        print("Available States:")
        for country in country_data:
            for state in country_data[country]:
                print(f"{state} (Country: {country})")

        selected_state = input("Select state for this city: ")

        state_found = False
        for country in country_data:
            if selected_state in country_data[country]:
                country_data[country][selected_state].append(city_name)
                state_found = True

        if not state_found:
            print("Invalid state")

        if get_yes_no("Add another city? (Y/N): ") == "N":
            break

    print("\n--- Current Data After Create ---")
    print(country_data)


def update_data():
    """
    Handles updating country, state, and city names.
    """
    print("\nUpdate Options:")
    print("1. Update Country")
    print("2. Update State")
    print("3. Update City")

    update_choice = int(input("Choose option: "))

    # -------- Update Country --------
    if update_choice == 1:
        print("Countries:", list(country_data.keys()))
        old_country = input("Enter country to update: ")

        if old_country in country_data:
            new_country = input("Enter new country name: ")
            country_data[new_country] = country_data.pop(old_country)

    # -------- Update State --------
    elif update_choice == 2:
        for country, states in country_data.items():
            print(country, ":", list(states.keys()))

        old_state = input("Enter state to update: ")

        for country, states in country_data.items():
            if old_state in states:
                new_state = input("Enter new state name: ")
                states[new_state] = states.pop(old_state)
                break

    # -------- Update City --------
    elif update_choice == 3:
        for country in country_data:
            for state in country_data[country]:
                print(state, ":", country_data[country][state])

        old_city = input("Enter city to update: ")

        for country in country_data:
            for state in country_data[country]:
                if old_city in country_data[country][state]:
                    new_city = input("Enter new city name: ")
                    index = country_data[country][state].index(old_city)
                    country_data[country][state][index] = new_city

    print("\n--- Current Data After Update ---")
    print(country_data)


def delete_data():
    """
    Handles deletion of country, state, and city.
    """
    print("\nDelete Options:")
    print("1. Delete Country")
    print("2. Delete State")
    print("3. Delete City")

    delete_choice = int(input("Choose option: "))

    # -------- Delete Country --------
    if delete_choice == 1:
        print("Countries:", list(country_data.keys()))
        country = input("Enter country to delete: ")
        country_data.pop(country, None)

    # -------- Delete State --------
    elif delete_choice == 2:
        state = input("Enter state to delete: ")
        for country in country_data:
            country_data[country].pop(state, None)

    # -------- Delete City --------
    elif delete_choice == 3:
        city = input("Enter city to delete: ")
        for country in country_data:
            for state in country_data[country]:
                if city in country_data[country][state]:
                    country_data[country][state].remove(city)

    print("\n--- Current Data After Delete ---")
    print(country_data)


# ================= MAIN MENU =================
while True:
    print("\nMAIN MENU")
    print("1. Create")
    print("2. Update")
    print("3. Delete")
    print("4. Exit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input. Enter a number from 1 to 4.")
        continue

    if choice == 1:
        create_data()
    elif choice == 2:
        update_data()
    elif choice == 3:
        delete_data()
    elif choice == 4:
        print("Program Ended")
        break
    else:
        print("Invalid choice. Enter 1 to 4.")
