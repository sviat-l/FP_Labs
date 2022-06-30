"""
Lab 8 re-based Validator
"""

import re

class Validator:
    """ Class to validate user information using regex """

    def validate_name_surname(self, name_surname:str) -> bool:
        """ Check correctness for user's name and surname information """
        return re.match(r'^[A-Z][a-z]{1,29} [A-Z][a-z]{1,29}$', name_surname) is not None

    def validate_age(self, age: str) -> bool:
        """ Check correctness for user's age information """
        return re.match(r"^(1[6-9]|[2-9]\d)$", age) is not None

    def validate_country(self, country: str) -> bool:
        """ Check correctness for user's country information """
        return re.match(r"^([A-Z][A-Za-z]{1,9})$", country) is not None

    def validate_region(self, region: str) -> bool:
        """ Check correctness for user's region information """
        return re.match(r"^([A-Z]\w{1,9})$", region)  is not None

    def validate_living_place(self, living_place: str) -> bool:
        """ Check correctness for user's living place information """
        return re.match(r"^[A-Z][a-z]{2,19} (st.|av.|prosp.|rd.) "
                        r"(\d[a-z0-9])$", living_place) is not None

    def validate_index(self, index: str) -> bool:
        """ Check correctness for user's postindex information """
        return re.match(r"^\d{5}$", index) is not None

    def validate_phone(self, phone: str) -> bool:
        """ Check correctness for user's phone information """
        return re.match(r"^\+\d{2}( \()?\d{,3}(\) )?\d{3}(-?\d{2}){2}$",
             phone) is not None

    def validate_email(self, email: str) -> bool:
        """ Check correctness for user's email information """
        sym = r"\w\!\#\$\%\&\'\*\+\-\/\=\?\^\_\`\{\|\}\~"
        return re.match( r"^(?=^[" +sym +r"\.]{,63}["+sym+r"]@)"
            r"(["+sym+r"][\.]?){,63}["+sym+"]@"
            r"[a-z]{1,255}(\.(com|org|edu|gov|net|ua)){1,5}$",  email) is not None

    def validate_id(self, id_str: str) -> bool:
        """ Check correctness for user's id information """
        return re.match(r"^(?=^[0-9]{6}$)[1-9]{,5}0[1-9]{,5}$", id_str) is not None

    def validate(self, user_info: str) -> bool:
        """ Check correctness for the whole user's information """
        func = [self.validate_name_surname, self.validate_age, self.validate_country,
            self.validate_region, self.validate_living_place, self.validate_index,
            self.validate_phone, self.validate_email, self.validate_id]
        splited = re.split(r'[\,\;]\s*', user_info)
        return len(splited)==9 and all(func[i](splited[i]) for i in range(9))
