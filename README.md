## ⚠️ Warning

This is just a toy project.

Anyone who has access to the FIFO pipe can post to your Bluesky account.

Seriously - don’t use this unless you’re okay with that.

# About
This script allows you to create device-like file in /dev/bluesky, so you can
pipe your thoughts `echo "My thoughts" > /dev/bluesky` straight into your feed.

# Initialization

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
```


Create .env file.

```bash
(umask 077; touch .env)
```

It should have following format:

```
BLUESKY_HANDLE=your.handle.bsky.social
BLUESKY_PASSWORD=your-app-password
FIFO_PATH=/tmp/bluesky
```

Then add symbolic link, so it can feel like real /dev/ pseudodevice.

```bash
sudo ln -sf /tmp/bluesky /dev/bluesky
```

# Running

```bash
./scripts/run.sh
```

Now you can post on Bluesky without ever leaving terminal

```bash
echo "I'm thinking about..." > /dev/bluesky 
```
