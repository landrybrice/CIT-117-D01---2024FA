# UseNumerologyInherit.py

from NumerologyLifePathDetails import NumerologyLifePathDetails
import re

def is_valid_date(date_str):
    # Check if the date is in the format mm-dd-yyyy or mm/dd/yyyy
    pattern = r'^(0[1-9]|1[0-2])[-/](0[1-9]|[12][0-9]|3[01])[-/](\d{4})$'
    return re.match(pattern, date_str) is not None

def main():
    # Ask the user to enter their full name
    name = input("Enter your full name: ").strip()
    while not name:
        print("Name cannot be empty. Please enter your name again.")
        name = input("Enter your full name: ").strip()

    # Ask the user to enter their date of birth
    dob = input("Enter your birth date (mm-dd-yyyy): ").strip()
    while not is_valid_date(dob):
        print("Invalid date format. Please enter in mm-dd-yyyy format.")
        dob = input("Enter your birth date (mm-dd-yyyy): ").strip()

    # Create an instance of the NumerologyLifePathDetails class
    numerology = NumerologyLifePathDetails(name, dob)

    # Output the findings using properties
    print("\nNumerology Findings:")
    print(f"Name: {numerology.Name}")
    print(f"Birth Date: {numerology.Birthdate}")
    print(f"Life Path Number: {numerology.LifePath}")
    print(f"Birth Day Number: {numerology.BirthDay}")
    print(f"Attitude Number: {numerology.Attitude}")
    print(f"Soul Number: {numerology.Soul}")
    print(f"Personality Number: {numerology.Personality}")
    print(f"Power Name Number: {numerology.PowerName}")
    print(f"Life Path Description: {numerology.LifePathDescription}")

# Run the main function
if __name__ == "__main__":
    main()
