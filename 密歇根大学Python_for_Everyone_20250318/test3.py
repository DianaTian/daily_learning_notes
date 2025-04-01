name = input("Enter a file name: ")
if name == "na na boo boo":
    print("NA NA BOO BOO TO YOU - You have been punk'd!")
    quit()

try :
    file = open(name)
except :
    print("File cannot be opened:", name)
    quit()

count = 0
for line in file :
    count += 1
print('There were {} subject lines in {}'.format(count, name))