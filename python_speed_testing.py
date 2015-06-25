# Ben Sandeen
# This is a little file I started to benchmark different ways of doing equivalent
# things in Python (almost exclusively inside loops).  It has grown over the past
# year or so to become a relatively large file, nigh 900 lines, although much of
# this is just the code used to print the times so I could figure out the quickest
# way to do things easily.  I'm sure I've made some blunders in here, but I haven't
# yet had the opportunity to go through this file thoroughly to rectify an mistakes,
# primarily in which I may be comparing two non-equivalent means to an end.  And
# for clarity, "equivalent" here simply means the output is either identical or 
# could be made identical by casting to a different data type (eg: numpy arrays
# and Python lists (and even sets, to a lesser extent) are considered "equivalent")

import time
totalTime = time.clock()

import random
import math
from math import log
from math import *
import operator
try:
	import numpy as np
except:
	pass

# How to use lambdas (to replace simple functions):
# ex. function:
# def square(x):
  	# return x**2
# 1) initialize lambda:
# square = lambda x: x**2
# 2) use the lambda just like a function:
# square(6) [outputs 36, unsurprisingly]

# measure process time
# """
# ##########################################

# # 5TH (~1/3 as fast as other three)
# t0 = time.clock()
# for i in range(1000000):
# 	random.gauss(0,5)
# print time.clock() - t0

#2ND
# t0 = time.clock()
# for i in range(1000000):
#         np.random.normal(0,5)
# print time.clock() - t0

# #3RD
# t0 = time.clock()
# i = 0
# while i < 1000000:
#         np.random.normal(0,5)
# 	i += 1
# print time.clock() - t0

# #1ST
# t0 = time.clock()
# for i in xrange(1000000):
#         np.random.normal(0,5)
# print time.clock() - t0

# #4TH (~1/3 as fast as fastest 3)
# t0 = time.clock()
# for i in xrange(1000000):
#     random.gauss(0,5)
# print time.clock() - t0

##########################################

# #2ND
# t0 = time.clock()
# for i in xrange(1000000):
#     ''.join('test')
# print time.clock() - t0

# #1ST ~25 faster than 2ND
# t0 = time.clock()
# for i in xrange(1000000):
#     ''+'test'
# print time.clock() - t0

##########################################

# #2ND
# t0 = time.clock()
# for i in xrange(1000000):
#     x = math.pi
# print time.clock() - t0

# #1ST ~33% faster than 2ND
# t0 = time.clock()
# p = math.pi
# for i in xrange(1000000):
#     x = p
# print time.clock() - t0

##########################################

# #3RD ~17% faster than 4TH
# t0 = time.clock()
# for i in xrange(10000):
# 	for i in xrange(100):
# 	    x = math.exp(i*3)
# print time.clock() - t0

# #2ND ~10% faster than 3RD
# t0 = time.clock()
# e = math.exp(1)
# for i in xrange(10000):
# 	for i in xrange(100):
# 	    x = e**(i*3)
# print time.clock() - t0

# #4TH
# t0 = time.clock()
# e = math.exp(1)
# for i in xrange(10000):
# 	for i in xrange(100):
# 	    x = pow(e,(i*3))
# print time.clock() - t0

# #1ST ~3% faster than 2ND
# t0 = time.clock()
# e = math.exp
# for i in xrange(10000):
# 	for i in xrange(100):
# 	    x = e(i*3)
# print time.clock() - t0

##########################################

# #2ND ~10% faster than 3RD
# t0 = time.clock()
# e = math.exp(1)
# L = [pow(e,(i/10000)) for i in xrange(1000000)]
# print time.clock() - t0

# #1ST ~27% faster than 2ND
# t0 = time.clock()
# e = math.exp(1)
# L = [e**(i/10000) for i in xrange(1000000)]
# print time.clock() - t0

# #4TH
# t0 = time.clock()
# e = math.exp(1)
# #L = np.zeros(1000000)
# L = np.array([e**(i/10000) for i in xrange(1000000)])
# print time.clock() - t0

# #3RD ~2% faster than 4TH
# t0 = time.clock()
# e = math.exp(1)
# L = np.zeros(1000000)
# for i in xrange(1000000):
#     L[i] = e**(i/10000)
# print time.clock() - t0

