# Testing

> [!NOTE]  
> Return back to the [README.md](README.md) file.

## Overview

In this section, we document the testing efforts made to ensure that Really Deep Photography functions as expected, providing a smooth and reliable experience for users. Each feature was thoroughly tested to verify that it meets its intended purpose, from navigation and responsive design to core functionality such as the shopping cart and checkout process. Testing was conducted across various devices and browsers to ensure compatibility and accessibility, aiming to deliver a well-rounded, user-friendly website.

### Feature-by-Feature Testing

- #### **Navigation Testing**

    - **Objective:** Verify that all navigation links lead to the correct destinations and that transitions between pages are smooth.
    - **Testing Steps:**
        - Click each link in the navigation bar (e.g., Home, Gallery, Cart, Checkout) to confirm it leads to the correct page.
        - Ensure the active page is clearly indicated by the highlighted menu item.
    - **Outcome:** All links function as expected, with smooth page transitions.
    - **Adjustments:** None needed.

- #### **Responsive Design Testing**

    - **Objective:** Ensure the site layout and features adjust correctly on different screen sizes and orientations.
    - **Testing Steps:**
        - Open the site on various devices (desktop, tablet, and mobile).
        - Use the browser's developer tools to test screen widths from 375px (mobile) to 1200px (large desktop).
    - **Outcome:** The design adjusts correctly across all tested screen sizes.
    - **Adjustments:** Minor CSS tweaks for spacing and alignment on mobile screens.

- #### **Gallery Feature Testing**

    - **Objective:** Confirm that customers can view a gallery of photos, each displaying accurately with details and a clickable link.
    - **Testing Steps:**
        - Browse the gallery page to check for photo visibility, layout, and functionality.
        - Click on each photo to ensure it opens the detailed photo view.
    - **Outcome:** All gallery items load correctly, with each photo link working as intended.
    - **Adjustments:** Updated alt tags for improved accessibility and SEO.

- #### **Search Function Testing**

    - **Objective:** Ensure customers can search for photos by keyword or category.
    - **Testing Steps:**
        - Enter a variety of search terms and verify that results display relevant photos.
        - Try searching with no results expected to ensure a “no results” message appears.
    - **Outcome:** The search function returns appropriate photos based on the input.
    - **Adjustments:** Fine-tuned the search results message for clarity.

- #### **Shopping Cart Testing**

    - **Objective:** Confirm that customers can add items to the cart, view the cart, update quantities, and remove items if needed.
    - **Testing Steps:**
        - Add multiple photos to the cart and verify they appear with the correct details (title, size, price).
        - Adjust item quantities in the cart and ensure the total price updates accordingly.
        - Remove an item from the cart and verify it is correctly removed, with the total price reflecting the change.
    - **Outcome:** Items are successfully added, updated, and removed from the cart, with correct totals displaying at each step.
    - **Adjustments:** Minor adjustments to update messages for clarity (e.g., “Item added to cart” notification).

- #### **Checkout Process Testing**

    - **Objective:** Ensure that the checkout process works smoothly, from entering payment details to receiving an order confirmation.
    - **Testing Steps:**
        - Go through the checkout steps by entering shipping and billing details, verifying that the form accepts valid inputs and shows appropriate validation errors for incomplete entries.
        - Complete a payment using Stripe and confirm the order success page appears.
        - Check the receipt email to verify that order details (e.g., items purchased, total cost) match the transaction.
    - **Outcome:** The checkout process completes successfully, with an order confirmation page and a correctly formatted receipt email sent to the user.
    - **Adjustments:** Updated validation messaging for missing or invalid fields to enhance user guidance.

### User Experience Testing

- #### **Usability Testing**

    - **Objective:** Assess ease of use by observing users as they navigate the site.
    - **Testing Steps:**
        - Select a group of users unfamiliar with the site and observe their interaction, noting any points of confusion or friction.
        - Collect feedback on the clarity of navigation, layout, and ease of completing core tasks (e.g., browsing, adding items to the cart, checkout).
    - **Outcome:** Users were able to navigate easily with minimal guidance, completing tasks with minimal difficulty.
    - **Adjustments:** Adjusted button labels for improved clarity (e.g., changing “Proceed” to “Checkout”).

- **Accessibility Testing**

    - **Objective:** Ensure the site is accessible to users with disabilities, including compatibility with screen readers and navigability by keyboard.
    - **Testing Steps:**
        - Use a screen reader to navigate the site, ensuring all images have descriptive alt text and page elements are labeled.
        - Verify keyboard-only navigation through all site elements.
    - **Outcome:** Site meets accessibility standards, with all elements accessible by keyboard and screen reader-compatible alt text added.
    - **Adjustments:** Minor tweaks to alt text descriptions for improved readability.

### Compatibility Testing

- #### **Browser Compatibility**

    - **Objective:** Ensure consistent performance across multiple browsers (Chrome, Firefox, Safari, Edge).
    - **Testing Steps:**
        - Open the site in each browser and check that all functionality and layout appear consistent.
    - **Outcome:** The site performs consistently across all tested browsers.
    - **Adjustments:** Minor CSS adjustments for Safari to improve alignment on some elements.

- #### **Device Compatibility**

    - **Objective:** Verify site functionality on a range of devices (desktop, laptop, tablet, and mobile).
    - **Testing Steps:**
        - Test on different devices to confirm that all elements render correctly and interact as intended.
    - **Outcome:** The site is fully functional on all tested devices.
    - **Adjustments:** Updated media queries to ensure consistent spacing on smaller screens.