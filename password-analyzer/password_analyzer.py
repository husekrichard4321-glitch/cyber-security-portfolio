import math
import string
from pathlib import Path

# established paths
BASE_DIR = Path(__file__).resolve().parent
COMMON_PWDS_PATH = BASE_DIR / "common_passwords.txt"

# password checker


def analyze_password():

    password = input("enter password: ")
    length = len(password)

    has_lower = any(char.islower() for char in password)
    has_upper = any(char.isupper() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in string.punctuation for char in password)

    # power of each character
    pool_size = 0

    if has_lower:
        pool_size += 26
    if has_upper:
        pool_size += 26
    if has_digit:
        pool_size += 10
    if has_special:
        pool_size += 32

    # password strength calculation
    entropy = 0

    if pool_size > 0:
        entropy = length * math.log2(pool_size)
    else:
        entropy = 0
    print(f"entropy: {entropy:.2f} bits")

    # checking common passwords
    is_common = False
    with open(COMMON_PWDS_PATH, "r") as file:
        common_passwords = [line.strip() for line in file.readlines()]
        if password in common_passwords:
            is_common = True

    # password strength evaluation
    rating = ""

    if is_common or entropy < 40:
        rating = "weak"
        recommendation = "use a longer password and avoid common words."

    elif entropy < 60:
        rating = "medium"
        recommendation = "add more special characters and numbers."

    else:
        rating = "strong"
        recommendation = "excellent password."

    # result listing
    print(f"rating: {rating}")
    print(f"recommendation: {recommendation}")


if __name__ == "__main__":
    analyze_password()
