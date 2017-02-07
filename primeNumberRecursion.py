""" Program takes a number as input and it will print whether
    its a prime number or not"""


def prime_checking(number, i):
    if i is 1:
        return True
    else:
        if number % i is 0:
            return False
        else:
            return prime_checking(number, i - 1)

if __name__ == '__main__':
    input_number = input('Enter a number\n')
    var = prime_checking(input_number, int(input_number / 2))
    if var:
        print("\n%d is a prime number" % input_number)
    else:
        print("\n%d is not a prime number" % input_number)

