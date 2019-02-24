VALID_SELECTION_FIELDS = {
    'person_group': ['name', 'gender', 'age'],
    'pet_types': ['cat', 'dog', 'fish']
}

AGL_JSON_URL = 'http://agl-developer-test.azurewebsites.net/people.json'

mock_data = [{'name': 'Bob', 'gender': 'Male', 'age': 23,
              'pets': [{'name': 'Garfield', 'type': 'Cat'}, {'name': 'Fido', 'type': 'Dog'}]},
             {'name': 'Jennifer', 'gender': 'Female', 'age': 18, 'pets': [{'name': 'Garfield', 'type': 'Cat'}]},
             {'name': 'Steve', 'gender': 'Male', 'age': 45, 'pets': None},
             {'name': 'Fred', 'gender': 'Male', 'age': 40,
              'pets': [{'name': 'Tom', 'type': 'Cat'}, {'name': 'Max', 'type': 'Cat'},
                       {'name': 'Sam', 'type': 'Dog'}, {'name': 'Jim', 'type': 'Cat'}]},
             {'name': 'Samantha', 'gender': 'Female', 'age': 40, 'pets': [{'name': 'Tabby', 'type': 'Cat'}]},
             {'name': 'Alice', 'gender': 'Female', 'age': 64,
              'pets': [{'name': 'Simba', 'type': 'Cat'}, {'name': 'Nemo', 'type': 'Fish'}]}]
