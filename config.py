"""
Configuration settings for the trading bot.
Load environment variables and define constants.
"""
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Blockchain Configuration
BSC_NODE_URL = os.getenv('BSC_NODE_URL', 'https://bsc-dataseed.binance.org/')
FACTORY_ADDRESS = '0xcA143Ce32Fe78f1f7019d7d551a6402fC5350c73'  # PancakeSwap V2 Factory
ROUTER_ADDRESS = '0x10ED43C718714eb63d5aA57B78B54704E256024E'  # PancakeSwap V2 Router
WBNB_ADDRESS = '0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c'  # Wrapped BNB

# Telegram Configuration
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')

# Analysis Settings
MIN_LIQUIDITY_BNB = float(os.getenv('MIN_LIQUIDITY_BNB', 5))
MAX_BUY_TAX = float(os.getenv('MAX_BUY_TAX', 10))
MAX_SELL_TAX = float(os.getenv('MAX_SELL_TAX', 10))

# Security Thresholds
MAX_OWNER_PERCENTAGE = 50  # Maximum percentage of supply owned by contract owner
MIN_LP_LOCKED_DAYS = 30   # Minimum days LP tokens should be locked
MAX_MINT_LIMIT = 5        # Maximum supply increase allowed (%)

# Scanning Configuration
BLOCKS_PER_SCAN = 50      # Number of blocks to scan at once
SCAN_INTERVAL = 3         # Seconds between each scan
MAX_RETRIES = 3          # Maximum retries for failed requests

# Logging Configuration
LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
LOG_FILE = os.getenv('LOG_FILE', 'bot.log')

# Development Settings
DEBUG = os.getenv('DEBUG', 'False').lower() == 'true'

# Alert Templates
ALERT_TEMPLATES = {
    'new_token': """
🚨 New Token Detected 🚨

Token: {name} ({symbol})
Address: {address}
Initial Liquidity: {liquidity} BNB
Market Cap: ${market_cap}

Security Checks:
✅ Contract Verified
✅ Liquidity Locked
✅ Ownership Renounced
⚠️ Buy Tax: {buy_tax}%
⚠️ Sell Tax: {sell_tax}%

Chart: https://poocoin.app/tokens/{address}
""",
    'error': """
❌ Error Alert ❌

Type: {error_type}
Details: {error_message}

Time: {timestamp}
""",
}

# Contract ABIs
FACTORY_ABI = [
    {
        "anonymous": False,
        "inputs": [
            {"indexed": True, "type": "address", "name": "token0"},
            {"indexed": True, "type": "address", "name": "token1"},
            {"indexed": False, "type": "address", "name": "pair"},
            {"indexed": False, "type": "uint256", "name": ""}
        ],
        "name": "PairCreated",
        "type": "event"
    }
]

PAIR_ABI = [
    {"inputs": [], "name": "token0", "outputs": [{"type": "address", "name": ""}], "type": "function"},
    {"inputs": [], "name": "token1", "outputs": [{"type": "address", "name": ""}], "type": "function"},
    {"inputs": [], "name": "getReserves", "outputs": [
        {"type": "uint112", "name": "_reserve0"},
        {"type": "uint112", "name": "_reserve1"},
        {"type": "uint32", "name": "_blockTimestampLast"}
    ], "type": "function"}
]

TOKEN_ABI = [
    {"inputs": [], "name": "name", "outputs": [{"type": "string", "name": ""}], "type": "function"},
    {"inputs": [], "name": "symbol", "outputs": [{"type": "string", "name": ""}], "type": "function"},
    {"inputs": [], "name": "decimals", "outputs": [{"type": "uint8", "name": ""}], "type": "function"},
    {"inputs": [], "name": "totalSupply", "outputs": [{"type": "uint256", "name": ""}], "type": "function"},
    {"inputs": [{"type": "address", "name": "account"}], "name": "balanceOf", "outputs": [{"type": "uint256", "name": ""}], "type": "function"}
]
