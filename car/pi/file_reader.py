
filename='car\pi\pi_digits.txt'

# with open(filename) as file_object:
#     contents = file_object.read()

# print(contents.rstrip())


with open(filename) as file_object:
    lines = file_object.readlines()

pi_string=''

for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))

# print(contents)你                                                                    