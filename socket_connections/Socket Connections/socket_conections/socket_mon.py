import psutil
class socket_conn:
    def __init__(self, pids, laddr, raddr, status):
        self.pids, self.laddr, self.raddr, self.status = pids, laddr, raddr, status
 
obj=socket_conn('123','1','1', 'str')

out_list=[]
def connection_attr():
    templ = "%2s %2s %2s %2s"
    print(templ % ("\"PID\",", "\"Laddr\",", "\"Raddr\",", "\"Status\""))
    for obj in psutil.net_connections(kind='tcp'):
        try:
                laddr = obj.laddr
                laddr=str(laddr[0])+"@"+str(laddr[1])
                raddr = obj.raddr 
                if(len(raddr)==2):
                    raddr=str(raddr[0])+"@"+str(raddr[1])
                pid=obj.pid
                status=obj.status
                ob= socket_conn(pid,laddr,raddr,status)
                out_list.append(ob)
        except psutil.NoSuchProcess:
                pass    
                     
connection_attr()

from collections import Counter

c = Counter(getattr(line, 'pids') for line in out_list)
fin_list=[]
class fin_obj:
    def __init__(self, pids, laddr, raddr, status,count):
        self.pids, self.laddr, self.raddr, self.status ,self.count= pids, laddr, raddr, status,count
        
for val in out_list:
    term=fin_obj(val.pids,val.laddr,val.raddr,val.status,c.get(val.pids))
    fin_list.append(term)

fin_list.sort(key=lambda x: (x.count,x.pids))
countx=0
for val in fin_list:
    if(countx==0):
        print("\""+str(val.pids)+"\""+","+"\""+str(val.laddr)+"\""+","+"\""+str(val.raddr)+"\""+","+"\""+str(val.status)+"\"")
        countx+=1
    else:
        print("\""+str(val.pids)+"\""+","+"\""+str(val.laddr)+"\""+","+"\""+str(val.raddr)+"\""+","+"\""+str(val.status)+"\"")
del out_list[:]
del fin_list[:]
c.clear()