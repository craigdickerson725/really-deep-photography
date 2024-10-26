document.addEventListener('DOMContentLoaded', function () {
    const stripe = Stripe('{{ stripe_publishable_key }}'); // Initialize Stripe with your publishable key
    const checkoutButton = document.getElementById('checkout-button');
    const form = document.getElementById('payment-form');

    // Function to toggle the visibility of shipping address fields based on the checkbox state
    function toggleShippingAddress() {
        const checkbox = document.getElementById('shipping_address_same');
        const shippingFields = document.getElementById('shipping_address_fields');
        if (shippingFields) { // Check if the shipping fields exist
            shippingFields.style.display = checkbox && checkbox.checked ? 'none' : 'block';
        }
    }

    // Initialize shipping address fields display on page load
    toggleShippingAddress();

    // Add event listener for the shipping address checkbox
    const shippingCheckbox = document.getElementById('shipping_address_same');
    if (shippingCheckbox) { // Check if the checkbox exists
        shippingCheckbox.addEventListener('change', toggleShippingAddress);
    }

    checkoutButton.addEventListener('click', async (event) => {
        // Prevent default form submission
        event.preventDefault();

        // Collect form data for backend processing
        const formData = {
            billing_name: form.first_name.value + ' ' + form.last_name.value, // Combine first and last name
            billing_address_1: form.billing_address_1.value,
            billing_address_2: form.billing_address_2.value, // Include optional field
            billing_city: form.city.value,
            billing_state: form.state.value,
            billing_zip_code: form.zip_code.value,
            billing_country: form.country.value,
            shipping_address_same: shippingCheckbox.checked,
        };

        if (!formData.shipping_address_same) {
            formData.shipping_address_1 = form.shipping_address_1.value;
            formData.shipping_address_2 = form.shipping_address_2.value; // Include optional shipping field
            formData.shipping_city = form.shipping_city.value;
            formData.shipping_state = form.shipping_state.value;
            formData.shipping_zip_code = form.shipping_zip_code.value;
            formData.shipping_country = form.shipping_country.value;
        }

        try {
            // Make a request to create a payment intent
            const response = await fetch('/create-payment-intent/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': form.elements.csrfmiddlewaretoken.value, // Include CSRF token
                },
                body: JSON.stringify(formData),
            });

            if (!response.ok) {
                throw new Error('Failed to create payment intent');
            }

            const { clientSecret } = await response.json();

            // Use Stripe.js to handle payment confirmation
            const cardElement = elements.create('card');
            cardElement.mount('#card-element'); // Mount card element
            const { error } = await stripe.confirmCardPayment(clientSecret, {
                payment_method: {
                    card: cardElement,
                },
            });

            if (error) {
                console.error('Payment failed:', error.message);
                alert('Payment failed. Please try again.');
            } else {
                alert('Payment succeeded! Redirecting to confirmation page...');
                window.location.href = '/confirmation/'; // Adjust this to your actual confirmation URL
            }
        } catch (error) {
            console.error('Error:', error.message);
            alert('An error occurred. Please try again.');
        }
    });
});
