import traceback

print("Script Starting... Please wait!")

try:
    import coconuts
    print("Coconuts module loaded successfully.")
except Exception as e:
    print("Error importing coconuts:", e)
    traceback.print_exc()

# Baaki code ab yahan se likho


