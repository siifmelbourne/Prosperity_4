# NOT WORKING YET
import os
import pathlib
import subprocess
from utils import get_new_run_name


ROOT = pathlib.Path(__file__).resolve().parent

MC_ENTRY = (
    ROOT
    / "external"
    / "monte_carlo"
    / "imc-prosperity-4"
    / "backtester"
    / "prosperity4mcbt"
    / "main.py"
)

VENV_PY = (
    ROOT
    / "backtester"
    / ".venv"
    / "Scripts"
    / "python.exe"
)


def run(mode="quick"):
    base_dir = "outputs/monte_carlo"
    run_name = get_new_run_name(base_dir)

    run_path = os.path.join(base_dir, run_name)
    os.makedirs(run_path, exist_ok=True)

    output_file = os.path.join(run_path, "dashboard.json")

    print(f"Running Monte Carlo: {run_name}")
    print(f"Mode: {mode}")

    cmd = [
        str(VENV_PY),          # 👈 uses venv directly (no activation needed)
        str(MC_ENTRY),
        "src/trader.py"
    ]

    if mode == "quick":
        cmd.append("--quick")
    elif mode == "heavy":
        cmd.append("--heavy")

    cmd += ["--out", output_file]

    subprocess.run(cmd, check=True)

    print(f"Saved to: {run_path}")


if __name__ == "__main__":
    run()
