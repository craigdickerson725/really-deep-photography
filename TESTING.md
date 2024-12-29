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

### Regression Testing
- **Objective:** Ensure that previous features continue to work as intended after updates and new implementations.
- **Testing Steps:**
    - After each significant change, retest all core features, including navigation, cart functionality, and checkout.
    - Run automated tests to confirm that functionality remains intact across features.
- **Outcome:** Regression testing confirmed that no new updates introduced issues to existing features.
- **Adjustments:** None needed; regression testing confirmed stability.

### Documentation and Logs
- **Objective:** Maintain clear documentation of testing procedures, outcomes, and any adjustments made.
- **Testing Steps:**
    - Log each testing session’s results and record any identified bugs along with the resolution steps.
    - Use these records to verify that all major issues were tracked and resolved systematically.
- **Outcome:** Complete documentation maintained for all testing, assisting in troubleshooting and future reference.
- **Adjustments:** Documentation reviewed and updated to improve clarity and detail.

## Code Validation

### HTML

I have used the recommended [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.

| Directory | File | Screenshot | Notes |
| --- | --- | --- | --- |
| about | about.html | ![screenshot](documentation/validation/about.png) | |
| cart | cart.html | ![screenshot](documentation/validation/cart.png) | |
| checkout | checkout.html | ![screenshot](documentation/validation/checkout.png) | |
| checkout | checkout_success.html | ![screenshot](documentation/validation/checkout_success.png) | |
| checkout | order_confirmation_email.html | ![screenshot](documentation/validation/order_confirmation_email.png) | |
| contact | contact.html | ![screenshot](documentation/validation/contact.png) | |
| home | index.html | ![screenshot](documentation/validation/home.png) | |
| photos | admin_panel.html | ![screenshot](documentation/validation/admin_panel.png) | |
| photos | edit_photo.html | ![screenshot](documentation/validation/edit_photo.png) | |
| faq | faq.html | ![screenshot](documentation/validation/faq.png) | |
| photos | gallery.html | ![screenshot](documentation/validation/gallery.png) | |
| photos | no_permission.html | ![screenshot](documentation/validation/no_permission.png) | |
| photos | photo_detail.html | ![screenshot](documentation/validation/photo_detail.png) | |
| photos | search_results.html | ![screenshot](documentation/validation/search_results.png) | |
| templates | 404.html | ![screenshot](documentation/validation/404.png) | |

### CSS

I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate all of my CSS files.

| Directory | File | Screenshot | Notes |
| --- | --- | --- | --- |
| checkout | checkout.css | ![screenshot](documentation/validation/checkout_css.png) | |
| static | style.css | ![screenshot](documentation/validation/style_css.png) | |

### JavaScript

I have used the recommended [JShint Validator](https://jshint.com) to validate all of my JS files.

| Directory | File | Screenshot | Notes |
| --- | --- | --- | --- |
| checkout | stripe_elements.js | ![screenshot](documentation/validation/stripe_elements.png) | |
| static | checkout.js | ![screenshot](documentation/validation/checkout_js.png) | |

### Python

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

| Directory | File | CI URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
| about | admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/craigdickerson725/really-deep-photography/main/about/admin.py) | ![screenshot](documentation/validation/python_validation/about_admin.png) | |
| about | models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/craigdickerson725/really-deep-photography/main/about/models.py) | ![screenshot](documentation/validation/python_validation/about_models.png) | |
| about | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/craigdickerson725/really-deep-photography/main/about/urls.py) | ![screenshot](documentation/validation/python_validation/about_urls.png) | |
| about | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/craigdickerson725/really-deep-photography/main/about/views.py) | ![screenshot](documentation/validation/python_validation/about_views.png) | |
| admin_panel | admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/craigdickerson725/really-deep-photography/main/about/admin.py) | ![screenshot](documentation/validation/python_validation/admin_panel_admin.png) | |
| admin_panel | models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/craigdickerson725/really-deep-photography/main/about/models.py) | ![screenshot](documentation/validation/python_validation/admin_panel_models.png) | |
| admin_panel | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/craigdickerson725/really-deep-photography/main/about/urls.py) | ![screenshot](documentation/validation/python_validation/admin_panel_urls.png) | |
| admin_panel | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/craigdickerson725/really-deep-photography/main/about/views.py) | ![screenshot](documentation/validation/python_validation/admin_panel_views.png) | |
| cart | admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/craigdickerson725/really-deep-photography/main/cart/admin.py) | ![screenshot](documentation/validation/python_validation/cart_admin.png) | |
| cart | contexts.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/craigdickerson725/really-deep-photography/main/cart/contexts.py) | ![screenshot](documentation/validation/python_validation/cart_contexts.png) | |
| cart | models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/craigdickerson725/really-deep-photography/main/cart/models.py) | ![screenshot](documentation/validation/python_validation/cart_models.png) | |
| cart | cart_tools.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/craigdickerson725/really-deep-photography/main/cart/templatetags/cart_tools.py) | ![screenshot](documentation/validation/python_validation/cart_cart_tools.png) | |
| cart | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/craigdickerson725/really-deep-photography/main/cart/urls.py) | ![screenshot](documentation/validation/python_validation/cart_urls.png) | |
| cart | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/craigdickerson725/really-deep-photography/main/cart/views.py) | ![screenshot](documentation/validation/python_validation/cart_views.png) | |
| checkout | admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/craigdickerson725/really-deep-photography/main/checkout/admin.py) | ![screenshot](documentation/validation/python_validation/checkout_admin.png) | |
| checkout | forms.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/craigdickerson725/really-deep-photography/main/checkout/forms.py) | ![screenshot](documentation/validation/python_validation/checkout_forms.png) | |
| checkout | models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/craigdickerson725/really-deep-photography/main/checkout/models.py) | ![screenshot](documentation/validation/python_validation/checkout_models.png) | |
| checkout | signals.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/craigdickerson725/really-deep-photography/main/checkout/signals.py) | ![screenshot](documentation/validation/python_validation/checkout_signals.png) | |
| checkout | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/craigdickerson725/really-deep-photography/main/checkout/urls.py) | ![screenshot](documentation/validation/python_validation/checkout_urls.png) | |
| checkout | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/craigdickerson725/really-deep-photography/main/checkout/views.py) | ![screenshot](documentation/validation/python_validation/checkout_views.png) | |
| contact | admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/craigdickerson725/really-deep-photography/main/contact/admin.py) | ![screenshot](documentation/validation/python_validation/contact_admin.png) | |
| contact | models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/craigdickerson725/really-deep-photography/main/contact/models.py) | ![screenshot](documentation/validation/python_validation/contact_models.png) | |
| contact | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/craigdickerson725/really-deep-photography/main/contact/urls.py) | ![screenshot](documentation/validation/python_validation/contact_urls.png) | |
| contact | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/craigdickerson725/really-deep-photography/main/contact/views.py) | ![screenshot](documentation/validation/python_validation/contact_views.png) | |
| faq | admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/craigdickerson725/really-deep-photography/main/faq/admin.py) | ![screenshot](documentation/validation/python_validation/faq_admin.png) | |
| faq | forms.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/craigdickerson725/really-deep-photography/main/faq/forms.py) | ![screenshot](documentation/validation/python_validation/faq_forms.png) | |
| faq | models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/craigdickerson725/really-deep-photography/main/faq/models.py) | ![screenshot](documentation/validation/python_validation/faq_models.png) | |
| faq | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/craigdickerson725/really-deep-photography/main/faq/urls.py) | ![screenshot](documentation/validation/python_validation/faq_urls.png) | |
| faq | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/craigdickerson725/really-deep-photography/main/faq/views.py) | ![screenshot](documentation/validation/python_validation/faq_views.png) | |
| home | admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/craigdickerson725/really-deep-photography/main/home/admin.py) | ![screenshot](documentation/validation/python_validation/home_admin.png) | |
| home | models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/craigdickerson725/really-deep-photography/main/home/models.py) | ![screenshot](documentation/validation/python_validation/home_models.png) | |
| home | custom_filters.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/craigdickerson725/really-deep-photography/main/home/templatetags/custom_filters.py) | ![screenshot](documentation/validation/python_validation/home_custom_filters.png) | |
| home | user_filters.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/craigdickerson725/really-deep-photography/main/home/templatetags/user_filters.py) | ![screenshot](documentation/validation/python_validation/home_user_filters.png) | |
| home | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/craigdickerson725/really-deep-photography/main/home/urls.py) | ![screenshot](documentation/validation/python_validation/home_urls.png) | |
| home | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/craigdickerson725/really-deep-photography/main/home/views.py) | ![screenshot](documentation/validation/python_validation/home_views.png) | |
|  | manage.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/craigdickerson725/really-deep-photography/main/manage.py) | ![screenshot](documentation/validation/python_validation/main_manage.png) | |
| photos | admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/craigdickerson725/really-deep-photography/main/photos/admin.py) | ![screenshot](documentation/validation/python_validation/photos_admin.png) | |
| photos | forms.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/craigdickerson725/really-deep-photography/main/photos/forms.py) | ![screenshot](documentation/validation/python_validation/photos_forms.png) | |
| photos | models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/craigdickerson725/really-deep-photography/main/photos/models.py) | ![screenshot](documentation/validation/python_validation/photos_models.png) | |
| photos | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/craigdickerson725/really-deep-photography/main/photos/urls.py) | ![screenshot](documentation/validation/python_validation/photos_urls.png) | |
| photos | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/craigdickerson725/really-deep-photography/main/photos/views.py) | ![screenshot](documentation/validation/python_validation/photos_views.png) | |
| really_deep_photography | settings.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/craigdickerson725/really-deep-photography/main/really_deep_photography/settings.py) | ![screenshot](documentation/validation/python_validation/rdp_settings.png) | |
| really_deep_photography | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/craigdickerson725/really-deep-photography/main/really_deep_photography/urls.py) | ![screenshot](documentation/validation/python_validation/rdp_urls.png) | |
| really_deep_photography | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/craigdickerson725/really-deep-photography/main/really_deep_photography/views.py) | ![screenshot](documentation/validation/python_validation/rdp_views.png) | |

