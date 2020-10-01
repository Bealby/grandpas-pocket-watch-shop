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

[Lighthouse Audit](https://developers.google.com/web/tools/lighthouse/) -
A feature in Chrome Developing Tools - Lighthouse Audit - was carried out
on Mobile and Desktop to assess **Performance**, **Accessibility**,
**Best Practices**, **CEO** and **Progressive Web App**.

- **Mobile:** An overall average of 92.75% was received.
- **Desktop:** An overall average of 90.25% was received.

Chrome Developing Tools also analysed the Progressive Web App,
which validate the aspects of a Progressive Web App. The results
were satisfactory.

[Validate Javascript](https://validatejavascript.com/) - Javascript
files were uploaded in in the Validate Javascript. Overall there
were no errors that needed to be changed and the javascript passed
general standards.

[Chrome DevTools - Console](https://developers.google.com/web/tools/chrome-devtools/)
Navigating through the Website rendered two different types of errors, that are not
critcial but worth addressing at a later date:

- `www-embed-player.js:453 GET https://googleads.g.doubleclick.net/pagead/id, net::ERR_BLOCKED_BY_CLIENT`
   These errors relate to Adblock or browser safety extensions. Which
   will not be addressed at this stage as such extensions can be
   disabled buy the user.

- `/favicon.ico:1 Failed to load resource:`
  `the server responded with a status of 404 (NOT FOUND)`
  Favicons are small 16x16 icon files that are displayed next to the
  URL of a Website. It would be benefical to add these at a later date.

## Non-Automated Testing


#### Desktop Browsers

- Chrome: Website renders well on all screen sizes.
- Safari: Website renders well on all screen sizes.
- Firefox: Website renders well on all screen sizes.
- Edge: Website renders well on all screen sizes.

#### Mobile and Tablet Devices

- The Website was tested on tablets and a variety of
  mobiles, including iPhone and Samsung. The results were
  satisfactory for all devices and continued to achieve the
  UX and UI goals.

#### User Testing

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

#### User Experience

#### Fixes

