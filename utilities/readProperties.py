import configparser

config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")
# config.read("C:\\Users\\Dell\\PycharmProjects\\pythonProject\\alberta\\Configurations\\config.ini")


class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url = config.get('common_info', 'baseURL')
        return url

    @staticmethod
    def getUseremail():
        username = config.get('common_info', 'UserName')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common_info', 'Password')
        return password
