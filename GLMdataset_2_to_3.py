import json


# flm2 转 glm3多轮  无用.
def conversion(path):
    list1 = [
        {
            "conversations": [
                {
                    "role": "system",
                    "content": "你是一个专门出题的人工智能"
                }
            ]
        }
    ]
    with open(path, "r", encoding="utf-8") as f:
        # 循环读取每一行
        while True:
            # 读取一行数据
            line = f.readline()
            # 如果没有数据了，就退出循环
            if not line:
                break
            # 解析json数据
            data = json.loads(line)
            # 打印或处理数据
            print(data['content'])
            print(data['summary'])
            list1[0]['conversations'].append({"role": "user", "content": str(data['content'])})
            list1[0]['conversations'].append({"role": "assistant", "content": str(data['summary'])})
    print(list1)

    with open("new_" + path, "w", encoding="utf-8") as f:
        json.dump(list1, f, indent=4, ensure_ascii=False)


# glm2 格式转 glm3 格式
def conversion2(path):
    list1 = []
    with open(path, "r", encoding="utf-8") as f:
        # 循环读取每一行
        while True:
            # 读取一行数据 main.py
            line = f.readline()
            # 如果没有数据了，就退出循环
            if not line:
                break
            # 解析json数据
            data = json.loads(line)
            # 打印或处理数据
            print(data['content'])
            print(data['summary'])
            list1.append({"prompt": str(data['content']), "response": str(data['summary'])})
    print(list1)

    with open("new2_" + path, "w", encoding="utf-8") as f:
        json.dump(list1, f, indent=4, ensure_ascii=False)


# glm2 格式转 alpaca
def conversion3(path):
    list1 = []
    with open(path, "r", encoding="utf-8") as f:
        # 循环读取每一行
        while True:
            # 读取一行数据 main.py
            line = f.readline()
            # 如果没有数据了，就退出循环
            if not line:
                break
            # 解析json数据
            data = json.loads(line)
            # 打印或处理数据
            print(data['content'])
            print(data['summary'])
            list1.append({"instruction": "你是一个编程算法题目出题助手，生成算法题目", "input": str(data['content']),
                          "response": str(data['summary'])})
    print(list1)

    with open("new3_" + path, "w", encoding="utf-8") as f:
        json.dump(list1, f, indent=4, ensure_ascii=False)


# glm3 格式转 alpaca
def conversion4(path):
    list1 = []
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
        # print(data)
        for i in data:
            list1.append({
                "instruction": "你是一个编程算法题目出题助手，生成算法题目",
                "input": i['prompt'],
                "response": i['response']
            })
    with open("new3a_" + path, "w", encoding="utf-8") as f:
        json.dump(list1, f, indent=4, ensure_ascii=False)


# conversion2("待转换文件路径")
# conversion3("待转换文件路径")
conversion4("待转换文件路径")

# 这里面的instruction或者system需要自己写 :）因为有的格式没有这个哦
