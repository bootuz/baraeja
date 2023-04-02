import os

from dotenv import load_dotenv

load_dotenv()

if os.getenv("IS_PULL_REQUEST") == "true":
    print("staging")
    from .staging import *
elif os.getenv("IS_PULL_REQUEST") == "false":
    print("prod")
    from .prod import *
else:
    from .local import *
