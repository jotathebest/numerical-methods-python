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

		if (show_result):
			print "max iterations passed, root found at: {0}".format(str(xr))
		return xr