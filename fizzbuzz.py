# Landing
print('FIZZBUZZ BUZZ')
print('----------------')
print('FIZZBUZZ BUZZ is a function that will tell you if a number you enter is a Fizz(even) or Buzz(odd)')

user_input = input('Enter a number: ')

for user_input in range(1, 101):
    if user_input % 3 == 0 and user_input % 5 == 0:
        print ('FizzBuzz')
    elif user_input % 3 == 0:
        print ('Fizz')
    elif user_input % 5 == 0:
        print ('Buzz')
    else:
        print (str(user_input))