document.addEventListener('DOMContentLoaded', function () {
    const stripe = Stripe('{{ stripe_publishable_key }}'); // Initialize Stripe with your publishable key
    const checkoutButton = document.getElementById('checkout-button');
    const form = document.getElementById('payment-form');

    // Function to toggle the visibility of shipping address fields based on the checkbox state
    function toggleShippingAddress() {
        const checkbox = document.getElementById('shipping_address_same');
        const shippingFields = document.getElementById('shipping_address_fields');
        shippingFields.style.display = checkbox.checked ? 'none' : 'block';
    }

    // Initialize shipping address fields display on page load
    toggleShippingAddress();

    // Add event listener for the shipping address checkbox
    document.getElementById('shipping_address_same').addEventListener('change', toggleShippingAddress);

    checkoutButton.addEventListener('click', async (event) => {
        // Prevent default form submission
        event.preventDefault();

        // Collect form data for backend processing
        const formData = {
            // Gather information such as total amount, billing, and shipping details
            billing_name: form.billing_name.value,
            billing_address_1: form.billing_address_1.value,
            billing_city: form.billing_city.value,
            billing_state: form.billing_state.value,
            billing_zip_code: form.billing_zip_code.value,
            billing_country: form.billing_country.value,
            shipping_address_same: document.getElementById('shipping_address_same').checked,
        };

        if (!formData.shipping_address_same) {
            // If shipping address is different, include shipping details
            formData.shipping_address_1 = form.shipping_address_1.value;
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
            const { error } = await stripe.confirmCardPayment(clientSecret);

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
