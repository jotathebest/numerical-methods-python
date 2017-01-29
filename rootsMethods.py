'''
The MIT License (MIT)

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files
(the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge,
publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Author: Jose García
reyes2000jose.wix.com/resume
reyes2000jose@gmail.com

'''


def bisection_2d(xu, xl, f, tol_error=0.1, max_iter=100, show_result=False): # Bisection
	iter = 0

	#Initial verification

	if (f(xu)*f(xl))>0 and iter == 0:
		if (show_result):
			print "Initial points are not up and low of the searched root"
		return None

	#First iteration

	xr = (xu+xl)/float(2)
	root_result = f(xl)*f(xr)
	if (root_result<0):
			xu = xr
	elif (root_result>0):
		xl=xr
	else:
		if (show_result):
			print "Root exact found at: {0}".format(str(xr))
		return xr
	iter = iter+1

	#Loop

	for i in range(max_iter):
		xrold = xr
		xr = (xu+xl)/float(2)
		root_result = f(xl)*f(xr)
		if (root_result<0):
			xu = xr
			ea = abs((xr-xrold))*100/xr
		elif (root_result>0):
			xl=xr
			ea = abs((xr-xrold))*100/xr
		else:
			if (show_result):
				print "Root exact found at: {0}".format(str(xr))
			return xr
		iter = iter+1

		if (ea<tol_error):
			if (show_result):
				print "max tolerance error passed, root found at: {0}".format(str(xr))
			return xr

		if (iter > max_iter):
			if (show_result):
				print "max iterations passed, root found at: {0}".format(str(xr))
			return xr


def mod_false_pos(xu, xl, f, tol_error=0.1, max_iter=100, show_result=False): # Modified False Position
	iter = 0

	#Initial verification
	if (f(xu)*f(xl))>0 and iter == 0:
		if (show_result):
			print "Initial points are not up and low of the searched root"
		return None

	#First iteration

	fl = f(xl)
	fu = f(xu)
	xr = xu-fu*(xl-xu)/float((fl-fu))
	root_result = f(xl)*f(xr)
	il , iu = 0, 0
	if (root_result<0):
			xu = xr
			fu = f(xu)
			iu = 0
			il = il+1
			if (il>=2):
				fl = fl/float(2)
	elif (root_result>0):
		xl=xr
		fl = f(xl)
		il = 0
		iu = iu+1
		if (iu>=2):
			fu = fu/float(2)
	else:
		if (show_result):
			print "Root exact found at: {0}".format(str(xr))
		return xr
	iter = iter+1

	#Loop

	for i in range(max_iter):
		xrold = xr
		xr = xu-fu*(xl-xu)/float((fl-fu))
		root_result = f(xl)*f(xr)
		if (root_result<0):
				xu = xr
				fu = f(xu)
				iu = 0
				il = il+1
				if (il>=2):
					fl = fl/float(2)
		elif (root_result>0):
			xl=xr
			fl = f(xl)
			il = 0
			iu = iu+1
			if (iu>=2):
				fu = fu/float(2)
		else:
			if (show_result):
				print "Root exact found at: {0}".format(str(xr))
			return xr
		iter = iter+1
		ea = abs((xr-xrold))*100/xr

		if (ea<tol_error):
			if (show_result):
				print "max tolerance error passed, root found at: {0}, ea: {1}".format(str(xr), str(ea))
			return xr

		if (iter>max_iter):
			if (show_result):
				print "max iterations passed, root found at: {0} with an ea of {1}".format(str(xr), str(ea))
			return xr