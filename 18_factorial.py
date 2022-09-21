import math

fact = int(input("kindly input a number "))

if fact > 0:
    f_char = list(range(1, fact + 1))

    f_char_rev = list(reversed(f_char))

    result = math.prod(f_char_rev)
    print(result)

else:
    print('input number greater than zero')


