import random


class PasswordGenerator:
    __letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    __numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    __symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    @staticmethod
    def generate_password():
        password_letters = [random.choice(PasswordGenerator.__letters) for _ in range(random.randint(8, 10))]
        password_symbols = [random.choice(PasswordGenerator.__symbols) for _ in range(random.randint(2, 4))]
        password_numbers = [random.choice(PasswordGenerator.__letters) for _ in range(random.randint(2, 4))]
        password = "".join(password_symbols+password_letters+password_numbers)
        print(f"Your password is: {password}")
        return password
