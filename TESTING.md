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

**Unit Tests** Django comes with a test suite of `Unit Tests` that all use the testing
infrastructure that ships with Django for testing applications.

A variaty of standard unit tests were carried for
test_forms.py and test_views.py. However a more expansive test program, which
would incude tests on models, would be beneficial and should be carried out
if more resource time was available.  


## Non-Automated Testing

### Main Header/ Navigation Bar

- 

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