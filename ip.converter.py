def is_valid_ip(ip):
    parts = ip.split(".")
    if len(parts)!=4:
        return False
    for part in parts:
        if not part.isdigit():
            return False
        num = int(part)
        if num < 0 or num > 255:
            return False

        return True

print(is_valid_ip("192.168.1.1"))
print(is_valid_ip("192.168.1"))

def decimal_to_binary(n):
    if n ==0:
        return "0"
    if n ==1:
        return "1"
    return decimal_to_binary(n // 2) + str(n % 2)

print(decimal_to_binary(5))
print(decimal_to_binary(10))

def decimal_to_binary_8bit(n):
    b = decimal_to_binary(n)
    missing_zeroes = 8 - len(b)

    padded = "0" * missing_zeroes + b
    return padded

print(decimal_to_binary_8bit(1))
print(decimal_to_binary_8bit(255))

def ip_to_binary(ip):
    if not is_valid_ip(ip):
        return "Invalid IP address"
    parts = ip.split(".")

    binary_parts = [decimal_to_binary_8bit(int(p)) for p in parts]
    return ".".join(binary_parts)

print(ip_to_binary("192.168.1.1"))
print(ip_to_binary("255.255.255.0"))
print(ip_to_binary("256.1.1.1"))

def binary_to_decimal(b):
    if b == "":
        return 0
    return int(b[-1]) + 2 * binary_to_decimal(b[:-1])

print(binary_to_decimal("1010"))
print(binary_to_decimal("11111111"))

def binary_to_ip(binary_ip):
    parts = binary_ip.split(".")
    if len(parts) != 4 or any(len(p) != 8 for p in parts):
        return "Invalid binary IP address"

    decimal = [str(binary_to_decimal(p)) for p in parts]
    return ".".join(decimal)

print(binary_to_ip("11000000.10101000.00000001.00000001"))

def ip_convert(ip):
    is_binary = True

    for c in ip:
        if c != "0" and c != "1" and c != ".":
            is_binary = False
            break

    if is_binary:
        return binary_to_ip(ip)
    else:
        return ip_to_binary(ip)

print(ip_convert("192.168.1.1"))
print(ip_convert("11000000.10101000.00000001.00000001"))


