# Get the current time in seconds since the epoch
current_time = time.time()

# Convert the current time to a local time tuple
local_time = time.localtime()

# Print the current time in a specific format
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", local_time)

# Convert a string representing a time to a time tuple
time_tuple = time.strptime("2023-03-08 14:30:00", "%Y-%m-%d %H:%M:%S")

# Suspend the execution of the current thread for 5 seconds
time.sleep(5)

# Get the CPU time used by the current process
cpu_time = time.clock()
