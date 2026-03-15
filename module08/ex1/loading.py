import sys
import importlib
from typing import Any


def check_dependencies(
        core_p: list[Any], optional_p: list[Any]) -> None:
    missing_core: bool = False

    for pkg in core_p:
        try:
            mod = importlib.import_module(pkg)
            print(f"[OK] {pkg} ({mod.__version__}) - {pkg} ready")
        except ImportError:
            print(f"[KO] {pkg} is missing!")
            missing_core = True

    for pkg in optional_p:
        try:
            mod = importlib.import_module(pkg)
            print(f"[OK] {pkg} ({mod.__version__}) - optional ready")
        except ImportError:
            print(f"[KO] {pkg} is missing (optional)")

    if missing_core:
        print("\nCannot run analysis: some core packages are missing.\n")
        sys.exit(1)


def analyzing_data() -> None:
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt

    print("\nAnalyzing Matrix data...")
    data_points: int = 1000
    x = np.linspace(0, 10, data_points)
    y = np.sin(x) + np.random.normal(0, 0.1, data_points)
    df = pd.DataFrame({"Time": x, "Signal": y})
    print(f"Processing {data_points} data points...")

    print("Generating visualization...")
    plt.figure(figsize=(10, 5))
    plt.plot(df["Time"], df["Signal"], label="Matrix Signal")
    plt.title("Matrix Data Analysis")
    plt.xlabel("Time")
    plt.ylabel("Signal")
    plt.legend()
    plt.tight_layout()
    plt.savefig("matrix_analysis.png")
    plt.close()
    print("Analysis complete!\nResults saved to: matrix_analysis.png")


if __name__ == '__main__':
    print("\nLOADING STATUS: Loading programs...\n")
    print("Checking dependencies:")

    core_packages: list[str] = ["pandas", "numpy", "matplotlib"]
    optional_packages: list[str] = ["requests"]

    check_dependencies(core_packages, optional_packages)

    analyzing_data()

    print("\nInstalled package versions:")
    for pkg in core_packages + optional_packages:
        try:
            mod = importlib.import_module(pkg)
            print(f"{pkg}: {mod.__version__}")
        except ImportError:
            print(f"{pkg}: Not installed")
