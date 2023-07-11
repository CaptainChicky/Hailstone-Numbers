import argparse
import os

# Function to process and run the chosen driver program
def process_driver(driver, version):
    driver_path = f"drivers/{driver}/{driver}-{version}.py"
    if os.path.exists(driver_path):
        print(f"Running {driver}-{version}...")
        os.system(f"python {driver_path}")
    else:
        print(f"Driver {driver}-{version} not found.")

# Create the argument parser
parser = argparse.ArgumentParser(description="Driver Program Runner")

# Add options for driver and version
parser.add_argument("driver", help="Choose the driver program")
parser.add_argument("version", help="Choose the version of the driver program")

# Parse the command-line arguments
args = parser.parse_args()

# Process the chosen driver program
process_driver(args.driver, args.version)
