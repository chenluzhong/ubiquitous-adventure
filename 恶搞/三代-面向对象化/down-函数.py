import os
import easygui as gui


class shut():
    strvar1 = " "*25+"哈哈,你中病毒了!哈哈哈"+" "*25
    def shutdown():
        os.system("shutdown /s /hybrid /t 200")

    def noshut():
        os.system("shutdown /a")
    a = 1
    i = 1
    count=3
    def main():
        gui.msgbox((" "*25 + "请立即马上保存好已编辑的软件,你还有三分钟时间" + " "*25)*3,"这是一个恶作剧" + " " * 10, "确定")
        while True:
            shut.strvar2 = "关闭此程序还有+++{}+++次后才可以终止哦".format(shut.count)
            shut.count-=1
            if shut.i == 1:
                shut.shutdown()
            shut.i+=1
            shut.a += 1
            if shut.a >= 5:
                shut.noshut()
                gui.msgbox("{}关机任务已取消.放心吧\n{}   此程序已中止".format("\t"*4,"\t"*4), "这是一个恶作剧" + " " * 10, "关闭")
                break
            elif shut.a < 5:
                gui.msgbox(shut.strvar1*2+shut.strvar2, "这是一个恶作剧" + " " * 10, "关闭")
shut = shut.main()
shut()     

