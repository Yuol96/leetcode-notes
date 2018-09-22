class ribbon:
    def __init__(self, points, ribbonLen):
        self.points = [tuple(p) for p in points]
        self.points.sort(key=lambda tup: (tup[0], tup[1]))
        self.ribbonLen = ribbonLen

    def vectorSubtract(self, p1, p2):
        return (p1[0]-p2[0], p1[1]-p2[1])

    def isConvex(self, p1, p2, p3):
        a = self.vectorSubtract(p2, p1)
        b = self.vectorSubtract(p3, p2)
        return a[0]*b[1] - a[1]*b[0] >= 0

    def findOuterPoints(self, points):
        if len(points)<=3:
            return points
        points.sort(key=lambda tup: (tup[0], tup[1]))
        st = [points[0], points[1]]
        for idx in range(2, len(points)):
            p = points[idx]
            while len(st)>1 and not self.isConvex(st[-2], st[-1], p):
                st.pop()
            st.append(p)
        return points

    def computeDist(self, p1, p2):
        v = self.vectorSubtract(p1, p2)
        return (v[0]**2 + v[1]**2) ** 0.5

    def computePerimeter(self, outerPoints):
        if len(outerPoints) == 1:
            return 0
        dists = []
        lastPoint = outerPoints[0]
        for idx in range(1, len(outerPoints)):
            currPoint = outerPoints[idx]
            dists.append((idx-1, idx, self.computeDist(currPoint, lastPoint)))
            lastPoint = currPoint
        currPoint = outerPoints[0]
        dists.append((len(outerPoints)-1, 0, self.computeDist(currPoint, lastPoint)))
        return dists

    def solve(self):
        points = self.points
        while True:
            if len(points) == 1:
                return 1
            if len(points) == 2:
                return 2 * self.computeDist(points[0], points[1])
            outerPoints = self.findOuterPoints(points)
            dists = self.computePerimeter(outerPoints)
            if sum(list(map(lambda tup: tup[2], dists))) <= self.ribbonLen:
                return len(points)
            else:
                distPerPoint = {i:0 for i in range(len(outerPoints))}
                for preIdx, postIdx, dist in dists:
                    distPerPoint[preIdx] += dist
                    distPerPoint[postIdx] += dist
                distAllPoints = sorted(list(distPerPoint.items()), key=lambda tup: tup[1], reverse=True)
                removeIdx = distAllPoints[0][0]
                removePoint = outerPoints[removeIdx]
                points.pop(points.index(removePoint))

if __name__ == '__main__':
    rib = ribbon([[0,0],[0,3],[3,3]], 10.25)
    print(rib.solve())









