from Numerology import Numerology  # Import the Numerology class

def main():
    # Ask the user to enter their full name
    name = input("Enter your full name: ").strip()
    # Ask the user to enter their date of birth 
    dob = input("Enter your birth date (mm-dd-yyyy): ").strip()

    # Check if the date of birth is valid 
    while not dob or len(dob.split('-')) != 3 or not all(part.isdigit() for part in dob.split('-')):
        dob = input("Please enter a valid birth date (mm-dd-yyyy): ").strip()

    # Check if the name is not empty
    while not name:
        name = input("Please enter a valid name: ").strip()

    # Create an instance of the Numerology class with the given name and date of birth
    numerology = Numerology(name, dob)

    # Print the name
    print(f"Name: {numerology.getName()}")
    # Print the birth date
    print(f"Birth Date: {numerology.getBirthdate()}")
    # Print the Life Path Number
    print(f"Life Path Number: {numerology.getLifePath()}")
    # Print the Birth Day Number
    print(f"Birth Day Number: {numerology.getBirthDay()}")
    # Print the Attitude Number
    print(f"Attitude Number: {numerology.getAttitude()}")
    # Print the Soul Number
    print(f"Soul Number: {numerology.getSoul()}")
    # Print the Personality Number
    print(f"Personality Number: {numerology.getPersonality()}")
    # Print the Power Name Number
    print(f"Power Name Number: {numerology.getPowerName()}")

# Run the main function 
if __name__ == "__main__":
    main()
