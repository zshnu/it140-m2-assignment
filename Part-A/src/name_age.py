Input:
    name = input("What is your name? ")
    age = int(input("How old are you? "))
Process:
    birth_year = CURRENT_YEAR - age

Output:
    print(f"Hello {name}! You were born in {birth_year}.")

# === Imports ===
from datetime import date

# === Constants ===
CURRENT_YEAR = date.today().year  # Get current year from system as integer


# === Main Function ===
def main() -> None:
    """Run the name-age program."""

    # Get user input.
    # TODO: Replace with code to get user's name as a string. See zyBooks 1.3.
    # TODO: Replace with code to get user's age as an integer. See zyBooks 2.6.

    # Calculate user's approximate birth year.
    # TODO: Replace with code to process data. See zyBooks 1.16 & 1.17.

    # Output personalized message with user's name and birth year.
    # TODO: Replace with code to output formatted results. zyBooks 1.3 & 2.7.


# === Main Guard ===
if __name__ == "__main__":
    main()
    
