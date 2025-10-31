from social_network.instagram import Instagram
from social_network.twitter import Twitter
from social_network.pinterest import Pinterest

class Builder:
    def __init__(self, username):
        self.networks = [
            Twitter(username),
            Instagram(username),
            Pinterest(username)
        ]

    def get_networks(self):
        return self.networks

    def all_network(self):
        for network in self.get_networks():
            print(network.request(network.get_profile_url()))