# -*- coding: utf-8 -*-
"""
FTP更新脚本 - 覆盖上传 jkjtsb.html 到已有目录
"""
import ftplib
import os

FTP_HOST = "103.236.79.184"
FTP_USER = "GY5WWwtr3kzi"
FTP_PASS = "GY5WWwtr3kzi"

FOLDER_NAME = "niuniu20260407_140414"
LOCAL_DIR = os.path.dirname(os.path.abspath(__file__))

FILES_TO_UPLOAD = ["jkjtsb.html"]

def upload():
    print(f"[*] 连接FTP服务器: {FTP_HOST}")
    ftp = ftplib.FTP()
    ftp.connect(FTP_HOST, 21, timeout=30)
    ftp.login(FTP_USER, FTP_PASS)
    ftp.encoding = "utf-8"
    print(f"[✓] 登录成功")

    ftp.cwd(FOLDER_NAME)
    print(f"[*] 进入目录: {ftp.pwd()}")

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

    ftp.quit()
    print(f"\n[✓] 更新完成！")
    print(f"  访问: https://anli.lcmfkj.com/{FOLDER_NAME}/jkjtsb.html")

if __name__ == "__main__":
    upload()
