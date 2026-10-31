from agent_hub.config import mask_secret

def main() -> None:
    print("Hello from agent-hub!")
    secret = "gsk_1234567890abcdef"
    masked_secret = mask_secret(secret)
    print(masked_secret)
