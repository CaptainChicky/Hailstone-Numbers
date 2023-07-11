import subprocess

ShouldProgramExit = False

while not ShouldProgramExit:
    print("Welcome!")
    print("Choose which program you want to run:")
    print("1. One Hailstone")
    print("2. Multiple Hailstones")
    print("3. Hailstone Lengths")
    print("4. Hailstone Max Height")
    
    # Get the user's input
    user_input = input("Enter your choice: ")

    # Check if the user wants to exit
    if user_input == "4":
        ShouldProgramExit = True
        break

    # Check if the user entered a valid choice
    if user_input not in ["1", "2", "3"]:
        print("Invalid choice!")
        continue


    # Specify the path to the Python file you want to run
    file_path = "/path/to/your/python/file.py"

    # Run the Python file using subprocess
    subprocess.run(["python", file_path])
