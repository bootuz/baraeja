import os

from dotenv import load_dotenv

load_dotenv()

if "RENDER" in os.environ:
    from .prod import *
elif "GITHUB" in os.environ:
    from .github import *
else:
    from .dev import *
