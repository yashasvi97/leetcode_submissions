// https://leetcode.com/problems/clone-graph

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is not None:
            # print("node val", node.val)
            
            nodeList = [None] * 101
            visit    = [False] * 101
            
            ind = node.val
            nodeList[ind] = Node(val=ind)
            parent = ind
            
            queue = []
            for n in node.neighbors:
                ind = n.val
                if nodeList[ind] is None:
                    nodeList[ind] = Node(val=ind)
                
                nodeList[parent].neighbors.append(nodeList[ind])
                visit[parent] = True
                queue.append(n)
                
            while len(queue) !=0 :
                n = queue.pop(0)
                if not visit[n.val]:
                    if nodeList[n.val] is None:
                        nodeList[n.val] = Node(val=n.val)

                    parent = n.val
                    # print("parent val", parent)
                    for nei in n.neighbors:
                        if nodeList[nei.val] is None:
                            nodeList[nei.val] = Node(val=nei.val)

                        nodeList[parent].neighbors.append(nodeList[nei.val])
                        queue.append(nei)
                    visit[parent] = True
            
            return nodeList[1]
        else:
            return None
            