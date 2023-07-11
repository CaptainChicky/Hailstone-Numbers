import argparse
import os

# Function to process and run the chosen driver program
def process_driver(driver, version, plotlist=None):
    driver_path = f'driver/{driver}/{driver}-{version}.py'
    if os.path.exists(driver_path):
        print(f'Running {driver}-{version}...')
        if plotlist is None:
            os.system(f'python {driver_path}')
        else:
            os.system(f'python {driver_path} -p "{plotlist}"')
    else:
        print(f'Driver {driver}-{version} not found.')

# Create the argument parser
parser = argparse.ArgumentParser(description="Driver Program Runner")

# Add options for driver and version
parser.add_argument("-d", "--driver", help="Choose the driver program", required=True)
parser.add_argument("-v", "--version", help="Choose the version of the driver program", required=True)
# Add an optional option for the plotlist argument
parser.add_argument('-p', '--plotlist', help='List of values for plotting', nargs='?')


# Parse the command-line arguments
args = parser.parse_args()

# Process the chosen driver program
process_driver(args.driver, args.version, args.plotlist)