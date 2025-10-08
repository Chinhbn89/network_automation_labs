# lab_single_device.py
from devices import single_device # Import the single device dictionary
from netmiko_operations import get_device_info, apply_config_commands, backup_running_config # Import the function to get device info

print("--- Lab 1.2: Connect to a Single Device ---")

# We call get_device_info with a simple command to test connectivity
# The function handles the connection and disconnection internally.
output = get_device_info(single_device, command="show running-config interface loopback 100")

print("\n--- Connection Test Result ---")
print(output)

print("\n--- Lab 2.1: Push Configuration Changes ---")

config_commands = [
    "interface Loopback100",
    "description CONFIGURED_BY_NETMIKO_LAB",
    "ip address 10.0.0.100 255.255.255.255",
    "no shutdown",
    "router ospf 1",
    "network 10.0.0.0 0.0.0.255 area 0"
]

print("\nApplying configuration commands...")
config_output = apply_config_commands(single_device, config_commands)
print("\n--- Configuration Output ---")
print(config_output)

output = get_device_info(single_device, command="show run interface loo100")
print("\n--- Result after change config ---")
print(output)

print("\nLab 2.1 complete.")