import queue
import threading
import socket
from scapy.sendrecv import sr
from scapy.layers.inet import IP, TCP

class TCP_connect():
    def __init__(self,ip,port,threads):
        self.openport_list = []
        self.closeport_list = []
        self.ip = ip
        self.port = port
        self.threads=threads
        self.q = queue.Queue()
        #TCP_connect_threads(ip, threadnum)

    def TCP_connect_threads(self):
        thread_joinlist = []
        for i in range(0, self.threads):  # 控制线程数
            new_thread = threading.Thread(target=self.TCP_connect_check, args=())
            new_thread.start()
            thread_joinlist.append(new_thread)
        for i in thread_joinlist:
            i.join()

    def TCP_connect_plist(self):
        [self.q.put(i) for i in self.port]
        self.TCP_connect_threads()
        self.TCP_connect_print()

    def TCP_connect_check(self):
        while True:
            if self.q.empty():  # 判断队列是否为空
                break
            else:
                self.pport = self.q.get()  # 取出一个端口
                self.TCP_connect_con()


    def TCP_connect_con(self):
        try:
            port = int(self.pport)
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            if port == 3306 or port == 22 or port == 23 or port == 1521:
                s.settimeout(4)
            else:
                s.settimeout(1)
            s.connect((self.ip, port))
            self.openport_list.append(port)
        except Exception as e:
            self.closeport_list.append(port)
        finally:
            s.close()

    def TCP_connect_print(self):  # 打印函数，排序
        self.openport_list.sort()
        for i in self.openport_list:
            print(self.ip + "\t" + str(i) + " Open\t\t")
        self.closeport_list.sort()
        for i in self.closeport_list:
            print(self.ip + "\t" + str(i) + " Close")

class SYN():
    def __init__(self, ip, port,threads):
        self.openport_list = []
        self.closeport_list = []
        self.ip = ip
        self.port = port
        self.threads = threads
        self.q = queue.Queue()

    def SYN_connect_threads(self):
        thread_joinlist = []
        for i in range(0, self.threads):  # 控制线程数
            new_thread = threading.Thread(target=self.SYN_connect_check, args=())
            new_thread.start()
            thread_joinlist.append(new_thread)
        for i in thread_joinlist:
            i.join()

    def SYN_connect_plist(self):
        [self.q.put(i) for i in self.port]
        self.SYN_connect_threads()
        self.SYN_connect_print()

    def SYN_connect_check(self):
        while True:
            if self.q.empty():  # 判断队列是否为空
                break
            else:
                self.pport = self.q.get()  # 取出一个端口
                self.SYN_connect_con()

    def SYN_connect_con(self):
        try:
            temp = sr(IP(dst=ip) /
                      TCP(dport=(int(self.pport)), flags='S'),
                      timeout=2, verbose=False)
            if temp[0].res:
                result = temp[0].res  # temp分回复和无回显
                if (result[0][1].payload.flags) == 'SA':
                    #print('端口开放')
                    self.openport_list.append(self.pport)
                    return 1
                else:
                    self.closeport_list.append(self.pport)
            else:
                self.closeport_list.append(self.pport)
                return 0
        except:
            self.closeport_list.append(self.pport)
            return 0

    def SYN_connect_print(self):  # 打印函数，排序
        self.openport_list.sort()
        for i in self.openport_list:
            print(self.ip + "\t" + str(i) + " Open\t\t")
        self.closeport_list.sort()
        for i in self.closeport_list:
            print(self.ip + "\t" + str(i) + " Close")

if __name__ == '__main__':
    port=[]
    ip=input('请输入目标IP地址\ntarget IP:')
    tport=input('请输入目标端口，若要输入端口范围则用"/"在起始和结束，例如"22/24"，或输入default，默认使用常用端口\ntarget port:')
    # threads=int(input('请输入线程\nthreads:'))
    choose=input("请选择探测方式(输入A或B)：\nA.TCP connect扫描\nB.SYN扫描\n")
    # ip='127.0.0.1'
    # tport='default'
    # threads=20
    # choose='B'
    if tport.lower() == 'default':
        port=[21, 22, 23, 53, 80, 111, 139, 161, 389, 443, 445, 512, 513, 514,
                 873, 1025, 1433, 1521, 3128, 3306, 3311, 3312, 3389, 5432, 5900,
                 5984, 6082, 6379, 7001, 7002, 8000, 8080, 8081, 8090, 9000, 9090,
                 8888, 9200, 9300, 10000, 11211, 27017, 27018, 50000, 50030, 50070]

    elif '/' in tport:
        start_port=int(tport.split('/')[0])
        end_port=int(tport.split('/')[-1])
        for i in range(start_port,end_port+1):
            port.append(i)
    elif tport.isdigit() == True :
        port.append(int(tport))
    if choose.upper() == 'A':
        threads = int(input('请输入线程\nthreads:'))
        TCP_connect(ip,port,threads).TCP_connect_plist()
        print("扫描完成")
    if choose.upper() == 'B':
        threads = 1
        SYN(ip,port,threads).SYN_connect_plist()
        print("扫描完成")