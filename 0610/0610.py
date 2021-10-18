def f():

    znach = {}
    nam = ''
    numbers = ''

    while nam != 'q' and numbers != 'q':
        nam = input()
        if nam == 'q':
            break
        numbers = input()
        if numbers == 'q':
            break
        if numbers[0] == '+' and numbers[1].isdigit \
            and numbers[2] == "-" and numbers[3:6].isdigit \
            and numbers[6] == '-' and numbers[7:10].isdigit \
            and numbers[10] == '-' and numbers[11:13].isdigit \
            and numbers[13] == '-' and numbers[14:] and len(numbers) == 16:
            znach[nam] = numbers
        else:
            print('Wrong!')
    print(znach)

f()