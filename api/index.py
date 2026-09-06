import os
import sys

# Add project root to sys.path so app.py is accessible
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app
