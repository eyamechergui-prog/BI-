
import logging
import sqlite3
from pathlib import Path

import pandas as pd

# Configuration des chemins
CLEAN = Path("data/clean")
MARTS = Path("data/marts")
DB = Path("data/retail.db")

# Configuration du logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

log = logging.getLogger(__name__)