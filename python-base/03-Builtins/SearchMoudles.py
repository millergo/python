import copy, pprint

# 使用dir()查看模块中包含的内容
print([i for i in dir(copy) if not i.startswith("_")])
print(copy.__all__)
pprint.pprint(dir(copy))


