"""
显示指定目录下的文件, 拼接 index.html 访问
"""

import os
import time

""" 扫描的目录 """
PATH = '/Users/mark/Downloads'



""" 指定一层目录 """
LEVEL = 1

def dirs_name():
    """  获取指定目录下的文件夹 """

    root_depth = len(PATH.split(os.path.sep))
    d = {}

    for root, dirs, files in os.walk(PATH, topdown=True):

        """ print dirs """
        for name in dirs:
            dir_path = os.path.join(root, name)
            dir_depth = len(dir_path.split(os.path.sep))
            if dir_depth == root_depth + LEVEL:
                d[name] = {}
                d[name]['name'] = name
                
                d[name]['time'] = time.strftime("%Y-%m-%d %H:%M:%S", (time.localtime(os.path.getmtime(dir_path))))
            
    return d

if __name__ == '__main__':
    dirs_name()
    # print(os.path.dirname(PATH))
    

