class Numerology:
    
    def __init__(self, sName, sDOB):
        # Initialize the class with the person's name and date of birth.
        self.name = sName
        self.dob = sDOB

    def getName(self):
        # Return the name of the person.
        return self.name

    def getBirthdate(self):
        # Return the date of birth of the person.
        return self.dob

    def _reduce_to_single_digit(self, number):
        # Keep adding the digits of the number until a single digit is obtained.
        while number > 9:
            number = sum(int(digit) for digit in str(number))
        return number

    def getLifePath(self):
        # Calculate the Life Path Number based on the date of birth.
        digits = [int(d) for d in self.dob if d.isdigit()]
        life_path_number = sum(digits)
        return self._reduce_to_single_digit(life_path_number)

    def getBirthDay(self):
        # Calculate the Birth Day number based on the day part of the date of birth.
        day = int(self.dob.split('-')[1])
        return self._reduce_to_single_digit(day)

    def getAttitude(self):
        # Calculate the Attitude Number based on the month and day of the date of birth.
        month, day = map(int, self.dob.split('-')[:2])
        attitude_number = month + day
        return self._reduce_to_single_digit(attitude_number)

    def _get_letter_value(self, letter):
        # Return the numerology value for a given letter.
        conversion_table = {
            'A': 1, 'J': 1, 'S': 1,
            'B': 2, 'K': 2, 'T': 2,
            'C': 3, 'L': 3, 'U': 3,
            'D': 4, 'M': 4, 'V': 4,
            'E': 5, 'N': 5, 'W': 5,
            'F': 6, 'O': 6, 'X': 6,
            'G': 7, 'P': 7, 'Y': 7,
            'H': 8, 'Q': 8, 'Z': 8,
            'I': 9, 'R': 9
        }
        return conversion_table.get(letter.upper(), 0)

    def getSoul(self):
        # Calculate the Soul Number using the vowels in the name.
        vowels = 'AEIOU'
        soul_number = sum(self._get_letter_value(char) for char in self.name if char.upper() in vowels)
        return self._reduce_to_single_digit(soul_number)

    def getPersonality(self):
        # Calculate the Personality Number using the consonants in the name.
        vowels = 'AEIOU'
        personality_number = sum(self._get_letter_value(char) for char in self.name if char.upper() not in vowels)
        return self._reduce_to_single_digit(personality_number)

    def getPowerName(self):
        # Calculate the Power Name Number by adding the Soul and Personality Numbers.
        soul = self.getSoul()
        personality = self.getPersonality()
        power_name_number = soul + personality
        return self._reduce_to_single_digit(power_name_number)
