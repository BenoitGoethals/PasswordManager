class Credentials:

    def __init__(self, url, user_email, passwd):
        self.__site_url = url
        self.__user_email = user_email,
        self.__password = passwd

    def to_string(self):
        return f"{self.__site_url} | {self.__user_email} | {self.__password}"
