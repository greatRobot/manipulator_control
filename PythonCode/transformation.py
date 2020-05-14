##################### 坐标转换（从小机械臂末端坐标系转换到“织女”的基座标系下  ##################
import numpy as np
from numpy import *
from math import *
#######################################################################
#程序基本参数介绍
#theta1 , theta2为2个关节角
#l1,l2为两个关节连杆的长度
#T为转换矩阵（Ts0s1，Ts1s2，Tb0s0）
#P为坐标系下的坐标点(Pb0obj,Ps2obj)物体分别在大机械臂基座标系下坐标，和在小机械臂第二关节坐标系下坐标
#DH参数：
#d为两连杆间的错位距离（平行距离）
#Tb0s0：小机械臂基座标系到大机械臂基坐标系的转换矩阵，即以大机械臂基坐标系为参考
#Ts0s1：小机械臂第一关节坐标系到小机械臂基坐标系的转换矩阵，即以小机械臂基坐标系为参考
#Ts1s2：小机械臂第二关节坐标系到小机械臂第一关节坐标系的转换矩阵，即以小机械臂第一关节坐标系为参考
#xsmallorg，ysmallorg，zsmallorg为小机械臂基座标的原点在大机械臂基座标下的坐标数据
#
#
#详细的理论推理说明，详见机械臂跟随系统.docx文件
#########################################################################
def transformSRendtoBRbase(Ps2obj,theta):
    """
    从小机械臂末端坐标系到大机械臂“织女”基座标系的坐标转换函数
    固定内部参数：（取决于小机械臂的机械结构）
    d：
    l1：
    l2：
    :param Ps2obj: 物体在小机械臂末端坐标系下的坐标
    :param theta: 当前小机械臂的各个关节角
    :return: Pb0obj:物体在大机械臂“织女”基坐标系下的坐标
    """
    d = 1
    l1 = 1
    l2 = 2
    # x = 0
    # y = 0
    # z = 1
    theta1 = theta[0]
    theta2 = theta[1]
    #Ps2obj = mat([x,y,z,1]).T
    print(Ps2obj)
    xsmallorg = 1
    ysmallorg = 1
    zsmallorg = 1
    Tb0s0 = mat([[1,0,0,xsmallorg],
            [0,1,0,ysmallorg],
            [0,0,1,zsmallorg],
            [0,0,0,1]])

    Ts0s1 = mat([[cos(theta1),-sin(theta1),0,0],
           [sin(theta1),cos(theta1),0,0],
           [0,             0,       1,0],
           [0,             0,       0,1]])

    Ts1s2 = mat([[sin(theta2-pi/2),0,sin(pi-theta2),-l2*cos(theta2-pi/2)],
           [0,1,0,d],
           [cos(theta2-pi/2),0,cos(pi-theta2),l1+l2*sin(theta2-pi/2)],
           [0,             0,       0,1]])

    Pb0obj = Tb0s0 * Ts0s1 * Ts1s2 * Ps2obj
    print("output the conclusion:")
    print(Pb0obj)
    print("output the conclusion1:")
    print(Pb0obj[0,0])
    return Pb0obj

#s = transformation()
#print(s)
#########################################################################
#写一个ip/tcp通讯程序（发送程序），向织女实时发送物体在织女基础坐标系下的位置数据，即Pb0obj
#当得知坐标后立即发送给大机械臂（织女）的控制器，控制其移动到物体的位置处
# from socket import *
# def ipcomunication():
#     server = socket()
#     server.bind(('127.0.0.1',8180))
#     server.listen()
#     conn,client_addr = server.accept()
#     Pb0obj = transformation()
#     x = Pb0obj[0,0]
#     y = Pb0obj[1,0]
#     z = Pb0obj[2,0]
#     p = 50
#     w = 60
#     r = 90
#     xstr = "x:" + str(x)
#     ystr = "y:" + str(y)
#     zstr = "z:" + str(z)
#     wstr = "w:" + str(w)
#     pstr = "y:" + str(p)
#     rstr = "z:" + str(r)
#     str1 = xstr + "," + ystr+","+zstr+","+wstr+","+pstr+","+rstr
#     data = str1.encode()
#     conn.send(data)
##############################################################

def transformCam2SRend(Pcamobj):
    """
    从相机坐标到小机械臂末端的坐标转换函数
    固定参数：相机的内外参数
    f:

    :param Pcamobj: 物体在相机坐标系下的坐标
    :return: Psrendobj:物体在机械臂末端坐标系下的坐标
    """
    Psrendobj = [1,1,1,1]
    return Psrendobj

def transformSRend2SRbase(Psrendobj,theta):
    """
    从小机械臂末端坐标系转换到小机械臂基座标系的坐标转换函数
    内部固定参数：
    d：
    l1：
    l2：
    :param Psrendobj: 物体在小机械臂末端坐标系下的坐标
    :param theta: 小机械臂的各个关节角，此处为二自由度（theta1，theta2）
    :return: Ps0obj：物体在小机械臂基坐标系下的坐标
    """
    d = 1
    L1 = 1
    L2 = 2
    theta1 = theta[0]
    theta2 = theta[1]
    Ts0s1 = mat([[cos(theta1), -sin(theta1), 0, 0],
                 [sin(theta1), cos(theta1), 0, 0],
                 [0, 0, 1, 0],
                 [0, 0, 0, 1]])

    Ts1s2 = mat([[sin(theta2 - pi / 2), 0, sin(pi - theta2), -L2 * cos(theta2 - pi / 2)],
                 [0, 1, 0, d],
                 [cos(theta2 - pi / 2), 0, cos(pi - theta2), L1 + L2 * sin(theta2 - pi / 2)],
                 [0, 0, 0, 1]])
    Ps0obj = Ts0s1*Ts1s2*Psrendobj
    return Ps0obj

def transformSRbase2BRbase(Ps0obj):
    """
    从小机械臂基坐标系转换到大机械臂“织女”基座标系的坐标转换函数
    函数内部固定参数：（小机械臂基座标系的原点在大机械臂基座标系下的坐标，取决于两机械臂的相对空间位置）
    xsmall:
    ysmall:
    zsmall:
    :param Ps0obj: 物体在小机械臂基坐标系下的坐标
    :return:Pb0obj：物体在大机械臂“织女”基坐标系下的坐标
    """
    xsmallorg = 1
    ysmallorg = 1
    zsmallorg = 1
    Tb0s0 = mat([[1, 0, 0, xsmallorg],
                 [0, 1, 0, ysmallorg],
                 [0, 0, 1, zsmallorg],
                 [0, 0, 0, 1]])
    Pb0obj = Tb0s0*Ps0obj
    return Pb0obj