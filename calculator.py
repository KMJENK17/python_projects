print ('Calculator')
print ('1. Add')
print ('2. Subtract')
print ('3. Divide')
print ('4. Multiply')
print ('q. quit')
print ('-----------------------')
user_input = input('Select one of the following: ')

for x in user_input:
    if user_input == '1':
        num1 = input('Enter 1st number: ')
        num2 = input('Enter 2nd number: ')
        sum = int(num1) + int(num2)
        print(sum)
    if user_input == '2':
        num1 = input('Enter 1st number: ')
        num2 = input('Enter 2nd number: ')
        sum = int(num1) - int(num2)
        print(sum)

    if user_input == '3':
        num1 = input('Enter 1st number: ')
        num2 = input('Enter 2nd number: ')
        sum = int(num1) / int(num2)
        print(sum)
    if user_input == '4':
        num1 = input('Enter 1st number: ')
        num2 = input('Enter 2nd number: ')
        sum = int(num1) * int(num2)
        print(sum)
    if user_input == 'q':
        break
        

        