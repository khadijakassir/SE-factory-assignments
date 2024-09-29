def valid_address(ip):
    parts = ip.split('.')
    if len(parts) != 4:
        return "invalid address"
    for part in parts:
        if not part.isdigit() or (part[0] == '0' and len(part) > 1):
            return "invalid IPv4 address"
        num = int(part)
        if num < 0 or num > 255:
            return "invalid  address"
    return "valid  address"
ipaddress = input("insert your IP address: ")
print(valid_address(ipaddress))