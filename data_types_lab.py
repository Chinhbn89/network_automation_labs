# Integer
vlan_id = 100
print(f"VLAN ID: {vlan_id}, Type: {type(vlan_id)}")

# Float
temperature = 25.7
print(f"Temperature: {temperature}, Type: {type(temperature)}")

# String
device_hostname = "CoreRouter-NYC"
print(f"Device Hostname: {device_hostname}, Type: {type(device_hostname)}")

# Boolean
is_up = True
print(f"Is Device Up?: {is_up}, Type: {type(is_up)}")

# List of interfaces
interfaces = ["GigabitEthernet0/1", "Loopback0", "Vlan10"]
print(f"Interfaces: {interfaces}, Type: {type(interfaces)}")
print(f"First interface in list: {interfaces}") # Accessing an item
interfaces.append("TenGigabitEthernet1/1") # Add a new item
print(f"Interfaces after append: {interfaces}")


# Tuple of IP and subnet mask
ip_subnet = ("192.168.1.1", "255.255.255.0")
print(f"IP/Subnet: {ip_subnet}, Type: {type(ip_subnet)}")
print(f"IP from tuple: {ip_subnet}") # Accessing an item


# Dictionary for device details
device_details = {
    "name": "EdgeSwitch-LA",
    "ip": "10.0.0.5",
    "vendor": "Cisco",
    "ports": 48
}
print(f"Device Details: {device_details}, Type: {type(device_details)}")
print(f"Device vendor from dictionary: {device_details['vendor']}") # Accessing by key
device_details["location"] = "Los Angeles" # Add a new key-value pair
print(f"Device details after adding location: {device_details}")
#////////////////////////////////////////////////////////////////////////////////
# Arithmetic Operators
print("\n--- Arithmetic Operations ---")
num_ports = 24
expansion_modules = 2
total_ports = num_ports + (expansion_modules * 8) # Assuming 8 ports per module
print(f"Total ports: {total_ports}")

uptime_minutes = 150
uptime_hours = uptime_minutes / 60
print(f"Uptime in hours: {uptime_hours:.2f}") # Format to 2 decimal places

# Comparison Operators
print("\n--- Comparison Operations ---")
current_temp = 75
threshold_temp = 80
is_over_threshold = current_temp > threshold_temp
print(f"Is current temp over threshold ({threshold_temp})?: {is_over_threshold}")

device_status = "active"
required_status = "active"
is_status_match = (device_status == required_status)
print(f"Does device status match required status?: {is_status_match}")

# Logical Operators
print("\n--- Logical Operations ---")
has_credentials = True
is_reachable = False
can_login = has_credentials and is_reachable # Both must be True
print(f"Can login to device?: {can_login}")

is_primary = False
is_backup = True
is_redundant = is_primary or is_backup # At least one must be True
print(f"Is device redundant?: {is_redundant}")

is_maintenance_mode = False
should_process = not is_maintenance_mode # Reverses the boolean
print(f"Should process device (not in maintenance)?: {should_process}")