##########################################

# #1ST (by a factor of ~13)
# from math import log
# t0 = time.clock()
# for i in xrange(1,1000000):
#     log(i)#1000)
# print time.clock() - t0

# #2ND
# t0 = time.clock()
# for i in xrange(1,1000000):
#     np.log(i)#1000)
# print time.clock() - t0

##########################################

# #2ND ~4X faster than 3RD
# t0 = time.clock()
# for i in xrange(1,1000000):
#     math.sqrt(i)
# print time.clock() - t0

# #1ST ~32% faster than 2ND
# sq = math.sqrt
# t0 = time.clock()
# for i in xrange(1,1000000):
#     sq(i)
# print time.clock() - t0

# #4TH
# t0 = time.clock()
# for i in xrange(1,1000000):
#     np.sqrt(i)
# print time.clock() - t0

# #3RD ~6% faster than 4TH
# s=np.sqrt
# t0 = time.clock()
# for i in xrange(1,1000000):
#     s(i)
# print time.clock() - t0

#############################################

# #3RD ~10% faster than 4TH
# t0 = time.clock()
# for i in xrange(1,1000000):
#     i**2
# print time.clock() - t0

# #1ST ~18% faster than 2ND
# t0 = time.clock()
# for i in xrange(1,1000000):
#     pow(i,2)
# print time.clock() - t0

# #4TH
# t0 = time.clock()
# f = lambda x: x**2
# for i in xrange(1,1000000):
#     f(i)
# print time.clock() - t0

# #2ND ~3.3X faster than 3RD
# t0 = time.clock()
# f = lambda x: x*x
# for i in xrange(1,1000000):
#     f(i)
# print time.clock() - t0

#########################################

# #2nd
# t0 = time.clock()
# i = 0
# while True:
#     pow(i,2)
#     i += 1
#     if i > 10000000:
#         break
# print time.clock() - t0

# #1st ~13% faster than 2ND!
# t0 = time.clock()
# i = 0
# while 1:
#     pow(i,2)
#     i += 1
#     if i > 10000000:
#         break
# print time.clock() - t0

#########################################

# #1st BY A FACTOR OF ABOUT 170!!!!!!!!!!!!!!!!!!!!
# t0 = time.clock()
# i = 0
# S = set([i])
# while 1:
#     if 10000 not in S:
#         S.add(i)
#         i += 1
#     else:
#         while len(S) > 0:
#             S.pop()
#         break
# print time.clock() - t0

# #2ND
# t0 = time.clock()
# i = 0
# L = [i]
# while 1:
#     if 10000 not in L:
#         L.append(i)
#         i += 1
#     else:
#         while len(L) > 0:
#             L.pop()
#         break
# print time.clock() - t0

##################################

#2ND
# t0 = time.clock()
# a = []
# for i in xrange(10000000):
#     a.append(i)
# print time.clock() - t0

# #1ST Faster by ~15%
# t0 = time.clock()
# a = []
# appender = a.append
# for i in xrange(10000000):
#     appender(i)
# print time.clock() - t0

####################################

# #4TH
# t0 = time.clock()
# for i in xrange(100000):
#     for Nchars in xrange(10):
#         if Nchars>8:
#           Nticks=3
#         elif Nchars>5:
#           Nticks=4
#         elif Nchars>4:
#           Nticks=6
#         else:
#           Nticks=6
# print time.clock() - t0

# #TIE 2ND ~10% faster than 4TH
# t0 = time.clock()
# for i in xrange(100000):
#     for Nchars in xrange(10):
#         if Nchars>4:
#             if Nchars>5:
#                 if Nchars>8:
#                     Nticks=3
#                 else:
#                     Nticks=4
#             else:
#                Nticks=6
#         else:
#             Nticks=6
# print time.clock() - t0

# #TIE 2ND ~10% faster than 4TH
# t0 = time.clock()
# for i in xrange(100000):
#     for Nchars in xrange(10):
#         if Nchars>8:
#             Nticks=3
#         else:
# 	        if Nchars>5:
# 	        	Nticks=4
# 	        elif Nchars>4:
# 	        	Nticks=6
# print time.clock() - t0

