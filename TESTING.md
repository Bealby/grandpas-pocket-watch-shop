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

[Validate Javascript](https://validatejavascript.com/) - Javascript
files were uploaded in in the Validate Javascript. Overall there
were no errors that needed to be changed and the javascript passed
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

Overall the results were satifactory with no critical issue that needed to
be addressed.

- **Mobile:** An overall average of 85% was received.
- **Desktop:** An overall average of 79% was received.

The Lighthouse Audit also analysed the Progressive Web App, which validates
the aspects of a Progressive Web App. The results were satisfactory.

[Chrome DevTools - Console](https://developers.google.com/web/tools/chrome-devtools/)
Throughout the Website buidling process console errors were continually assessed
and fixed accordingly. Currently there are no errors when navigating through the Website.

[Unit Tests](https://docs.djangoproject.com/en/dev/internals/contributing/writing-code/unit-tests/)
Django comes with a test suite of `Unit Tests` that all use the
testing infrastructure that ships with Django for testing applications.

A variaty of standard unit tests were carried for test_forms.py
and test_views.py. However a more expansive test program, which
would incude tests on models, would be beneficial and should be
carried out if more resource time was available.  

## Non-Automated Testing

### Main Header

- Ensure that clicking on the 'Logo' you are returned to the
  `Home` page.
- Navigate through Website rigorously, ensuring 'Logo', when clicked,
  takes you back to the `Home` page.
- Ensure 'Repair' icon, when clicked, requires you to 'Register' if not
  already.
- Ensure 'Repair' icon, when clicked, takes you to the `Services` page
  when you are registered.
- Ensure 'Profile' icon, when clicked, dropsdown a menu to 'Register'
  or 'Sign' in.
- Ensure 'Repair' icon, when clicked, takes you to the 'Register' or
  'Login' page.
- Ensure 'Basket' icon, when clicked, takes you to the 'Basket' page.
- Ensure number under 'Basket' icon, is `0` and color `rgb(220, 149, 35, 1)`.
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
  postioned far right respectively.
- Ensure for smaller devices 'Logo' decreases in size; 'Search Bar'
  is removed; and that all respective icons decrease in size.

### Navigation Bar

- `All Products`, `Pocket Watches`, `Parts`, `Tools` and
  `Services` links should be displayed in Navigation Bar.
- Ensure headers in naviagation bar have font `Bershire Swash`.
- The Navigation bar should be centered in Medium and higher
  devices.
- All Navigation links should, when hovered over, turn orange 
  (`rgb(220, 149, 35, 1)`).
- Each link when clicked should display a dropdown menu of relevant
  items assigned to `Pocket Watches`, `Parts`, `Tools` and
  `Services` respectively. Except for `All Products` which
  stands alone and display all products when clicked.
- Ensure items in dopdown menu have font `Roboto`.
- Click through each dropdown menu item and ensure correct page loads
  up when item is clicked.
- For mobile devices ensure simalar tests above are carried
  out.

**Layout**

- As the screen decreases to a medium size, ensure link fonts
  decrease in size.
- For mobile screen sizes, ensure Navigation links collapse to a toggle
  menu hamburger icon that is positioned to the far left. 
- For mobile screen sizes ensure search bar drops down to Navigation Bar,
  positioned to the right of the toggle hamburger menu.

### Home (Index) Page

- Main title `Grandpa's Pocket Watch Shop` should be font
  `Berkshire Swash` and centred.
- Ensure orange horiztonal divider is shown underneath main header
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
- Enusure for each icon text link that a `Font Awesome` icon is
  positioned to the right.
- For mobile devices ensure simalar tests above are carried
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

**Product Page**

- Main title `Products` should be font
  `Berkshire Swash` and centred.
- Descriptive text should be font `Roboto`.
- Ensure orange horiztonal divider is shown underneath main header
- Ensure product images are consistant in size
- Ensure underneath all product images there is `Name`, `Price`
  `Sku` headings with relevant content in a lighter shade of grey.
- Ensure for each product card there is a `Read More`next to `Sku`
  number and a `Add to Basket` button that stretches width of product
  underneath.
- Ensure that the image, when hovered over, changes in opacity and when 
  clicked directs you to ´Product Details` page.
- Ensure that the `Read More`, when hovered over, changes in opacity and when 
  clicked directs you to `Product Details` page.
- Ensure that the `Add to Basket` button, when clicked chnages in opacity
  and adds product to the `Basket`.
- Ensure number changes in `Basket`to account for new product.
- Enusure pop up window is displayed when a product is added to the 
  basket.
- Ensure that if a product is already in the basket, that if a user tries
  to add the product again, a pop up window will inform user that product
  is already in basket. 
- Ensure when product is added to `Basket` the user is redirected to current
  page.
- Ensure products are always centred, whether there is 4, 3, 2 or 1 column
  of images. 
- For categories, `Pocket Watches`, `Parts` and `Tools` ensure that
  `Badges`are displayed that inform user of products in selected options.
- For mobile devices ensure simalar tests above are carried
  out.

**Layout**

- For larger devices image cards should have a 1 row, 4 column layout.
- As screen devices decrease in size product cards should display 1 row,
  3 column layout; 1 row, 2 column layout; and lastly 1 row, 1 column layout
  for mobile.

**Product Detail Page**

- Main title `Products Details` should be font
  `Berkshire Swash` and centred.
- Ensure orange horiztonal divider is shown underneath main header.
- Ensure when product is added to `Basket` the user is redirected to current
  page.
- Descriptive text should be font `Roboto`.
- Ensure that there is a `Keep Shopping` link and an `Add to Basket`
  button shown under product description.
- Ensure that the `Keep shopping` link, when hovered over, changes in opacity
  and when clicked directs you to `All Products` page.
- Ensure that the `Add to Basket` button, when clicked chnages in opacity
  and adds product to the `Basket`.
- Enusure pop up window is displayed when a product is added to the 
  basket.
- Ensure that if a product is already in the basket, that if a user tries
  to add the product again, a pop up window will inform user that product
  is already in basket. 
- For mobile devices ensure simalar tests above are carried
  out.

**Layout**
- For larger devices there should be a 1 row, 2 column layout, of firstly
  an image and secondly text.
- For mobile devices there should be a 1 row, 1 column layout. Image and then
  text respectively.

### Basket App

- Main title `Shopping Basket` should be font
  `Berkshire Swash` and centred.
- Ensure orange horiztonal divider is shown underneath main header.
- Descriptive text should be font `Roboto`.
- For Desktop there should be a 1 row, 2 column structure. First column
  a table thats list all items in basket, and in the second column a basket
  total summary.
- The first column shoul dhave table headers of `Product Name` and
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
  `Delivery`and `Grand Total`.
- Each summary header should show relevant costs and be adjusted when
  items are deleted from the basket.
- Deliveyr charge should always be 10% of item(s) total.
- Ensure that there is a `Checkout` link and `Keep Shopping` link underneath
  the summary of costs.
- Ensure that the `Checkout` button has white text over a black backgrouud.
- Ensure that the `Checkout` button, when clicked changes in opacity
  directs user to `Checkout´page.
- Ensure that the `Keep shopping` link, when hovered over, changes in opacity
  and when clicked directs you to `All Products` page.
- Flood the 'Basket` with products and ensure product items and their
  totals are correct and look clean as a list on page.
- For mobile devices ensure simalar tests above are carried
  out.

**Layout**

- For smaller devices there should be a 1 row, 1 column layout with basket list
  of items first and basket total summary second.

### Checkout App (Stripe/ Webhooks/ Signals)

- Main title `Checkout` should be font
  `Berkshire Swash` and centered.
- Ensure orange horiztonal divider is shown underneath main header.
- Descriptive text should be font `Roboto`.
- `Order Summary` header should display in bold ans show number of
  items in order.
- Add and remove items from basket and ensure item count is correct
- Ensure table headers `Product Name` and `Item Price` are visable
  bold.
- Ensure that under the headers there is a product image, name, sku
  number and price.
- Ensure details are correct for product image, name, sku
  number and price.
- Flood the order with items and ensure layout remains cohesive
  and that details are correct for each item.
- For `Order Grand Total` table details ensure `ITEM(S) TOTAL`,
  `DELIVERY`, `GRAND TOTAL` are bold and undernearth each other
  respectively.
- Ensure `ITEM(S) TOTAL`, `DELIVERY`, `GRAND TOTAL` costs are correct and
  and change as items are deleted or added to `Basket`.
- Underneath the Payment Form ensure there is a `Complete Payment`
  with white font against a black background.
- Underneath the `Complete Payment`icon ensufre there
  is a link to Àdjust Basket`that is underlined and with back font,
  with white font against a black background, that when hovered
  over changes opacity.
- For mobile devices ensure simalar tests above are carried
  out.

**Payment Details Form**

- Ensure form is split by `Details`, `Delivery` and `Payment`.
- Ensure `Details` form fields have correct placeholder text.
- Ensure `Delivery` form fields have correct placeholder text.
- Ensure `Payment` form field have correct placeholder text.
- Ensure each required field display error messgae when not filled in
- Complete form details, and each time leave a required filled empty
  and try and `Complete Payment`. Error messages should be displayed
  each time informing user field which is missing. 
- Ensure `Email` can not be filled out wiht out correct `@` sign and
  `.com`.
- Type incorrect payment details and ensure red error message appears
- Fill in all fields correctly and process payment. 
- Ensure there is a `Spinning Wheel` over a green background when
  payment is being processed. 
- Once payment is processed ensure user is redirected to a
  confirmation success page
- Confirmation success page should display the email order has been made to
  and all order details.
- Ensure email is sent to user with correct order detail information
- Enusre that when unrequired fields are are not inputted in form they do not
  display in in order summary success page.
- On the payments success page when clicking back error message appears
  sttaing there is nothing in user's basket
- Ensure there is an icon for `BACK TO GRANDPA'S SHOP` under order
  confirmation, that has whote font on an orange background, that when
  hovered chnages opacity.
- For mobile devices ensure simalar tests above are carried
  out.

**Stripe/ Webhooks/ Signal**

- When order is confirmed ensure pop up window is displayed displaying
  order number information.
- When clicking `Complete Payment`, during load spinning, press the bacck button.
  Order should still get placed.
- When clicking `Complete Payment`, during load spinning, close page.
  Order should still get placed.
- For each `Complete Payment` access Stripe and it's Webhok events and
  ensure all payment Intents are successfull.
- For mobile devices ensure simalar tests above are carried
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
 
### Profile

- Main title `Checkout` should be font
  `Berkshire Swash` and centered.
- Ensure orange horiztonal divider is shown underneath main header.
- Descriptive text should be font `Roboto`.




- For mobile devices ensure simalar tests above are carried
  out.

**Form**

**Layout**

### Services

- Main title `Checkout` should be font
  `Berkshire Swash` and centered.
- Ensure orange horiztonal divider is shown underneath main header.
- Descriptive text should be font `Roboto`.




- For mobile devices ensure simalar tests above are carried
  out.

  **Layout**

### Contact

- Main title `Checkout` should be font
  `Berkshire Swash` and centered.
- Ensure orange horiztonal divider is shown underneath main header.
- Descriptive text should be font `Roboto`.




- For mobile devices ensure simalar tests above are carried
  out.

  **Layout**

### About

- Main title `Checkout` should be font
  `Berkshire Swash` and centered.
- Ensure orange horiztonal divider is shown underneath main header.
- Descriptive text should be font `Roboto`.




- For mobile devices ensure simalar tests above are carried
  out.

**Layout**

### Footer

- Main title `Checkout` should be font
  `Berkshire Swash` and centered.
- Ensure orange horiztonal divider is shown underneath main header.
- Descriptive text should be font `Roboto`.




- For mobile devices ensure simalar tests above are carried
  out.



**Layout**

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
  that a user can pick a date and time with a calendar that is formated
  with specific date options.

  Calibrating a `Date Picker` with good UI and UX became an issue with
  UI of the Date Picker being very un user friendly with the time aspect
  needing to be chosen as well as the date.

  It was therefore decided to create a separate model for 'Time'
  with the two options of 09:00 and 12:00. Allowing for a better
  user experience for the user when picking a date.

- While commiting chnages there was an error which caused the env.py
  with Stripe and Google Map secret keys being exposed in the commits
  in GitHub. 
  
  Due to this all secret keys were updated and the old secret keys
  being made rendundant.env.py file.
