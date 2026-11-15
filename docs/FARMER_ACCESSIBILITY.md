# Farmer-first readability and accessibility

The interface is intended to work for farmers who may have limited experience with computers or technical language.

## Interface choices

- Body text and small labels are enlarged; buttons and form controls have larger touch targets.
- Text and controls use stronger contrast and a clear keyboard-focus outline.
- The interface uses plain-language labels such as “Rain in the rainy season” and “How do you get water for your crops?”.
- Optional soil-test values have separate accessible names and can be left blank.
- The plant-growth tab reports loading steps, keeps the latest selected location, and provides a clear error or retry option rather than silently leaving the detail area empty.
- The map and charts explain that their data describe the surrounding area, not a measurement of an individual field.

## Important MODIS note

Live MODIS data are satellite observations. If the satellite service cannot be reached and the example option is enabled, the app may show an illustrative computer-made estimate. The screen labels this as an example only. It must not be presented as an observed satellite reading or used to judge an individual field.

## Further improvements

The current interface is still English-only. Before field deployment, translate the main screens into the local languages required by the intended users and test the wording with farmers and agricultural extension workers. Icons should support text, not replace it. A local agricultural officer should review crop advice before it is used for planting decisions.



## Dashboard display modes

The dashboard is available in English. It does not contain an automatic translation selector or a machine-translation service. The independent landing page retains its own language selector and built-in translated copy.

The crop-plan cards offer **Easy view** and **Detailed view**. Easy view presents the key scores and farmer-facing explanations. Detailed view retains technical information such as crop calendars, model inputs, assumptions, criterion weights, weighted contributions, benefits and trade-offs.

A score such as “75/100” is the plan's raw performance for one criterion. The “Importance” percentage is how much the selected farmer priority counts that criterion in the final ranking. The weighted contribution is the part that changes with the selected priority.
