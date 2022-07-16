import matplotlib.pyplot as plt
import time
import math

global v0, ang, x0, y0, g, m, k, c1, c2, c3, c4



#Definição de constantes:
g = 9.807
m = 0.15
k = 0.66

#Dados retirados da análise do vídeo, no software Tracker:
v0 = 55.0
ang = 17.0
x0 = 4.42
y0 = 1.36

#Constantes de integração:
c1 = -(1/(v0*math.cos(ang*math.pi/180.0)))
c2 = ((math.atan((v0*math.sin(ang*math.pi/180.0))/math.sqrt((m*g)/k)))/math.sqrt(m*g*k))
c3 = x0
c4 = y0



#Funções:
def vx(t):
    return -(m/((c1*m)-(k*t)))
def vy(t):
    return (math.sqrt((m*g)/k)*math.tan(math.sqrt((g*k)/m)*((c2*m)-t)))
def x(t):
    



#Simulações
t0 = time.time()
while(True):
    t = (time.time()-t0)
    print(vy(t))
