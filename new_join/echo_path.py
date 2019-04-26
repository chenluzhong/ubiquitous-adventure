import os,sys,winreg,time
import easygui as e

# 获取当前执行的脚本所在的路径
dirname, filename = os.path.split(os.path.abspath(sys.argv[0]))
print("running from", dirname)
print("file is", filename)

# 获取当前系统的桌面路径(通过注册表 这里引入了winreg模块)


def get_desktop():
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                         r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders')  # 利用系统的链表
    return winreg.QueryValueEx(key, "Desktop")[0]  # 返回的是Unicode类型数据


get_desktop()
if __name__ == '__main__':
    Desktop_path = str(get_desktop())  # Unicode转化为str
    print(Desktop_path)

# 主函数  运行前请输入所有课件所在的目录
filename = e.enterbox(msg="输入文件名字", title='第一步', default='', strip=True, image=None, root=None)

def zuijia(filename):
    Flag = True
    # os.chdir(pathvar)
    if filename == "exit()":
        time.sleep(0.3)
        print("即将退出,欢迎下次再来")
        time.sleep(2)
        os._exit(0)
    elif filename == "":
        time.sleep(0.3)
        print("输入错误.程序崩溃,请重新运行")
        time.sleep(2)
        os._exit(0)
    dirsa = Desktop_path+"\\"+filename
    if not os.path.exists(dirsa):
        open(dirsa+".py",mode="w",encoding="utf-8")
    while Flag:
        pathvar = e.enterbox(msg="输入课件的路径", title='第二步', default='', strip=True, image=None, root=None)
        if pathvar == "exit()":
            print("即将退出,请等待")
            time.sleep(2)
            os._exit(0)
        elif pathvar == "":
            time.sleep(0.3)
            print("程序异常,即将退出,请再次运行")
            time.sleep(2)
            os._exit(0)
        os.chdir(pathvar)
        listvar = os.listdir(".")
        if listvar == []:
            print("当前路径下为空")
            continue
        else:
            break
    listvar2 = []
    for a in listvar:
        # print(a[len(a)-3:])
        if a[len(a)-3:] == ".py":
            listvar2.append(a)
    for i in listvar2:
        with open(i, mode="r+", encoding="utf-8") as fp:
            res = fp.readlines()
            with open(Desktop_path+"\\"+filename+".py", mode="a+", encoding="utf-8") as fp2:
                fp2.writelines(res)

while True:
    print("*"*20+"欢迎使用本程序"+"*"*20)
    print("友情提示,如果想要退出此程序,请输入==> exit()")
    zuijia(filename)

'''
# 对listvar 进行数据清洗
def shujuqingxi():
    listvar = ["2312.py", "231.py", "432.5"]
    listvar2 = []
    for a in listvar:
        rea = len(a)
        if a[rea-3:] == ".py":
        listvar2.append(a)
        else:
            pass
'''