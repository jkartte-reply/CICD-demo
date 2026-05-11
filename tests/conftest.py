import sys
from pathlib import Path

# Add the root directory to Python path so tests can import main
sys.path.insert(0, str(Path(__file__).parent.parent))
