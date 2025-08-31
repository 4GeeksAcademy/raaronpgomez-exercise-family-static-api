"""
Update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- get_member: Should return a member from the self._members list
"""

import random

class FamilyStructure:

    def __init__(self, last_name):
        self.last_name = last_name
        self._members = [
            {"id": 1, "first_name": "John", "age": 33, "lucky_numbers": [7, 13, 22]},
            {"id": 2, "first_name": "Jane", "age": 35, "lucky_numbers": [10, 14, 3]},
            {"id": 3, "first_name": "Jimmy", "age": 5, "lucky_numbers": [1]}
        ]

    def _generateId(self):
        return random.randint(0, 99999999)

    def add_member(self, member):
        if "id" not in member:
            member["id"] = self._generateId()
        self._members.append(member)
        return member  # 👈 devolvemos el miembro agregado

    def get_member(self, id):
        for m in self._members:
            if m["id"] == id:
                return m
        return None

    def delete_member(self, id):
        member = self.get_member(id)
        if member:
            self._members.remove(member)
            return True
        return False

    def get_all_members(self):
        return self._members
