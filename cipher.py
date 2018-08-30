import base64


if __name__ == '__main__':
    with open('./xxx.txt', 'rb') as f:
        b = f.read()
    cipher = base64.b64encode(b)

    with open('osd', 'wb') as f:
        f.write(cipher)


    with open('osd', 'rb') as f:
        c = f.read()
    plain = base64.b64decode(c).decode()

