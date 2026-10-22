temperatures = [98.6, 101.2, 99.5, 102.1, 97.8, 105.2]

for temp in temperatures:
    if temp >= 105.0:
        print(f"Patient temp is {temp}F. CRITICAL EMERGENCY.")
    elif temp >= 100.4:
        print(f"Patient temp is {temp}F. Fever detected. Alert doctor.")
    else:
        print(f"Patient temp is {temp}F. Temperature normal.")