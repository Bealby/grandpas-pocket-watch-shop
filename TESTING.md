# Testing

---

## Contents

---

1.[Automated Testing](#automated-testing)

- [W3C](#w3c)
- [WSC](#wsc)
- [PEP8](#pep8)
- [Markdownlint](#markdownlint)
- [Validate JavaScript](#validate-javascript)
- [Terminal](#terminal)
- [Lighthouse Audit](#lighthouse-audit)
- [Chrome Developer Tools](#chrome-developer-tools)
- [Unit Tests](#unit-tests)

2.[Non-Automated Testing](#non-automated-testing)

- [Main Header](#main-header)
- [Navigation Bar](#navigation-bar)
- [Home Page](#home-page)
- [Products App](#products-app)
- [Basket App](#basket-app)
- [Checkout App](#checkout-app)
- [Profile App](#profile-app)
- [Services App](#services-app)
- [Contact App](#contact-app)
- [Footer](#footer)
- [Desktop Browsers](#desktop-browsers)
- [Mobile and Tablet Devices](#mobile-and-tablet-devices)
- [User Testing](#user-testing)
- [Agile User Stories](#agile-user-stories)

3.[Fixes](#fixes)

4.[Not Fixed](#not-fixed)

---

## Automated Testing

---

### W3C

- [W3C](https://validator.w3.org/) - All HTML files with
  their data were directly input into the Mark-Up
  Validation Service.

- Results: All HTML code adheres to validation requirements.
  Errors for Python only.

### WSC

- [WSC](https://jigsaw.w3.org/css-validator/) - CSS data was
  directly input into the CSS Validation Service.

  Results: `Congratulations! No Error Found.`

### PEP8

- [PEP8](http://pep8online.com/) - Python script - `app.py`-
  was run through PEP8 online for PEP8 requirements.

  Results: `All Right` (Adheres to PEP requirements)

### Markdownlint

- [Markdownlint](https://github.com/Bealby/markdownlint) -
   Markdownlint was used to validate README.md and TESTING.md
   file.

   Results: 'Validation Successful'

### Validate JavaScript

- [Validate JavaScript](https://validatejavascript.com/) -
  JavaScript files were uploaded in the Validate JavaScript.
  Overall there were no errors that needed to be changed and
  the JavaScript passed general standards.

### Terminal

- **Terminal** - `python3 -m flake8` was typed in command
  line to highlight any issues within the entire project.
  Majority of issues were fixed, aside from:
  - **Migration** file issues
  - **Imports** that were unused in empty files, or
   where it was necessary to include them for production
  - **Lines** that were too long that could not be shortened.

#### Lighthouse Audit

- [Lighthouse Audit](https://developers.google.com/web/tools/lighthouse/) -
  A feature in Chrome Developing Tools - Lighthouse Audit -
  was carried out on Mobile and Desktop to assess
  **Performance**, **Accessibility**, **Best Practices**,
  **CEO** and **Progressive Web App**.

  Overall the results were satisfactory with no critical issues
  that needed to be addressed.

- **Mobile:** An overall average of 85% was received.
- **Desktop:** An overall average of 80% was received.

  The Lighthouse Audit also analysed the Progressive Web App,
  which validates the aspects of a Progressive Web App.
  The results were satisfactory.

### Chrome Developer Tools

- [Chrome DevTools - Console](https://developers.google.com/web/tools/chrome-devtools/)
  Throughout the Website building process, console errors were
  continually assessed and fixed accordingly. The deployed
  Website should have no concole errors.

### Unit Tests

- [Unit Tests](https://docs.djangoproject.com/en/dev/internals/contributing/writing-code/unit-tests/)
  Django comes with a test suite of `Unit Tests` that all
  use the testing infrastructure that ships with Django for
  testing applications.

  A variety of standard unit tests were carried out for
  `test_forms.py` and `test_views.py`. However a more
  expansive test program would be more beneficial, which
  would include tests on `models.py`, if resource
  time would allow it.

[Go to top](#contents)

## Non-Automated Testing

### Main Header

(Registered & Non Registered Users)

- Ensure that when clicking on the 'Logo' you are returned
  to the `Home` page.
- Navigate through Website rigorously, ensuring the 'Logo',
  when clicked, takes you back to the `Home` page.
- Ensure 'Repair' icon, when clicked, requires you to
  'Register' if not already signed in.
- Ensure 'Repair' icon, when clicked, takes you to the
 `Services` page when you are a registered user.
- Ensure 'Profile' icon, when clicked, has a dropdown menu
  of options to `Register` or `Signin`.
- Ensure 'Repair' icon, when clicked, takes you to the
  `Register` or `Signin` page.
- Ensure 'Basket' icon, when clicked, takes you to the
  `Basket` page.
- Ensure number under 'Basket' icon, is `0` and colour
  orange `rgb(220, 149, 35, 1)`.
- Ensure number under 'Basket' icon, accumulates the total
  each time a 'Product' is added to the basketand, and
  displays number accordingly.
- When the search icon is clicked with an empty field entry,
  the user is redirected to the `Products` page along with
  an error toast message.
- Ensure search function works with searches made in
  'Product' details and 'Product' description.
- Test various product category searches.
- Ensure that when a product search is not found a
  message for the user is displayed on page.
- Ensure all three icons turn from orange
  (`rgb(220, 149, 35, 1)`) to
  `(rgb(220, 149, 35, 0.6)` when hovered over.
- All above tests should be carried on mobile devices.

#### Main Header Layout

- Ensure main header, for desktop devices, has the
  'Logo' far left; 'Search Bar' center; and icons
  for 'Repair', 'Profile' and 'Basket', positioned
  far right respectively.
- Ensure for smaller devices 'Logo' decreases in
  size; 'Search Bar' is removed; and that all
  respective icons decrease in size.

[Go to top](#contents)

### Navigation Bar

(Registered & Non Registered Users)

- `All Products`, `Pocket Watches`, `Parts`, `Tools`
  and `Services` links should be displayed in Navigation
  Bar.
- Ensure headers in navigation bar have font
  `Berkshire Swash`.
- The Navigation bar should be centered in Medium and
  large devices.
- All Navigation links should, when hovered over,
  turn orange (`rgb(220, 149, 35, 1)`).
- Each link when clicked should display a dropdown menu
  of relevant items assigned to `Pocket Watches`, `Parts`,
  `Tools` and `Services` respectively. Except for
  `All Products`, which stands alone and displays
  all products when clicked.
- Ensure items in dropdown menu have font `Roboto`.
- Click through each dropdown menu item and ensure
  correct page loads up when item is clicked.
- For mobile devices ensure similar tests above are
  carried out.

#### Navigation Bar Layout

- As the screen decreases to a medium size, ensure
  link fonts decrease in size.
- For mobile screen sizes, ensure Navigation links
  collapse to a toggle menu hamburger icon that is
  positioned to the far left.
- For mobile screen sizes ensure search bar drops
  down to Navigation Bar, positioned to the right
  of the toggle hamburger menu.

[Go to top](#contents)

### Home Page

(Registered & Non Registered Users)

- Main title `Grandpa's Pocket Watch Shop` should
  be font `Berkshire Swash` and centered.
- Ensure orange horizontal divider is shown underneath
  main header
- Sub heading `Choose a Category` should be font
  `Roboto` and centered.
- Ensure there are 4 images with icon/ text links
  underneath for `Watches`, `Parts`, `Tools`, and
  `Services`.
- Ensure all images can be hovered/ clicked and
  naviagte to relevant page.
- Ensure all images fade in opacity when hovered
  over.
- Ensure all icon/ text links can be hovered/ clicked
  and navigate to correct page.
- Ensure all icon/ text links increase in size when
  hovered over.
- Ensure for each icon text link that a `Font Awesome`
  icon is positioned to the right.
- For mobile devices ensure similar tests above are
  carried out.

#### Home Layout

- For large screen sizes there should be 4 images
  along with their icon text links underneath on the
  same row in 4 columns.
- For medium screen sizes there should be 2 images
  along with their icon text links underneath, in a 2
  row, 2 column layout.
- For small screen sizes there should be no images
  just icon text links.
- For small screen sizes there should be a
  1 column layout for all icon text links.
- For smaller devices the main title
  `Grandpa's Pocket Watch Shop` should decrease in
  font size and remain centered.

[Go to top](#contents)

### Products App

(Registered & Non Registered Users)

#### Product Page

- Main title `Products` should be font
  `Berkshire Swash` and centred.
- Descriptive text should be font `Roboto`.
- Ensure orange horizontal divider is shown
  underneath main header.
- Ensure product images are consistent in size.
- Ensure underneath all product images there
  is `Name`, `Price`, `Sku` headings with relevant
  content in a lighter shade of grey.
- Ensure for each product card there is a `Read More`
  next to `Sku` number and a `Add to Basket` button
  that stretches width of product underneath.
- Ensure that the image, when hovered over, changes
  in opacity and when clicked directs you to the
  `Product Details` page.
- Ensure that the `Read More` link, when hovered over,
  changes in opacity and when clicked naviagtes you
  to the `Product Details` page.
- Ensure that the `Add to Basket` button, when clicked
  changes in opacity and adds product to the `Basket`.
- Ensure number changes in `Basket` to account for
  new product.
- Ensure pop up window is displayed when a product is
  added to the `Basket`.
- Ensure that if a product is already in the `Basket`,
  that if a user tries to add the product again, a pop
  up window will inform user that the product is already
  in the `Basket`.
- Ensure when product is added to the `Basket` the user
  is redirected back to the current page.
- Ensure products are always centered, whether there is
  4, 3, 2 or 1 column of products.
- For categories, `Pocket Watches`, `Parts` and `Tools`,
  ensure that `Badges` are displayed that inform user of
  products in selected category.
- For mobile devices ensure similar tests above are carried
  out.

#### Products Layout

- For larger devices image cards should have a 1 row,
  4 column layout.
- As screen devices decrease in size product cards should
  display a 1 row, 3 column layout; 1 row, 2 column layout;
  and lastly 1 row, 1 column layout
  for mobile.

#### Product Detail Page

- Main title `Products Details` should be font
  `Berkshire Swash` and centered.
- Ensure orange horizontal divider is shown underneath
  main header.
- Ensure when product is added to the `Basket` the user
  is redirected to current page.
- Descriptive text should be font `Roboto`.
- Ensure that there is a `Keep Shopping` link and an
  `Add to Basket` button shown under product description.
- Ensure that the `Keep shopping` link, when hovered over,
  changes in opacity and when clicked directs you to the
  `All Products` page.
- Ensure that the `Add to Basket` button, when clicked
  changes in opacity and adds product to the `Basket`.
- Ensure pop up window is displayed when a product is
  added to the basket.
- Ensure that if a product is already in the `Basket`,
  that if a user tries to add the product again, a pop
  up window will inform the user that the product is
  already in `Basket`.
- For mobile devices ensure similar tests above are
  carried out.

#### Product Degtail Layout

- For larger devices there should be a 1 row, 2 column
  layout, of firstly an image and secondly text.
- For mobile devices there should be a 1 column layout.
  Image and then text respectively.

[Go to top](#contents)

### Basket App

(Register & Non Registered Users)

- Main title `Shopping Basket` should be font
  `Berkshire Swash` and centered.
- Ensure orange horizontal divider is shown underneath
  main header.
- Descriptive text should be font `Roboto`.
- For Desktop there should be a 1 row, 2 column
  structure. First column a table that lists all items
  in basket, and in the second column a basket total
  summary.
- The first column should have table headers of
  `Product Name` and `Item Price`.
- Ensure product image is clickable and directs you to
  the `Product Details` page
- Under the table headers each item in the basket should
  show an image, product name and sku number.
- Font should be of a light grey colour.
- Next to each table line item there should be a delete
  icon. Which should be black in colour and when hovered
  over turn red.
- If delete icon is clicked the item from the basket
  should be removed and a pop up message confirming
  removal should appear.
- Ensure that when the basket is empty a page displays
  a message 'Your basket is empty' and a 'Keep Shopping'
  link.
- In the second column there should be a summary of
  costs, of `Item(s) Total`, `Delivery` and `Grand Total`.
- Each summary header should show relevant costs and be
  adjusted when items are deleted from the basket.
- Delivery charge should always be 10% of item(s) total.
- Ensure that there is a `Checkout` link and `Keep Shopping`
  link underneath the summary of costs.
- Ensure that the `Checkout` button has white text over a
  black background.
- Ensure that the `Checkout` button, when clicked changes
  in opacity and navigates user to `Checkout` page.
- Ensure that the `Keep shopping` link, when hovered over,
  changes in opacity and when clicked naviagtyes user to
  the `All Products` page.
- Flood the `Basket` with products and ensure product items
  and their totals are correct and look clean as a list on
  page.
- For mobile devices ensure similar tests above are carried
  out.

#### Basket Layout

- For smaller devices there should be a 1 column layout
  with basket list of items first and basket total summary
  second.

[Go to top](#contents)

### Checkout App

(Registered & Non Registered Users)

- Main title `Checkout` should be font
  `Berkshire Swash` and centered.
- Ensure orange horizontal divider is shown underneath
  main header.
- Descriptive text should be font `Roboto`.
- `Order Summary` header should display in bold and show
  number of items in order.
- Add and remove items from basket and ensure item count
  is correct
- Ensure table headers `Product Name` and `Item Price`
  are visible and bold.
- Ensure that under the headers there is a product image,
  name, sku number and price.
- Ensure image/ details are correct for product image,
  name, sku number and price.
- Flood the order with items and ensure layout remains
  cohesive and that details are correct for each item.
- For `Order Grand Total` details ensure
  `ITEM(S) TOTAL`, `DELIVERY`, `GRAND TOTAL` are bold
  and underneath each other respectively.
- Ensure `ITEM(S) TOTAL`, `DELIVERY`, `GRAND TOTAL`
  costs are correct and change as items are deleted or
  added to the `Basket`.
- Underneath the Payment Form ensure there is a
  `Complete Payment` link with white font against a black
  background.
- Underneath the `Complete Payment` link ensure there
  is a link to `Adjust Basket`, that is underlined
  with back font, and that when hovered over changes
  opacity.
- For mobile devices ensure similar tests above are
  carried out.

#### Payment Details Form

- Ensure form is split by `Details`, `Delivery`
  and `Payment`.
- Ensure `Details` form fields have correct placeholder
  text.
- Ensure `Delivery` form fields have correct placeholder
  text.
- Ensure `Payment` form field have correct placeholder
  text.
- Ensure each required field displays an error message
  when not filled in
- Complete form details, and each time leave a required
  filled empty and try and `Complete Payment`. Error
  messages should be displayed accordingly, informing
  user which field is missing or incorrect.
- Ensure `Email` cannot be filled out without correct `@`
  sign and `.com`.
- Type incorrect payment details and ensure red error
  message appears
- Fill in all fields correctly and process payment using
  card number `4242 4242 4242 4242 4242 4242 424`.
- Ensure there is a `Spinning Wheel` over a green
  background when payment is being processed.
- Once payment is processed ensure user is redirected
  to a confirmation success page
- Confirmation success page should display the order
  details.
- Ensure email is sent to user with correct order detail
  information.
- Ensure that when unrequired fields are not inputted in
  form they do not display in order summary success
  page.
- Ensure on the payments success page, when clicking
  back page, an error message appears stating there is
  nothing in user's basket
- Ensure there is an icon for `BACK TO GRANDPA'S SHOP`
  under order confirmation, that has white font on an
  orange background, that when hovered changes opacity.
- For mobile devices ensure similar tests above are
  carried out.

#### Stripe/ Webhooks/ Signals

- When order is confirmed ensure pop up window
  appears displaying order number information.
- When clicking `Complete Payment`, during load
  spinning, press the back button. Order should
  still get placed.
- When clicking `Complete Payment`, during load
  spinning, close page. Order should still get placed.
- For each `Complete Payment` access Stripe and it's
  Webhook events and ensure all payment Intents are
  successful.
- For mobile devices ensure similar tests above are
  carried out.

#### Checkout Layout

- Ensure Checkout App has a 1 row, 2 column layout
  that decreases to 1 column on mobile devices, with
  `Order Summary` details first, then `Order Grand Total`
  and `Payment Details`
- Ensure confirmation success order details have a
  table of contents with field headers on the left
  and details on the right forr larger devices. Order
  dtetails are tabulated in 1 column for mobile devices.
- Ensure order number condenses to a scrolling feature
  for mobile devices.
- For mobile devices ensure similar tests above are carried
  out.

[Go to top](#contents)

### Profile App

(Registered Users)

- Main title `Profile` should be font
  `Berkshire Swash` and centered.
- Ensure orange horizontal divider is shown
  underneath main header.
- Descriptive text should be font `Roboto`.
- `Default Delivery Information` should include
  profile field information.
- Under `Default Delivery Infomraiton` fields,
  there should be an `Update Information` and
  `Keep Shopping` link.
- `Update Information` link should be of white font
  over a black background, which when hovered over
  changes opacity
- `Keep Shopping` link should be of black font and
  underlined, which when hovered over changes opacity
- `Order Summary` information should contain headers
  `Order`, `Date`, `Items` and `Total`.
- Under each heading there should be correct 'Order'
  information.
- Order number under `Order` heading should be
  contracted to 6 characters.
- Order number should be clickable and open up the
  order confirmation detail on a separate page.
- When order number is clicked a pop up information
  window should appear with a message stating it is a
  past order.
- Ensure past order details are correct.
- At the bottom of the past order confirmation there
  should be an link `BACK TO MY PROFILE`, that is orange
  in colour with white font, and when hovered over
  changes opacity.
- `Appointments` information should contain headers
  `Appointment`, `Model`, `Type`, `Date` and `Time`.
- There also should be 2 icons for 'Edit' and Delete'
- Under each heading there should be correct 'Appointment'
  information.
- The 'Delete' icon when hovered over should turn red
- When the 'Delete' icon is clicked the appointment
  should be removed.
- A message confirming deletion of appointment should
  appear.
- When the 'Edit' icon is hovered over it should change
  opacity
- When the 'Edit' icon is clicked a new page should
  open with prefilled information from previous booked
  appointment.
- At bottom of appointment form there should be a
  `UPDATE APPOINTMENT`link with white font against
  an orange background.
- Edit details in appointment form and click
  `UPDATE APPOINTMENT`. A confirmation page should open
  up with confirmation of updated appointment.
- Ensure message pops up with confirmation of updated
  appointment.
- Ensure email with updated appointment information is
  sent with correct updated appointment details.
- In `My Profile` ensure appointment is visible and check
  to see if updated details are correct.
- Flood the `My Profile` page with orders and
  appointments and ensure the max height is instigated
  displaying both `Order` and `Appointment` details
  even on page at level with delivery information.
- For mobile devices ensure similar tests above are carried
  out.

#### Default Delivery Information Form

- Ensure all fields have correct placeholder
  information.
- Ensure each required field displays an error message
  when not filled in.
- Complete form details, and each time leave a
  required filled empty and try and `UPDATE INFORMATION`.
  An error messages should be displayed each time,
  informing user the field which is missing information.
- Fill in all fields correctly and `UPDATE INFORMATION`.
- Ensure profile form details saved are used as default
  information for payment details.
- Ensure profile form details saved are used as default
  information for name and email for `Contact` and
  `Services` form.
- Changes profile information and
  ensure changes are updated accodingly in forms for
  `Checkout`, `Contact` and `Services`.
- For mobile devices ensure similar tests above are
  carried out.

#### Edit Appointment Form

- Please repeat same steps for tests carried out for
  the - [Book an Appointment Form](#services) for
  Services

#### Profile Layout

- The `Profile` page should be split into 2 columns.
  The first column should have the
  `Default Delivery Information` and the second column
  including the `Order History` and `Appointments`
  details.
- For Mobile devices there should only be 1 column
  with  `Default Delivery Information` first,
  then `Order History` and `Appointments`.
- For mobile devices the `Order History` should only
  include the headers `Order Number` and `Total`.
- For mobile devices the `Order History` should only
  include the headers `Date` and `Time`, as well as
  the 'Edit' and `Delete' icons

[Go to top](#contents)

### Services App

(Registered Users)

- Main title `Visit our Shop` should be font in
 `Berkshire Swash` and centered.
- Ensure orange horizontal divider is shown underneath
  main header.
- Descriptive text should be font `Roboto`.
- Ensure header `For a Repair or Valuation!` is
  centered with font `Berkshire Swash`.
- Under header there should be 2 columns with 2 icons
  for `Repair` and `Valuation`.
- Under each icons ensure details of services for each
  is correct
- Ensure image is directly underneath and responsive
- Underneath image ensure `Book an Appointment` header
  has a flashing orange double chevron pointing to the
  right towards the Service Appointment form.
- Ensure Appointment Form includes all correct fields
  and has a `CONFIRM APPOINTMENT` link with a small
  'tick' box icon.
- Ensure `CONFIRM APPOINTMENT` link has white font
  with orange background and when hovered over changes
  opacity.
- For mobile devices ensure similar tests above are
  carried out.

#### Book an Appointment Form

- Ensure the `Name` and `Email` fields are prefilled
  with registered users details.
- Ensure dropdown options for `Appointment Type`,
  `Watch Model`, `Watch Type` and `Time` are correct
  and show all options.
- Ensure Date field displays current date only.
- For `Date` field ensure users cannot type a date
  manually.
- For `Date` field ensure users cannot select a date
  within 5 days of current date in calendar.
- Ensure calendar month can be selected.
- Ensure user cannot fix a date less than 3 days away.
- Ensure user can fix a date in next month.
- Ensure user can fox a date in future year
- Ensure calendar year can be selected.
- Ensure all field are mandatory.
- Test required fields by leaving blank while other
  fields are inputted and try to confirm appointment.
- Ensure error messages appear for user when fields
  are missing or not filled in correctly.
- Ensure `Email` cannot be filled out without correct
  `@` sign and `.com`.
- Fill all fields of form and click confirm
  appointment, and ensure new page is opened up to
  confirm appointment is booked.
- Ensure pop up window displays message appointment
  is booked.
- Ensure email is sent to user with correct appointment
  booking details.
- Ensure `BACK TO GRANDPA's SHOP` link is displayed
  under confirmation success page.
- Ensure `BACK TO GRANDPA's SHOP` link has white font
  against a black background and when hovered over
  changes opacity.
- Ensure `BACK TO GRANDPA's SHOP` directs user back to
  `Home`
- For mobile devices ensure similar tests above are
  carried out.

#### Services Layout

- The `Services` page should have a 2 column structure
  for desktop and a 1 column structure for mobile.
- For Desktop the first column should display the detail
  for the appointment and the second column the
  appointment form.
- For mobile screen sizes the appointment details
  will be displayed first and then the appointment
  form.
- Underneath the image ensure `Book an Appointment`
  header has a flashing orange double chevron pointing
  downwards towards the appointment form.
- Ensure main title `Visit our Shop` reduces in size for
  smaller devices.

[Go to top](#contents)

### Contact App

(Registered & Non Registered Users)

- Main title `Contact` should be font
  `Berkshire Swash` and centered.
- Ensure orange horizontal divider is shown underneath
  main header.
- Descriptive text should be font `Roboto`.
- Ensure address details are correct.
- Ensure logo is displayed with address details
  underneath.
- Ensure icons are shown for phone number and email.
- Ensure Google Map is rendered on page
- Ensure Google Map has a marker displayed of correct
  location.
- Ensure Google Map marker, upon click, opens up info
  window.
- Ensure info window displays logo and correct opening
  times.
- Ensure Contact form renders on page.
- Ensure contact form has the header `GET IN TOUCH`
  along with icon.
- Ensure contact form has three fields with correct
  placeholder names.
- Ensure `SEND´ link is displayed at bottom of form
  with icon.
- Ensure send icon has white font over an orange
  background and when hovered over changes opacity.
- For mobile devices ensure similar tests above are
  carried out.

#### Contact Form

- Ensure the `Name` and `Email` fields are prefilled
  with registered users details.
- Test required fields by leaving blank while other
  fields are inputted and try to send.
- Ensure `Email` cannot be filled out without correct
  `@` sign and `.com`.
- Ensure error messages appear for user when fields
  are missing or not filled in correctly.
- Fill in contact form and click send. Users should
  then be redirected to a confirmation email page.
- Ensure pop-up windows appears with message confirming
  email sent.
- Check that email has been sent.
- Ensure `Keep Shopping` link is displayed under
  confirmation success page.
- Ensure `Keep Shopping` link has black font and is
  underlined, and when hovered over changes opacity.
- Ensure `Keep Shopping` navigates user back to
  `Product` page
- For mobile devices ensure similar tests above are
  carried out.

#### Contact Layout

- The `Contact` page should have a 2 column structure
  for desktop and a 1 column structure for mobile.
- For Desktop the first column should display address
  and map content and then the second column the contact
  form.
- For mobile the address and map will be displayed first
  and then ther contact form

[Go to top](#contents)

### About App

(Registered & Non Registered Users)

- Main title `About` should be font
  `Berkshire Swash` and centered.
- Ensure orange horizontal divider is shown underneath
  main header.
- Descriptive text should be font `Roboto`.
- Ensure image is centered on page.
- Ensure content is centered on page.
- For smaller screen sizes text should be justified.

[Go to top](#contents)

### Footer

(Registered & Non Registered Users)

- Ensure `Basket` icon, `About Us`, `Contact` links are
  displayed on the left in `Footer`.
- Ensure `Copyright` is displayed on right in `Footer`
- Ensure `Footer` background colour is
  `rgb(186, 220, 192, 1)`.
- Ensure `Basket` icon, `About Us`, `Contact`, when
  clicked navigate the user to the correct page.
- Ensure links change from black to Orange
  (`rgb(220, 149, 35, 0.6)`) when hovered over.
- Ensure on mobile screen sizes `Basket` icon,
  `About Us`, `Contact` are centred in one row.
  While `Copyright` text is centered in row underneath.
- For mobile devices ensure similar tests above are
  carried out.

[Go to top](#contents)

### Allauth

(User Authentication)

- Ensure that the standard format for authentication
  pages have a main header font `Berkshire Swash` that
  centered.
- Ensure that the standard format for authentication
  pages have an orange horizontal divider underneath
  main header.
- Descriptive text should be font `Roboto`.
- Ensure that 'Primary' links have white text
  with black background, that when hovered over change
  opacity.
- Ensure that ´secondary` links have black text and
  are underlined and when hovered over change opacity.
- Text should be centered on all screen sizes.
- Users while logged in on Website can click profile
  to `Signout` and be redirected to `Sign Out` page.
- Ensure when user clicks `Sign Out` that users are
  navigated back to `Home` page and a pop up message
  confirms user has signed out.
- Ensure registered users can sign in with correct
  details and that pop up window confirms the user is
  signed in.
- Ensure that registered users are notifiedd
  when their username and password is incorrect.
- Type incorrect user name but correct password. User
  should be informed with an error message.
- Type incorrect password but correct user name. User
  should be informed with an error message.
- Check `Forgot Password` functionality and ensure new
  password is sent to email and can be received and
  confirmed by user.
- Type a password already used when asked to input new
  password. Error message with guiding info should appear.
- Ensure that new user can register in `Sign Up` form.
- As a potential new user type inconsistent email address.
  Error message with guiding info should appear.
- Type in a user name that already exists. Error message
  with guiding info should appear.
- Type a short and easy password. Error message
  with guiding info should appear.
- Type a password already used.
- As a potential new user type inconsistent passwords.
  Error message with guiding info should appear.
- For mobile devices ensure similar tests above are
  carried out.

[Go to top](#contents)

### Toasts

- Ensure all toast message info windows correctly
  appear for all signals, throughout Website
  navigation.
- Ensure pop-up window is viewable for only a
  `data-delay=10000`.
- Ensure Toast window can be manually closed.

### Desktop Browsers

- Chrome: Website renders well on all screen sizes.
- Safari: Website renders well on all screen sizes.
- Firefox: Website renders well on all screen sizes.
- Edge: Website renders well on all screen sizes.

### Mobile and Tablet Devices

- The Website was tested in
  [Chrome Developer Tools](https://www.google.com/chrome/dev/Google)
  which allowed the Website to be viewed on desktop,
  ipad and mobile devices. The results were
  satisfactory for all devices and continued to achieve
  the UX and UI goals.

### User Testing

- Family and friends were asked to use the finished
  Website to test usability and comment on whether
  they felt it met their needs as discussed in
  [Agile User Stories](https://github.com/Bealby/grandpas-pocket-watch-shop/blob/master/documentation/readme/user-stories.pdf)

  User testing was also invaluavle in challenging
  the definsive design of the Website and
  the authetication aspect.

  Devices used by users in the User Testing:

- iphone 8 - Chrome: Good
- iphone xs - Chrome: Good
- iphone xs - Safari: Good
- iphone 8 - Chrome: Good
- iphone 8 - Safari: Good
- iphone 8 - Chrome: Good
- iphone 11 - Safari: Good
- iphone 11 - Safari: Good
- Samsung 7 - Chrome: Good

### Agile User Stories

[Agile User Stories](https://github.com/Bealby/grandpas-pocket-watch-shop/blob/master/documentation/readme/user-stories.pdf)

[Go to top](#contents)

## Fixes

- For Web pages with `Crispy-Forms` it was found that when loading
  the Web page on mobile devices the page load to the section of
  the Crispy Form rather than top of the page.

  To fix this the onload command, `<body onLoad="window.scroll(0, 0)">`,
  was used in the `Body` of base.html to ensure all pages loading to
  section at top of page.

- It was important to have a `Date Picker` for the services form so
  that a user can pick a date and time with a calendar that is formatted
  with specific date options.

  Calibrating a `Date Picker` with good UI and UX became an issue with
  UI of the Date Picker being very un user friendly with the time aspect
  needing to be chosen as well as the date.

  It was therefore decided to create a separate model for 'Time'
  with the two options of 09:00 and 12:00. Allowing for a better
  user experience for the user when picking a date.

- While committing changes there was an error which caused the env.py
  with Stripe and Google Map secret keys being exposed in the commits
  in GitHub.

  Due to this all secret keys were updated and the old secret keys
  being made rendundant.env.py file.

## Not Fixed

[Go to top](#contents)