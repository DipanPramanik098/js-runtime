from runtime.interpreter import JSRuntime
import sys
import os

if len(sys.argv) != 2:
    print("Usage: python run.py <javascript_file>")
    sys.exit(1)

filename = sys.argv[1]

if not os.path.exists(filename):
    print(f"File not found: {filename}")
    sys.exit(1)

with open(filename, "r", encoding="utf-8") as file:
    code = file.read()

runtime = JSRuntime()
runtime.execute(code)