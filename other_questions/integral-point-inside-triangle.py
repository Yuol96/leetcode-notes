class triangle:
    def __init__(self, p1, p2, p3):
        self.points = [tuple(p1), tuple(p2), tuple(p3)]
        self.points.sort()

    def vectorSubtract(self, p1, p2):
        """
        - p1 - p2
        """
        return (p1[0]-p2[0], p1[1]-p2[1])

    def vectorDot(self, v1, v2):
        return v1[0]*v2[1] - v1[1]*v2[0]

    def inTriangle(self, p):
        """
        Input:
            - p: a tuple of (x, y)
        Output:
            - Boolean
        """
        a = self.vectorSubtract(p, self.points[0])
        b = self.vectorSubtract(p, self.points[1])
        c = self.vectorSubtract(p, self.points[2])

        u,v,w = self.vectorDot(a,b), self.vectorDot(b,c), self.vectorDot(c,a)
        if u==0 or v==0 or w==0:
            return True, a, b, c
        elif u>0 and v>0 and w>0:
            return True, a, b, c
        elif u<0 and v<0 and w<0:
            return True, a, b, c
        return False

    def getBox(self):
        import math
        xmin, ymin, xmax, ymax = float('inf'), float('inf'), float('-inf'), float('-inf')
        for p in self.points:
            if p[0]>xmax:
                xmax = p[0]
            if p[0]<xmin:
                xmin = p[0]
            if p[1]<ymin:
                ymin = p[1]
            if p[1]>ymax:
                ymax = p[1]
        return math.ceil(xmin), math.ceil(ymin), math.floor(xmax), math.floor(ymax)

    def computeVectorLength(self, v):
        return (v[0]**2 + v[1]**2)**0.5

    def solve(self):
        minLen = float('inf')
        minLenPoints = []
        xmin, ymin, xmax, ymax = self.getBox()
        for i in range(xmin, xmax+1):
            for j in range(ymin, ymax+1):
                tup = self.inTriangle((i,j))
                if tup is not False:
                    __, a, b, c = tup
                    totLen = self.computeVectorLength(a) + self.computeVectorLength(b) + self.computeVectorLength(c)
                    if totLen < minLen:
                        minLenPoints = [[i,j]]
                        minLen = totLen
                    elif totLen == minLen:
                        minLenPoints.append([i,j])
        if len(minLenPoints) == 0:
            return [None, None]
        minLenPoints.sort(key=lambda p: (p[0],p[1]), reverse=True)
        return minLenPoints[0]



if __name__ == '__main__':
    tri = triangle((0,0), (1,0), (1,1))
    print(tri.solve())



