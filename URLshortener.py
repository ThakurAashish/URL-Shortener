# url_shortener.py
# Simple URL Shortener using hashing (no database)

import hashlib

url_mapping = {}
BASE_URL = "http://short.ly/"


def shorten_url(long_url):
    hash_object = hashlib.md5(long_url.encode())
    short_key = hash_object.hexdigest()[:6]
    short_url = BASE_URL + short_key
    url_mapping[short_key] = long_url
    return short_url


def expand_url(short_url):
    short_key = short_url.replace(BASE_URL, "")
    return url_mapping.get(short_key, "URL not found")


def main():
    while True:
        print("\nPython URL Shortener")
        print("1. Shorten URL")
        print("2. Expand URL")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            long_url = input("Enter long URL: ")
            print("Short URL:", shorten_url(long_url))

        elif choice == "2":
            short_url = input("Enter short URL: ")
            print("Original URL:", expand_url(short_url))

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()