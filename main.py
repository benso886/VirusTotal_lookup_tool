import os
import truststore
import requests

truststore.inject_into_ssl()

def validate_hash(hash_value):

    if len(hash_value) not in (32, 40, 64):
        return False

    allowed_characters = "0123456789abcdef"

    for character in hash_value.lower():
        if character not in allowed_characters:
            return False

    return True

api_key = os.environ["VT_API_KEY"]

while True:
    hash_value = input("Enter a file hash (or type 'exit'): ").strip()

    if hash_value.lower() == "exit":
        break

    if not validate_hash(hash_value):
        print("Invalid hash format.")
        continue

    url = f"https://www.virustotal.com/api/v3/files/{hash_value}"

    headers = {
        "x-apikey": api_key
    }

    response = requests.get(url, headers=headers, timeout=15)

    data = response.json()

    stats = data["data"]["attributes"]["last_analysis_stats"]

    malicious = stats["malicious"]
    total = sum(stats.values())

    if len(hash_value) == 32:
        hash_type = "MD5"
    elif len(hash_value) == 40:
        hash_type = "SHA-1"
    else:
        hash_type = "SHA-256"

    vt_link = f"https://www.virustotal.com/gui/file/{hash_value}"

    print(f"Hash type: {hash_type}")
    print(f"VirusTotal detection: {malicious} / {total}")
    print(f"VirusTotal report: {vt_link}")