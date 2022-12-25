class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        graph = defaultdict(list)
        for dept, dest in tickets:
            graph[dept].append(dest)
        for k in graph:
            graph[k].sort()
        
        answer = []
        def dfs(spot, l):
            if len(answer) != 0:
                return
            if len(l) == len(tickets)+1:
                answer.append(l[:])
                return
            
            available = graph[spot]
            for i in range(len(available)):
                dest = available[i]
                if dest != "":
                    graph[spot][i] = ""
                    l.append(dest)
                    dfs(dest, l)
                    l.pop()
                    graph[spot][i] = dest
        
        
        jfk_list = graph["JFK"]
        for i in range(len(jfk_list)):
            dest = jfk_list[i]
            graph["JFK"][i] = ""
            if len(answer) == 0:
                dfs(dest, ["JFK", dest])
                graph["JFK"][i] = dest
        
        return answer[0]
        