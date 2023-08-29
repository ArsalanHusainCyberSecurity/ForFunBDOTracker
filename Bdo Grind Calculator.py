def main():
    # Define grind spots and their trashloot value
    grind_spots = {
        'Fogans': 2200,
        'Gahaz': 2500,
        'Manshaums': 15000,
    }

    # Ask user for grind spot
    print("Available grind spots:")
    for spot in grind_spots.keys():
        print("- " + spot)
    spot_choice = input("Where did you grind? ")

    # Check if the choice is valid
    if spot_choice not in grind_spots:
        print("Invalid choice!")
        return

    # Ask user for amount of trashloot
    try:
        trashloot_amount = int(input("How much trashloot did you get? "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    # Calculate the total silver
    silver_value = grind_spots[spot_choice] * trashloot_amount
    print(f"Total silver earned at {spot_choice}: {silver_value:,} silver")

if __name__ == "__main__":
    main()
