from synapse.social_network.base import SocialNetwork

class Twitter (SocialNetwork):
    def __init__(self, username):
        super().__init__(username)
        self.domain = "https://x.com/"


