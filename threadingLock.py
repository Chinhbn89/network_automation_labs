import threading
import time # For simulating work

shared_data = 0 # This is our shared number
data_lock = threading.Lock() # This is our lock

def increment_data_safe():
    global shared_data
    # 'with data_lock:' means:
    # 1. Acquire the lock
    # 2. Run the code inside this 'with' block
    # 3. Automatically release the lock when the block finishes (or errors)
    with data_lock:
        # This part is the "critical section" - only one thread can be here at a time
        local_copy = shared_data
        time.sleep(0.00001) # Small delay to make it clear lock is working
        local_copy += 1
        shared_data = local_copy
        print(f"Thread {threading.current_thread().name} updated data to: {shared_data}")

# Example Usage:
print("--- Lock Example ---")
threads = []
for i in range(10):
    t = threading.Thread(target=increment_data_safe, name=f"Thread-{i+1}")
    threads.append(t)
    t.start()
for t in threads:
    t.join()
print(f"Final shared_data: {shared_data}")