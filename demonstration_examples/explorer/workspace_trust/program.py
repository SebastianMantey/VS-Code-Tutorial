import time

# helper code
print("\nProgram initialized:\n")
time.sleep(1)

for i in range(1, 4):
    print(f"Process {i}/3 completed")    
    time.sleep(1)

print("\nProcessing done... the result is:")
time.sleep(3)

# actual code
with open("files/‮g_elif‬.txt") as f:
    content = f.read()

print(content)