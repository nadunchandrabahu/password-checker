import requests
import hashlib


def request_api_data(query_char):
    url = "https://api.pwnedpasswords.com/range/" + query_char
    res = requests.get(url)

    if res.status_code != 200:
        raise RuntimeError(
            f"Error fetching {res.status_code}, check API and try again.")
    return res


def get_password_leaks(hashes, hash_to_check):
    list_of_lines = hashes.text.splitlines()
    flag_found = False
    for line in list_of_lines:
        hash_per_line, count_per_line = line.split(
            ":")[0], int(line.split(":")[1])
        if hash_per_line == hash_to_check:
            flag_found = True
            print(f"Your password has been hacked {count_per_line} times.")
    if flag_found == False:
        print("Congrats, your password has not been hacked!")


def pwned_api_check(password):
    sha1password = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    first5_hash, tail_hash = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_hash)
    return get_password_leaks(response, tail_hash)


password_to_check = input(
    "Please enter the password you would like to check if it has been hacked: \n")

pwned_api_check(str(password_to_check))
