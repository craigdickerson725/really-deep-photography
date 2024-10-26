// Stripe instance created using the publishable key (this can be dynamically set if needed)
const stripe = Stripe(document.getElementById('checkout-button').getAttribute('data-stripe-publishable-key'));

// Event listener for the checkout button to initiate the Stripe checkout process
document.getElementById('checkout-button').addEventListener('click', function () {
    
    // Fetch a new checkout session ID from the server
    fetch("/create-checkout-session/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": csrfToken // CSRF token passed as a header for security
        },
    })
    .then(response => response.json())
    .then(session => {
        // Redirect to Stripe's hosted checkout page with the session ID
        return stripe.redirectToCheckout({ sessionId: session.id });
    })
    .then(function (result) {
        // Handle any errors during the redirection process
        if (result.error) {
            alert(result.error.message);
        }
    })
    .catch(error => console.error("Error:", error));
});
