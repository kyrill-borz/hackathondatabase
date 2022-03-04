# Basic Flask App

This small repo demonstrates a proper file structure for a Flask app. The folders named *static* and *templates* are required.

**Routes** and **static files** are handled correctly in all `src` and `href` attributes in the template files.

The template file `base.html` is used as a shell by the other three HTML templates. This means they insert content into `base.html` according to Jinja2 template rules.

After installing all dependencies, run the app by entering its folder and typing:

`$ python routes.py`

# Purpose
- The purpose of this project is to allow for the easy comparison between different suppliers and materials in terms of:
    - Cost
    - Lead time
    - Sustainability

- This data is collated in an open source data base allowing for anyone to add data and thus improve the tool


## Website
- The website allows for the sorting and displaying of data for comparison between suppliers
- User preference can be input to weight sorting to your needs


## Database
- The data base is the collection of data accessed by the website, or external data viewing platform