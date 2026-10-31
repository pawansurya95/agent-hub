

def mask_secret(secret: str,visible: int = 4) -> str: 
      return "\n" + secret[:visible] + "..." + secret[-visible]