# encoding: utf-8
__author__ = 'zhanghe'


import rsa


def create_keys():
    """
    创建密钥对，然后保存.pem格式文件，当然也可以直接使用
    :return:
    """
    (_pub_key, _pri_key) = rsa.newkeys(1024)

    pub = _pub_key.save_pkcs1()
    with open('public.pem', 'w+') as pub_file:
        pub_file.write(pub)

    pri = _pri_key.save_pkcs1()
    with open('private.pem', 'w+') as pri_file:
        pri_file.write(pri)


def get_pri_key():
    """
    获取密钥
    :return:
    """
    with open('private.pem') as private_file:
        p = private_file.read()
        pri_key = rsa.PrivateKey.load_pkcs1(p)
    return pri_key


def get_pub_key():
    """
    获取公钥
    :return:
    """
    with open('public.pem') as public_file:
        p = public_file.read()
        pub_key = rsa.PublicKey.load_pkcs1(p)
    return pub_key


def encrypt(message):
    """
    加密
    :param message:
    :return:
    """
    pub_key = get_pub_key()
    cipher_text = rsa.encrypt(message, pub_key)
    return cipher_text


def decrypt(message):
    """
    解密
    :param message:
    :return:
    """
    pri_key = get_pri_key()
    plain_text = rsa.decrypt(message, pri_key)
    return plain_text


def sign(plain_text):
    """
    用私钥签名认证
    :param plain_text:
    :return:
    """
    pri_key = get_pri_key()
    signature = rsa.sign(plain_text, pri_key, 'SHA-256')
    return signature


def verify_sign(plain_text, cipher_text):
    """
    用公钥验证签名
    :param plain_text:
    :param cipher_text:
    :return:
    """
    pub_key = get_pub_key()
    try:
        rsa.verify(plain_text, cipher_text, pub_key)
        return True
    except:
        return False


def test(message):
    """
    测试,打印密文和明文,签名和验证签名结果
    :param message:
    :return:
    """
    cipher_text = encrypt(message)
    plain_text = decrypt(cipher_text)
    print cipher_text
    print('-------------------------')
    print plain_text
    print('-------------------------')
    sign_text = sign('this is a test!')
    print sign_text
    print('-------------------------')
    print verify_sign('this is a test!', sign_text)
    print('-------------------------')
    print verify_sign('this is another test!', sign_text)


if __name__ == '__main__':
    # create_keys()  # 初次运行,需要创建密钥对
    test('hello word!')


# rsa模块安装
# pip install rsa