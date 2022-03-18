import os
import random
import sys, pprint

# Python解释器到查找模块的路径，这些模块下的Python文件所有程序都能够导入它
# 其中\\Python38\\lib\\site-packages 目录为推荐路径，我们通过pip3 install 的模块默认都会安装到此目录下。
import time

pprint.pprint(sys.path)

print("platform：", sys.platform)
print("modules：", sys.modules)
print("stdout：", sys.stdout)
print("argv：", sys.argv[1:])
# print("exit：", sys.exit())


print("环境变量：", os.environ)
print("在子shell中执行操作系统命令：", os.system("echo 'Hello' "))
print("分隔不同路径的分隔符：", os.pathsep)
# 用引号将Program Files括起来了因为有空白字符
# os.system(r'C:\"Program Files"\"Microsoft Office"\root\Office16\WINWORD.EXE')

print(time.localtime())
print(time.sleep(1))
print(time.time())

print("0~1之间的随机数：", random.random())
print("1~10之间的随机数：", random.randrange(1, 11))
print("以长整数方式返回n个随机的二进制位：", random.getrandbits(3))

print()
