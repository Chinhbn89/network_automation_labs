# file_io_lab.py
print("--- Writing Configuration to File ---")
device_config_to_save = """
    version 15.6
    hostname My-Lab-Router
    interface Loopback0
    ip address 1.1.1.1 255.255.255.255
    end"""
output_config_filename = "router_config_backup.txt"

try:
    # Open in "w" (write) mode. This will create the file or overwrite it if it exists.
    with open(output_config_filename, "w") as f: 
        f.write(device_config_to_save)
    print(f"Configuration backup successfully written to: {output_config_filename}")
except IOError as e:
    print(f"Error writing backup file: {e}")