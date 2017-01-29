import objectiveFunctions as obj
import rootsMethods as roots

roots.bisection_2d(15, 14, obj.paracaidist_speed, tol_error = 0.5, show_result = True, max_iter = 4)