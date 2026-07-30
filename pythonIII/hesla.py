import secrets
import string
 
def generate_password(length):
    """Generate a secure random password."""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password


for x in range(10):
    print(generate_password(10))