## Browser Compatibility

I've tested my deployed project on multiple browsers to check for compatibility issues.

| Browser | Home | Gallery | About | Contact | Cart | Checkout | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Chrome | ![screenshot](documentation/browsers/chrome01.png) | ![screenshot](documentation/browsers/chrome02.png) | ![screenshot](documentation/browsers/chrome03.png) | ![screenshot](documentation/browsers/chrome04.png) | ![screenshot](documentation/browsers/chrome05.png) | ![screenshot](documentation/browsers/chrome06.png) | Works as expected |
| Edge | ![screenshot](documentation/browsers/edge01.png) | ![screenshot](documentation/browsers/edge02.png) | ![screenshot](documentation/browsers/edge03.png) | ![screenshot](documentation/browsers/edge04.png) | ![screenshot](documentation/browsers/edge05.png) | ![screenshot](documentation/browsers/edge06.png) | Works as expected |
| Firefox | ![screenshot](documentation/browsers/firefox01.png) | ![screenshot](documentation/browsers/firefox02.png) | ![screenshot](documentation/browsers/firefox03.png) | ![screenshot](documentation/browsers/firefox04.png) | ![screenshot](documentation/browsers/firefox05.png) | ![screenshot](documentation/browsers/firefox06.png) | Works as expected |

## Responsiveness

