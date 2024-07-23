from cryptography.fernet import Fernet
import base64

def generate_custom_key(token):
    """Generate a Fernet key from a custom token"""
    # 確保 token 至少有 32 個字節
    if len(token) < 32:
        token += ' ' * (32 - len(token))
    elif len(token) > 32:
        token = token[:32]
    
    # 將 token 編碼為 URL 安全的 base64
    key = base64.urlsafe_b64encode(token.encode())
    return key

def decrypt_message(encrypted_message, key):
    """Decrypt an encrypted message"""
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message)
    return decrypted_message.decode()

if __name__ == "__main__":
    token = input("請輸入您的 token: ")
    key = generate_custom_key(token)
    with open('encrypted_message', 'rb') as file:
        encrypted_message = file.read()
    decrypted_message = decrypt_message(encrypted_message, key)
    print("解密後的訊息: ", decrypted_message)