import traceback

print("Script Starting... Please wait!")

try:
    import coconuts
    print("Coconuts module loaded successfully.")
except Exception as e:
    print("Error importing coconuts:", e)
    traceback.print_exc()
    import traceback

print("Script Starting... Please wait!")

try:
    import coconuts
    print("Coconuts module loaded successfully.")

    # Agar koi function run ho raha ho, usko comment kar ke dekho
    # coconuts.main()  # <- agar aisa kuch likha ho toh hata ke run karo

except Exception as e:
    print("Error importing coconuts:", e)
    traceback.print_exc()

print("Script Reached End.")


# Baaki code ab yahan se likho


