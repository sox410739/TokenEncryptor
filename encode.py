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

def read_message():
    """Read a message from the user"""
    with open('message', 'r', encoding='utf-8') as file:
        message = file.read()
    return message

def encrypt_message(message, key):
    """Encrypt a message"""
    encoded_message = message.encode()
    f = Fernet(key)
    encrypted_message = f.encrypt(encoded_message)
    with open('encrypted_message', 'wb') as file:
        file.write(encrypted_message)
    return encrypted_message

if __name__ == "__main__":
    token = input("請輸入您的 token: ")
    key = generate_custom_key(token)
    message = read_message()
    encrypted_message = encrypt_message(message, key)
    print("加密後的訊息已儲存到 encrypted_message 檔案中。")
    