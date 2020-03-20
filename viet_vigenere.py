viet_alphabet = ['q','e','r','t','y','ỳ','ỷ','ỹ','ý','ú','ủ','u','ù','ũ','ụ','ứ','ử','ư','ừ','ữ','ự','i','ì','ỉ',
                 'ĩ','í','ị','ò','o','ỏ','õ','ó','ọ','ô','ồ','ổ','ộ','ỗ','ố','ơ','ờ','ở','ỡ','ớ','ợ','p','a','à',
                 'ả','ã','á','ạ','ă','ằ','ẳ','ẵ','ắ','ặ','â','ầ','ẩ','ẫ','ấ','ậ','s','d','đ','f','g','h','k','l',
                 'x','c','v','b','n','m', 'è', 'é', 'ẻ', 'ẽ', 'ẹ', 'ế', 'ể', 'ê', 'ề', 'ễ', 'ệ']
new_code = ""
message = input("Enter ecret message:").lower()
key = input("Enter phrase that's long as secret message:").lower()

for i in range(0, len(key)):
    x = viet_alphabet.index(message[i])
    y = viet_alphabet.index(key[i])
    z = x + y
    new_code += viet_alphabet[z % 89]
    if x < -1:
        new_code = ""

print("\n" + "-"*10)
print(new_code)
print("-"*10)