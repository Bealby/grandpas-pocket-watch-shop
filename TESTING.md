# Testing

---

## Automated Testing

[W3C](https://validator.w3.org/) - All HTML files with their data were directly
    input into the Mark-Up Validation Service.
    The results: All HTML code adheres to validation requirements. Errors for
    Python only.

[WSC](https://jigsaw.w3.org/css-validator/) - CSS data was directly input into
    the CSS Validation Service. The results: `Congratulations! No Error Found.`

[PEP8](http://pep8online.com/) - Python script - `app.py`- was run through PEP8 online
    for PEP8 requirements. Results: `All Right` (Adheres to PEP requirements)

[Markdownlint](https://github.com/Bealby/markdownlint) - Markdownlint was
used to validate README.md file. 'Validation successful'

[Validate JavaScript](https://validatejavascript.com/) - JavaScript
files were uploaded in in the Validate JavaScript. Overall there
were no errors that needed to be changed and the JavaScript passed
general standards.

**Terminal** - `python3 -m flake8` in command line was used to highlight any
issues within entire project. Majority of issues were fixed, except:

- **Migration** issues
- **Imports** unused in empty files or where it was necessary to include
- **Lines** too long where it was not suitable to shorten

[Lighthouse Audit](https://developers.google.com/web/tools/lighthouse/) -
A feature in Chrome Developing Tools - Lighthouse Audit - was carried out
on Mobile and Desktop to assess **Performance**, **Accessibility**,
**Best Practices**, **CEO** and **Progressive Web App**. 

Overall the results were satisfactory with no critical issue that needed to
be addressed.

- **Mobile:** An overall average of 85% was received.
- **Desktop:** An overall average of 79% was received.

The Lighthouse Audit also analysed the Progressive Web App, which validates
the aspects of a Progressive Web App. The results were satisfactory.

[Chrome DevTools - Console](https://developers.google.com/web/tools/chrome-devtools/)
Throughout the Website building process console errors were continually assessed
and fixed accordingly. Currently there are no errors when navigating through the Website.

[Unit Tests](https://docs.djangoproject.com/en/dev/internals/contributing/writing-code/unit-tests/)
Django comes with a test suite of `Unit Tests` that all use the
testing infrastructure that ships with Django for testing applications.

A variety of standard unit tests were carried for test_forms.py
and test_views.py. However a more expansive test program, which
would include tests on models, would be beneficial and should be
carried out if more resource time was available.  

## Non-Automated Testing

### Main Header

#### Register & Non Registered Users

- Ensure that clicking on the 'Logo' you are returned to the
  `Home` page.
- Navigate through Website rigorously, ensuring 'Logo', when clicked,
  takes you back to the `Home` page.
- Ensure 'Repair' icon, when clicked, requires you to 'Register' if not
  already.
- Ensure 'Repair' icon, when clicked, takes you to the `Services` page
  when you are registered.
- Ensure 'Profile' icon, when clicked, dropdown a menu to 'Register'
  or 'Sign' in.
- Ensure 'Repair' icon, when clicked, takes you to the 'Register' or
  'Login' page.
- Ensure 'Basket' icon, when clicked, takes you to the 'Basket' page.
- Ensure number under 'Basket' icon, is `0` and colour `rgb(220, 149, 35, 1)`.
- Ensure number under 'Basket' icon, accumulates the total each time a
  'Product' is added and displays number accordingly.
- When search icon is click with empty field user is redirected to `Products`
  page and error message is displayed.
- Ensure search function work with searches made in 'Product' details
  and 'Product' description 
- Test various product category searches.
- Ensure all three icons turn from orange (`rgb(220, 149, 35, 1)`) to
  `rgb(220, 149, 35, 0.6)` when hover over.
- All above tests should be carried on mobile devices with same results.

**Layout**

- Ensure main header, for desktop devices, has the 'Logo' far left;
  'Search Bar' center; and icons for 'Repair', 'Profile' and 'Basket',
  positioned far right respectively.
- Ensure for smaller devices 'Logo' decreases in size; 'Search Bar'
  is removed; and that all respective icons decrease in size.

### Navigation Bar

#### Register & Non Registered Users

- `All Products`, `Pocket Watches`, `Parts`, `Tools` and
  `Services` links should be displayed in Navigation Bar.
- Ensure headers in navigation bar have font `Berkshire Swash`.
- The Navigation bar should be centered in Medium and higher
  devices.
- All Navigation links should, when hovered over, turn orange 
  (`rgb(220, 149, 35, 1)`).
- Each link when clicked should display a dropdown menu of relevant
  items assigned to `Pocket Watches`, `Parts`, `Tools` and
  `Services` respectively. Except for `All Products` which
  stands alone and display all products when clicked.
- Ensure items in dropdown menu have font `Roboto`.
- Click through each dropdown menu item and ensure correct page loads
  up when item is clicked.
- For mobile devices ensure similar tests above are carried
  out.

**Layout**

- As the screen decreases to a medium size, ensure link fonts
  decrease in size.
- For mobile screen sizes, ensure Navigation links collapse to a toggle
  menu hamburger icon that is positioned to the far left. 
- For mobile screen sizes ensure search bar drops down to Navigation Bar,
  positioned to the right of the toggle hamburger menu.

### Home (Index) Page

#### Register & Non Registered Users

- Main title `Grandpa's Pocket Watch Shop` should be font
  `Berkshire Swash` and centred.
- Ensure orange horizontal divider is shown underneath main header
- Sub heading `Choose a Category` should be font `Roboto`
  and centred.
- Ensure there are 4 images with icon/ text links underneath
  for `Watches`, `Parts`, `Tools`, and `Services`.
- Ensure all images can be hovered/ clicked and directed to relevant
  page.
- Ensure all images fade in opacity when hovered over.
- Ensure all icon/ text links can be hovered/ clicked and navigate
  to correct page.
  page.
- Ensure all icon/ text links increase in size when hovered over.
- Ensure for each icon text link that a `Font Awesome` icon is
  positioned to the right.
- For mobile devices ensure similar tests above are carried
  out.

**Layout**

- For large screen sizes there should be 4 images along with their
  icon text links underneath on the same row in 4 columns.
- For medium screen sizes there should be 2 images along with their
  icon text links underneath, in a 2 row, 2 column layout.
- For small screen sizes there should be no images just icon
  text links.
- For small screen sizes there should be a 1 row, 1 column layout
  for all icon text links.
- For smaller devices the main title `Grandpa's Pocket Watch Shop`
  should decrease in font size and remain centered.

### Products App

#### Register & Non Registered Users

**Product Page**

- Main title `Products` should be font
  `Berkshire Swash` and centred.
- Descriptive text should be font `Roboto`.
- Ensure orange horizontal divider is shown underneath main header
- Ensure product images are consistent in size
- Ensure underneath all product images there is `Name`, `Price`
  `Sku` headings with relevant content in a lighter shade of grey.
- Ensure for each product card there is a `Read More` next to `Sku`
  number and a `Add to Basket` button that stretches width of product
  underneath.
- Ensure that the image, when hovered over, changes in opacity and when 
  clicked directs you to ´Product Details` page.
- Ensure that the `Read More`, when hovered over, changes in opacity and when 
  clicked directs you to `Product Details` page.
- Ensure that the `Add to Basket` button, when clicked changes in opacity
  and adds product to the `Basket`.
- Ensure number changes in `Basket` to account for new product.
- Ensure pop up window is displayed when a product is added to the 
  basket.
- Ensure that if a product is already in the basket, that if a user tries
  to add the product again, a pop up window will inform user that product
  is already in basket. 
- Ensure when product is added to `Basket` the user is redirected to current
  page.
- Ensure products are always centred, whether there is 4, 3, 2 or 1 column
  of images. 
- For categories, `Pocket Watches`, `Parts` and `Tools` ensure that
  `Badges` are displayed that inform user of products in selected options.
- For mobile devices ensure similar tests above are carried
  out.

**Layout**

- For larger devices image cards should have a 1 row, 4 column layout.
- As screen devices decrease in size product cards should display 1 row,
  3 column layout; 1 row, 2 column layout; and lastly 1 row, 1 column layout
  for mobile.

**Product Detail Page**

- Main title `Products Details` should be font
  `Berkshire Swash` and centred.
- Ensure orange horizontal divider is shown underneath main header.
- Ensure when product is added to `Basket` the user is redirected to current
  page.
- Descriptive text should be font `Roboto`.
- Ensure that there is a `Keep Shopping` link and an `Add to Basket`
  button shown under product description.
- Ensure that the `Keep shopping` link, when hovered over, changes in opacity
  and when clicked directs you to `All Products` page.
- Ensure that the `Add to Basket` button, when clicked changes in opacity
  and adds product to the `Basket`.
- Ensure pop up window is displayed when a product is added to the 
  basket.
- Ensure that if a product is already in the basket, that if a user tries
  to add the product again, a pop up window will inform user that product
  is already in basket. 
- For mobile devices ensure similar tests above are carried
  out.

**Layout**
- For larger devices there should be a 1 row, 2 column layout, of firstly
  an image and secondly text.
- For mobile devices there should be a 1 row, 1 column layout. Image and then
  text respectively.

### Basket App

#### Register & Non Registered Users

- Main title `Shopping Basket` should be font
  `Berkshire Swash` and centred.
- Ensure orange horizontal divider is shown underneath main header.
- Descriptive text should be font `Roboto`.
- For Desktop there should be a 1 row, 2 column structure. First column
  a table that list all items in basket, and in the second column a basket
  total summary.
- The first column should have table headers of `Product Name` and
  `Item Price`.
- Ensure product image is clickable and directs you to product detail page
- Under the table headers each item in basket should show an image, 
  product name and sku number.
- Font should be of a light grey colour.
- Next to each table line item there should be a delete icon. Which should
  be black in colour and when hovered over turn red.
- If delete icon is clicked the item from the basket should be removed and
  a pop up message confirming removal should appear. 
- Ensure that when basket is empty a page only displays a message
  'Your basket is empty' and a 'Keep Shopping'.
- In the second column there should show a summary of costs, of `Item(s) Total`,
  `Delivery` and `Grand Total`.
- Each summary header should show relevant costs and be adjusted when
  items are deleted from the basket.
- Delivery charge should always be 10% of item(s) total.
- Ensure that there is a `Checkout` link and `Keep Shopping` link underneath
  the summary of costs.
- Ensure that the `Checkout` button has white text over a black background.
- Ensure that the `Checkout` button, when clicked changes in opacity
  directs user to `Checkout´ page.
- Ensure that the `Keep shopping` link, when hovered over, changes in opacity
  and when clicked directs you to `All Products` page.
- Flood the 'Basket` with products and ensure product items and their
  totals are correct and look clean as a list on page.
- For mobile devices ensure similar tests above are carried
  out.

**Layout**

- For smaller devices there should be a 1 row, 1 column layout with basket list
  of items first and basket total summary second.

### Checkout App (Stripe/ Webhooks/ Signals)

#### Register & Non Registered Users

- Main title `Checkout` should be font
  `Berkshire Swash` and centered.
- Ensure orange horizontal divider is shown underneath main header.
- Descriptive text should be font `Roboto`.
- `Order Summary` header should display in bold and show number of
  items in order.
- Add and remove items from basket and ensure item count is correct
- Ensure table headers `Product Name` and `Item Price` are visible
  bold.
- Ensure that under the headers there is a product image, name, sku
  number and price.
- Ensure details are correct for product image, name, sku
  number and price.
- Flood the order with items and ensure layout remains cohesive
  and that details are correct for each item.
- For `Order Grand Total` table details ensure `ITEM(S) TOTAL`,
  `DELIVERY`, `GRAND TOTAL` are bold and underneath each other
  respectively.
- Ensure `ITEM(S) TOTAL`, `DELIVERY`, `GRAND TOTAL` costs are correct and
  and change as items are deleted or added to `Basket`.
- Underneath the Payment Form ensure there is a `Complete Payment`
  with white font against a black background.
- Underneath the `Complete Payment` icon ensure there
  is a link to `Adjust Basket` that is underlined and with back font,
  with white font against a black background, that when hovered
  over changes opacity.
- For mobile devices ensure similar tests above are carried
  out.

**Payment Details Form**

- Ensure form is split by `Details`, `Delivery` and `Payment`.
- Ensure `Details` form fields have correct placeholder text.
- Ensure `Delivery` form fields have correct placeholder text.
- Ensure `Payment` form field have correct placeholder text.
- Ensure each required field display error message when not filled in
- Complete form details, and each time leave a required filled empty
  and try and `Complete Payment`. Error messages should be displayed
  each time informing user field which is missing. 
- Ensure `Email` cannot be filled out without correct `@` sign and
  `.com`.
- Type incorrect payment details and ensure red error message appears
- Fill in all fields correctly and process payment using card number
  `4242 4242 4242 4242 4242 4242 424` 
- Ensure there is a `Spinning Wheel` over a green background when
  payment is being processed. 
- Once payment is processed ensure user is redirected to a
  confirmation success page
- Confirmation success page should display the email order has been made to
  and all order details.
- Ensure email is sent to user with correct order detail information
- Ensure that when unrequired fields are not inputted in form they do not
  display in in order summary success page.
- On the payments success page when clicking back error message appears
  stating there is nothing in user's basket
- Ensure there is an icon for `BACK TO GRANDPA'S SHOP` under order
  confirmation, that has white font on an orange background, that when
  hovered changes opacity.
- For mobile devices ensure similar tests above are carried
  out.

**Stripe/ Webhooks/ Signal**

- When order is confirmed ensure pop up window is displayed displaying
  order number information.
- When clicking `Complete Payment`, during load spinning, press the back button.
  Order should still get placed.
- When clicking `Complete Payment`, during load spinning, close page.
  Order should still get placed.
- For each `Complete Payment` access Stripe and it's Webhook events and
  ensure all payment Intents are successful.
- For mobile devices ensure similar tests above are carried
  out.

**Layout**

- Ensure Checkout App has a 1 row, 2 column layout that
  decreases to 1 column on mobile devices, with
  `Order Summary` details first, the `Order Grand Total`
  and `Payment Details`
- Ensure confirmation success order details have a table of contents
  with field headers on the left and details on the right for larger devices
  that are tabulated in 1 column for mobile devices.
- Ensure order number condenses to a scrolling feature for mobile devices.
- For mobile devices ensure similar tests above are carried
  out.
 
### Profile

#### Register Users

- Main title `Profile` should be font
  `Berkshire Swash` and centered.
- Ensure orange horizontal divider is shown underneath main header.
- Descriptive text should be font `Roboto`.
- `Default Delivery Information` should include profile field information
- Under profile field information there should be a `Update Information`
  icon and a `Keep Shopping` link.
- `Update Information` icon should be of white font over a black background,
   which when hovered over changes opacity
- `Keep Shopping` link should be of black font and underlined,
   which when hovered over changes opacity
- `Order Summary` information should contain headers `Order`, `Date`, `Items`
   and `Total`.
-  Under each heading should be correct 'Order' information.
-  Order number under `Order` heading should be contracted to 6 characters.
- Order number should be clickable and open up the confirmation detail in 
a separate page
- When order number is clicked a pop up information window should appear
  with a message that this is a past order.
- ensure past order details are correct
- At the bottom of the past order confirmation there should be an icon
  `BACK TO MY PROFILE`, that is orange in colour and with white font, and
  when hovered over changes opacity.
- `Appointments` information should contain headers `Appointment`,
  `Model`, `Type`, `Date` and `Time`.
-  There also should be 2 icons for 'Edit' and Delete'
-  Under each heading should be correct 'Appointment' information.
- The 'Delete' icon when hovered over should turn red
- when the 'Delete' icon is clicked the appointment should be removed
- A message confirming delete of appointment should appear
- When the 'Edit' icon is hover over it should change in opacity
- when the 'Edit' icon is clicked a new page should open with prefilled
  information from previous booked appointment. 
- At bottom of appointment form there should be a `UPDATE APPOINTMENT``
  icon with white font against an orange background.
- Edit details in appointment form and click ÙPDATE APPOINTMENT'. A confirmation
  page should open up with confirmation of updated appointment
- Ensure message pops up with confirmation of updates appointment
- Ensure email with updated appointment information id received.
- In `My Profile´ Ensure appointment is visible and check to see if updated derails
  are correct.
- Flood the `My Profile` page with order and appointment and ensure max height kicks information
  and is display even on page at level with delivery information.
- For mobile devices ensure similar tests above are carried
  out.

**Default Delivery Information Form**

- Ensure all fields have correct placeholder information.
- Ensure each required field display error message when not filled in
- Complete form details, and each time leave a required filled empty
  and try and `UPDATE INFORMATIN`. An error messages should be displayed
  each time informing user the field which is missing information.
- Fill in all fields correctly and 'UPDATE INFORMATIN`
- Ensure profile form details saved are used as default information for
  Payment Details.
- Ensure profile form details saved are used as default information for
  name and email for `Contact` and `Services` form.
- Repeat different changes in Profile information and ensure changes are
  updated accodinkg6 in forms for `Checkout`, `Contact` and `Services` 
- For mobile devices ensure similar tests above are carried
  out.

**Edit Appointment Form**
- Please refer to test run in ´Services´ App test ...link???

**Layout**

- The `Profile` page should be split into 2 columns. The first column should
  have the `Default Delivery Information` and the second column including the
  `Order History` and `Appointments`.
- For Mobile devices there should only be 1 column in order of
  `Default Delivery Information`, `Order History` and `Appointments`.
- For mobile devices the `Order History` should only include the headers
  `Order Number` and `Total`
- For mobile devices the `Order History` should only include the headers
  `Date` and `Time`, as well as 'Edit' and `Delete' icons

### Services

#### Register Users

- Main title `Visit our Shop` should be font
  `Berkshire Swash` and centered.
- Ensure orange horizontal divider is shown underneath main header.
- Descriptive text should be font `Roboto`.
- Ensure header `For a Repair or Valuation!` is centered with
  font `Berkshire Swash`.
- Under header there should be 2 columns with 2 icons for
  `Repair` and `Valuation``
- Under each icons ensure details of services for each is correct
- Ensure image is directly underneath and responsive
- Underneath image ensure `Book an Appointment` header has a flashing
  orange double chevron pointing to the right of the Service appointment form
- ensure Appointment Form includes all correct fields and has a
  `CONFIRM APPOINTMENT` button with small 'tick 'box' icon.
- Ensure `CONFIRM APPOINTMENT` button has white font with orange
  background and when hovered over changes opacity.
- For mobile devices ensure similar tests above are carried
  out.

**Book an Appointment Form**

- Ensure the `Name` and `Email` fields are prefilled with
  registered users details.
- ensure dropdown options for `Appointment Type`, `Watch Model`
  `Watch Type` and `Time` are correct and show all options.
- Ensure Date field display current date only.
- For `Date` field ensure user cannot type a date manually. 
- For `Date` field ensure user cannot select a date within
  5 days of current date in Date Picker.
- Ensure Date picker month can be selected
- Ensure Date picker year can be selected.
- Ensure all field are mandatory
- Test required fields by leaving blank while other fields
  are inputted and try to confirm appointment.
- Ensure error messages appear for user when fields are missing
  or not filled in correctly.
- Fill all fields of form and click confirm appointment, and ensure
  new page is opened up to confirm appointment is booked.
- Ensure `Email` cannot be filled out without correct `@` sign and
  `.com`.
- Ensure pop up window displays message appointment is booked. 
- Ensure email is sent to user with correct appointment booking 
  details.
- Ensure `BACK TO GRANDPA's SHOP` icon is displayed under confirmation
  success page.
- Ensure `BACK TO GRANDPA's SHOP` icon has white font against a 
  black background and when hovered over changes opacity.
- Ensure `BACK TO GRANDPA's SHOP` directs user back to home
- For mobile devices ensure similar tests above are carried
  out.

**Layout**
- The `Services` page should have a 2 column structure for desktop
    and a 1 column structure for mobile.
- For Desktop the first column should display the detail for the appointment 
  and the second column the appointment form.
- For mobile the appointment details will be displayed first and then appointment
  form
- Underneath image ensure `Book an Appointment` header has a flashing
  orange double chevron pointing downwards towards Service appointment form
- Ensure main title `Visit our Shop` reduces in size for smaller devices

### Contact

#### Register & Non Registered Users

- Main title `Contact` should be font
  `Berkshire Swash` and centered.
- Ensure orange horizontal divider is shown underneath main header.
- Descriptive text should be font `Roboto`.
- Ensure address details are correct
- Ensure logo is displayed with address details Underneath
- Ensue icons are shown for phone number and email 
- Ensure Google Maps is rendered on page
- Ensure Google Maps has a marker displayed of correct location
- Ensure Google Maps marker, up click opens up info window
- Ensure info window displays logo and correct opening times.
- Ensure Contact form renders on page
- Ensure contact form has the header `GET IN TOUCH` along with
  icon. 
- Ensure contact form has three fields with correct placeholder
  names.
- Ensure `SEND´ icon is displayed at bottom of form with icon.
- Ensure send icon has white font over an orange background
  and when hovered over changed opacity.
- For mobile devices ensure similar tests above are carried
  out.
- For mobile devices ensure similar tests above are carried
  out.

**Contact Form**

- Ensure the `Name` and `Email` fields are prefilled with
  registered users details.
- Test required fields by leaving blank while other fields
  are inputted and try to send.
- Ensure `Email` cannot be filled out without correct `@` sign and
  `.com`.
- Ensure error messages appear for user when fields are missing
  or not filled in correctly.
- Fill in contact form and click send. Users should then be
  redirected to confirmation email page.
- Ensure pop-up windows appears with message confirming email section
- Check that email has been received
- Ensure `Keep Shopping` link is displayed under confirmation
  success page.
- Ensure `Keep Shopping` link has black font and is underlined,
  and when hovered over changes opacity.
- Ensure `Keep Shopping` directs user back to product page
- For mobile devices ensure similar tests above are carried
  out.

**Layout**

- The `Contact` page should have a 2 column structure for desktop
    and a 1 column structure for mobile.
- For Desktop the first column should display address and map content and then
  the second column the contact form.
- For mobile the address and map will be displayed first and then 
  contact form

### About

#### Register & Non Registered Users

- Main title `About` should be font
  `Berkshire Swash` and centered.
- Ensure orange horizontal divider is shown underneath main header.
- Descriptive text should be font `Roboto`.
- Ensure image is centred on page
- Ensure content is centred on page
- For smaller screen sizes text should be justified.

### Footer

#### Register & Non Registered Users

- Ensure `Basket` icon, `About Us`, `Contact` links are
  displayed on the left of `Footer`.
- Ensure `Copyright` is displayed right on `Footer``
- Ensure `Footer` background colour is `rgb(186, 220, 192, 1)`
- Ensure `Basket` icon, `About Us`, `Contact` upon hover
  and click navigate use to correct pages.
- Ensure links change from black to Orange `rgb(220, 149, 35, 0.6)``
  when hovered over.¨
- Ensure on mobile screen sizes `Basket` icon, `About Us`, `Contact`
  are centred in one row. While `Copyright` text is centred in
  row underneath
- For mobile devices ensure similar tests above are carried
  out.

### Allauth - (User Authentication)

- Ensure that the standard format for authentication pages
  have a main header font `Berkshire Swash` and centered.
- Ensure that the standard format for authentication pages
  have a orange horizontal divider underneath main header.
- Descriptive text should be font `Roboto`.
- Ensure that ´Primary` buttons are of white text with 
  black background, that when hovered over change opacity.
- Ensure that ´secondary` links are of black text and
  underlined and when hovered over change opacity.
- Text should be centered on all screen sizes.
- Users while logged in on Website can click profile to
  `Signout` and be redirected to `Sign Out` page .
- Ensure when user click `Sign Out´ that you are directed back
  `Home` page and a pop up message confirms you have signed out. 
- Ensure registered user can sign in with correct details
  and that pop up window confirms the user is signed in.
- Ensure that registered user, when typing is user details
  and password is notified if details are incorrect
- Type incorrect user name but correct password. User should be
  informed of error message
- Type incorrect password but correct user name. User should be
  informed of error message
- Check `Forgot Password` functionality and ensure new password is sent to 
  email and can be received and confirmed by user.
- Type a password already used when asked to input new password. Error message
  with guiding info should appear. 
- Ensure that new user can register in `Sign Up` form.
- As a potential new user type inconsistent email address. Error message
  with guiding info should appear. 
- Type in a user name that already exist. Error message
  with guiding info should appear. 
- Type a short and easy password. Error message
  with guiding info should appear. 
- Type a password already
- As a potential new user type inconsistent passwords. Error message
  with guiding info should appear. 
- For mobile devices ensure similar tests above are carried
  out.

### Toasts

- Ensure all toast message windows correctly appear for all error signals with correct message.
- Ensure window is viewable for only a data-delay=10000.
- Ensure Toast window can be manually closed.

### Desktop Browsers

- Chrome: Website renders well on all screen sizes.
- Safari: Website renders well on all screen sizes.
- Firefox: Website renders well on all screen sizes.
- Edge: Website renders well on all screen sizes.

### Mobile and Tablet Devices

- The Website was tested on 
  mobiles, . The results were
  satisfactory for all devices and continued to achieve the
  UX and UI goals. Chrome Developing tools

### User Testing

Helped test defensive design and allauth app

- Family and friends were asked to use the finished Website to test
  usability and comment on whether they felt it met their needs as
  discussed in the Strategy section 
  - iphone 8 - Chrome: Good
  - iphone xs - Chrome: Good
  - iphone xs - Safari: Good
  - iphone 8 - Chrome: Good
  - iphone 8 - Safari: Good
  - iphone 8 - Chrome: Good
  - iphone 11 - Safari: Good
  - iphone 11 - Safari: Good
  - Samsung 7 - Chrome: Good

### User Experience

[User Stories](#user-stories).

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


