import phonenumbers

def is_valid_cell_phone(phone_number):
    """
    Validate if the given phone number is a valid cell phone number.

    Args:
        phone_number (str): The phone number to be validated.

    Returns:
        bool: True if the phone number is a valid cell phone number, False otherwise.
    """
    try:
        # Attempt to parse the phone number
        parsed_number = phonenumbers.parse(phone_number, None)

        # Check if the parsed number is possible, valid, and a mobile number
        if (
            phonenumbers.is_possible_number(parsed_number) and
            phonenumbers.is_valid_number(parsed_number) and
            phonenumbers.number_type(parsed_number) == phonenumbers.PhoneNumberType.MOBILE
        ):
            return True
        else:
            return False

    except phonenumbers.phonenumberutil.NumberParseException as e:
        # Handle NumberParseException, e.g., log the error or return False
        print(f"NumberParseException: {e}")
        return False

    except Exception as e:
        # Handle other exceptions, log the error, and return False
        print(f"An unexpected error occurred: {e}")
        return False
