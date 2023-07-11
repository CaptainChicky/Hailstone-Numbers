import argparse
import time
import os

# Function to process and run the chosen driver program
def process_driver(driver, version, plot=None, log=None, height=None):
    driver_path = f'driver/{driver}/{driver}-{version}.py'
    if os.path.exists(driver_path):
        print(f'Running {driver}-{version}...')
        command = f'python {driver_path}'
        if plot is not None:
            command += f' -p "{plot}"'
        if log is not None:
            command += f' -l {log}'
        if height is not None:
            command += f' -ht {height}'
        os.system(command)
    else:
        print(f'Driver {driver}-{version} not found.')

# Create the argument parser
parser = argparse.ArgumentParser(description="Driver Program Runner")

# Add options for driver and version
parser.add_argument("-d", "--driver", help="Choose the driver program", required=True)
parser.add_argument("-v", "--version", help="Choose the version of the driver program", required=True)
# Add an optional option for the plot argument
parser.add_argument('-p', '--plot', help='List of values for plotting', nargs='?')
parser.add_argument('-l', '--log', help='Log axis scaling, 0 for non, 1 for y axis, 2 for both', nargs='?')
parser.add_argument('-ht', '--height', help='Specify the height of a graph (does not affect log graphs)', nargs='?')


# Parse the command-line arguments
args = parser.parse_args()

# Process the chosen driver program
process_driver(args.driver, args.version, args.plot, args.log, args.height)

# Add the infinite loop to keep the script running
while True:
    time.sleep(1)  # Keep the script running indefinitely