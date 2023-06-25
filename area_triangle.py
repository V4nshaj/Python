class Triangle:
    def Perimeter(self, s1, s2, s3):
        return (s1 + s2 + s3)

    def Area(self, s1, s2, s3):
        p = (s1 + s2 + s3)
        s = p/2
        return (s * (s-s1) * (s-s2)*(s-s3))**0.5

t = Triangle()
print("The perimeter of the triangle is : %.2f" % t.Perimeter(3, 4, 5))
print("The area of the triangle is : %.2f" % t.Area(3, 4, 5))
