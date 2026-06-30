def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    ciphertext = ""
    for ch in plaintext:
        if 'A' <= ch <= 'Z':
            shifted = (ord(ch) - ord('A') + shift) % 26
            ciphertext += chr(ord('A') + shifted)
        elif 'a' <= ch <= 'z':
            shifted = (ord(ch) - ord('a') + shift) % 26
            ciphertext += chr(ord('a') + shifted)
        else:
            ciphertext += ch
    return ciphertext

def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    plaintext = ""
    for ch in ciphertext:
        if 'A' <= ch <= 'Z':
            shifted = (ord(ch) - ord('A') - shift) % 26
            plaintext += chr(ord('A') + shifted)
        elif 'a' <= ch <= 'z':
            shifted = (ord(ch) - ord('a') - shift) % 26
            plaintext += chr(ord('a') + shifted)
        else:
            plaintext += ch
    return plaintext