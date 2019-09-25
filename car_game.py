while True:
    command = input('> ').lower()
    if command.lower() == 'help':
        print("""
start - to start the car
stop - to stop the car
quit - to exit
        """)
    elif command == 'start':
        print('Car Started...Ready to go!')
    elif command.lower() == 'stop':
        print('Car Stopped.')
    elif command == 'quit':
        break
    else:
        print("I don't understand that...")