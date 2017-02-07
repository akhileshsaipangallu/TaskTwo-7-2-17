""" Program takes range as input and it will print Prime Number list
    based on the range"""


def prime_checking(number, i):
    if i is 1:
        return True
    else:
        if number % i is 0:
            return False
        else:
            return prime_checking(number, i - 1)


def prime_number_series(input_range, prime_number_list):
    if input_range is 1:
        prime_number_list.append(1)
        return prime_number_list
    else:
        if prime_checking(input_range, int(input_range / 2)):
            prime_number_list.append(input_range)
        return prime_number_series(input_range - 1, prime_number_list)

if __name__ == '__main__':
    series_range = input("Enter range for prime number series(>1)\n")
    series = []
    print list(reversed(prime_number_series(series_range, series)))

