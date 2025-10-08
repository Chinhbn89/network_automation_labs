import json
import yaml
import xmltodict
print("--- Working with JSON ---")

# 1. Python Dictionary (our data)
device_inventory = {
    "device_id": "R1-Core",
    "ip_address": "10.0.0.1",
    "vendor": "Cisco",
    "model": "ISR4431",
    "interfaces": [
        {"name": "GigabitEthernet0/0/0", "status": "up", "ip": "10.0.0.1"},
        {"name": "GigabitEthernet0/0/1", "status": "down", "ip": "unassigned"}
    ],
    "credentials": {"username": "admin", "password": "cisco"}
}

# 2. Convert Python Dictionary to JSON String (Serialization)
json_output_string = json.dumps(device_inventory, indent=4) # indent for pretty-print
print("\nPython Dictionary converted to JSON String:")
print(json_output_string)
print(f"Type of json_output_string: {type(json_output_string)}")

# 3. Convert JSON String to Python Dictionary (Deserialization)
json_input_string = '{"switch_name": "SW1", "vlans": 100, "ports": ["Fa0/1", "Fa0/2"]}'
python_dict_from_json = json.loads(json_input_string)
print("\nJSON String converted to Python Dictionary:")
print(python_dict_from_json)
print(f"Type of python_dict_from_json: {type(python_dict_from_json)}")
print(f"Switch Name: {python_dict_from_json['switch_name']}, VLANs: {python_dict_from_json['vlans']}")

# 4. Write Python Dictionary to a JSON File
output_filename_json = "device_inventory.json"
with open(output_filename_json, "w") as f:
    json.dump(device_inventory, f, indent=4)
print(f"\nPython dictionary saved to {output_filename_json}")

# 5. Read JSON File to Python Dictionary
with open(output_filename_json, "r") as f:
    loaded_json_data = json.load(f)
print(f"\nData loaded from {output_filename_json}:")
print(loaded_json_data)
print(f"Loaded device ID: {loaded_json_data['device_id']}")


print('------------------------------------------------------------')

print("\n--- Working with YAML ---")

# 1. Python Dictionary (our data)
network_topology = {
    "site": "Headquarters",
    "routers": [
        {"name": "R1", "ip": "192.168.1.1", "os": "IOS-XE"},
        {"name": "R2", "ip": "192.168.1.2", "os": "IOS-XR"}
    ],
    "switches": [
        {"name": "SW1", "ip": "192.168.1.10", "model": "Catalyst 9300"}
    ],
    "firewall": {"name": "FW1", "ip": "192.168.1.20"}
}

# 2. Convert Python Dictionary to YAML String
yaml_output_string = yaml.dump(network_topology, sort_keys=False, default_flow_style=False)
print("\nPython Dictionary converted to YAML String:")
print(yaml_output_string)
print(f"Type of yaml_output_string: {type(yaml_output_string)}")

# 3. Convert YAML String to Python Dictionary
yaml_input_string = """
device_name: AccessSwitch
ports:
    - Gi0/1
    - Gi0/2
vlan_access: 10
"""
python_dict_from_yaml = yaml.safe_load(yaml_input_string)
print("\nYAML String converted to Python Dictionary:")
print(python_dict_from_yaml)
print(f"Type of python_dict_from_yaml: {type(python_dict_from_yaml)}")
print(f"Device Name: {python_dict_from_yaml['device_name']}, Ports: {python_dict_from_yaml['ports']}")

# 4. Write Python Dictionary to a YAML File
output_filename_yaml = "network_topology.yaml"
with open(output_filename_yaml, "w") as f:
    yaml.dump(network_topology, f, sort_keys=False, default_flow_style=False)
print(f"\nPython dictionary saved to {output_filename_yaml}")

# 5. Read YAML File to Python Dictionary
with open(output_filename_yaml, "r") as f:
    loaded_yaml_data = yaml.safe_load(f)
print(f"\nData loaded from {output_filename_yaml}:")
print(loaded_yaml_data)
print(f"Loaded site: {loaded_yaml_data['site']}")

print('--------------------------------------------------------------------------')

print("\n--- Working with XML (using xmltodict) ---")

# 1. XML String (simulating data from a device or old API)
xml_input_string = """
<device_status>
    <hostname>LabRouter</hostname>
    <uptime_days>150</uptime_days>
    <interfaces>
        <interface>
            <name>GigabitEthernet0/0</name>
            <state>up</state>
            <ip_address>192.168.1.1</ip_address>
        </interface>
        <interface>
            <name>Loopback0</name>
            <state>up</state>
            <ip_address>1.1.1.1</ip_address>
        </interface>
    </interfaces>
    <cpu_utilization>25</cpu_utilization>
</device_status>
"""

# 2. Convert XML String to Python Dictionary
# force_list=('interface',) ensures 'interface' is always a list, even if only one exists.
# This makes iterating over interfaces safer.
python_dict_from_xml = xmltodict.parse(xml_input_string, force_list=('interface',))
print("\nXML String converted to Python Dictionary:")
print(json.dumps(python_dict_from_xml, indent=4)) # Pretty-print the dict
print(f"Type of python_dict_from_xml: {type(python_dict_from_xml)}")

# Accessing data from the converted dictionary
hostname = python_dict_from_xml['device_status']['hostname']
print(f"\nHostname from XML: {hostname}")
print("Interface States:")
for iface in python_dict_from_xml['device_status']['interfaces']['interface']:
    print(f"  - {iface['name']}: {iface['state']} (IP: {iface['ip_address']})")

# 3. Convert Python Dictionary to XML String
python_dict_to_xml = {
    'network_device': {
        'hostname': 'SwitchA',
        'model': 'Cisco 2960',
        'vlans': {
            'vlan': [
                {'id': 10, 'name': 'DATA'},
                {'id': 20, 'name': 'VOICE'}
            ]
        }
    }
}

# pretty=True for human-readable XML output
xml_output_string = xmltodict.unparse(python_dict_to_xml, pretty=True)
print("\nPython Dictionary converted to XML String:")
print(xml_output_string)
print(f"Type of xml_output_string: {type(xml_output_string)}")