# TokenEncryptor
一個簡單的加密工具，可以將字串加密成一串亂碼，並且可以將加密後的亂碼解密成原本的字串。

## 使用方法
### 安裝必要套件
    pip install cryptography

### 加密
1. 把要加密的字串放在 `message` 檔案中。
2. 執行 `encode.py`。
    ```python
    python encode.py
    ```
3. 輸入自訂義的 token。
4. 加密後的亂碼會存放在 `encrypted_message` 檔案中。

### 解密
1. 把要解密的亂碼放在 `encrypted_message` 檔案中。
2. 執行 `decode.py`。
    ```python
    python decode.py
    ```
3. 輸入加密時的 token。
4. 解密後的字串 print 出來。