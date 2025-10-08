import asyncio # The module for asynchronous programming
import time    # For measuring time and basic delays
import random  # For simulating variable delays

async def simulate_task(task_name, delay):
    """
    This is a 'coroutine' (an async function).
    It simulates an operation that involves waiting (like a network call or file I/O).
    'await asyncio.sleep(delay)' is a NON-BLOCKING pause.
    """
    print(f"[{time.strftime('%H:%M:%S')}] Starting {task_name} (delay: {delay}s)...")
    # When 'await' is used, this coroutine pauses and tells the asyncio manager:
    # "I'm waiting for {delay} seconds. While I wait, you can run other tasks!"
    await asyncio.sleep(delay) 
    print(f"[{time.strftime('%H:%M:%S')}] Finished {task_name}.")
    return f"Result for {task_name}"

async def main_sequential():
    """
    This main coroutine will run our simulated tasks one after another (sequentially).
    """
    print("--- Running Tasks Sequentially (Blocking Simulation) ---")
    start_time = time.time()

    # We 'await' each task. This means the program will fully wait for the first one
    # to complete before starting the second one.
    result1 = await simulate_task("Task 1 (Sequential)", 3) # Will wait 3 seconds
    result2 = await simulate_task("Task 2 (Sequential)", 2) # Will wait 2 seconds AFTER the first one finishes

    print(f"\nSequential results: {result1}, {result2}")
    end_time = time.time()
    print(f"Total sequential time: {end_time - start_time:.2f} seconds")


async def main_concurrent():
    """
    This main coroutine will run our simulated tasks concurrently (at the same time).
    """
    print("\n--- Running Tasks Concurrently (Non-Blocking Simulation) ---")
    start_time = time.time()

    # 1. Create coroutine objects (these are just "plans" for tasks, they don't run yet)
    task1 = simulate_task("Task A (Concurrent)", 3)
    task2 = simulate_task("Task B (Concurrent)", 2)
    task3 = simulate_task("Task C (Concurrent)", 4)

    # 2. Use asyncio.gather() to run all these "plans" concurrently.
    #    It starts them all, and then waits for the *longest* one to finish.
    results = await asyncio.gather(task1, task2, task3)

    print(f"\nConcurrent results: {results}")
    end_time = time.time()
    print(f"Total concurrent time: {end_time - start_time:.2f} seconds")

# IMPORTANT: Modify the '__main__' block at the bottom of your file
# to run this new concurrent example instead of the sequential one.

# This is the standard way to start an asyncio program.
# It runs the 'main_sequential' coroutine and manages the asyncio event loop.




async def configure_device_sim(device_name, config_commands_count):
    """
    Simulates sending configuration commands to a device.
    """
    print(f"[{time.strftime('%H:%M:%S')}] Configuring {device_name} (commands: {config_commands_count})...")
    # Simulate variable config time for each device
    await asyncio.sleep(random.uniform(1, 3)) 
    print(f"[{time.strftime('%H:%M:%S')}] Configuration complete for {device_name}.")
    return f"Configured {device_name} with {config_commands_count} commands."

async def main_config_automation():
    """
    This coroutine orchestrates concurrent configuration of multiple devices.
    """
    print("\n--- Concurrent Device Configuration Automation Simulation ---")
    start_time = time.time()

    devices_to_configure = {
        "Router-HQ": 3, # 3 simulated commands
        "Switch-Access-1": 5,
        "Firewall-DMZ": 2,
        "Core-Router-Backup": 4
    }

    config_tasks = []
    for name, commands_count in devices_to_configure.items():
        # Create a list of coroutine "plans" for each device
        config_tasks.append(configure_device_sim(name, commands_count))
        # print(config_tasks)

    # Run all configuration tasks concurrently
    config_results = await asyncio.gather(*config_tasks)

    print("\nAll device configurations completed:")
    print(config_results)
    for res in config_results:
        print(f"- {res}")

    end_time = time.time()
    print(f"Total configuration time: {end_time - start_time:.2f} seconds")

# IMPORTANT: Modify the '__main__' block at the bottom of your file
# to run this new example.



async def fetch_status_or_log(source_name):
    """
    Simulates fetching status or log data from a source.
    """
    print(f"[{time.strftime('%H:%M:%S')}] Monitoring {source_name} status/logs...")
    delay = random.uniform(0.5, 2.5) # Simulate variable monitoring time
    await asyncio.sleep(delay)
    
    # Simulate different types of data
    if "Device" in source_name:
        status_data = f"Device {source_name} - Interface Gi0/1 is {'up' if random.random() > 0.3 else 'down'}"
    else: # Assume it's a log source
        status_data = f"Log from {source_name}: Critical event detected at {time.ctime()}"

    print(f"[{time.strftime('%H:%M:%S')}] Finished monitoring {source_name}.")
    return {source_name: status_data}

async def main_monitoring_and_logs():
    """
    Orchestrates concurrent monitoring and log collection simulation.
    """
    print("\n--- Concurrent Log Collection & Real-time Monitoring Simulation ---")
    start_time = time.time()

    sources_to_monitor = [
        "Device-1", "Device-2", "Log-Server-A", "Device-3", 
        "API-Gateway-B", "Device-4", "Syslog-C", "Sensor-D",
    ] # 8 conceptual sources

    monitor_tasks = []
    for source in sources_to_monitor:
        monitor_tasks.append(fetch_status_or_log(source))

    # Run all monitoring tasks concurrently
    monitoring_results = await asyncio.gather(*monitor_tasks)

    print("\n--- All Monitoring Results ---")
    for res in monitoring_results:
        for source, data in res.items():
            print(f"  {source}: {data}")

    end_time = time.time()
    print(f"\nTotal monitoring time: {end_time - start_time:.2f} seconds")

# IMPORTANT: Modify the '__main__' block at the bottom of your file
# to run this new example.

if __name__ == "__main__":
    # asyncio.run(main_sequential())
    # asyncio.run(main_concurrent())
    # asyncio.run(main_config_automation()) # <--- UNCOMMENT THIS LINE
    asyncio.run(main_monitoring_and_logs()) # <--- UNCOMMENT THIS LINE
