import unittest

from project import Project
from organisation import Organisation
from contact import Contact


class TestProject(unittest.TestCase):
    # arrange
    # Step 4
    def test_project_create(self):
        # Create an organisation
        org = Organisation('test')

        # act
        # Create a project associated with the organisation
        project = Project('test', 'org')

        print(org)

        # assert

    # Step 5
    # Add a test that test a contact can be created and
    def test_add_contact_to_project(self):
        # arrange
        # Create an organisation & contact
        org = Organisation('test')
        contact = Contact('ashton', 'a@a.com')
        org.add_contact(contact)

        # act
        # Create a project associated with the organisation
        project = Project('test', 'org')
        project.add_contact(contact)


        # added to an organisation and can also be added to a project
        self.assertIn(contact, project.contacts)

        # Challenge test that you can add a contact to an organisation
        # and a project using the project class

if __name__ == '__main__':
    unittest.main()
