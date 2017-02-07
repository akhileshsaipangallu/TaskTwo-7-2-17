""" Program takes range as input for Fibonacci Series and it will print
    a list of Fibonacci numbers based on the range"""


def series(series_range, fibonacci_list):
    last_but_one, last_one = fibonacci_list[-2], fibonacci_list[-1]
    temp = last_one
    last_one += last_but_one
    last_but_one = temp

    if last_one <= series_range:
        fibonacci_list.append(last_one)
        return series(series_range, fibonacci_list)
    else:
        return fibonacci_list

if __name__ == '__main__':
    fibonacci = [0, 1, 1]
    input_range = input("Enter the range \n")
    print('Fibonacci Series:\n')
    print series(input_range, fibonacci)

