# Sin list comprehension
symbols = '$¢£¥€¤'
codes = []
for symbol in symbols:
    codes.append(ord(symbol))
print(codes)

# Con list comprehension
symbols = '$¢£¥€¤'
codes_list_comprehension = [ord(symbol) for symbol in symbols]
print(codes_list_comprehension)

# Ahora con map/filter 
symbols = '$¢£¥€¤'
beyond_ascii = [ord(s) for s in symbol if ord(s) > 127] # list comprehension
print(beyond_ascii)
beyond_ascii = list(filter(lambda c: c > 127, map(ord, symbols)))
print(beyond_ascii)
# List comprehension es mas rapido, ademas de que en escencia es mas legible
