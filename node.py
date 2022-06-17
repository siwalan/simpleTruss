import numpy as np

class Node(object):
    def __init__(self, x,y):
        self.id = -1
        self.pos = np.array([x,y])
        self.disp = np.array([0.0, 0.0])
        self.force = np.array([0.0, 0.0])
        self.fixity = [False,False]
        self._hasLoad = False

    def __str__(self):
        s = "Node({})".format(self.id)
        return s

    def __repr__(self):
        return str(self)

    def getNode(self):
        return self.id
    def fixDOF(self,dof):
        self.fixity[dof] = True

    def isFixed(self,dof):
        return self.fixity[dof]

    def setDisp(self,u,v):
        self.disp = np.array([u,v])

    def getDisp(self):
        return self.disp

    def getPos(self):
        return self.pos

    def getDeformedPos(self,factor):
        return (self.pos + self.disp * factor)

    def addLoad(self,Px,Py):
        self.force += np.array([Px,Py])
        self._hasLoad = True

    def setLoad(self,Px,Py):
        self.force = np.array([Px,Py])
        self._hasLoad = True

    def getLoad(self):
        return self.force

    def hasLoad(self):
        return self._hasLoad