I've tested my deployed project on multiple devices to check for responsiveness issues.

| Device | Home | Gallery | About | Contact | Cart | Checkout | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Mobile (DevTools) | ![screenshot](documentation/responsiveness/mobile01.png) | ![screenshot](documentation/responsiveness/mobile02.png) | ![screenshot](documentation/responsiveness/mobile03.png) | ![screenshot](documentation/responsiveness/mobile04.png) | ![screenshot](documentation/responsiveness/mobile05.png) | ![screenshot](documentation/responsiveness/mobile06.png) | Works as expected |
| Tablet (DevTools) | ![screenshot](documentation/responsiveness/tablet01.png) | ![screenshot](documentation/responsiveness/tablet02.png) | ![screenshot](documentation/responsiveness/tablet03.png) | ![screenshot](documentation/responsiveness/tablet04.png) | ![screenshot](documentation/responsiveness/tablet05.png) | ![screenshot](documentation/responsiveness/tablet06.png) | Works as expected |
| Desktop | ![screenshot](documentation/responsiveness/desktop01.png) | ![screenshot](documentation/responsiveness/desktop02.png) | ![screenshot](documentation/responsiveness/desktop03.png) | ![screenshot](documentation/responsiveness/desktop04.png) | ![screenshot](documentation/responsiveness/desktop05.png) | ![screenshot](documentation/responsiveness/desktop06.png) | Works as expected |
| XL Monitor | ![screenshot](documentation/responsiveness/xl01.png) | ![screenshot](documentation/responsiveness/xl02.png) | ![screenshot](documentation/responsiveness/xl03.png) | ![screenshot](documentation/responsiveness/xl04.png) | ![screenshot](documentation/responsiveness/xl05.png) | ![screenshot](documentation/responsiveness/xl06.png) | Scaling starts to have minor issues |
| 4K Monitor | ![screenshot](documentation/responsiveness/4k01.png) | ![screenshot](documentation/responsiveness/4k02.png) | ![screenshot](documentation/responsiveness/4k03.png) | ![screenshot](documentation/responsiveness/4k04.png) | ![screenshot](documentation/responsiveness/4k05.png) | ![screenshot](documentation/responsiveness/4k06.png) | Scaling has minor issues |

