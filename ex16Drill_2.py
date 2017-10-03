from sys import argv

Script, filename, repeat = argv

print(f"You choose to read {filename} {repeat} times. \nContinue?")

File = open(filename)

svar = input()
x = 1
if svar.lower() == "y":
    while x <= int(repeat):
        print(File.read())
        File.seek(0)
        x = x + 1
else:
    print("No confirmation received.\nShutting down...")
File.close()
