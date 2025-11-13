class Solution(object):
    def dfs(self,i,visited,adjlst):
        visited[i]=1
        for it in adjlst[i]:
            if(visited[it]==0):
                visited[it]=1
                self.dfs(it,visited,adjlst)
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        n=len(isConnected)
        m=len(isConnected[0])
        adjlst=[]
        for i in range(n):
            adjlst.append([])
        for i in range(n):
            for j in range(m):
                if(isConnected[i][j]==1 and i!=j):
                    adjlst[i].append(j)
                    adjlst[j].append(i)
        visited=[0]*n
        c=0
        for i in range(0,n):
            if(visited[i]==0):
                visited[i]=1
                self.dfs(i,visited,adjlst)
                c+=1
        return c


        