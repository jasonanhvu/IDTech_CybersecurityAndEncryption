german_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
                   'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'ä', 'ö', 'ü', 'ß']
new_code = ""
message = input("Enter secret message:").lower()
key = input("Enter phrase that's long as secret message:").lower()

for i in range(0, len(key)):
    x = german_alphabet.index(message[i])
    y = german_alphabet.index(key[i])
    z = x + y
    new_code += german_alphabet[z % 30]
    if x < -1:
        new_code = ""

print("\n" + "-"*15)
print(new_code)
print("-"*15)