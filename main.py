# main.py
import sys
import time
import os
import numpy as np

def rotateX(i:float,j:float,k:float, theta:float):
    cosTheta = np.cos(theta)
    sinTheta = np.sin(theta)
    mat = np.array([[1,0,0],[0,cosTheta, - sinTheta],[0, sinTheta, cosTheta]])
    result  = np.dot(mat, [i,j,k])
    return result

def rotateY(i:float, j:float, k:float, theta:float):
    cosTheta = np.cos(theta)
    sinTheta = np.sin(theta)
    mat = np.array([[cosTheta, 0, sinTheta],[0, 1, 0],[-sinTheta, 0, cosTheta]])
    result  = np.dot(mat, [i,j,k])
    return result

def rotateZ(i:float, j:float, k:float, theta:float):
    cosTheta = np.cos(theta)
    sinTheta = np.sin(theta)
    mat = np.array([[cosTheta, -sinTheta, 0], [sinTheta, cosTheta, 0], [0, 0, 1]])
    result  = np.dot(mat, [i,j,k])
    return  result

def rotate(i,j,k,thetaA,thetaB,thetaC):
    tmp = rotateX(i,j,k,thetaA)
    tmp = rotateY(*tmp,thetaB)
    tmp = rotateZ(*tmp,thetaC)
    return tmp

def show(thetaA, thetaB, thetaC):
    """
    @return ([121 * 2 matrix] * 3 tuple) [[float, float], [float,float], ..., [float, float]]
        
    """

    result = []

    for t in range(3):
        r1 = []
        k = 15
        vector = [0,0]
        vector.insert(t, k)
        direction =  rotate(*vector,thetaA=thetaA, thetaB=thetaB, thetaC=thetaC)[0]
        if direction > 0:
            pass
        elif direction < 0:
            k = -k
        else:
            result.append([])
            continue

        for ii in range(31):
            for jj in range(31):
                i = ii - 15
                j = jj - 15
                vector = [i,j]
                vector.insert(t,k)
                r1.append(rotate(*vector,thetaA=thetaA,thetaB=thetaB,thetaC=thetaC))

        result.append(r1[:])

    return result


def simplify(matrix):
    for i in range(len(matrix)):
        matrix[i] = list(map(int, np.ceil(matrix[i]/3)))
    return matrix

def getScreen(row, col):
    tmp = [' '] * col
    result = []
    for i in range(row):
        result.append(tmp[:])
    return result

    


    
def main( a = 0.2, b = 0.2, c = 0.2):
    
    
    thetaA,thetaB,thetaC = theta[0], theta[1], theta[2]
    while True:
        
        screen = getScreen(30,30)

        matrix = show(thetaA,thetaB,thetaC)
        m1, m2, m3 = map(simplify, matrix)

        for _ in m1:
            x, y, z = _[0]+15, _[1]+15, _[2]+15
            screen[y][z] = '#'

        for _ in m2:
            x, y, z = _[0]+15, _[1]+15, _[2]+15
            screen[y][z] = '.'

        for _ in m3:
            x, y, z = _[0]+15, _[1]+15, _[2]+15
            screen[y][z] = '-'
            


        prom = ''
        for i in range(len(screen)):
            # prom = prom + "[%02d] " % i
            for j in range(len(screen)):
                prom = prom + screen[i][j]
            prom = prom + '\n'


        thetaA = thetaA + a
        thetaB = thetaB + b
        thetaC = thetaC + c

        os.system('cls')
        print(prom)
        time.sleep(0.01)    




if __name__ == '__main__':
    t = sys.argv[1:]
    theta = [0,0,0]
    try:
        a,b,c = map(lambda x: int(x)/10, t)
        main(a=a, b=b, c=c)
    except KeyboardInterrupt:
        pass
    except:
        try:
            main()
        except KeyboardInterrupt:
            pass
    
    