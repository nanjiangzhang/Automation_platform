# -*- coding:utf8 -*-
import re
import subprocess

import paramiko


class Get_Folder:

    _sftp_name = None  # 名称
    __all_class = {}  # 所有文件夹和对应的文件集
    __file_yun = '/root/Auto_Mation'

    def __init__(self, Server_ip, Server_point, Username, Password):

        self.__server_ip = Server_ip
        self.__server_point = Server_point
        self.__username = Username
        self.__password = Password

    def __Login_sftp(self):  # 登录云的sftp

        t = paramiko.Transport((self.__server_ip, self.__server_point))
        t.connect(username=self.__username, password=self.__password)
        self._sftp_name = paramiko.SFTPClient.from_transport(t)

    def __All_class_document(self):  # 获取所有目录和文件

        files_fir = self._sftp_name.listdir(self.__file_yun)
        for first_class in files_fir:
            files_sec = self._sftp_name.listdir(self.__file_yun + '/%s/' % first_class)
            sec_list = []  # 二级目录集合
            for second_class in files_sec:
                if '.py' in second_class:  # 将所有的.pyc文件导出
                    sec_list.append(second_class)
            self.__all_class[first_class] = sec_list

    def Directory_Structure(self):  # 提供返回的结构的取值
        self.__Login_sftp()
        self.__All_class_document()
        return self.__all_class


def net_check(pip):  # ping包
    p = subprocess.Popen('ping %s\n' % pip, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    line = p.stdout.read().decode("gbk")
    matchobj = re.search(r'TTL', line, re.M | re.I)
    p.kill()
    if matchobj:
        return 0  # 成功
    else:
        return 1  # 失败
