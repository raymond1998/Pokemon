__author__ = 'Charles-Jianye Chen'
import rgine as rgine

t = input("-> Ordered? (T/F) ").lower()
width = int(input("-> Width? "))
height = int(input("-> Height? "))
t = rgine.Terrain("w", width, height, 32, 32)
if t == "t":
        i = 0
        for y in range(height):
                for x in range(width):
                        t.setIdentifier(x, y, i)
                        i += 1
        print(i)
        t.writeTerrain("%dx%d_ordered"%(width, height))
        input("Done! ")
else:
        t.writeTerrain("%dx%d"%(width, height))
        input("Done! ")
