previous_command = ''
while True:
    command = input('> ').lower()
    if command == 'help':
        print("""
start - to start the car
stop - to stop the car
quit - to exit
        """)
    elif command == 'start':
        if previous_command == command:
            print('Car is already Started.')
        else:
            print('Car Started...Ready to go!')
            previous_command = command
    elif command == 'stop':
        if previous_command == command:
            print('Car is already Stopped.')
        else:
            print('Car Stopped.')
            previous_command = command
    elif command == 'quit':
        break
    else:
        print("I don't understand that...")