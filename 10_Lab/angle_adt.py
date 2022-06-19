"""
Module with angle abstract date type to encode messages with camera rotation
"""


class angleADT:
    """ class for absract data type angle """

    def __init__(self, message):
        """init message value"""
        self.message = message

    def encode_message(self):
        """encode message in angle rotation values"""
        hex_repr = self.hexadecimal_string_repr(self.message)

        # find angle change values for hexi code
        rotate_angles = [hex_repr[0]*22.5 if hex_repr else 360.0]
        for i in range(1, len(hex_repr)):
            diff = hex_repr[i] - hex_repr[i-1]
            rotate_angles.append(diff*22.5 if diff else 360.0)
        return rotate_angles

    def hexadecimal_string_repr(self, text):
        """ represent text as list with hexadecimal value
        That represent symbol in ASCII table"""
        return [num for sym in text for num in self.encode_symbol(sym)]

    def encode_symbol(self, chrt):
        """encode one symbol into hex representation
        return list with code sequence"""
        hex_repr = hex(ord(chrt))
        return [int(s, base=16) for s in hex_repr[2:]]
