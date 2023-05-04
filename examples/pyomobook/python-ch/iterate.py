# iterate.py

# @all:
D = {'Mary': 231, 'Bob': 123, 'Alice': 331, 'Ted': 987}
for i in sorted(D):
    if i == 'Alice':
        continue
    if i == 'John':
        print("Loop ends. Cleese alert!")
        break;
    print(f"{i} {str(D[i])}")
else:
    print("Cleese is not in the list.")
# @:all
