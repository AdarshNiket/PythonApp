# print('Adarsh Niket')
# name = 'Adarsh Niket'
# age = 30
# is_newpatient = True
# print(f'{name[-5:]} , {name[:6]}')

# weight = input('What is your weight(pound)? ')
# print(type(weight))
# color = input('What is your favourite color? ')
# print(name + ' likes ' + color)
# print(float(weight) * 0.453592)

# price = 1000000
# is_goodCredit = True
# if is_goodCredit:
#     print('put down 10%')
#     print(f'Down Payment: ${price * .1}')
# else:
#     print('put down 20%')
#     print(f'Down Payment: ${price * .2}')

# Logical Operators/Comparison Operator
# name = 'Jake';
# if len(name) < 3:
#     print('Name must be atleast 3 characters')
# elif len(name) > 50:
#     print('Name can be max of 50 characters')
# else:
#     print('Name looks good!')

# For Loop
# prices = [10,20,30]
# total_price = 0
# for item in prices:
#     total_price += item
# print(total_price)

# Nested For Loop
# numbers = [5, 2, 5, 2, 2]
# # numbers = [1, 1, 1, 1,  5]
# for item in numbers:
#     output = ''
#     for x in range(item):
#         output += 'x'
#     print(output)

# List - find largest number.
list = [3, 6, 2, 8, 4, 10]
max = list[0]
for item in list:
    if item > max:
        max = item
print(f'Lagest Number is: {max}')

