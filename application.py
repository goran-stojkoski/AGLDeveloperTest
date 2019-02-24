#!/usr/bin/env python
"""
The following module utilises the PetParser class from the pet_parser module. It renders a html template to display the requested data
"""

from flask import Flask, render_template, request, flash
from pet_parser.pet_parser import PetParser
import static.constants

application = app = Flask(__name__)
app.secret_key = "all good here"


@app.route('/', methods=['GET', 'POST'])
@app.route('/index.html', methods=['GET', 'POST'])
def index():
    selection_fields = static.constants.VALID_SELECTION_FIELDS
    valid_form = True
    default_settings_string = ""

    if request.method == "POST":
        for selection_field, selected_item in selection_fields.items():
            if selection_field not in request.form:
                flash("Please select an option from the " + selection_field.replace("_", " ").title() + " dropdown",
                      "danger")
                valid_form = False

        if not valid_form:

            return render_template('index.html', selection_fields=selection_fields)

        else:
            pet_type = request.form['pet_types']
            person_group = request.form['person_group']

    else:
        # Apply requested AGL test selection as default selection, i.e. Cat Names in alphabetical order by owner gender
        # Note: Result list is already sorted in alphabetical order
        pet_type = "Cat"
        person_group = 'gender'
        default_settings_string = "Default Settings: "

    try:
        pet_names = PetParser.get_pet_names_by_field(pet_type, person_group)
        flash(default_settings_string + "Displaying " + pet_type.lower() + " names by owner " + person_group, "success")

        return render_template('index.html', pet_names=pet_names, selection_fields=selection_fields)

    except IOError:
        flash("Could not load JSON file", "danger")

        return render_template('index.html', selection_fields=selection_fields)


if __name__ == '__main__':
    app.run()
