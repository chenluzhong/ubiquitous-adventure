import os
import easygui as gui
strvar1 = " "*25+"哈哈,你中病毒了!哈哈哈"+" "*25

#第一个弹窗
gui.msgbox((" "*25 + "请立即马上保存好已编辑的软件,你还有三分钟时间" + " "*25)*3,"这是一个恶作剧" + " " * 10, "确定")
"""
    shutdown的参数:
    /s 关机
    /t 设置关机的时间(s为单位)
    /a 中止关机
"""
def shutdown():
    os.system("shutdown /s /hybrid /t 200")

def noshut():
    os.system("shutdown /a")
a = 1
i = 1
count=3
while True:

    strvar2 = "关闭此程序还有+++{}+++次后才可以终止哦".format(count)
    count-=1
    if i == 1:
        shutdown()
    i+=1
    # res = input("退出请输入q:")
    # if res == "q":
    #     break
    # else:
    a += 1
    if a >= 5:
        noshut()
        gui.msgbox("{}关机任务已取消.放心吧\n{}   此程序已中止".format("\t"*4,"\t"*4), "这是一个恶作剧" + " " * 10, "关闭")
        break
    elif a < 5:
        gui.msgbox(strvar1*2+strvar2, "这是一个恶作剧" + " " * 10, "关闭")

        

