"""
Purpose
Shared utilities for backtesting.

Good things to include:
Parsing PnL from logs
Aggregating results
Comparing runs

Why useful
You’ll quickly want:
“Which version is better?”
“What’s my avg PnL?”

"""
import os
from datetime import datetime

def get_new_run_name(base_dir="outputs/monte_carlo"):
    today = datetime.now().strftime("%Y-%m-%d")
    
    # ensure directory exists
    os.makedirs(base_dir, exist_ok=True)

    # find existing runs today
    existing = [
        d for d in os.listdir(base_dir)
        if d.startswith(f"run_{today}")
    ]

    # extract version numbers
    versions = []
    for name in existing:
        try:
            v = int(name.split("_v")[-1])
            versions.append(v)
        except:
            continue

    next_version = max(versions, default=0) + 1

    return f"run_{today}_v{next_version}"
