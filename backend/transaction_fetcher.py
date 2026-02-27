import requests
import os
from dotenv import load_dotenv

load_dotenv()

ETHERSCAN_API_KEY = os.getenv("ETHERSCAN_API_KEY")

def get_wallet_transactions(address, page=1, offset=100):
    url = f"https://api.etherscan.io/v2/api"

    params = {
        "chainid": 1,  # Ethereum Mainnet
        "module": "account",
        "action": "txlist",
        "address": address,
        "page": page,
        "offset": offset,
        "sort": "desc",
        "apikey": ETHERSCAN_API_KEY
    }

    response = requests.get(url, params=params)
    data = response.json()

    print("Etherscan Response:", data)

    if data.get("status") == "1":
        return data.get("result", [])
    else:
        return []