import time

wait_time = 1 
max_retries = 5

for attempt in range(1, max_retries + 1):
    print(f"Attempt {attempt}... waiting {wait_time} seconds before retry.")
    time.sleep(wait_time) 
    wait_time *= 2  

print("Stopped after maximum retries.")
