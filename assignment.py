# # (0°C × 9/5) + 32 = 32°F
# # (32°F − 32) × 5/9 = 0°C

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
# def isprime(n) -> bool:
#     """
#     매개변수로 넘겨받은 수가 소수인지 여부를 boolean으로 리턴
#     : param n: 판정할 매개변수
#     : return: 소수면 True 아니면 False
#     """
#     if n < 2:
#         return False
#     else:
#         i = 2
#         while i*i <= n:
#             if n % i == 0:
#                 return False
#             i += 1
#         return True
# print(isprime.__doc__)
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
#             n = int(input("Input an integer: "))
#             if isprime(n):
#                 print(f'{n} is a prime number')
#             else:
#                 print(f'{n} is not a prime number')
#         except ValueError:
#             print("Invalid input. Please enter an integer.")
#
#     elif Menu == '4' :
#         try:
#             n1, n2 = map(int,input("Input two different numbers : ").split())
#             n1, n2 = min(n1, n2), max(n1, n2)
#
#             for n in range(n1, n2 + 1):
#                 if isprime(n):
#                     print(n, end=' ')
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

# #8.1
# e2f = {'dog':'chien', 'cat':'chat', 'walrus':'morse'}
# print(e2f)
#
# #8.2
# print(e2f['walrus'])
#
# #8.3
# f2e = {value: key for key, value in e2f.items()}
# print(f2e)
#
# #8.4
# print(e2f['dog'])
#
# #8.5
# print(e2f.keys())
#
# #8.6
# life = {'animals': {'cats': 'Henri', 'octopi': 'Grumpy', 'emus': 'Lucy'}, 'plants': {},'others': {}}
#
# #8.7
# print(life.keys())
#
# #8.8
# print((life['animals']).keys())
#
# #8.9
# print(life['animals']['cats'])
#
# #8.10
# squares = {n:pow(n,2) for n in range(10)}
# print(squares)

#9.1

def good() :
    return ['Harry', 'Ron', 'Hermione']

print(good())

#9.2
def get_odds() :
    for a in range(10):
        if a % 2 == 1:
            yield a

odds_generator = get_odds()

third_odd = list(get_odds())[2]
print(third_odd)

#9.3
def test(func):
    def wrapper(*args, **kwargs):
        print("start")
        result = func(*args, **kwargs)
        print("end")
        return result
    return wrapper