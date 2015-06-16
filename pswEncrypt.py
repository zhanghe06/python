# encoding: utf-8
__author__ = 'zhanghe'

import hashlib


class EncryptPsw():
    def __init__(self):
        pass

    def _user_to_bin(self, user):
        return self._hex_to_bin(hex(int(user))[2:].zfill(16))

    def encrypt(self, user, psw, verify_code):
        bin_user = self._user_to_bin(user)
        psw_1 = self._md5_encrypt_1(psw)

        psw_1 = self._hex_to_bin(psw_1)
        psw_2 = self._md5_encrypt_2(psw_1, bin_user)
        psw_3 = self._md5_encrypt_3(psw_2, verify_code)

        return psw_3

    @staticmethod
    def _hex_to_bin(string):  # 字符串转bytes数组
        length = len(string)
        tmp = []
        for i in range(0, length, 2):
            tmp.append(int("0x" + string[i:i + 2], base=16))
        return bytes(tmp)

    @staticmethod
    def _md5_encrypt_1(psw):  # 密码的第一次加密
        md5 = hashlib.md5()
        md5.update(psw.encode("ISO-8859-1"))
        return md5.hexdigest().upper()

    @staticmethod
    def _md5_encrypt_2(psw, user):  # 密码的第二次加密
        md5 = hashlib.md5()
        md5.update(psw + user)
        return md5.hexdigest().upper()

    @staticmethod
    def _md5_encrypt_3(psw, verify_code):  # 密码的第三次加密
        md5 = hashlib.md5()
        md5.update((psw + verify_code.upper()).encode("ISO-8859-1"))
        return md5.hexdigest().upper()


def main():
    a = EncryptPsw()
    psw = a.encrypt("888888888", "123456", "!xyz")
    print(psw)


if __name__ == "__main__":
    main()