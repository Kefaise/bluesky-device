import os
import sys
import time
from atproto import Client
from dotenv import load_dotenv

def ensure_fifo(path: str):
    if not os.path.exists(path):
        os.mkfifo(path)

def connect():
    handle = os.getenv("BLUESKY_HANDLE")
    password = os.getenv("BLUESKY_PASSWORD")

    if not handle or not password:
        print("Missing credentials in .env", file=sys.stderr)
        sys.exit(1)

    client = Client()
    client.login(handle, password)
    return client

def main():
    load_dotenv()

    fifo_path = os.getenv("FIFO_PATH", "/tmp/bluesky")
    ensure_fifo(fifo_path)

    client = connect()

    print(f"[bluesky-dev] Listening on {fifo_path}")

    while True:
        try:
            with open(fifo_path, "r") as fifo:
                for line in fifo:
                    text = line.strip()
                    if not text:
                        continue

                    print(f"[post] {text}")
                    try:
                        client.send_post(text)
                    except Exception as e:
                        print(f"[error] failed to post: {e}", file=sys.stderr)

        except Exception as e:
            print(f"[error] fifo read failed: {e}", file=sys.stderr)
            time.sleep(1)

