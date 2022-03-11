def run():
    literal = "Let's Go"
    print(literal)
    literal = literal + "it"
    print(literal)

    # 使用 repr 将值转换为字符串
    result = "Hello, \nWrold!"
    result = repr(result)
    print("repr()函数结果:" + result)
    # 使用 str 将值转换为字符串
    result_str = "Hello, \nWorld!"
    result_str = str(result_str)
    print("str()函数结果:" + result_str)

    # 使用'''或者“”“ 长字符串包裹字符串
    string1 = '''
    Hello Miller's Home,
    "That is good"\n,Haha
    '''
    print(string1)

    # 原始字符串 r 可以保证所有字符串都保持原样,但是如果里面有单引号，那就需要使用三引号将字符串包裹起来了。这里的\n会作为原始字符串而不是转义字符
    o = r'''C:\now\two\row Let's GO'''
    print("打印原始字符串:" + o)
    print(len(o.encode("UTF-8")))
    print(len(o.encode("UTF-32")))


if __name__ == "__main__":
    run()
