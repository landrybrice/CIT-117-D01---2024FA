# NumerologyLifePathDetails.py

from Numerology import Numerology  # Importing the base class

class NumerologyLifePathDetails(Numerology):
    def __init__(self, Name: str, DateOfBirth: str):
        super().__init__(Name, DateOfBirth)  # Call the parent constructor
        self._name = Name  # Store the name

    @property
    def Name(self):
        return self.name

    @property
    def Birthdate(self):
        return self.dob

    @property
    def Attitude(self):
        return self.getAttitude()

    @property
    def BirthDay(self):
        return self.getBirthDay()

    @property
    def LifePath(self):
        return self.getLifePath()

    @property
    def Personality(self):
        return self.getPersonality()

    @property
    def PowerName(self):
        return self.getPowerName()

    @property
    def Soul(self):
        return self.getSoul()

    @property
    def LifePathDescription(self):
        life_path = self.LifePath  # Access the computed life path number
        descriptions = {
            1: "The Independent: Wants to work/think for themselves",
            2: "The Mediator: Avoids conflict and wants love and harmony",
            3: "The Performer: Likes music, art and to perform or get attention",
            4: "The Teacher/Truth Seeker: Is meant to be a teacher or mentor and is truthful",
            5: "The Adventurer: Likes to travel and meet others, often an extrovert",
            6: "The Inner Child: Is meant to be a parent and/or one that is young at heart",
            7: "The Naturalist: Enjoy nature and water and alternative life paths, open to spirituality",
            8: "The Executive: Gravitates to money and power",
            9: "The Humanitarian: Helps others and/or experiences pain and learns the hard way"
        }
        return descriptions.get(life_path, "Unknown Life Path")  # Return a default message if not found

# End of NumerologyLifePathDetails.py
