from web3 import Web3
import os
from dotenv import load_dotenv

load_dotenv()

RPC_URL = os.getenv("ETH_RPC_URL")

w3 = Web3(Web3.HTTPProvider(RPC_URL))

def is_connected():
    return w3.is_connected()