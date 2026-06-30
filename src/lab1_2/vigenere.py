def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    ciphertext = ""
    key_index = 0
    for ch in plaintext:
        if ch.isalpha():
            shift = ord(keyword[key_index % len(keyword)].lower()) - ord('a')
            key_index += 1
            if 'A' <= ch <= 'Z':
                shifted = (ord(ch) - ord('A') + shift) % 26
                ciphertext += chr(ord('A') + shifted)
            else:
                shifted = (ord(ch) - ord('a') + shift) % 26
                ciphertext += chr(ord('a') + shifted)
        else:
            ciphertext += ch
    return ciphertext

def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    plaintext = ""
    key_index = 0
    for ch in ciphertext:
        if ch.isalpha():
            shift = ord(keyword[key_index % len(keyword)].lower()) - ord('a')
            key_index += 1
            if 'A' <= ch <= 'Z':
                shifted = (ord(ch) - ord('A') - shift) % 26
                plaintext += chr(ord('A') + shifted)
            else:
                shifted = (ord(ch) - ord('a') - shift) % 26
                plaintext += chr(ord('a') + shifted)
        else:
            plaintext += ch
    return plaintext