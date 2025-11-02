from synapse.social_network.builder import Builder, Instagram

def main():
    build = Builder("")
    results = build.all_network()
    for result in results:
        print(f"=== {result.get('network', 'Unknown')} ===")
        print(f"Username   : {result.get('username')}")
        print(f"User ID    : {result.get('id')}")
        print(f"Followers  : {result.get('followers')}")
        print(f"Following  : {result.get('following')}")
        print(f"Posts      : {result.get('posts')}")
        print(f"Profile Img: {result.get('profile_image')}")
        print(f"Description: {result.get('description')}\n")

if __name__ == "__main__":
    main()