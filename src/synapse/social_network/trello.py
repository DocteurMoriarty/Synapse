from synapse.social_network.base import SocialNetwork

class Trello(SocialNetwork):
    def __init__(self, username):
        super().__init__(username)
        self.domain = "https://trello.com/"

    