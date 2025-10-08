# net_libs_conceptual_lab.py
# import ConnectHandler # We're just showing the concept, not running real code here

print("--- Conceptual Netmiko Usage ---")

# Imagine this is your device's information
device_info = {
    "device_type": "cisco_ios",
    "host": "192.168.1.10",
    "username": "admin",
    "password": "cisco",
    "secret": "enable_pass"
}

print(f"Netmiko would connect to {device_info['host']} via SSH.")
print("It would then send commands like 'show version' or 'configure terminal'.")
print("Example: net_connect = ConnectHandler(**device_info)")
print("         output = net_connect.send_command('show ip interface brief')")
print("         net_connect.send_config_set(['hostname NEW_ROUTER', 'no logging console'])")
print("\n(Note: This is conceptual. Running this requires a real, reachable device.)")


# ... (previous code) ...
# import get_network_driver # We're just showing the concept, not running real code here

print("\n--- Conceptual NAPALM Usage ---")

# NAPALM provides a unified way to get data and configure different vendors
print("NAPALM abstracts away vendor differences.")
print("You'd specify a driver (e.g., 'ios', 'junos').")
print("Example: driver = get_network_driver('ios')")
print("         device = driver(hostname='192.168.1.10', username='admin', password='cisco')")
print("         device.open()")
print("         facts = device.get_facts()")
print("         device.load_merge_candidate(filename='new_config.txt')")
print("         device.commit_config()")
print("\n(Note: This is conceptual. Running this requires a real, reachable device.)")