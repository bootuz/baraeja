import os

from dotenv import load_dotenv

load_dotenv()

if os.getenv("LOCAL"):
    from .local import *
else:
    from .prod import *
