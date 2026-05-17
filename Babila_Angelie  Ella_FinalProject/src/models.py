"""
Password entry model
"""

from datetime import datetime

class PasswordEntry:

    def __init__(
        self,
        website,
        username,
        password,
        strength
    ):

        self.website = website
        self.username = username
        self.password = password
        self.strength = strength

        self.date_added = datetime.now().strftime(
            "%Y-%m-%d %H:%M"
        )

        # Tuple example
        self.account_id = (
            website[:3].upper(),
            username[:3]
        )

    def to_dict(self):

        return {

            "website": self.website,
            "username": self.username,
            "password": self.password,
            "strength": self.strength,
            "date_added": self.date_added,
            "account_id": self.account_id
        }
compile
# Write to Angelie Ella Babila


