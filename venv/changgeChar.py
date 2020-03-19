#!/usr/bin/python3
# !coding=utf-8
# __author__='Zhang Liangdong'
# Date:2020/3/12 17:19
# fileName:changgeChar.py
# -*- coding:utf-8 -*-


import os, sys
import chardet


def convert(filename, in_enc="GBK", out_enc="UTF-8"):
    try:
        print("convert " + filename)
        f = open(filename, 'rb')
        content = f.read()
        result = chardet.detect(content)  # 通过chardet.detect获取当前文件的编码格式串，返回类型为字典类型
        print(result)
        f.close()
        coding = result.get('encoding')  # 获取encoding的值[编码格式]
        if coding != 'UTF-8-SIG' and coding == 'utf-8':  # 文件格式如果是utf-8的时候，才进行转码
            print(coding + " to " + out_enc + "!")
            new_content = content.decode(in_enc).encode(out_enc)
            f = open(filename, 'wb')
            f.write(new_content)
            f.close()
            print(" done")
        else:
            print(coding)
    except IOError as e:
        # except:
        print(e)


def explore(dir):
    for root, dirs, files in os.walk(dir):
        for file in files:
            path = os.path.join(root, file)
            convert(path)


def main(dir):
    if (os.path.isdir(dir)):
        fpaths = [fpath for fpath in os.listdir(dir) if os.path.isfile(dir + "\\" + fpath) and fpath.endswith('.js')]
        dpaths = [dpath for dpath in os.listdir(dir) if os.path.isdir(dir + "\\" + dpath)]
        for f in fpaths:
            convert(dir + "\\" + f, 'utf-8', 'UTF-8-SIG')
        for d in dpaths:
            print(d)
            main(dir + "\\" + d)


if __name__ == "__main__":
    main(os.getcwd()+"/static/b.js")

