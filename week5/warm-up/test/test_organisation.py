import unittest
from organisation import Organisation
from contact import Contact

# Step 1
class TestOrganisation(unittest.TestCase):
    def test_add_organisation(self):
        # Create an organization
        org = Organisation("TAFE")
        self.assertEqual(org.name, 'TAFE', "NAME NOT EQUAL")

    # Step 3
    def test_add_contact(self):
        # Create an organisation
        org = Organisation("TAFE")

        # Create a contact
        contact = Contact("ashton", "a@a.com")
        # Add contact to organisation
        org.add_contact(contact)
        # Check if contact is added to the organisation
        self.assertIn(contact, org.get_contacts())

if __name__ == '__main__':
    unittest.main()