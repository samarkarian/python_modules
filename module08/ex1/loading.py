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
    array_x = np.array([x for x in range(0, 1000)])
    array_y = np.array([y for y in range(0, 1000)])
    print("Processing 1000 data points...")

    x = pd.Series(array_x)
    y = pd.Series(array_y)

    plt.plot(x, y)
    plt.savefig("matrix_analysis.png")
    print("Generating visualization...")

    print("\nAnalysis complete!")
    print("Results saved to: matrix_analysis.png")


if __name__ == '__main__':

    print("\nLOADING STATUS: Loading programs...\n")
    print("Checking dependencies:")

    core_packages: list[str] = ["pandas", "numpy", "matplotlib"]
    optional_packages: list[str] = ["requests"]

    check_dependencies(core_packages, optional_packages)

    analyzing_data()
