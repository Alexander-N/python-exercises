def is_armstrong(number):
    str_number = str(number)
    n_digits = len(str_number)
    Peter = 0

    for digit in str_number:

        Peter += int(digit)**n_digits

    return Peter == number
