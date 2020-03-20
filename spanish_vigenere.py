spanish_alphabet = ['a', 'b', 'c', 'ch', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'll', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
new_code = ""
message = input("Enter secret message:").lower()
key = input("Enter phrase that's long as secret message:").lower()

for i in range(0, len(key)):
    x = spanish_alphabet.index(message[i])
    y = spanish_alphabet.index(key[i])
    z = x + y
    new_code += spanish_alphabet[z % 27]
    if x < -1:
        new_code = ""

print("\n" + "-"*10)
print(new_code)
print("-"*10)