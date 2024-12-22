import random
import string
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization, hashes

# Step 1: Generate OTP
def generate_otp():
    capital_letters = random.choices(string.ascii_uppercase, k=2)
    special_characters = random.choices("!@#$%^&*()-_=+<>?", k=2)
    other_characters = random.choices(string.ascii_lowercase + string.digits, k=2)
    otp = capital_letters + special_characters + other_characters
    random.shuffle(otp)
    return ''.join(otp)

# Step 2: Generate RSA Key Pair
def generate_key_pair():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )
    public_key = private_key.public_key()
    return private_key, public_key

# Step 3: Encrypt OTP
def encrypt_otp(otp, public_key):
    encrypted_otp = public_key.encrypt(
        otp.encode(),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return encrypted_otp

# Step 4: Decrypt OTP
def decrypt_otp(encrypted_otp, private_key):
    decrypted_otp = private_key.decrypt(
        encrypted_otp,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return decrypted_otp.decode()

# Example Usage
if __name__ == "__main__":
    # Generate OTP
    otp = generate_otp()
    print(f"Generated OTP: {otp}")

    # Generate RSA Key Pair
    private_key, public_key = generate_key_pair()

    # Encrypt OTP
    encrypted_otp = encrypt_otp(otp, public_key)
    print(f"Encrypted OTP: {encrypted_otp}")

    # Decrypt OTP
    decrypted_otp = decrypt_otp(encrypted_otp, private_key)
    print(f"Decrypted OTP: {decrypted_otp}")
