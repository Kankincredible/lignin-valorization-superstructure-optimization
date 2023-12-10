import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def main():
    try:
        # List of packages to install
        packages = [
            "numpy",
            "numpy-financial",
            "pandas",
            "pyomo"
        ]

        for package in packages:
            print(f"Installing {package}...")
            install(package)
        print("All packages installed successfully.")

    except subprocess.CalledProcessError as e:
        print(f"An error occurred while installing packages: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
