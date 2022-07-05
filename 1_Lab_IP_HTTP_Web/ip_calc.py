"""
Lab 1.1 Ip calculator
"""

def get_ip_from_raw_address(raw_address: str) -> str:
    """
    return string with ip address
    >>> get_ip_from_raw_address('91.124.230.205/30')
    '91.124.230.205'
    >>> get_ip_from_raw_address('1.1.1.1/1')
    '1.1.1.1'
    >>> get_ip_from_raw_address('255.255.255.255/25')
    '255.255.255.255'
    """
    return raw_address[:raw_address.rfind('/')]


def num_to_bin(ip_address: str)->list:
    """
    return ip addres in 4 parts of 8-length bin format string in list
    >>> num_to_bin('91.124.230.205')
    ['0', '1', '0', '1', '1', '0', '1', '1', '0', '1', '1', '1', '1', '1', '0', '0', '1',\
 '1', '1', '0', '0', '1', '1', '0', '1', '1', '0', '0', '1', '1', '0', '1']
    >>> num_to_bin('111.193.225.5')
    ['0', '1', '1', '0', '1', '1', '1', '1', '1', '1', '0', '0', '0', '0', '0', '1', '1', '1',\
 '1', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '1', '0', '1']
    >>> num_to_bin('155.65.25.146')
    ['1', '0', '0', '1', '1', '0', '1', '1', '0', '1', '0', '0', '0', '0', '0', '1', '0', '0', '0',\
 '1', '1', '0', '0', '1', '1', '0', '0', '1', '0', '0', '1', '0']
    """
    ip_list = []
    for number in ip_address.split('.'):
        part_bin_format = bin(int(number))[2:]
        ip_list += list('0'*(8-len(part_bin_format)) + part_bin_format)
    return ip_list


def get_network_address_from_raw_address(raw_address: str) -> str:
    """
    return network address by raw addres in format ip/mask
    >>> get_network_address_from_raw_address('91.124.230.205/30')
    '91.124.230.204'
    >>> get_network_address_from_raw_address('111.193.225.5/15')
    '111.192.0.0'
    >>> get_network_address_from_raw_address('155.65.25.146/3')
    '128.0.0.0'
    """
    full_ip, maska = raw_address.split('/')
    bin_address, maska = num_to_bin(full_ip), int(maska)
    for i in range(31,-1,-1):
        maska+=1
        bin_address[i] = '0'
        if maska == 32:
            return '.'.join(str(int( ''.join(bin_address[i*8:i*8+8]), 2))  for i in range(4))


def get_broadcast_address_from_raw_address(raw_address: str) -> str:
    """
    return broadcast address by raw addres in format ip/mask
    >>> get_broadcast_address_from_raw_address('91.124.230.205/30')
    '91.124.230.207'
    >>> get_broadcast_address_from_raw_address('111.193.225.5/15')
    '111.193.255.255'
    >>> get_broadcast_address_from_raw_address('155.65.25.146/3')
    '159.255.255.255'
    """
    full_ip, maska = raw_address.split('/')
    bin_address, maska = num_to_bin(full_ip), int(maska)
    for i in range(31,-1,-1):
        maska+=1
        bin_address[i] = '1'
        if maska == 32:
            return '.'.join(str(int( ''.join(bin_address[i*8:i*8+8]), 2))  for i in range(4))

def get_binary_mask_from_raw_address(raw_address: str) -> str:
    """
    return mask in binary format
    >>> get_binary_mask_from_raw_address('91.124.230.205/30')
    '11111111.11111111.11111111.11111100'
    >>> get_binary_mask_from_raw_address('191.124.20.5/1')
    '10000000.00000000.00000000.00000000'
    >>> get_binary_mask_from_raw_address('1.2.3.2/15')
    '11111111.11111110.00000000.00000000'
    """
    ones = '11111111.11111111.11111111.11111111'
    zeros = '00000000.00000000.00000000.00000000'
    maska = int(raw_address.split('/')[1])
    index = maska + maska//8
    return ones[:index] + zeros[index:]

def get_first_usable_ip_address_from_raw_address(raw_address: str) -> str:
    """
    return broadcast address by raw addres in format ip/mask
    >>> get_first_usable_ip_address_from_raw_address('91.124.230.205/30')
    '91.124.230.205'
    >>> get_first_usable_ip_address_from_raw_address('111.193.225.5/15')
    '111.192.0.1'
    >>> get_first_usable_ip_address_from_raw_address('155.65.25.146/3')
    '128.0.0.1'
    """
    zero_ip = get_network_address_from_raw_address(raw_address)
    ind = zero_ip.rfind('.')
    return zero_ip[:ind+1] + str(int(zero_ip[ind+1:])+1)


def get_penultimate_usable_ip_address_from_raw_address(raw_address: str) -> str:
    """
    return broadcast address by raw addres in format ip/mask
    >>> get_broadcast_address_from_raw_address('91.124.230.205/30')
    '91.124.230.207'
    >>> get_broadcast_address_from_raw_address('111.193.225.5/15')
    '111.193.255.255'
    >>> get_broadcast_address_from_raw_address('155.65.25.146/3')
    '159.255.255.255'
    """
    zero_ip = get_broadcast_address_from_raw_address(raw_address)
    ind = zero_ip.rfind('.')
    return zero_ip[:ind+1] + str(int(zero_ip[ind+1:])-2)


def get_number_of_usable_hosts_from_raw_address(raw_address: str) -> int:
    """ return number of availiable host by ip/mask address
    >>> get_number_of_usable_hosts_from_raw_address('91.124.230.205/30')
    2
    >>> get_number_of_usable_hosts_from_raw_address('91.124.230.205/1')
    2147483646
    >>> get_number_of_usable_hosts_from_raw_address('91.124.230.205/15')
    131070
    """
    return 2**(32 - int(raw_address.split('/')[1])) - 2

def get_ip_class_from_raw_address(raw_address: str) -> str:
    """
    return ip class by ip/mash address
    >>> get_ip_class_from_raw_address('169.124.230.205/30')
    'B'
    >>> get_ip_class_from_raw_address('240.24.2.2/15')
    'E'
    >>> get_ip_class_from_raw_address('96.12.30.25/3')
    'A'
    """
    flag = int(raw_address.split('/')[0].split('.')[0])
    return 'E' if flag > 239 else 'D' if flag > 223 else\
           'C' if flag > 191 else 'B' if flag>127 else 'A'


def check_private_ip_address_from_raw_address(raw_address: str) -> bool:
    """
    check if ip address is private return True if yes else False
    >>> check_private_ip_address_from_raw_address('10.124.247.205/30')
    True
    >>> check_private_ip_address_from_raw_address('172.32.308.2/13')
    False
    >>> check_private_ip_address_from_raw_address('192.168.230.5/22')
    True
    >>> check_private_ip_address_from_raw_address('192.96.450.20/22')
    False
    """
    bite_1, bite_2, _, _ =  map(int, raw_address.split('/')[0].split('.'))
    return True if bite_1==10 or bite_1 == 172 and 15 < bite_2 < 32\
                              or (bite_1, bite_2) == (192,168) else False
