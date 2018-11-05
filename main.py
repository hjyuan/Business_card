# 无限循环
while True:

    # 显示功能菜单

    action_str = input("请选择希望进行的操作：")
    print("您选择的操作是【%s】"% action_str)

    # 1,2,3 针对名片的操作
    if action_str in ["1","2","3"]:

        # 新增名片
        pass

    # 0 退出系统
    elif action_str == "0":

        print("欢迎再次使用【名片管理系统】")

        break
        # 如果在开发程序时，不希望立刻编写分支内部的代码
        # 如果可以使用 pass 关键字，表示一个占位符，能够保证程序的代码正确
        # 程序运行时，pass 关键字不会有任何动作
        # pass

    # 其他内容输入错误，需要提示用户
    else:
        print("您输入的不正确，请重新选择")

