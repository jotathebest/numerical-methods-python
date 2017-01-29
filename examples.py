'''
The MIT License (MIT)

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files
(the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge
publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Author: Jose García
reyes2000jose.wix.com/resume
reyes2000jose@gmail.com

'''

import objectiveFunctions as obj
import rootsMethods as roots

'''
Example script. Please uncomment the example that you want to test
'''

#Example 5.3
#roots.bisection_2d(xu=15, xl=14, f=obj.paracaidist_speed, tol_error = 0.5, show_result = True, max_iter = 4)
#roots.mod_false_pos(xu=16, xl=12, f=obj.paracaidist_speed, tol_error=0.5, max_iter=100, show_result=True)

#Example 5.6
roots.mod_false_pos(xu=1.3, xl=0, f=obj.f_5_14, tol_error=0.5, max_iter=5, show_result=True)