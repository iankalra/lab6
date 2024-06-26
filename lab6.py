
# Chaitanya Rana (Collaborator)
# Ian Kalra (Owner of Repository)

def encode(password):
    result = ''
    for i in range(len(password)):
        if password[i] == "7":
            result += "0"
        elif password[i] == "8":
            result += "1"
        elif password[i] == "9":
            result += "2"
        else:
            new_num = int(password[i]) + 3
            result += str(new_num)
    return result


def decode(encodedPassword):
    decodedPass = ""
    for char in encodedPassword:
        decodedPass += str(int(char)-3)
    return decodedPass


def main():
    var = ''
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit\n")
        selection = int(input("Please enter an option: "))
        if selection == 3:
            exit()
        elif selection == 1:
            password = input("Please enter your password to code: ")
            print("Your password has been encoded and stored!\n")
            var = encode(password)
        elif selection == 2:
            decoded_password = decode(var)
            print(f'The encoded password is {var}, and the original password is {decoded_password}.')


if __name__ == "__main__":
    main()