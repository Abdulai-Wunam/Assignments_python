first_num = int(input('Enter the first number: '))

second_num = int(input('Enter the second number: '))

operation_type = input('Choose an operator. eg: + - / *: ' )


if operation_type == '+':
    results = first_num + second_num
    print(results)
elif operation_type =='-':
    results = first_num - second_num
    print(results)
elif operation_type =='*':
    results = first_num * second_num
    print(results)
elif operation_type == '/':
    results = first_num / second_num
    print(results)
else:
    print('An error has happened')



