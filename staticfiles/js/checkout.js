document.addEventListener('DOMContentLoaded', function () {
    const stripe = Stripe('{{ stripe_publishable_key }}'); // Initialize Stripe with your publishable key
    const elements = stripe.elements(); // Initialize Stripe Elements
    const checkoutButton = document.getElementById('checkout-button');
    const form = document.getElementById('payment-form');

    // Create a Card Element and mount it to the DOM
    const cardElement = elements.create('card');
    cardElement.mount('#card-element');

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

        // Collect shipping address data if the checkbox is unchecked
        if (!formData.shipping_address_same) {
            formData.shipping_address_1 = form.shipping_address_1.value;
            formData.shipping_address_2 = form.shipping_address_2.value; // Include optional shipping field
            formData.shipping_city = form.shipping_city.value;
            formData.shipping_state = form.shipping_state.value;
            formData.shipping_zip_code = form.shipping_zip_code.value;
            formData.shipping_country = form.shipping_country.value;
        }

        try {
            // Create a payment intent
            const response = await fetch('/create-payment-intent/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrftoken'),
                },
                body: JSON.stringify(formData),
            });

            if (!response.ok) {
                throw new Error('Failed to create payment intent');
            }

            const { clientSecret } = await response.json();

            // Use Stripe.js to handle payment confirmation
            const { error, paymentIntent } = await stripe.confirmCardPayment(clientSecret, {
                payment_method: {
                    card: cardElement,
                    billing_details: {
                        name: formData.billing_name,
                        address: {
                            line1: formData.billing_address_1,
                            line2: formData.billing_address_2,
                            city: formData.billing_city,
                            state: formData.billing_state,
                            postal_code: formData.billing_zip_code,
                            country: formData.billing_country,
                        }
                    }
                }
            });

            if (error) {
                console.error('Payment failed:', error.message);
                alert('Payment failed. Please try again.');
            } else if (paymentIntent.status === 'succeeded') {
                // Payment was successful
                alert('Payment succeeded! Redirecting to success page...');

                // Clear the cart on the server
                const clearCartResponse = await fetch('/clear-cart/', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': getCookie('csrftoken'),
                    }
                });

                if (!clearCartResponse.ok) {
                    console.error('Failed to clear cart:', await clearCartResponse.text());
                    alert('Payment succeeded, but failed to clear the cart.');
                }

                // Redirect to success page
                window.location.href = '/checkout-success/';
            }
        } catch (error) {
            console.error('Error:', error.message);
            alert('An error occurred. Please try again.');
        }
    });

    // Helper function to get CSRF token
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});
