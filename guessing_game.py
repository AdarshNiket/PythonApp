count = 0
guess = 9
while count < 3:
    value = int(input('Guess: '))
    count += 1
    if value == guess:
        print('You Win!')
        break
else:
    print('You Loss!')