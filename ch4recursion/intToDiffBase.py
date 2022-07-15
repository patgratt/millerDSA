# recursive algorithm to convert an in string format to its representation in any base

def to_str(n, base):
    convert_string = "0123456789ABCDEF"
    # base case, when we've narrowed it down to a single digit
    if n < base:
        return convert_string[n]
    else:        
        return to_str(n // base, base) + convert_string[n % base]

print(to_str(1453, 16))