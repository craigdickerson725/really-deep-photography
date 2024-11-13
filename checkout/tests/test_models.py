# checkout/tests/test_models.py
from django.test import TestCase
from decimal import Decimal
from photos.models import Photo
from checkout.models import Order, OrderLineItem
from django.utils import timezone


class OrderModelTest(TestCase):
    """Test the Order model."""

    def setUp(self):
        """Create an order instance for testing."""
        self.order = Order.objects.create(
            full_name="John Doe",
            email="johndoe@example.com",
            phone_number="1234567890",
            country="US",
            town_or_city="New York",
            street_address1="123 Elm St",
            order_total=Decimal("50.00"),
            grand_total=Decimal("50.00"),
            original_cart="[]",
            stripe_pid="stripe_pid_12345"
        )

    def test_generate_order_number(self):
        """Test the order number generation."""
        self.assertTrue(self.order.order_number)
        self.assertEqual(len(self.order.order_number), 32)

    def test_update_total(self):
        """Test the update_total method."""
        # Create a photo to add to the order
        photo = Photo.objects.create(
            title="Test Photo",
            price=Decimal("25.00"),
            image="test.jpg"
        )
        
        # Create an order line item
        line_item = OrderLineItem.objects.create(
            order=self.order,
            photo=photo,
            quantity=2
        )
        
        self.order.update_total()
        self.assertEqual(self.order.order_total, Decimal("50.00"))
        self.assertEqual(self.order.grand_total, Decimal("50.00"))

    def test_save_method(self):
        """Test the save method that generates order number if not set."""
        new_order = Order.objects.create(
            full_name="Jane Doe",
            email="janedoe@example.com",
            phone_number="0987654321",
            country="US",
            town_or_city="Los Angeles",
            street_address1="456 Oak St",
            order_total=Decimal("30.00"),
            grand_total=Decimal("30.00"),
            original_cart="[]",
            stripe_pid="stripe_pid_67890"
        )
        self.assertTrue(new_order.order_number)
        self.assertEqual(len(new_order.order_number), 32)


class OrderLineItemModelTest(TestCase):
    """Test the OrderLineItem model."""

    def setUp(self):
        """Create an order and line item for testing."""
        photo = Photo.objects.create(
            title="Test Photo",
            price=Decimal("25.00"),
            image="test.jpg"
        )
        self.order = Order.objects.create(
            full_name="John Doe",
            email="johndoe@example.com",
            phone_number="1234567890",
            country="US",
            town_or_city="New York",
            street_address1="123 Elm St",
            order_total=Decimal("50.00"),
            grand_total=Decimal("50.00"),
            original_cart="[]",
            stripe_pid="stripe_pid_12345"
        )
        self.line_item = OrderLineItem.objects.create(
            order=self.order,
            photo=photo,
            quantity=2
        )

    def test_lineitem_total(self):
        """Test that the lineitem total is calculated correctly."""
        self.assertEqual(self.line_item.lineitem_total, Decimal("50.00"))

    def test_save_method(self):
        """Test that the lineitem save method correctly updates the order total."""
        self.line_item.quantity = 3
        self.line_item.save()
        self.order.refresh_from_db()
        self.assertEqual(self.line_item.lineitem_total, Decimal("75.00"))
        self.assertEqual(self.order.order_total, Decimal("75.00"))
        self.assertEqual(self.order.grand_total, Decimal("75.00"))
