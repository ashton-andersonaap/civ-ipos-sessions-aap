import unittest

from src.contact import Contact

class TestContact(unittest.TestCase):
    # Step 2
    def test_contact_creation(self):
        # Create a contact
        contact = Contact("ashton", "a@a.com")
        # Check if attributes are set correctly
        self.assertEqual(contact.name, "ashton")
        self.assertEqual(contact.email, "a@a.com")

if __name__ == '__main__':
    unittest.main()