## Lighthouse Audit

I've tested my deployed project using the Lighthouse Audit tool to check for any major issues.

| Page | Mobile | Desktop | Notes |
| --- | --- | --- | --- |
| Home | ![screenshot](documentation/lighthouse/home01.png) | ![screenshot](documentation/lighthouse/home02.png) | Some minor warnings |
| Gallery | ![screenshot](documentation/lighthouse/gallery01.png) | ![screenshot](documentation/lighthouse/gallery02.png) | Some minor warnings |
| About | ![screenshot](documentation/lighthouse/about01.png) | ![screenshot](documentation/lighthouse/about02.png) | Slow response time due to large images |
| Contact | ![screenshot](documentation/lighthouse/contact01.png) | ![screenshot](documentation/lighthouse/contact02.png) | Slow response time due to large images |
| Cart | ![screenshot](documentation/lighthouse/cart01.png) | ![screenshot](documentation/lighthouse/cart02.png) | Slow response time due to large images |
| Checkout | ![screenshot](documentation/lighthouse/checkout01.png) | ![screenshot](documentation/lighthouse/checkout02.png) | Slow response time due to large images |

## Devensive Programming

Defensive programming ensures the security and reliability of the Really Deep Photography website by preventing unauthorized actions and handling invalid or malicious inputs effectively. This section documents the manual and automated tests conducted to validate defensive programming measures, focusing on the following key areas:

- Form Validation: 
    - Ensuring users provide valid inputs and required fields are completed.
- Authentication and Authorization: 
    - Restricting access to pages and features based on user roles.
- Data Protection: 
    - Preventing unauthorized users from accessing or manipulating another user's data.
- Error Handling: 
    - Gracefully handling unexpected behavior to maintain site stability.

### Manual Test Cases

The table below summarizes manual tests performed across key pages to validate defensive programming practices.

| Page | Expectation | Test | Result | Fix | Screenshot |
| --- | --- | --- | --- | --- | --- |
| Home | | | | | |
| | Only three featured photos should display at a time. | Added more than three photos with is_featured=True via the admin panel. | Only three featured photos displayed on the home page. | Test concluded and passed | ![screenshot](documentation/defensive_programming/defensive01.png) |
| Gallery | | | | | |
| | Admins must upload image files when updating the gallery in the admin panel. | Attempted to upload a gallery entry without a selected image | Server rejected the files and displayed a validation error. | Test concluded and passed | ![screenshot](documentation/defensive_programming/defensive02.png) |
| Cart | | | | | |
| | Users cannot update the cart if they are not logged in. | Attempted to add an item to the cart without logging in. | Redirected to the login page before adding the item. | Test concluded and passed | ![screenshot](documentation/defensive_programming/defensive03.png) |
| Checkout | | | | | |
| | Only authenticated users can access the checkout page. | Attempted to access /checkout/ while logged out. | Redirected to the login page. | Test concluded and passed | ![screenshot](documentation/defensive_programming/defensive04.png) |
| | Form fields must not accept invalid data. | Entered invalid credit card details (e.g., 1234 5678 9012 3456, expiration: 13/2024). | Stripe rejected the input, and the user was notified of invalid card details. | Test concluded and passed | ![screenshot](documentation/defensive_programming/defensive05.png) |
| Contact | | | | | |
| | Users must enter all required fields to submit the contact form. | Attempted to submit the form with one or more empty fields. | Form displayed an error: "This field is required." | Test concluded and passed | ![screenshot](documentation/defensive_programming/defensive06.png) |

