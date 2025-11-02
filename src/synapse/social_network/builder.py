from social_network.instagram import Instagram
from social_network.twitter import Twitter
from social_network.pinterest import Pinterest

class Builder:
    def __init__(self, username):
        self.networks = [
            # Twitter(username),
            Instagram(username),
            Pinterest(username)
        ]
        
    def get_networks(self):
        return self.networks

    def all_network(self):
        results = []
        for network in self.get_networks():
            html = network.request(network.get_profile_url())
            if not html:
                results.append({
                    "network": network.__class__.__name__,
                    "error": "Empty response or request failed"
                })
                continue

            parsed = network.parse_profile(html)
            parsed["network"] = network.__class__.__name__
            results.append(parsed)
        return results