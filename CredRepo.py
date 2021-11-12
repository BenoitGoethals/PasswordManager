from Credentials import Credentials


class CredRepo:

    @staticmethod
    def save(credentials: Credentials):
        try:
            with open("data.data", "a") as file:
                file.write(credentials.to_string())
                return True
        except ValueError:
            print(ValueError)
            return False
