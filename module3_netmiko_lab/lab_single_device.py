# lab_single_device.py
from devices import single_device # Import the single device dictionary
from netmiko_operations import get_device_info, apply_config_commands, backup_running_config # Import the function to get device info

print("--- Lab 1.2: Connect to a Single Device ---")

# We call get_device_info with a simple command to test connectivity
# The function handles the connection and disconnection internally.
output = get_device_info(single_device, command="show clock")

print("\n--- Connection Test Result ---")
print(output)
print("\nLab 1.2 complete.")