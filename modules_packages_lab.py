# modules_packages_lab.py
import os # Provides a way of using operating system dependent functionality
import sys # Provides access to system-specific parameters and functions

print("--- OS Module Examples ---")
# Get the current working directory
current_dir = os.getcwd()
print(f"Current working directory: {current_dir}")

# List contents of the current directory
print("Files and directories in current path:")
for item in os.listdir(current_dir):
    print(f"  - {item}")

# Check if a file exists
if os.path.exists("modules_packages_lab.py"):
    print("\n'modules_packages_lab.py' exists in this directory.")
else:
    print("\n'modules_packages_lab.py' does NOT exist in this directory.")

print("\n--- Sys Module Examples ---")
# Get Python version
print(f"Python version: {sys.version.split()}") # Just the version number

# Get the operating system platform
print(f"Operating System Platform: {sys.platform}")

# Get the Python executable path
print(f"Python Executable Path: {sys.executable}")