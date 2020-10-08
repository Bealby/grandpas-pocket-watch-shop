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

- **Mobile:** An overall average of ?% was received.
- **Desktop:** An overall average of ?% was received.

[Chrome DevTools - Console](https://developers.google.com/web/tools/chrome-devtools/)
?

[Unit Tests](https://docs.djangoproject.com/en/dev/internals/contributing/writing-code/unit-tests/)
Django comes with a test suite of `Unit Tests` that all use the
testing infrastructure that ships with Django for testing applications.

A variaty of standard unit tests were carried for test_forms.py
and test_views.py. However a more expansive test program, which
would incude tests on models, would be beneficial and should be
carried out if more resource time was available.  

## Non-Automated Testing

### Main Header

- Ensure main header, for desktop devices, has the 'Logo' far left;
  'Search Bar' center; and icons for 'Repair', 'Profile' and 'Basket',
  postioned far right respectively.
- Ensure for smaller devices 'Logo' decreases in size; 'Search Bar'
  is removed; and that all respective icons decrease in size.
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
- When search icon is click with empty field user is redirected to `Products``
  page and error message is displayed.
- Ensure search function works and searches ar emade in 'Product' details
  and 'Product' description.
- Test various product category searches.
- Ensure all three icons turn from `rgb(220, 149, 35, 1)` to
  `rgb(220, 149, 35, 0.6)` when hover over.
- All above tests should be carried on mobile devices with same results.

### Navigation Bar

- All above tests should be carried on mobile devices with same results.

### Desktop Browsers

- Chrome: Website renders well on all screen sizes.
- Safari: Website renders well on all screen sizes.
- Firefox: Website renders well on all screen sizes.
- Edge: Website renders well on all screen sizes.

### Mobile and Tablet Devices

- The Website was tested on tablets and a variety of
  mobiles, including iPhone and Samsung. The results were
  satisfactory for all devices and continued to achieve the
  UX and UI goals.

### User Testing

- Family and friends were asked to use the finished Website to test
  usability and comment on whether they felt it met their needs as
  discussed in the Strategy section - [User Stories](#user-stories).
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

## Fixes

Date Picker

Crispy Forms loading in middle

<body onLoad="window.scroll(0, 0)">