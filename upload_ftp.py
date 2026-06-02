# -*- coding: utf-8 -*-
"""
FTP上传脚本 - 上传 jkjtsb.html、logo.png 到远程服务器
"""
import ftplib
import os
import datetime

# FTP配置
FTP_HOST = "103.236.79.184"
FTP_USER = "GY5WWwtr3kzi"
FTP_PASS = "GY5WWwtr3kzi"

# 基础URL
BASE_URL = "https://anli.lcmfkj.com"

# 要上传的文件列表
FILES_TO_UPLOAD = [
    "jkjtsb.html",
    "logo.png",
]

# 本地文件目录
LOCAL_DIR = os.path.dirname(os.path.abspath(__file__))

# 生成文件夹名 (使用日期+时间)
FOLDER_NAME = "niuniu" + datetime.datetime.now().strftime("%Y%m%d_%H%M%S")


def upload():
    print(f"[*] 连接FTP服务器: {FTP_HOST}")
    ftp = ftplib.FTP()
    ftp.connect(FTP_HOST, 21, timeout=30)
    ftp.login(FTP_USER, FTP_PASS)
    ftp.encoding = "utf-8"
    print(f"[✓] 登录成功")

    # 显示当前目录
    print(f"[*] 当前目录: {ftp.pwd()}")

    # 创建文件夹
    try:
        ftp.mkd(FOLDER_NAME)
        print(f"[✓] 创建文件夹: {FOLDER_NAME}")
    except ftplib.error_perm as e:
        print(f"[!] 文件夹可能已存在: {e}")

    # 进入文件夹
    ftp.cwd(FOLDER_NAME)
    print(f"[*] 进入目录: {ftp.pwd()}")

    # 上传文件
    for filename in FILES_TO_UPLOAD:
        local_path = os.path.join(LOCAL_DIR, filename)
        if not os.path.exists(local_path):
            print(f"[✗] 文件不存在: {local_path}")
            continue

        file_size = os.path.getsize(local_path)
        print(f"[*] 上传: {filename} ({file_size / 1024:.1f} KB) ...")

        with open(local_path, "rb") as f:
            ftp.storbinary(f"STOR {filename}", f)

        print(f"[✓] 上传完成: {filename}")

    # 关闭连接
    ftp.quit()
    print(f"\n[✓] 全部上传完成！\n")

    # 输出访问链接
    print("=" * 60)
    print("  访问链接:")
    print("=" * 60)
    for filename in FILES_TO_UPLOAD:
        url = f"{BASE_URL}/{FOLDER_NAME}/{filename}"
        print(f"  {filename}:")
        print(f"    {url}")
        print()
    print("=" * 60)


if __name__ == "__main__":
    upload()
