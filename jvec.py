
# VROOM!!! Vector Graphic Gacing
# Copyright 2003-2007 George Gonzalez
#
# This file is part of VROOM!!!
# 
# VROOM!!! is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
# 
# VROOM!!! is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with VROOM!!!; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

from math import sqrt, acos, pi

def unit( (a,b) ):
	f = 1/sqrt(a*a + b*b)
	return (f*a, f*b)

def mag( (a,b) ):
	f = sqrt(a*a + b*b)
	return f

def norm((x,y), w):
	return (-1*w*y, w*x)

def reverse((x,y)):
	return (-x, -y)

def add((a,b), (c,d)):
	return (a+c, b+d)

def diff((a,b), (c,d)):
	return (a-c, b-d)

def scale(a, (x,y)):
	return (a*x, a*y)

def dot( (x1,y1), (x2,y2) ):
	return (x1*x2 + y1*y2)

def cross( (x1,y1), (x2,y2) ):
	return y1*x2 - x1*y2

def angle((x0, y0), (x1, y1)): 
	if x0==0 and y0==0:
		return 0.0
	if x1==0 and y1==0:
		return 0.0
	d = dot( (x0, y0), (x1, y1))
	s = y0*x1 > x0*y1
	a = acos( d / (sqrt(x0*x0+y0*y0) * sqrt(x1*x1+y1*y1)) )
	if `a` == "nan":
		return pi
	a = a*(-1,1)[s]
	return a
