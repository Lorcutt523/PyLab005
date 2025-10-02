def is_valid_part(part:str):
    try:
        part = part.strip()
        i_part = int(part)
        if 0 <= i_part <= 255:
            if i_part == 0 and len(part) > 2:
                return False
            if i_part != 0 and part[0] == '0':
                return False
            return True
        else:
           return False
    except ValueError:
        return False

def is_valid_ip(ip:str):
    ip_parts = ip.split('.')
    print(len(ip_parts))
    if len(ip_parts) != 4:
        return False

    for i in ip_parts:
        if not is_valid_part(i):
            return False

    return True

is_valid_ip("192.168.1.1")
print(is_valid_ip("192.168.1.1"))  # True
print(is_valid_ip("192.168.256.1"))  # False
print(is_valid_ip("192.168.1"))  # False
print(is_valid_ip("192.168.01.1"))  # False
#print(is_valid_part("255"))  # True
#print(is_valid_part("256"))  # False
#print(is_valid_part("01"))   # False
#print(is_valid_part("0"))    # True

