# 1. Define the list of temperatures
temperatures = [98.6, 101.2, 99.5, 102.1, 97.8]

# 2. Loop through each temperature
for temp in temperatures:
    # 3. Check the condition
    if temp >= 100.4:
        print(f"Patient temp is {temp}F. Fever detected. Alert doctor.")
    else:
        print(f"Patient temp is {temp}F. Temperature normal.")