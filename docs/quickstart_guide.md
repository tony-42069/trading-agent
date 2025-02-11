# :rocket: Quickstart Guide

## Prerequisites
- Python 3.9+
- Screen or Tmux
- BSC Node URL
- Telegram Bot Token

## Installation Steps
1. Clone repository:
```bash
git clone <repo-url>
cd trading-agent
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure environment:
```bash
cp .env.example .env
# Edit .env with your keys
```

4. Basic configuration:
```python
# config.py
MIN_LIQUIDITY = 5  # BNB
MAX_BUY_TAX = 10  # 10%
MAX_SELL_TAX = 10  # 10%
```

## Running the Bot
1. Start in screen:
```bash
screen -S tradingbot
python run.py
# Ctrl+A+D to detach
```

2. Monitor logs:
```bash
tail -f bot.log
```

## Verification
1. Send `/start` to your bot
2. Check for "Bot Online" message
3. Wait for first pair detection

## Common Issues
1. Node connection:
   - Check node URL
   - Verify network status

2. Missing events:
   - Check scanner.py logs
   - Verify event filter

3. No alerts:
   - Check Telegram token
   - Verify alert thresholds