# #1ST ~1% faster than 2ND
# t0 = time.clock()
# for i in xrange(100000):
#     for Nchars in xrange(10):
#         if Nchars>8:
#             Nticks=3
#         else:
# 	        if Nchars>5:
# 	        	Nticks=4
# 	        else:
# 	        	Nticks=6
# print time.clock() - t0

#################################

# #4TH
# t0 = time.clock()
# a = 1
# b = 2
# for i in xrange(1000000):
#     c = a + b
#     d = c * a
# print(time.clock() - t0)

# #3RD ~2% faster than 4TH
# t0 = time.clock()
# a = 1
# b = 2
# for i in xrange(1000000):
#     d = a + b
#     d = d * a
# print(time.clock() - t0)

# #2ND ~2% faster than 3RD
# t0 = time.clock()
# a = 1
# b = 2
# for i in xrange(1000000):
#     d = a + b
#     d *= a
# print(time.clock() - t0)

# #1ST ~24% faster than 2ND
# t0 = time.clock()
# a = 1
# b = 2
# for i in xrange(1000000):
#     d = (a + b) * a
# print(time.clock() - t0)

################################

# #2ND ~3% faster than 3RD
# t0 = time.clock()
# a = 2.0
# for i in xrange(10000000):
#     d = a / 2
# print(time.clock() - t0)

# # ####
# # # these 3 blocks are to ensure that I wasn't going insane; it appears that, in
# # # python, given the option to divide a float by an int, an int by a float, or a
# # # float by a float, we ought to pick the last option, then the 2ND, and then the
# # # 1ST (in order of decreasing performance).  Particularly surprising is that the
# # # first 2 options differ by a non-negligible amount (about 4% (the 3RD option,
# # # the fastest, is about 7% faster than the 2ND))

# # t0 = time.clock()
# # for i in xrange(10000000):
# #     d = 2 / 2.0
# # print(time.clock() - t0)

# # t0 = time.clock()
# # for i in xrange(10000000):
# # 	d = 2.0 / 2
# # print(time.clock() - t0)

# # t0 = time.clock()
# # for i in xrange(10000000):
# # 	d = 2.0 / 2.0
# # print(time.clock() - t0)
# # ####

# #4TH
# t0 = time.clock()
# a = 2
# for i in xrange(10000000):
#     d = a / 2.0
# print(time.clock() - t0)

# #3RD ~1% faster than 4TH
# t0 = time.clock()
# a = 2
# for i in xrange(10000000):
#     d = a *.5
# print(time.clock() - t0)

# #1ST ~2% faster than 2ND
# t0 = time.clock()
# a = 2
# for i in xrange(10000000):
#     d = .5 * a
# print(time.clock() - t0)

###################################

# #TIE for 1ST
# t0 = time.clock()
# a = 2
# for i in xrange(1000000):
#     d = a << 1
# print(time.clock() - t0)

# #TIE for 1ST
# t0 = time.clock()
# a = 2
# for i in xrange(1000000):
#     d = a * 2
# print(time.clock() - t0)

# #6TH
# t0 = time.clock()
# a = 2
# for i in xrange(1000000):
#     d = a * 2.0
# print(time.clock() - t0)

# #TIE for 1ST
# t0 = time.clock()
# a = 2
# for i in xrange(1000000):
#     d = 2 * a
# print(time.clock() - t0)

# #5TH slightly but consistently faster than 6TH
# t0 = time.clock()
# a = 2
# for i in xrange(1000000):
#     d = 2.0 * a
# print(time.clock() - t0)

# #TIE for 1ST
# t0 = time.clock()
# a = 2
# for i in xrange(1000000):
#     d = a + a
# print(time.clock() - t0)

################################

# # this section isn't really comparing speed, but rather shows how one can call
# # functions from within a list by selecting the desired element of the list and
# # then passing its arguments to it  

# def addone(x):
# 	print x+100
# def addtwo(x):
# 	print x+200

# #1ST ~twice as fast as 2ND
# t0 = time.clock()
# a = 0
# summ = 0
# for i in xrange(100):
#     if a:
#     	print summ+1
#     else:
#     	print summ+2
#     a = ~a
# print(time.clock() - t0)

