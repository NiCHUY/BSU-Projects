def get_last_digit(number):
    last_digit = number % 10
    return last_digit


def get_fractional_part(x):
    fractional_part = x - int(x)
    return fractional_part


def get_first_decimal_digit(x):
    fractional_part = x - int(x)
    decimal_digit = int(fractional_part * 10)
    return decimal_digit


def round_ru(x):
    return round(x)


print(get_last_digit(1213136))
print(get_fractional_part(12.312321312))
print(get_first_decimal_digit(12.312321312))
print(round_ru(12.512321312))
