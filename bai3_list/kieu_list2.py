from time import sleep

your_name = "Henry"
your_great = "Hello! My name is "

for c in your_great + your_name:
    print(c, end='', flush=True)
    #print('\a')
    sleep(0.1)
print()
