
files = [];

for i in range(1000):
    files.append(open('script.py', 'r'))
    print(i)
    
f = open('work.py', 'r')
file_data = f.read()
f.close()

print(file_data)


# With
# Python provides a special syntax that auto-closes a file for you once you're finished using it.

# Quiz Solution: Flying Circus Cast List
def create_cast_list(filename):
    cast_list = []
    with open(filename) as f:
        for line in f:
            name = line.split(",")[0]
            cast_list.append(name)

    return cast_list

cast_list = create_cast_list('script.py')
for actor in cast_list:
    print(actor)