# Loc Lien Algorithms and Data Structures Refresher Course
# https://www.youtube.com/watch?v=1-l_UOFi1Xw&list=PLBZBJbE_rGRV8D7XZ08LK6z-4zPoWzu5H&index=9&ab_channel=CSDojo
# ===================
# Binary Tree
# ===================

class BinaryTreeNode:
    def __init__(self,val) -> None:
        self.val = val
        self.left = None
        self.right = None
        
class BinaryTree:
    def __init__(self) -> None:
        self.root = None
    def insert(self,val) -> None:
        # Base case for when the tree is initally empty and we are trying to push the first element onto the tree
        if not self.root:
            self.root = BinaryTreeNode(val)
        else:
            currNode = self.root
            while True:
                # If the value is less than the current node's value, we look to place the new node to the left of the current node.
                # If the current node already has a left node, then we know we should instead check the left node to see if 
                # if the value can be inserted there. 
                if val < currNode.val:
                    if currNode.left:
                        currNode = currNode.left
                    else:
                        currNode.left = BinaryTreeNode(val)
                        break
                # Inverse logic for the right side of the tree insertion
                elif val > currNode.val:
                    if currNode.right:
                        currNode = currNode.right
                    else:
                        currNode.right = BinaryTreeNode(val) 
                        break
                # Checks to ensure we don't accidentally add more than 1 instance of each node. 
                else:
                    print("This value is already present in the tree")
                    break
    def ResetTree(self):
        self.root = None
    def ArrayInsert(self, arr):
        for i in arr:
            self.insert(i)
    def invertInsert(self,val) -> None:
        if not self.root:
            self.root = BinaryTreeNode(val)
        else:
            currNode = self.root
            while True:
                if val < currNode.val:
                    if currNode.right:
                        currNode = currNode.right
                    else:
                        currNode.right = BinaryTreeNode(val)
                        break
                elif val > currNode.val:
                    if currNode.left:
                        currNode = currNode.left
                    else:
                        currNode.left = BinaryTreeNode(val) 
                        break
                else:
                    print("This value is already present in the tree")
                    break
    def invert(self):
        arr = self.ArrayofElements()
        self.root = None
        for i in arr:
            self.invertInsert(i)

        
    def ArrayofElements(self):
        tempQueue = []
        retArr = []
        if not self.root:
            return retArr
        else:
            currNode = self.root
            while True:
                if len(tempQueue) == 0 and currNode == self.root:
                    retArr.append(currNode.val)
                    if currNode.left:
                        tempQueue.append(currNode.left)
                    if currNode.right:
                        tempQueue.append(currNode.right)
                elif len(tempQueue) == 0 and currNode != self.root:
                    break
                else:
                    currNode = tempQueue.pop(0)
                    retArr.append(currNode.val)
                    if currNode.left:
                        tempQueue.append(currNode.left)
                    if currNode.right: 
                        tempQueue.append(currNode.right)
        return retArr
    def FindLeafNodes(self):
        nodeQueue = []
        leafArr = []
        
        if not self.root:
            return False
        else:
            currNode = self.root
            while True:
                if len(nodeQueue) == 0 and currNode == self.root:
                    if currNode.right:
                        nodeQueue.append(currNode.right)
                    if currNode.left:
                        nodeQueue.append(currNode.left)
                    if not currNode.left and not currNode.right:
                        leafArr.append(currNode.val)
                elif len(nodeQueue) == 0 and currNode != self.root:
                    break
                else:
                    currNode = nodeQueue.pop(-1)
                    if currNode.right: 
                        nodeQueue.append(currNode.right)     
                    if currNode.left:
                        nodeQueue.append(currNode.left)           
                    if not currNode.left and not currNode.right:
                        leafArr.append(currNode.val)    
        return leafArr   
        
                
            
    # Pretty Print function for generic balance trees from user Alejandro Mera on StackOverflow
    # https://stackoverflow.com/questions/34012886/print-binary-tree-level-by-level-in-python
    def PrettyPrintTree(self, root):
        def height(root):
            return 1 + max(height(root.left), height(root.right)) if root else -1  
        nlevels = height(root)
        width =  pow(2,nlevels+1)

        q=[(root,0,width,'c')]
        levels=[]

        while(q):
            node,level,x,align= q.pop(0)
            if node:            
                if len(levels)<=level:
                    levels.append([])
            
                levels[level].append([node,level,x,align])
                seg= width//(pow(2,level+1))
                q.append((node.left,level+1,x-seg,'l'))
                q.append((node.right,level+1,x+seg,'r'))
        for i,l in enumerate(levels):
            pre=0
            preline=0
            linestr=''
            pstr=''
            seg= width//(pow(2,i+1))
            for n in l:
                valstr= str(n[0].val)
                if n[3]=='r':
                    linestr+=' '*(n[2]-preline-1-seg-seg//2)+ '¯'*(seg +seg//2)+'\\'
                    preline = n[2] 
                if n[3]=='l':
                    linestr+=' '*(n[2]-preline-1)+'/' + '¯'*(seg+seg//2)  
                    preline = n[2] + seg + seg//2
                pstr+=' '*(n[2]-pre-len(valstr))+valstr #correct the potition acording to the number size
                pre = n[2]
            print(linestr)
            print(pstr)  

            

def main():
    binTree = BinaryTree()
    binTree.insert(10)
    binTree.insert(6)
    binTree.insert(12)
    binTree.insert(5)
    binTree.insert(7)
    binTree.insert(11)
    binTree.insert(13)
    binTree.PrettyPrintTree(binTree.root)
    print(binTree.ArrayofElements())
    binTree.invert()
    binTree.PrettyPrintTree(binTree.root)
    temp = binTree.ArrayofElements()
    binTree.ResetTree()
    binTree.ArrayInsert(temp)
    binTree.PrettyPrintTree(binTree.root)
    print(binTree.FindLeafNodes())

main()

