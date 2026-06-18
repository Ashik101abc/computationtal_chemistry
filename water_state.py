# Water State Logic for Electrolysis
temperature =120  # Temperature in Celsius

if temperature <= 0:
    print("State: Solid (Ice).")
    print("Action: Cannot perform standard water splitting.")
elif temperature < 100:
    print("State: Liquid (Water).")
    print("Action: Optimal for standard HER/OER electrolysis.")
else:
    print("State: Gas (Steam).")
    print("Action: Requires High-Temperature Solid Oxide Electrolyzer.")
