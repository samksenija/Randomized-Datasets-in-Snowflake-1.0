#Random name and surname generator using the Random User API
import requests

def generate_random_name_and_surname(number_of_records):
    try:
        response = requests.get(f"https://randomuser.me/api/?inc=name,email&results={number_of_records}")
        data = response.json()

        persons = []
        i = number_of_records

        for person in data['results']:
            user_id = i
            name = person['name']['first']
            surname = person['name']['last']
            email = person['email']

            i -= 1

            persons.append([user_id, name, surname, email])
        
        return persons
    except:
        print('Something went wrong with radnomuser API, unfortunately. Please check.')
