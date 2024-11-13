from django.test import TestCase
from django.urls import reverse
from django.contrib.messages import get_messages
from contact.models import ContactMessage

class ContactViewTests(TestCase):
    
    def test_contact_page_renders(self):
        """Test that the contact page renders successfully with a GET request."""
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact/contact.html')

    def test_contact_form_submission_success(self):
        """Test that a valid form submission creates a ContactMessage and redirects."""
        response = self.client.post(reverse('contact'), {
            'name': 'Test User',
            'email': 'test@example.com',
            'message': 'This is a test message.',
        })
        
        # Check that the ContactMessage was created
        self.assertEqual(ContactMessage.objects.count(), 1)
        
        # Check for the success message
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), 'Thank you for reaching out! Your message has been sent.')
        
        # Check that it redirects to the contact page
        self.assertRedirects(response, reverse('contact'))
        