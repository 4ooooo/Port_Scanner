# Port_Scanner

## 一、概述

代码可以实现针对一个IP目标的简单的端口扫描。可以选择TCP_connect和SYN两种扫描方式

`TCP_connect`支持多线程，`SYN`只支持单线程。

> **环境**
>
> Python3
>
> **所需库**
>
> queue
>
> threading
>
> socket
>
> scapy

`scapy`需手动安装

## 二、使用方法

### IDE运行

直接点击运行即可，按提示输入即可。

> 输入实例1：
>
> ```
> 请输入目标IP地址
> target IP:127.0.0.1
> 请输入目标端口，若要输入端口范围则用"/"在起始和结束，例如"22/24"，或输入default，默认使用常用端口
> target port:80
> 请选择探测方式(输入A或B)：
> A.TCP connect扫描
> B.SYN扫描
> B
> 127.0.0.1       80 Open
> 扫描完成
> ```
>
> 输入实例2：
>
> ```
> 请输入目标IP地址
> target IP:127.0.0.1
> 请输入目标端口，若要输入端口范围则用"/"在起始和结束，例如"22/24"，或输入default，默认使用常用端口
> target port:default
> 请选择探测方式(输入A或B)：
> A.TCP connect扫描
> B.SYN扫描
> A
> 请输入线程
> threads:20
> 127.0.0.1	80 Open		
> 127.0.0.1	445 Open		
> 127.0.0.1	27018 Open		
> 127.0.0.1	21 Close
> 127.0.0.1	22 Close
> ...
> 127.0.0.1	50030 Close
> 127.0.0.1	50070 Close
> 扫描完成
> 
> 进程已结束,退出代码0
> ```
>
> 输入实例3：
>
> ```
> 请输入目标IP地址
> target IP:127.0.0.1
> 请输入目标端口，若要输入端口范围则用"/"在起始和结束，例如"22/24"，或输入default，默认使用常用端口
> target port:10/100
> 请选择探测方式(输入A或B)：
> A.TCP connect扫描
> B.SYN扫描
> A
> 请输入线程
> threads:20
> 127.0.0.1	80 Open		
> 127.0.0.1	10 Close
> 127.0.0.1	11 Close
> 127.0.0.1	12 Close
> 127.0.0.1	13 Close
> 127.0.0.1	14 Close
> ...
> 127.0.0.1	99 Close
> 127.0.0.1	100 Close
> 扫描完成
> 
> 进程已结束,退出代码0
> ```

### 命令行运行

输入同IDE

```
C:\Users\86135\Desktop\扫描器>python3 main.py
请输入目标IP地址
target IP:127.0.0.1
请输入目标端口，若要输入端口范围则用"/"在起始和结束，例如"22/24"，或输入default，默认使用常用端口
target port:default
请选择探测方式(输入A或B)：
A.TCP connect扫描
B.SYN扫描
A
请输入线程
threads:20
127.0.0.1       80 Open
127.0.0.1       445 Open
127.0.0.1       27018 Open
127.0.0.1       21 Close
127.0.0.1       22 Close
...
扫描完成
```



#### 特别鸣谢

代码部分借鉴于博客：http://t.csdn.cn/3tE9M