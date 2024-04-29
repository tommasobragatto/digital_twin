import pandapower as pp
import json
import network_function_FdiPOLO_with_correct_coordinations2

# import numba
# import network_function_FdiPOLO_with_correct_coordinations2
import subprocess

net = network_function_FdiPOLO_with_correct_coordinations2.fdipolo_network()
pp.runpp(net)

while True:
    inizio = time.time()
### INDIVIDUAL METERS ARE INVOKED IN ORDER TO COLLECT DATA ###
    subprocess.call(['python', "testMain.py"])
    

    ############################################                 #check manual for Active Power 
    # Load the JSON data from the file
    data_1 = json.load("received_1.json")
    all_p_values_1 = []     # Extract all "P" values from all lines
    all_q_values_1 = []     # Extract all "Q" values from all lines
    for line in data_1["Lines"]:
        all_p_values_1.extend(line["P"]["Value"])
        all_q_values_1.extend(line["Q"]["Value"])
    print("Sum of all P values across Tre T:", sum(all_p_values_1))
    print("Sum of all Q values across Tre T:", sum(all_q_values_1))
    net.load.p_mw.at[13] = sum(all_p_values_1)/1000000
    net.load.q_mvar.at[13] = sum(all_q_values_1)/1000000
    ############################################             
    # Load the JSON data from the file
    data_4 = json.load("received_4.json")
    all_p_values_4 = []     # Extract all "P" values from all lines
    all_q_values_4 = []     # Extract all "Q" values from all lines
    for line in data_4["Lines"]:
        all_p_values_4.extend(line["P"]["Value"])
        all_q_values_4.extend(line["Q"]["Value"])
    print("Sum of all P values across Siemens:", sum(all_p_values_4))
    print("Sum of all Q values across Siemens:", sum(all_q_values_4))
    net.load.p_mw.at[16] = sum(all_p_values_4)/1000000
    net.load.q_mvar.at[16] = sum(all_q_values_4)/1000000
    ############################################                  
    # Load the JSON data from the file
    data_5 = json.load("received_5.json")
    all_p_values_5 = []     # Extract all "P" values from all lines
    all_q_values_5 = []     # Extract all "Q" values from all lines
    for line in data_5["Lines"]:
        all_p_values_5.extend(line["P"]["Value"])
        all_q_values_5.extend(line["Q"]["Value"])
    print("Sum of all P values across Angelini:", sum(all_p_values_5))
    print("Sum of all Q values across Angelini:", sum(all_q_values_5))
    net.load.p_mw.at[5] = sum(all_p_values_5)/1000000
    net.load.q_mvar.at[5] = sum(all_q_values_5)/1000000
    ############################################              
    # Load the JSON data from the file
    data_6 = json.load("received_6.json")
    all_p_values_6 = []     # Extract all "P" values from all lines
    all_q_values_6 = []     # Extract all "Q" values from all lines
    for line in data_6["Lines"]:
        all_p_values_6.extend(line["P"]["Value"])
        all_q_values_6.extend(line["Q"]["Value"])
    print("Sum of all P values across Aviosuperficie:", sum(all_p_values_6))
    print("Sum of all Q values across Aviosuperficie:", sum(all_q_values_6))
    net.load.p_mw.at[1] = sum(all_p_values_6)/1000000
    net.load.q_mvar.at[1] = sum(all_q_values_6)/1000000
    ############################################                
    # Load the JSON data from the file
    data_7 = json.load("received_7.json")
    all_p_values_7 = []     # Extract all "P" values from all lines
    all_q_values_7 = []     # Extract all "Q" values from all lines
    for line in data_7["Lines"]:
        all_p_values_7.extend(line["P"]["Value"])
        all_q_values_7.extend(line["Q"]["Value"])
    print("Sum of all P values across Fontana di Polo:", sum(all_p_values_7))
    print("Sum of all Q values across Fontana di Polo:", sum(all_q_values_7))
    net.load.p_mw.at[6] = sum(all_p_values_7)/1000000
    net.load.q_mvar.at[6] = sum(all_q_values_7)/1000000
    ############################################

    print(data_7["Lines"][0]["V"]["Value"][0])
# bus_results = net.res_bus
# line_results = net.res_line
# load_results = net.res_load
# sgen_results = net.res_sgen
# 
# print("Bus Results:")
# print(net.res_bus)
# 
# print("\nLine Results:")
# print(net.res_line)
# 
# print("\nLoad Results:")
# print(net.res_load)
# 
# print("\nSynchronous Generator Results:")
# print(net.res_sgen)
# 
# print("\nExternal Grid Results:")
# print(net.res_ext_grid)
# 
# pp.plotting.simple_plot(net)

# Run the MQTT client





