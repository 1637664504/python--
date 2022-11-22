import ftpclt
import ftplib
import os

def main():
    ftp = ftpclt.connect(ftpclt.ftpHost,ftpclt.ftpName,ftpclt.ftpPassword)                  #连接登陆ftp
    dirpath = 'lp'                   #目录，不能使用lp/lp1这种多级创建，而且要保证你的ftp目录，右键属性不能是只读的
    try: ftp.mkd(dirpath)                 #新建远程目录
    except ftplib.error_perm:
        print("目录已经存在或无法创建")
    try:ftp.cwd(dirpath)             #重定向到指定路径
    except ftplib.error_perm:
        print('不可以进入目录："%s"' % dirpath)
    print(ftp.pwd())                        #返回当前所在位置
    try: ftp.mkd("dir1")                  #在当前路径下创建dir1文件夹
    except ftplib.error_perm:
        print("目录已经存在或无法创建")
    
    oldFile = '/home/liuj/1.sh'
    ftpclt.upload(ftp,oldFile)       #上传本地文件
    filename="test1.txt"
    ftp.rename('1.sh', filename) #文件改名
    if os.path.exists(filename):   #判断本地文件是否存在
        os.unlink(filename)    #如果存在就删除
    ftpclt.download(ftp,filename)        #下载ftp文件
    ftpclt.listinfo(ftp)                   #打印目录下每个文件或文件夹的详细信息
    files = ftp.nlst()              #获取路径下文件或文件夹列表
    print(files)
    
    ret = ftpclt.find(ftp,'1.sh')
    print('find ret',ret)
    ret = ftpclt.find(ftp,filename)
    print('find ret',ret)
    ftp.delete(filename)              #删除远程文件    
    ftp.rmd("dir1")                  #删除远程目录
    ftp.quit()  #退出

if __name__ == '__main__':
    main()