from organisation import Organisation
class Project:
    def __init__(self, name, organisation):
        self.name = name
        self.organisation = organisation
        self.contacts = []
# add contacts
    def add_contact(self, contact):
        self.contacts.append(contact)
# Challenge - For a contact to be added to a
# project it must already exist in the organisation

# TODO add rest of setters
