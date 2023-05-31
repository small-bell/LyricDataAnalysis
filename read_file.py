import os
import re


def get_files_dir(dir):
    """
    获取所有文件的目录
    :param dir:
    :return:
    """
    allfiles = []
    extensions = ["txt"]
    for root, dirs, files in os.walk(dir):
        for files_path in files:
            file_path = os.path.join(root, files_path)
            extension = os.path.splitext(file_path)[1][1:]
            if extension in extensions:
                allfiles.append(file_path)
    return allfiles


def replace_tags(str):
    """
    替换特殊符号
    :param str:
    :return:
    """
    return re.sub('([^\u4e00-\u9fa5\u0041-\u007a])', '', str)
