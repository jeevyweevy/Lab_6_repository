
def encode(password):
    str_password = str(password)
    encoded_string = ""
    for num in str_password:
        encoded_value = str((int(num) + 3) % 10)
        encoded_string += encoded_value
    return encoded_string

if __name__ == '__main__':
    while True:
        print(f'Menu'
              f'-------------\n'
              f'1. Encode\n'
              f'2. Decode\n'
              f'3. Exit\n\n')
        option = int(input('Please enter an option: '))
        if option == 1:
            password = input('Please enter your password to encode: ')
            print('Your password has been encoded and stored!')
            encoded_password = encode(password)
        elif option == 2:
            print(f'The encoded password is {encoded_password}, and the original password is {password}.')
        elif option == 3:
            exit()



