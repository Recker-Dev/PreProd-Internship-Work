from faker import Faker
import json

def createFakeDeliveryAgent():

    """
    Creates a fake delivery agent with random data.

    This function uses the Faker library to generate fake data for a delivery agent, including name, address, email, location, and phone number.
    The data is then converted to a JSON string and returned.

    Parameters:
    None

    Returns:
    str: A JSON string representing the fake delivery agent data.
    """


    fake = Faker()


    message = {
        'name': fake.name(),
        'address': fake.address(),
        'email':fake.ascii_safe_email(),
        'location':fake.local_latlng(),
        'phone':fake.phone_number()
    }

    return json.dumps(message)