# #2ND
# t0 = time.clock()
# a = 0
# summ = 0
# for i in xrange(100):
#     [addone,addtwo][a](summ) # creates list of functions, then calls the function
#     					# at index a, then passes summ as its input
#     a = ~a
# print(time.clock() - t0)

# ####################################

# # 3RD ~2X slower than bitwise shifts (below)
# t0 = time.clock()
# for j in xrange(1000000):
# 	for i in xrange(10):
# 	    x = pow(2,(i))
# print time.clock() - t0

# # 2ND
# t0 = time.clock()
# for j in xrange(1000000):
# 	for i in xrange(10):
# 	    x = 2**(i)
# print time.clock() - t0

# # 1ST ~12% faster than a**b function
# t0 = time.clock()
# for j in xrange(1000000):
# 	for i in xrange(10):
# 	    x = 2<<((i))
# print time.clock() - t0

####################################

# #4TH ~20% faster than 5TH
# t0 = time.clock()
# i = 0
# for i in xrange(10000000):
#     x = i
# print time.clock() - t0

# #5TH ~50% faster than 6TH
# t0 = time.clock()
# i = 0
# for i in range(10000000):
#     x = i
# print time.clock() - t0

# #6TH
# t0 = time.clock()
# i = 0
# while i <= 10000000:
#     x = i
#     i+=1
# print time.clock() - t0

# #3RD ~40% faster than 4TH
# t0 = time.clock()
# i = 0
# while i <= 10000000:
#     x = i
#     x = i+1
#     x = i+2
#     x = i+3
#     x = i+4
#     x = i+5
#     x = i+6
#     x = i+7
#     x = i+8
#     x = i+9
#     x = i+10
#     x = i+11
#     x = i+12
#     x = i+13
#     x = i+14
#     x = i+15
#     x = i+16
#     x = i+17
#     x = i+18
#     x = i+19
#     x = i+20
#     x = i+21
#     x = i+22
#     x = i+23
#     x = i+24
#     x = i+25
#     i += 26
# print time.clock() - t0

# #2ND ~33% faster than 3RD
# t0 = time.clock()
# i = 0
# while i <= 10000000:
#     x = i
#     x = i+1
#     x = i+2
#     x = i+3
#     x = i+4
#     x = i+5
#     x = i+6
#     x = i+7
#     x = i+8
#     x = i+9
#     x = i+10
#     x = i+11
#     x = i+12
#     x = i+13
#     x = i+14
#     x = i+15
#     x = i+16
#     x = i+17
#     x = i+18
#     x = i+19
#     x = i+20
#     x = i+21
#     x = i+22
#     x = i+23
#     x = i+24
#     x = i+25
#     x = i+26
#     x = i+27
#     x = i+28
#     x = i+29
#     x = i+30
#     x = i+31
#     x = i+32
#     x = i+33
#     x = i+34
#     x = i+35
#     x = i+36
#     x = i+37
#     x = i+38
#     x = i+39
#     x = i+40
#     x = i+41
#     x = i+42
#     x = i+43
#     x = i+44
#     x = i+45
#     x = i+46
#     x = i+47
#     x = i+48
#     x = i+49
#     x = i+50
#     x = i+51
#     i += 52
# print time.clock() - t0

# #1ST ~4% faster than 2ND
# t0 = time.clock()
# i = 0
# while i <= 10000000:
#     x = i
#     x = i+1
#     x = i+2
#     x = i+3
#     x = i+4
#     x = i+5
#     x = i+6
#     x = i+7
#     x = i+8
#     x = i+9
#     x = i+10
#     x = i+11
#     x = i+12
#     x = i+13
#     x = i+14
#     x = i+15
#     x = i+16
#     x = i+17
#     x = i+18
#     x = i+19
#     x = i+20
#     x = i+21
#     x = i+22
#     x = i+23
#     x = i+24
#     x = i+25
#     x = i+26
#     x = i+27
#     x = i+28
#     x = i+29
#     x = i+30
#     x = i+31
#     x = i+32
#     x = i+33
#     x = i+34
#     x = i+35
#     x = i+36
#     x = i+37
#     x = i+38
#     x = i+39
#     x = i+40
#     i += 41
# print time.clock() - t0

