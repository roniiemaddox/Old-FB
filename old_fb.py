import coconuts

print("Script Starting... Please wait!")

try:
    coconuts.main()  # <-- yeh line zaroori hai agar usme main() function bana tha
except Exception as e:
    print("Error:", e)

print("Script Reached End.")



