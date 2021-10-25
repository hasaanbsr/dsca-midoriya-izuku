import random

def generate_password(n_token=3):
    """Generate password from words.txt

    Args:
        n_token (int): number of token to be included
            in password. Default is 3.

    Returns:
        str: password
    """
    with open("words.txt", "r") as f:
        word_list = f.read().split("\n")

    tokens = random.sample(word_list, k=n_token)
    return "".join(tokens)