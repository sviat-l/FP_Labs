"""
Lab 8 re-based Validator
"""

import re

class Validator:
    """ Class to validate user information using regex """

    def validate_name_surname(self, name_surname:str) -> bool:
        """ Check correctness for user's name and surname information """
        return bool(re.match(r'^[A-Z][a-z]{1,29} [A-Z][a-z]{1,29}$', name_surname))

    def validate_age(self, age: str) -> bool:
        """ Check correctness for user's age information """
        return bool(re.match(r"^(1[6-9]|[2-9]\d)$", age))

    def validate_country(self, country: str) -> bool:
        """ Check correctness for user's country information """
        return bool(re.match(r"^([A-Z][A-Za-z]{1,9})$", country))

    def validate_region(self, region: str) -> bool:
        """ Check correctness for user's region information """
        return bool(re.match(r"^([A-Z]\w{1,9})$", region))

    def validate_living_place(self, living_place: str) -> bool:
        """ Check correctness for user's living place information """
        return bool(re.match(r"^[A-Z][a-z]{2,19} (st.|av.|prosp.|rd.) (\d[a-z0-9])$", living_place))

    def validate_index(self, index: str) -> bool:
        """ Check correctness for user's postindex information """
        return bool(re.match(r"^\d{5}$", index))

    def validate_phone(self, phone: str) -> bool:
        """ Check correctness for user's phone information """
        return bool(re.match(r"^/+38\d{7,10})$", phone))

    def validate_email(self, email: str) -> bool:
        """ Check correctness for user's email information """
        return bool(re.match( r"^([^\s\.][^\s]{,62}[^\s]|[\s\.])@"+\
                 r"[a-z]{1,255}(\.(com|org|edu|gov|net|ua)){1,5}$",\
                            email))

    def validate_id(self, id_str: str) -> bool:
        """ Check correctness for user's id information """
        return bool(re.match(r"^((?=^[0-9]{6}$)[1-9]{,5}0[1-9]{,5})$", id_str))

    def validate(self, user_info: str) -> bool:
        """ Check correctness for the whole user's information """
        return bool(re.match(r"^([A-Z][A-Za-z]{1,9})$", user_info))
