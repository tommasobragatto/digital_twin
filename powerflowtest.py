import pandapower as pp
import json
import network_function_FdiPOLO_with_correct_coordinations2_LV

net = network_function_FdiPOLO_with_correct_coordinations2_LV.fdipolo_network()
pp.runpp(net,numba=False)

A=net.res_line.i_from_ka
print(A)