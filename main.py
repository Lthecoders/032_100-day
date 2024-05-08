import os
import random
import time

print("\n\n\nLoading all language's greetings.....\vPlease wait")
time.sleep(2)
os.system("clear")
different_hello = [
    "hello there", "Konichiwa", "Guten Tag!", "Bore Da!", "Namaste",
    "Namaskar", "Anyoang"
]

i = random.randint(0, 6)
print(f"{different_hello[i]}")

print(
    "\n\npress run the programe again to see the different language greeting")
