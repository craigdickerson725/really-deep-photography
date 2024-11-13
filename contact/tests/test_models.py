from django.test import TestCase
from contact.models import ContactMessage

class ContactMessageModelTest(TestCase):
    def setUp(self):
        # Set up a sample ContactMessage instance for testing
        self.contact_message = ContactMessage.objects.create(
            name="John Doe",
            email="johndoe@example.com",
            message="This is a test message."
        )

    def test_contact_message_creation(self):
        """Test that a ContactMessage instance is created successfully."""
        self.assertIsInstance(self.contact_message, ContactMessage)
        self.assertEqual(self.contact_message.name, "John Doe")
        self.assertEqual(self.contact_message.email, "johndoe@example.com")
        self.assertEqual(self.contact_message.message, "This is a test message.")

    def test_contact_message_str_method(self):
        """Test the __str__ method returns the correct string."""
        expected_str = f"Message from John Doe - johndoe@example.com"
        self.assertEqual(str(self.contact_message), expected_str)

    def test_auto_now_add_date_sent(self):
        """Test that date_sent is automatically set on creation."""
        self.assertIsNotNone(self.contact_message.date_sent)
