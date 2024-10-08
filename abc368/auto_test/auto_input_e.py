#!/usr/bin/env python3

import subprocess

# Definitions of file paths
INPUT_FILE = "../input_data/data_e.txt"
SCRIPT_NAME = "../scripts/e.py"


def load_input_patterns(file_name):
    """
    This function reads 2D list input data from a file
    """
    with open(file_name, "r") as file:
        content = file.read().strip()

    # Split patterns by blank lines and convert each pattern to a list of lines
    patterns = [pattern.splitlines() for pattern in content.split("\n\n")]
    return patterns


def run_with_auto_input(script_name, inputs):
    """
    This function runs a Python script with automatic input.
    """
    # Join the inputs with newlines
    input_data = "\n".join(inputs)

    # Run the script with the input piped to it
    process = subprocess.Popen(
        ["python3", script_name],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    stdout, stderr = process.communicate(input=input_data.encode())

    # Print the output from the script
    print(stdout.decode())
    if stderr:
        print(stderr.decode())


def main():
    # Load input patterns from the file
    input_patterns = load_input_patterns(INPUT_FILE)

    # Execute each input pattern sequentially
    for index, inputs in enumerate(input_patterns, start=1):
        print(f"\n--- Execution {index} ---")

        # Call the function to simulate input and run the script
        run_with_auto_input(SCRIPT_NAME, inputs)


if __name__ == "__main__":
    main()
