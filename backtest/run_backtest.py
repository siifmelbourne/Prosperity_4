import os
from utils import get_new_run_name
import sys

def run(round_id="0"):

    if len(sys.argv) < 2:
        print("Usage: python run_backtest.py <trader_path> <round_id>")
        sys.exit(1)

    trader_path = sys.argv[1]

    base_dir = "outputs/backtests"
    run_name = get_new_run_name(base_dir)

    run_path = os.path.join(base_dir, run_name)
    os.makedirs(run_path, exist_ok=True)

    output_file = os.path.join(run_path, "output.log")

    print(f"Running Backtest: {run_name}")

    cmd = (
        f"py external\\replay_backtester\\imc-prosperity-4-backtester\\"
        f"prosperity4bt\\__main__.py {trader_path} {round_id}"
        f" --out {output_file}"
    )

    os.system(cmd)

    print(f"Saved to: {run_path}")


if __name__ == "__main__":
    run()