This section provides a view of some of the security measures and their effectiveness across the site, ensuring a reliable and secure user experience.

## User Story Testing

| User Story | Screenshot |
| --- | --- |
| As a customer I can browse a gallery of available photos so that I can choose which prints to purchase | ![screenshot](documentation/user_story_testing/ust01.png) |
| As a customer I can view details of a photo so that I can see a larger image and more information (e.g., description, dimensions, price) | ![screenshot](documentation/user_story_testing/ust02.png) |
| As a customer I can create an account so that I can log in to add/purchase items | ![screenshot](documentation/user_story_testing/ust03.png) |
| As a customer I can receive password reset emails so that I can regain access to my account if I forget my password | ![screenshot](documentation/user_story_testing/ust04.png) |
| As a customer I can search for specific photos or categories so that I can find something specific to buy | ![screenshot](documentation/user_story_testing/ust05.png) |
| As a customer I can review the items in my cart so that I can make sure I'm ready to checkout | ![screenshot](documentation/user_story_testing/ust06.png) |
| As a customer I can add a photo to my shopping cart so that I can purchase it later | ![screenshot](documentation/user_story_testing/ust07.png) |
| As a customer I can complete a checkout process so that I can purchase the selected photos | ![screenshot](documentation/user_story_testing/ust08.png) |
| As a customer I can receive an email confirmation after I make a purchase so that I have a record of my order | ![screenshot](documentation/user_story_testing/ust09.png) |
| As a site admin I can upload new photos to the website so that customers can purchase them | ![screenshot](documentation/user_story_testing/ust10.png) |
| As a site admin I can manage existing photos (edit titles, prices, or remove them) so that my gallery stays up to date | ![screenshot](documentation/user_story_testing/ust11.png) |
| As a site admin I can view a list of all orders so that I can keep track of what has been sold and needs to be shipped | ![screenshot](documentation/user_story_testing/ust12.png) |
| As a site admin I can employ SEO strategies so that my website ranks higher in search results | ![screenshot](documentation/user_story_testing/ust13.png) |
| As a site admin I can integrate social media links so that I can promote my work easily | ![screenshot](documentation/user_story_testing/ust14.png) |

## Bugs

**Fixed Bugs**

During the development of the Really Deep Photography project, several bugs were encountered, particularly when I refactored the application by breaking each page into its own app. This restructuring led to issues with reverse lookups, redirects, and incorrect URL paths, as I occasionally missed updating the paths after splitting the apps. These issues often resulted in the site not loading the correct pages or redirecting users to incorrect URLs.

A security issue was also raised when it was demonstrated that the edit photo section of the on-site admin panel could be accessed (without authorized credentials) by brute force if the url was pasted into the web-browser.  This was quite an easy fix, once the issue was exposed.

The most significant bug occurred within the shopping cart functionality. Specifically, the cart would not update when multiple instances of the same photo were added. This bug was challenging to capture with a screenshot since the problem was related to something that did not happen. After investigation, I discovered that the issue was caused by a statement where an integer was being used. The integer needed to be converted to a string for the cart to properly handle the update. I would not have discovered the cause at all if not for Oisin from Code Institute's Tutor Support Team.  He was very thorough, and patient, and brilliant for catching this one.  His help was certainly vital to this project!  Once this conversion was made, the issue was resolved, and the cart began updating correctly when multiple identical photos were added.

## Unfixed Bugs

> [!NOTE]  
> There are no remaining bugs that I am aware of, though even after thorough testing, I cannot rule out the possibility.
