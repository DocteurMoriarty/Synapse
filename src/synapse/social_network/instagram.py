from synapse.social_network.base import SocialNetwork
from bs4 import BeautifulSoup
import re

class Instagram(SocialNetwork):
    def __init__(self, username):
        super().__init__(username)
        self.domain = "https://www.instagram.com/"

    def parse_profile(self, html):
        soup = BeautifulSoup(html, "html.parser")

        user_id = username = profile_image = followers = following = posts = description = None

        script = soup.find("script", string=re.compile("profile_id"))
        if script:
            m_id = re.search(r'"profile_id"\s*:\s*"(\d+)"', script.string)
            m_user = re.search(r'"username"\s*:\s*"([^"]+)"', script.string)
            if m_id: user_id = m_id.group(1)
            if m_user: username = m_user.group(1)

        img_tag = soup.find("meta", property="og:image")
        if img_tag and img_tag.has_attr("content"):
            profile_image = img_tag["content"]

        desc_tag = soup.find("meta", {"name": "description"})
        if desc_tag and desc_tag.has_attr("content"):
            description = desc_tag["content"]
            clean_desc = re.sub(r'[\r\n\xa0]', ' ', description)
            match = re.search(
                r'([\d,\.]+[MK]?)\s*[Ff]ollowers?.*?([\d,\.]+)\s*[Ff]ollowing.*?([\d,\.]+)\s*[Pp]osts?',
                clean_desc
            )
            if match:
                followers, following, posts = match.groups()

        if not followers:
            for span in soup.find_all("span"):
                if span.text and "followers" in span.text.lower():
                    m = re.search(r'([\d,.]+)\s*[MK]?', span.text.replace("\xa0","").replace(" ",""))
                    if m:
                        followers = m.group(0)
                        break

        return {
            "id": user_id,
            "username": username,
            "profile_image": profile_image,
            "description": description,
            "followers": followers,
            "following": following,
            "posts": posts
        }
