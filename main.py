import argparse
import sys
import subprocess
import os

# Function to process and run the chosen driver program
def process_driver(driver, version, plot=None, log=None, height=None):
    """Process and run the chosen driver program."""
    driver_path = f"driver/{driver}.py"
    if os.path.exists(driver_path):
        print(f"Running {driver}-{version}...")
        command = [sys.executable, driver_path, "-v", version]
        if plot is not None:
            command += ["-p", plot]
        if log is not None:
            command += ["-l", log]
        if height is not None:
            command += ["-ht", height]
        result = subprocess.run(command)
        if result.returncode != 0:
            print(f"Driver {driver}-{version} exited with code {result.returncode}.")
    else:
        print(f"Driver {driver}-{version} not found.")


parser = argparse.ArgumentParser(description="Driver Program Runner")

parser.add_argument("-d", "--driver", help="Choose the driver program", required=True)
parser.add_argument(
    "-v", "--version", help="Choose the version of the driver program", required=True
)
parser.add_argument("-p", "--plot", help="List of values for plotting", nargs="?")
parser.add_argument(
    "-l", "--log", help="Log axis scaling: 0=none, 1=y axis, 2=both", nargs="?"
)
parser.add_argument(
    "-ht",
    "--height",
    help="Specify the height of a graph (does not affect log graphs)",
    nargs="?",
)

args = parser.parse_args()

process_driver(args.driver, args.version, args.plot, args.log, args.height)
