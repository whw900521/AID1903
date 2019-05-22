'''
    ftp文件服务器
    功能
    【1】 分为服务端和客户端,要求可以有多个客户端同时操作。
    【2】 客户端可以查看服务器文件库中有什么文件。
    【3】 客户端可以从文件库中下载文件到本地。
    【4】 客户端可以上传一个本地文件到文件库。
    【5】 使用print在客户端打印命令输入提示,引导操作
    思路分析:
        1,技术点分析
            *并发模型  多线程并发模式
            *数据传输  tcp传输
        2,结构设计
            *客户端发起请求,打印请求提示界面
            *文件传输功能封装成类
        3,功能分析
            *网络搭建
            *查看文件库信息
            *下载文件
            *上传文件
            *客户端退出
        4,协议
            *L--表示请求文件列表
            *Q--表示退出
            *G--表示下载
            *P--表示上传
'''