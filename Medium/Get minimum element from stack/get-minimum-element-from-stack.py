#User function Template for python3

class stack:
    def __init__(self):
        self.s=[]
        self.temp=[]
        self.minEle=None

    def push(self,x):
        if len(self.temp)==0 or x<=self.temp[-1]:
            self.temp.append(x)
        self.s.append(x)
        #CODE HERE

    def pop(self):
        if not self.s:
            return -1
        if self.s[-1]==self.temp[-1]:
            self.temp.pop(-1)
        return self.s.pop(-1)
        
        #CODE HERE
        

    def getMin(self):
        if not self.temp:
            return -1
        return self.temp[-1]
        
        #CODE HERE


#{ 
 # Driver Code Starts
#contributed by RavinderSinghPB
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        q = int(input())

        arr = [int(x) for x in input().split()]

        stk=stack()  

        qi = 0
        qn=1
        while qn <= q:
            qt = arr[qi]

            if qt == 1:
                stk.push(arr[qi+1])
                qi+=2
            elif qt==2:
                print(stk.pop(),end=' ')
                qi+=1
            else:
                print(stk.getMin(),end=' ')
                qi+=1
            qn+=1
        print()

# } Driver Code Ends