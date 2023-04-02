import os

from dotenv import load_dotenv

load_dotenv()

if "RENDER" in os.environ:
    from .prod import *
else:
    from .local import *
