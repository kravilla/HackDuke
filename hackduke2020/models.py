from sqlalchemy import Column, Integer, String, Boolean, ARRAY
from database import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String(), unique=True)
    username = Column(String(), unique=True)
    password = Column(String(), unique=False)
    isMentor = Column(Boolean, unique=False)
    name = Column(String(), unique=False)
    preferences = Column(ARRAY(String()), unique=False)

    def __init__(self, email, username, password, name, preferences, isMentor=False):
        self.email = email
        self.username = username
        self.password = password
        self.name = name
        self.isMentor = isMentor
        self.preferences = preferences

    def changeName(self, newName):
        self.name = newName

    def changeUsername(self, newUsername):
        self.username = newUsername

    def changePassword(self, newPassword):
        self.password = newPassword

    def changeEmail(self, newEmail):
        self.email = newEmail

    def becomeMentor(self):
        self.isMentor = True

    def addPreferences(self, newPrefs):
        self.preferences += newPrefs

    def clearPrefs(self):
        self.preferences = []

    def deletePrefs(self, delPrefs):
        for delete in delPrefs:
            if delete in self.preferences:
                self.preferences.remove(delete)

    def __repr__(self):
        return ""
