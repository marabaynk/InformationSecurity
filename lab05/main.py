from OpenSSL import crypto

if __name__ == '__main__':
    fl = input("Введите имя файла: ")
    f = open(fl, 'rb')
    data = f.read()

    #создаём закрытый ключ
    key = crypto.PKey()
    key.generate_key(crypto.TYPE_RSA, 1024)
    print(f'Private and public keys were generated')

    #Получаете открытый ключ из закрытого
    cert = crypto.X509()
    cert.set_pubkey(key)

    #Подписываете хэш
    signature = crypto.sign(key, data, "sha256")
    print(f'Created signature: {signature}')

    # OK
    try:
        crypto.verify(cert, signature, data, "sha256")
        print('Signature checking passed ok!')
    except Exception:
        print('Wrong signature!')

    # Wrong
    try:
        crypto.verify(crypto.X509(), signature, data, "sha256")
        print('Signature checking passed ok!')
    except Exception:
        print('Wrong signature!')