import os,sys;from io import BytesIO, IOBase
BUFSIZE = 8192
class FastIO(IOBase):
    newlines = 0
    def __init__(self, file):
        self._fd = file.fileno();self.buffer = BytesIO();self.writable = "x" in file.mode or "r" not in file.mode;self.write = self.buffer.write if self.writable else None
    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:break
            ptr = self.buffer.tell();self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()
    def readline(self):
        while self.newlines == 0:b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE));self.newlines = b.count(b"\n") + (not b);ptr = self.buffer.tell();self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()
    def flush(self):
        if self.writable:os.write(self._fd, self.buffer.getvalue());self.buffer.truncate(0), self.buffer.seek(0)
class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file);self.flush = self.buffer.flush;self.writable = self.buffer.writable;self.write = lambda s: self.buffer.write(s.encode("ascii"));self.read = lambda: self.buffer.read().decode("ascii");self.readline = lambda: self.buffer.readline().decode("ascii")
sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
try:sys.stdin,sys.stdout=open('in.txt','r'),open('out.txt','w')
except:pass
ii1=lambda:int(sys.stdin.readline().strip()) # for interger
is1=lambda:sys.stdin.readline().strip() # for str
iia=lambda:list(map(int,sys.stdin.readline().strip().split())) # for List[int]
isa=lambda:sys.stdin.readline().strip().split() # for List[str]
mod=int(1e9 + 7);from collections import *;from math import *
# abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# sys.setrecursionlimit(500000)

###################### Start Here ######################

V = 4
color = [0]*V # V is no of vertices
parent = [-1]*V
cycle_start = - 1
cycle_end = -1
def help_find_cycle_dir(v):
    color[v]=1 # grey (on the way)
    global cycle_start
    global cycle_end
    for u in graph[v]:
        if color[u]==0:
            parent[u] = v #(v->u)
            if help_find_cycle_dir(u):
                return True # cycle found
        elif color[u]==1:
            cycle_start = u
            cycle_end = v
            return True # cycle found
    color[v] = 2 # black for visited
    return False



def find_cycle_dir(V):
    # graph should be directed
    # no self loops
    # no multiple edges

    for u in range(V):
        if color[u]==0 and help_find_cycle_dir(u):
            break
    if cycle_start == -1:
        print('acyclic')
    else:
        print('cyclic')
        cycle = [ ]
        cycle.append(cycle_start)

        v = cycle_end
        while v!=cycle_start:
            cycle.append(v)
            v = parent[v]
        cycle.append(cycle_start)
        cycle.reverse()
        print(*cycle)

graph = defaultdict(list)
for i in range(4):
    u,v = iia()
    u-=1
    v-=1
    graph[u].append(v)

find_cycle_dir(V)


