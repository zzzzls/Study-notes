# @Time    : 2021-03-09
# @Author  : zzzzls
# @Github  : https://github.com/zzzzls
# @Blog    : https://blog.csdn.net/qq_36078992

import time
import random
import hashlib
import requests


def md5Encrypt(obj):
    """MD5加密"""
    md5 = hashlib.md5()
    md5.update(obj.encode())
    return md5.hexdigest()


def youdao_translate(search_key: str) -> str:
    """
    有道翻译 API
    :param search_key: 将要翻译的词
    :return: str or None, 翻译结果
    """

    # 构建加密参数
    ts = int(time.time() * 1000)
    salt = str(ts) + str(random.randint(1, 9))
    bv = md5Encrypt(
        '5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36')
    sign = md5Encrypt("fanyideskweb" + search_key + salt + "Tbh5E8=q6U3EXe+&L[4c@")

    url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
    headers = {
        'Host': 'fanyi.youdao.com',
        'Origin': 'http://fanyi.youdao.com',
        'Referer': 'http://fanyi.youdao.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': 'OUTFOX_SEARCH_USER_ID=-1644523005@10.108.160.100; OUTFOX_SEARCH_USER_ID_NCOO=857549368.4207594; JSESSIONID=aaahQdbLzSjY3dSU_V1Fx; DICT_UGC=be3af0da19b5c5e6aa4e17bd8d90b28a|; JSESSIONID=abcXf1BO34WgqbzPvg3Fx; _ntes_nnid=550e7be268d446cac20d6f763fbdc8c7,1614758394523; ___rl__test__cookies=1615258741826'
    }
    data = {
        "i": search_key,
        "from": "AUTO",
        "to": "AUTO",
        "smartresult": "dict",
        "client": "fanyideskweb",
        "salt": salt,
        "sign": sign,
        "lts": ts,
        "bv": bv,
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "action": "FY_BY_REALTlME"
    }

    try:
        res = requests.post(url, headers=headers, data=data).json()
        result = res['translateResult'][0][0]['tgt']
    except:
        print('请求失败，请检查参数！')
        result = None

    return result


if __name__ == '__main__':
    kw = input('请输入待翻译内容：')
    result = youdao_translate(kw)
    print(result)
