# if a name starts with an underscore, it's name should never be changed without good reason
# if a name starts with a double underscore, it's name should never be changed without good reason at all
# there is no such thing as a  private variable in python. everything is a variable everywhere, but the convention
# is to use an underscore to indicate intention
print(dir())
# print(dir(__builtins__))

for m in dir(__builtins__):
    print(m)
