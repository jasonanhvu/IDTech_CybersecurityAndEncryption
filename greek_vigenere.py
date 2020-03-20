greek_alphabet = ['Α', 'Β', 'Γ', 'Δ', 'Ε', 'Ζ', 'Η', 'Θ', 'Ι', 'Κ', 'Λ', 'M',
                  'N', 'Ξ', 'Ο', 'Π', 'Ρ', 'Σ', 'Τ', 'Υ', 'Φ', 'Χ', 'Ψ', 'Ω']
new_code = ""
message = input("Please enter a secret message:").lower()
key = input("Please enter any phrase that's long as the secret message:").lower()

for i in range(0, len(key)):
    x = greek_alphabet.index(message[i])
    y = greek_alphabet.index(key[i])
    z = x + y
    new_code += greek_alphabet[z % 24]
    if x < -1:
        new_code = ""

print("\n" + "-"*10)
print(new_code)
print("-"*10)