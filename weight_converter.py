weight = input('Weight : ')
unit = input('(L)bs or (K)g : ')
if unit.upper() == 'L':
    weight = float(weight) * 0.453592
    print(f'You are {weight} kilos')
elif unit.upper() == 'K':
    weight = float(weight) * 2.20462
    print(f'You are {weight} pounds')