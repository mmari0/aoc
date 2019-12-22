"""
AOC-2019
day: 4
story: 1&2
"""
from arepl_dump import dump

def get_digit(number):
    digit = []
    for char in str(number):
        digit.append(char)
    return digit

def count_repeated(number, value):
    digit = get_digit(number)
    return digit.count(value)

def check_double(number):
    digit = get_digit(number)
    for char in digit:
        if count_repeated(number, char) > 1:
            return True
    return False

def check_decrease(number):
    digit = get_digit(number)
    for i in range(len(digit) - 1):
        if int(digit[i]) > int(digit[i + 1]):
            return False
    return True

def check_group(number):
    digit = get_digit(number)
    for char in digit:
        if count_repeated(number, char) == 2:
            return True
    return False

def check_criteria(number, step):
    if not check_double(number):
        return False
    if not check_decrease(number):
        return False

    if step == 'step1':
        return True

    if not check_group(number):
        return False
    return True


assert check_criteria(111123, 'step1') == True
assert check_criteria(122345, 'step1') == True
assert check_criteria(223450, 'step1') == False
assert check_criteria(123789, 'step1') == False

assert check_criteria(112233, 'step2') == True
assert check_criteria(123444, 'step2') == False
assert check_criteria(111122, 'step2') == True

def count_password_step1(start, stop):
    count = 0
    for i in range(start, stop):
        if check_criteria(i, 'step1'):
            count += 1
    return count

def count_password_step2(start, stop):
    count = 0
    for i in range(start, stop):
        if check_criteria(i, 'step2'):
            count += 1
    return count

if __name__ == '__main__':
    start = 236491
    stop = 713787

    count_pass = count_password_step1(start, stop)
    assert count_pass == 1169
    print('ans for step1: ' + str(count_pass))

    count_pass = count_password_step2(start, stop)
    assert count_pass == 757
    print('ans for step2: ' + str(count_pass))