# # 3RD faster than 4TH place by ~40%
# t0 = time.clock()
# i = 0
# for i in range(0,10000000,26):
#     x = i
#     x = i+1
#     x = i+2
#     x = i+3
#     x = i+4
#     x = i+5
#     x = i+6
#     x = i+7
#     x = i+8
#     x = i+9
#     x = i+10
#     x = i+11
#     x = i+12
#     x = i+13
#     x = i+14
#     x = i+15
#     x = i+16
#     x = i+17
#     x = i+18
#     x = i+19
#     x = i+20
#     x = i+21
#     x = i+22
#     x = i+23
#     x = i+24
#     x = i+25
# print time.clock() - t0

#################################

# L = []
# for i in xrange(1000):
#     L.append(i)

# # 2ND This is surprisingly marginally slower
# # However, this one is faster when len(L) < about 1000 
# t0 = time.clock()
# for i in L:
#       x = 2**(i)
# print time.clock() - t0

# # 1ST no statistically significant advantage, but it is faster
# t0 = time.clock()
# for i in xrange(len(L)):
#       x = 2**L[i]
# print time.clock() - t0

#################################

# L = []
# for i in xrange(109900):
#     L.append(i)

# #1ST from about 100 times faster when len(L) is about 100 to
# # about 500 times when len(L) is around 10^5
# t0 = time.clock()
# for i in xrange(len(L)):
#       x = L[i]*i
# print time.clock() - t0

# #2ND not a chance
# t0 = time.clock()
# for i in L:
#       x = i*(L.index(i))
# print time.clock() - t0

#################################

# #2ND
# t0 = time.clock()
# for i in xrange(10000000):
# 	if (i > 9000000 and i %2 ==0):
# 		a=i
# print(time.clock() - t0)

# #1ST always faster, but by how much depends on the proportion of loops that 
# # are prevented from reaching the innermost loop
# t0 = time.clock()
# for i in xrange(10000000):
# 	if i > 9000000:
# 		if i %2 ==0:
# 			a=i
# print(time.clock() - t0)

#################################

# #2ND ~5% slower than the 3RD
# t0 = time.clock()
# for i in range(10000000):
# 	i=i+i
# print(time.clock() - t0)

# #1ST slightly faster than 2ND
# t0 = time.clock()
# for i in range(10000000):
# 	i=i*2
# print(time.clock() - t0)

# #3RD
# t0 = time.clock()
# for i in range(10000000):
# 	i=i<<1
# print(time.clock() - t0)

#################################

# #1ST full second faster than other two (~2.2s to ~3.3s)
# L=[]
# t0 = time.clock()
# for i in range(0,10000000,10):
# 	L.extend([i,i+1,i+2,i+3,i+4,i+5,i+6,i+7,i+8,i+9])
# print(time.clock() - t0)

# #3RD 
# L.clear()
# t0 = time.clock()
# for i in range(10000000):
# 	L.append(i)
# print(time.clock() - t0)

# #2ND a tidge faster than 3RD
# L.clear()
# S=set()
# t0 = time.clock()
# for i in range(10000000):
# 	S.add(i)
# print(time.clock() - t0)

#################################

# L=[]
# a=L.append
# for i in xrange(0,10000000):
# 	a(i)

# #2ND actually slower by ~12.5%
# t0 = time.clock()
# x=list(np.array(L)*2)
# print(time.clock() - t0)

# #1ST
# t0 = time.clock()
# for i in xrange(len(L)):
# 	L[i]*=2
# print(time.clock() - t0)

#################################

# L=[]
# a=L.append
# for i in xrange(0,100000):
# 	a(i)

# #1ST faster for small enough lists, but then loses precision, while np doesn't
# t0 = time.clock()
# print('reg',sum(L))
# print(time.clock() - t0)

# #2ND
# t0 = time.clock()
# print('np',np.sum(L))
# print(time.clock() - t0)

