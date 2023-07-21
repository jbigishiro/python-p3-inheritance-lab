#!/usr/bin/env python

from user import User

import random

# Assuming the User class is already defined in user.py

class Teacher(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.knowledge = ["Math", "Science", "History"]  # Example knowledge list

    def teach(self):
        return random.choice(self.knowledge)  # select randomly in the knowledge list
