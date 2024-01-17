# # (0°C × 9/5) + 32 = 32°F
# # (32°F − 32) × 5/9 = 0°C
#
# def c_to_f(Celsius):
#     if Celsius < -273.15:
#         print("Invalid input. Temperature cannot be below absolute zero.")
#         return None
#     return (Celsius * 9/5) + 32
#
# def f_to_c(Fahrenheit):
#     if Fahrenheit < -459.67:
#         print("Invalid input. Temperature cannot be below absolute zero.")
#         return None
#     return (Fahrenheit - 32) * 5/9
#
# while True :
#     Menu = input("1) Celsius to Fahrenheit 2)Fahrenheit to Celsius 3)Prime number checker 4)Prime number checker between two numbers 5) Quit : ")
#     print()
#     if Menu not in ['1', '2', '3', '4', '5'] :
#         print("Please choose from the menu.")
#     if Menu == '1' :
#         try :
#             Celsius = float(input('Input Celsius : '))
#             result = c_to_f(Celsius)
#             if result is not None:
#                 print(f'{Celsius}°C, {result:.4f}°F')
#         except ValueError :
#             print("Invalid input. Please enter an integer.")
#     elif Menu == '2' :
#         try :
#             Fahrenheit = float(input('Input Fahrenheit : '))
#             result = f_to_c(Fahrenheit)
#             if result is not None:
#                 print(f'{Fahrenheit}°F, {result:.4f}°C')
#         except ValueError :
#             print("Invalid input. Please enter an integer.")
#     elif Menu == '3' :
#         try:
#             number = int(input("Input an integer: "))
#             is_prime = True
#             if number < 2:
#                 print(f'{number} is not a prime number')
#             else:
#                 i = 2
#                 while i < number:
#                     if number % i == 0:
#                         is_prime = False
#                         break
#                     i += 1
#                 if is_prime:
#                     print(f'{number} is a prime number')
#                 else:
#                     print(f'{number} is not a prime number')
#         except ValueError:
#             print("Invalid input. Please enter an integer.")
#
#     elif Menu == '4' :
#         try:
#             numbers = input("Input two different numbers : ").split()
#             if len(numbers) != 2:
#                 raise ValueError("Please enter exactly two numbers.")
#
#             n1 = int(numbers[0])
#             n2 = int(numbers[1])
#             if n1 == n2 :
#                 raise ValueError("Please enter exactly two numbers.")
#             if n1 > n2:
#                 n1, n2 = n2, n1
#
#             for number in range(n1, n2 + 1):
#                 is_prime = True
#                 if number < 2:
#                     pass
#                 else:
#                     i = 2
#                     while i * i <= number:
#                         if number % i == 0:
#                             is_prime = False
#                             break
#                         i = i + 1
#                         # print(i, end= ' ')
#                     if is_prime:
#                         print(number, end=' ')
#
#         except ValueError:
#             print("Invalid input. Please enter two different integers.")
#
#     elif Menu == '5' :
#         print('Terminating the program.')
#         break
#     print()
#
# #6.1
# list = [3, 2, 1, 0]
#
# for num in list:
#     print(num)
#
# #6.2
# guess_me = 7
# number = 1
# while number :
#     if guess_me>number :
#         print('too low')
#     elif guess_me==number :
#         print('found it!')
#         break
#     elif guess_me<number :
#         print('oops')
#         break
#     number = number + 1
# #6.3
# guess_me = 5
# for number in range(10):
#     if guess_me > number:
#         print('too low')
#     elif guess_me==number :
#         print('found it!')
#         break
#     elif guess_me<number :
#         print('oops')
#         break

#8.1
e2f = {'dog':'chien', 'cat':'chat', 'walrus':'morse'}
print(e2f)

#8.2
print(e2f['walrus'])

#8.3
f2e = {value: key for key, value in e2f.items()}
print(f2e)

#8.4
print(e2f['dog'])

#8.5
print(e2f.keys())

#8.6
life = {'animals': {'cats': 'Henri', 'octopi': 'Grumpy', 'emus': 'Lucy'}, 'plants': {},'others': {}}

#8.7
print(life.keys())

#8.8
print((life['animals']).keys())