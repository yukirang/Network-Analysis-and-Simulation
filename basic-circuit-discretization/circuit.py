#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 21:31:54 2019

@author: rangke
"""
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['lines.linewidth'] = 1

E = 10;
R = 10;
L = 20;
T = 10;
V1 =[0];
I1 = [0];
V2 = [0];
I2 = [0];

Vb1 =[0];
Ib1 = [0];
Vb2 = [0];
Ib2 = [0];
timeArr = np.arange(0, 10.1, 0.1);
delta = 0.1;

loop = get_loop();

# ∆t = 0.1 ms
for i in range(1,loop+1):
    I1.append((E*delta + V1[i-1]*delta + 2*L*I1[i-1])/(2*L+R*delta));
    V1.append(2*L*I1[i]/delta - V1[i-1] - 2*L*I1[i-1]/delta);


for i in range(1,loop+1):
    Ib1.append((E*delta + L*Ib1[i-1])/(L+R*delta));
    Vb1.append(L*(Ib1[i] - Ib1[i-1])/delta);
  
# ∆t = 0.8 ms
delta = 0.8;
loop = get_loop(); 
for i in range(1,loop+1):
    I2.append((E*delta + V2[i-1]*delta + 2*L*I2[i-1])/(2*L+R*delta));
    V2.append(2*L*I2[i]/delta - V2[i-1] - 2*L*I2[i-1]/delta);

for i in range(1,loop+1):
    Ib2.append((E*delta + L*Ib2[i-1])/(L+R*delta));
    Vb2.append(L*(Ib2[i] - Ib2[i-1])/delta);
    

plt.plot(get_timeArr(0.1),I1,'r',label='trapezoidal rule with ∆t1 = 0.1 ms');
plt.plot(get_timeArr(0.8),I2,'g',label='trapezoidal rule with ∆t1 = 0.8 ms');
plt.plot(get_timeArr(0.1),Ib1,'b--',label='backward Euler rule with ∆t2 = 0.1 ms');
plt.plot(get_timeArr(0.8),Ib2,'c--',label='backward Euler rule with ∆t2 = 0.8 ms');
plt.xlabel('t (ms)')
plt.ylabel('I (A)')
plt.legend();
plt.savefig("test",dpi=1000);
plt.show();

plt.plot(get_timeArr(0.1),V1,'r',label='trapezoidal rule with ∆t1 = 0.1 ms');
plt.plot(get_timeArr(0.8),V2,'g',label='trapezoidal rule with ∆t1 = 0.8 ms');
plt.plot(get_timeArr(0.1),Vb1,'b--',label='backward Euler rule with ∆t2 = 0.1 ms');
plt.plot(get_timeArr(0.8),Vb2,'c--',label='backward Euler rule with ∆t2 = 0.8 ms');
plt.xlabel('t (ms)')
plt.ylabel('V_L (V)')
plt.legend();
plt.savefig("test2",dpi=1000);
plt.show();

def get_loop():
    return int(T/delta);

def get_timeArr(de):
    return np.arange(0, 10.1, de);

