from requests import get

class SocialNetwork:
    def __init__(self, username):
        self.username = username
        self.domain = None

    def get_username(self):
        return self.username

    def get_profile_url(self):
        if self.domain is None:
            raise NotImplementedError("[KO] Domain not define in mother class")
        return f"{self.domain}{self.get_username()}/"

    def request(self, link=None) -> str:
        return get(link).text