# #3RD Barely slower than 2ND
# # HOWEVER, IT RETURNS A LIST OF THE SUM OF ALL ELEMENTS PRIOR TO THE CURRENT POINT IN THE LIST,
# # RATHER THAN ONLY THE SUM OF ALL THE ELEMENTS IN THE LIST
# t0 = time.clock()
# print('npcum',np.cumsum(L))
# print(time.clock() - t0)

#################################

# d= {}
# for i in xrange(0,100000):
# 	d[i]=i

# #2ND slightly slower
# t0 = time.clock()
# for key in d.keys():
# 	d[key]+=1
# print(time.clock() - t0)

# #1ST
# t0 = time.clock()
# for key in d:
# 	d[key]+=1
# print(time.clock() - t0)

#################################

# L=[]
# for i in xrange(1,10000):
# 	L.append(i)

# logger = np.vectorize(math.log)

# #2ND slightly slower
# t0 = time.clock()
# [log(i) for i in L]	
# print(time.clock() - t0)

# #1ST
# t0 = time.clock()
# list(logger(L))
# print(time.clock() - t0)

# #################################

# L=[]
# for i in xrange(1,100001):
# 	L.append(i)

# #1ST
# t0 = time.clock()
# for i in xrange(10000,0,-2):
# 	L.pop(i)
# print(time.clock() - t0)

# for i in xrange(1,100001):
# 	L.append(i)

# #2ND twice as slow
# t0 = time.clock()
# for i in xrange(10000,0,-2):
# 	del L[i]
# print(time.clock() - t0)

#################################

# L=[]
# for i in xrange(1,100001):
# 	L.append(i)

# #1ST
# t0 = time.clock()
# sum(L)
# print(time.clock() - t0)

# # lol doesn't actually work: operator.add() takes only two inputs
# t0 = time.clock()
# operator.add(*L)
# print(time.clock() - t0)

#################################

# t0 = time.clock()
# L=[]
# for i in xrange(1,10000001):
# 	L.append(i)
# print(time.clock() - t0)

# # somehow faster than creating the list in increasing order
# t0 = time.clock()
# M=[]
# for i in reversed(xrange(1,10000001)):
# 	M.append(i)
# print(time.clock() - t0)
# #########
# # it looks like numpy is is about 100x faster at creating these arrays
# # than regular python is at creating equivalent lists
# t0 = time.clock()
# N = np.arange(1,10000001)
# print(time.clock() - t0)

# t0 = time.clock()
# P = np.arange(10000001,1,-1) # gives reversed array
# print(time.clock() - t0)
# #########
# #1ST ~40% faster using the python lists
# t0 = time.clock()
# zip(L,M)
# # print zip(L[:10],M[:10])
# print(time.clock() - t0)

# #2ND
# t0 = time.clock()
# np.column_stack((L,M))
# # print np.column_stack((L[:10],M[:10]))
# print(time.clock() - t0)

# #########
# #2ND
# t0 = time.clock()
# zip(N,P)
# # print zip(N[:10],P[:10])
# print(time.clock() - t0)

# #1ST over 100x faster when both use numpy arrays
# t0 = time.clock()
# np.column_stack((N,P))
# # print np.column_stack((N[:10],P[:10]))
# print(time.clock() - t0)

# uncomment the commented prints to see that these are both indeed doing the
# exact same thing, giving the exact same results in all 4 cases

#################################

# # too close to call for the following 5 methodologies
# def sq(x):
# 	return x**2
# #TIE for 1ST
# t0 = time.clock()
# for i in xrange(1000000):
# 	sq(i)
# print(time.clock() - t0)

# #TIE for 1ST
# t0 = time.clock()
# map(sq, xrange(1000000))
# print(time.clock() - t0)

# #TIE for 1ST
# square = lambda x: x**2
# t0 = time.clock()
# for i in xrange(1000000):
# 	square(i)
# print(time.clock() - t0)

# #TIE for 1ST
# t0 = time.clock()
# map(square, xrange(1000000))
# print(time.clock() - t0)

# #TIE for 1ST
# t0 = time.clock()
# map(lambda x:x**2, xrange(1000000))
# print(time.clock() - t0)

#################################


#################################
print(time.clock() - totalTime)

