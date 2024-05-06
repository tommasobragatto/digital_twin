import pandapower as pp
import json
import network_function_FdiPOLO_with_correct_coordinations2_LV
import time
import pygad
import numpy
import time
import csv
import matplotlib.pyplot as plt
from datetime import datetime
import paho.mqtt.client as mqtt

from datetime import datetime
import pandas as pd

import subprocess
import openpyxl

fig, ax = plt.subplots(3, 1, sharex=True)  # Create a figure with 3 subplots (3 rows, 1 column)

timestamps = numpy.linspace(0, 2 * numpy.pi, 100)
y = numpy.sin(timestamps)

line1, = ax[0].plot(timestamps, y)
line2, = ax[1].plot(timestamps, y)
line3, = ax[2].plot(timestamps, y)
ax[0].set_xlabel('X-axis')
ax[0].set_ylabel('Y-axis')

ax[0].set_title("Power(kW)")
ax[1].set_title("GA Fitness")
ax[2].set_title("Reverse Power Flow")


def update_plot():
    global timestamps, y0, y1, y2

    
    line1.set_xdata(timestamps)
    line1.set_ydata(y0)
    
    line2.set_xdata(timestamps)
    line2.set_ydata(y1)
    
    line3.set_xdata(timestamps)
    line3.set_ydata(y2)
    
    
    ax[0].relim()
    ax[0].autoscale_view()
    
    ax[1].relim()
    ax[1].autoscale_view()

    ax[2].relim()
    ax[2].autoscale_view()

    plt.draw()
    plt.pause(0.01)
 
broker= "185.131.248.7"  #Broker address
port = 1883                         #Broker port
user = "wisegrid"                    #Connection username
password = "wisegrid"            #Connection password
client = mqtt.Client()
client.username_pw_set(user, password=password)
client.connect(broker, port, 60)
json_object = {"d": 4,
      "dt": 4,
      "ts": 4,
      "q": 192}

attivo_flessibilita=False
MAX_TIME=5

net = network_function_FdiPOLO_with_correct_coordinations2_LV.fdipolo_network()
initial_population=[[0.0001,0.0001,0.0001,0.0001,0.0001,0.0001,0.0001,0.0001,0.0001,0.0001,1],[0.0001,0.0001,0.0001,0.0001,0.0001,0.0001,0.0001,0.0001,0.0001,0.0001,1],[0.0001,0.0001,0.0001,0.0001,0.0001,0.0001,0.0001,0.0001,0.0001,0.0001,1],[0.0001,0.0001,0.0001,0.0001,0.0001,0.0001,0.0001,0.0001,0.0001,0.0001,1],[0.0001,0.0001,0.0001,0.0001,0.0001,0.0001,0.0001,0.0001,0.0001,0.0001,1],[0.0001,0.0001,0.0001,0.0001,0.0001,0.0001,0.0001,0.0001,0.0001,0.0001,1],[0.0001,0.0001,0.0001,0.0001,0.0001,0.0001,0.0001,0.0001,0.0001,0.0001,1],[0.0001,0.0001,0.0001,0.0001,0.0001,0.0001,0.0001,0.0001,0.0001,0.0001,1],[0.0001,0.0001,0.0001,0.0001,0.0001,0.0001,0.0001,0.0001,0.0001,0.0001,1],[0.0001,0.0001,0.0001,0.0001,0.0001,0.0001,0.0001,0.0001,0.0001,0.0001,1]] #TODO

carichiSE = ["Siemens_2", "Tre_T_2", "Fontana_di_polo_2", "Tecnomultiservice", "Angelini"]   # Loads to be estimated
nodi_noti = ["23", "24", "18", "20", "19"] #nodi_noti in english means nodes_known


while True:
    inizio = time.time()
### INDIVIDUAL METERS ARE INVOKED IN ORDER TO COLLECT DATA ###
    #subprocess.call(['python', "testMain.py"])
    
    ####################################################################################################################################              
    ora_attuale = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    # Load the MV dataset
    file_path = "implement_MV.xlsx"
    df = pd.read_excel(file_path)
    # Get the current day of the week (Monday = 0, Sunday = 6) and current time
    current_day = datetime.now().weekday()
    current_time = datetime.now().replace(second=0, microsecond=0, minute=(datetime.now().minute // 15) * 15)
    # Calculate the index of the time interval in the dataset
    time_interval_index = current_day * 96 + current_time.hour * 4 + current_time.minute // 15
    
    ############################################                 #check manual for Active Power 
    # Load the JSON data from the file
    F = open("received_1.json")
    data_1 = json.load(F)
    all_p_values_1 = []     # Extract all "P" values from all lines
    all_q_values_1 = []     # Extract all "Q" values from all lines
    for line in data_1["Lines"]:
        all_p_values_1.extend(line["P"]["Value"])
        all_q_values_1.extend(line["Q"]["Value"])
    print("Sum of all P values across Tre T:", sum(all_p_values_1))
    print("Sum of all Q values across Tre T:", sum(all_q_values_1))
    net.load.p_mw[pp.get_element_index(net, "load", "Tre_T_1")] = sum(all_p_values_1)/1000000
    net.load.q_mvar.at[pp.get_element_index(net, "load", "Tre_T_1")] = sum(all_q_values_1)/1000000

# Extract active and reactive values for the calculated index
    P_TRET_max = df.iloc[time_interval_index]["P_TRET_max"]/1000000
    Q_TRET_max = df.iloc[time_interval_index]["Q_TRET_max"]/1000000
    P_TRET_min = df.iloc[time_interval_index]["P_TRET_min"]/1000000
    Q_TRET_min = df.iloc[time_interval_index]["Q_TRET_min"]/1000000
    ############################################             
    # Load the JSON data from the file
    F = open("received_3.json")
    data_3 = json.load(F)
    all_p_values_3 = []     # Extract all "P" values from all lines
    all_q_values_3 = []     # Extract all "Q" values from all lines
    for line in data_3["Lines"]:
        all_p_values_3.extend(line["P"]["Value"])
        all_q_values_3.extend(line["Q"]["Value"])
    print("Sum of all P values across Archimede:", sum(all_p_values_3))
    print("Sum of all Q values across Archimede:", sum(all_q_values_3))
    net.load.p_mw.at[pp.get_element_index(net, "load", "Archimede")] = sum(all_p_values_3)/1000000
    net.load.q_mvar.at[pp.get_element_index(net, "load", "Archimede")] = sum(all_q_values_3)/1000000  
    ############################################             
    # Load the JSON data from the file
    F = open("received_4.json")
    data_4 = json.load(F)
    all_p_values_4 = []     # Extract all "P" values from all lines
    all_q_values_4 = []     # Extract all "Q" values from all lines
    for line in data_4["Lines"]:
        all_p_values_4.extend(line["P"]["Value"])
        all_q_values_4.extend(line["Q"]["Value"])
    print("Sum of all P values across Siemens:", sum(all_p_values_4))
    print("Sum of all Q values across Siemens:", sum(all_q_values_4))
    net.load.p_mw.at[pp.get_element_index(net, "load", "Siemens_1")] = sum(all_p_values_4)/1000000
    net.load.q_mvar.at[pp.get_element_index(net, "load", "Siemens_1")] = sum(all_q_values_4)/1000000
    
    # Extract active and reactive values for the calculated index
    P_SIEMENS_6_max = df.iloc[time_interval_index]["P_SIEMENS_6_max"]/1000000
    Q_SIEMENS_6_max = df.iloc[time_interval_index]["Q_SIEMENS_6_max"]/1000000
    P_SIEMENS_6_min = df.iloc[time_interval_index]["P_SIEMENS_6_min"]/1000000
    Q_SIEMENS_6_min = df.iloc[time_interval_index]["Q_SIEMENS_6_min"]/1000000
    # Extract active and reactive values for the calculated index
    P_SIEMENS_1000_max = df.iloc[time_interval_index]["P_SIEMENS_1000_max"]/1000000
    Q_SIEMENS_1000_max = df.iloc[time_interval_index]["Q_SIEMENS_1000_max"]/1000000
    P_SIEMENS_1000_min = df.iloc[time_interval_index]["P_SIEMENS_1000_min"]/1000000
    Q_SIEMENS_1000_min = df.iloc[time_interval_index]["Q_SIEMENS_1000_min"]/1000000
    # Extract active and reactive values for the calculated index
    P_SIEMENS_P_max = df.iloc[time_interval_index]["P_SIEMENS_P_max"]/1000000
    Q_SIEMENS_P_max = df.iloc[time_interval_index]["Q_SIEMENS_P_max"]/1000000
    P_SIEMENS_P_min = df.iloc[time_interval_index]["P_SIEMENS_P_min"]/1000000
    Q_SIEMENS_P_min = df.iloc[time_interval_index]["Q_SIEMENS_P_min"]/1000000

    ############################################                  
    # Load the JSON data from the file
    F = open("received_5.json")
    data_5 = json.load(F)
    all_p_values_5 = []     # Extract all "P" values from all lines
    all_q_values_5 = []     # Extract all "Q" values from all lines
    for line in data_5["Lines"]:
        all_p_values_5.extend(line["P"]["Value"])
        all_q_values_5.extend(line["Q"]["Value"])
    print("Sum of all P values across Angelini:", sum(all_p_values_5))
    print("Sum of all Q values across Angelini:", sum(all_q_values_5))
    net.load.p_mw.at[pp.get_element_index(net, "load", "Angelini")] = sum(all_p_values_5)/1000000
    net.load.q_mvar.at[pp.get_element_index(net, "load", "Angelini")] = sum(all_q_values_5)/1000000
 
 
    o = open(r"ANGELINI_MEASURED.txt", "a")
    o.write("\n" + f"[{ora_attuale}];" + str(sum(all_q_values_5)/1000000))
    o.close()
    
    # Extract active and reactive values for the calculated index
    
    P_ANGELINI_max = df.iloc[time_interval_index]["P_ANGELINI_LV_max"]/1000000
    Q_ANGELINI_max = df.iloc[time_interval_index]["Q_ANGELINI_LV_max"]/1000000
    P_ANGELINI_min = df.iloc[time_interval_index]["P_ANGELINI_LV_min"]/1000000
    Q_ANGELINI_min = df.iloc[time_interval_index]["Q_ANGELINI_LV_min"]/1000000
       

    ############################################              
    # Load the JSON data from the file
    F = open("received_6.json")
    data_6 = json.load(F)
    all_p_values_6 = []     # Extract all "P" values from all lines
    all_q_values_6 = []     # Extract all "Q" values from all lines
    for line in data_6["Lines"]:
        all_p_values_6.extend(line["P"]["Value"])
        all_q_values_6.extend(line["Q"]["Value"])
    print("Sum of all P values across Aviosuperficie:", sum(all_p_values_6))
    print("Sum of all Q values across Aviosuperficie:", sum(all_q_values_6))
    net.load.p_mw.at[pp.get_element_index(net, "load", "Aviosuperficie")] = sum(all_p_values_6)/1000000
    net.load.q_mvar.at[pp.get_element_index(net, "load", "Aviosuperficie")] = sum(all_q_values_6)/1000000
    
    P_PV_PROD = data_6["Lines"][1]["P"]["Value"]
    P_PV_PROD = sum(P_PV_PROD)/1000000
    ############################################                
    # Load the JSON data from the file
    F = open("received_7.json")
    data_7 = json.load(F)
    all_p_values_7 = []     # Extract all "P" values from all lines
    all_q_values_7 = []     # Extract all "Q" values from all lines
    for line in data_7["Lines"]:
        all_p_values_7.extend(line["P"]["Value"])
        all_q_values_7.extend(line["Q"]["Value"])
    print("Sum of all P values across Fontana di Polo:", sum(all_p_values_7))
    print("Sum of all Q values across Fontana di Polo:", sum(all_q_values_7))
    net.load.p_mw.at[pp.get_element_index(net, "load", "Fontana_di_polo_1")] = sum(all_p_values_7)/1000000
    net.load.q_mvar.at[pp.get_element_index(net, "load", "Fontana_di_polo_1")] = sum(all_q_values_7)/1000000
    
    # Extract active and reactive values for the calculated index
    P_FDP_max = df.iloc[time_interval_index]["P_FDP_max"]/1000000
    Q_FDP_max = df.iloc[time_interval_index]["Q_FDP_max"]/1000000
    P_FDP_min = df.iloc[time_interval_index]["P_FDP_min"]/1000000
    Q_FDP_min = df.iloc[time_interval_index]["Q_FDP_min"]/1000000
    # konig
    # Extract active and reactive values for the calculated index
    P_TECHNO_max = df.iloc[time_interval_index]["P_TECHNO_max"]/1000000
    Q_TECHNO_max = df.iloc[time_interval_index]["Q_TECHNO_max"]/1000000
    P_TECHNO_min = df.iloc[time_interval_index]["P_TECHNO_min"]/1000000
    Q_TECHNO_min = df.iloc[time_interval_index]["Q_TECHNO_min"]/1000000
    ############################################    ## COLLECTION OF THE VOLTAGES FOR THE STATE ESTIMATION
    misure = [data_1["Lines"][0]["V"]["Value"][0], data_3["Lines"][0]["V"]["Value"][0], data_4["Lines"][0]["V"]["Value"][0], data_5["Lines"][0]["V"]["Value"][0], data_6["Lines"][0]["V"]["Value"][0], data_7["Lines"][0]["V"]["Value"][0]]
#### STATE ESTITMATION ##########    
    def fitness_func(ga_instance, solution, solution_idx):
        
        for i in range(len(carichiSE)-1):
            net.load.p_mw.at[pp.get_element_index(net, "load", carichiSE[i])] = float(solution[2 * i])
            net.load.q_mvar.at[pp.get_element_index(net, "load", carichiSE[i])] = float(solution[2 * i +1])
        df.loc[0, 'net.ext_grid.vm_pu'] =float(solution[2*len(carichiSE)])
        pp.runpp(net,numba=False)

        tensioni_calc, delta = [], []
        for i in range(len(nodi_noti)-1):
            tensione = net.res_bus.vm_pu.at[float(nodi_noti[i])]
            tensioni_calc.append(tensione)
            delta.append(float(misure[i]) - tensioni_calc[i]*230)
            print(delta)
        fitness = len(nodi_noti) / numpy.dot(delta, delta)
        print(fitness)
        return fitness


    fitness_function = fitness_func

    num_generations = 3
    num_parents_mating = 4
    sol_per_pop = 10
    num_genes = 11

    # Leggo i valori medi delle potenze che passano nei nodi 9, 10 e 11, così da fare una stima più accurata ed inserirli nel gene_space con + o - 20%
    h=time.localtime().tm_hour
    m=time.localtime().tm_min

    gene_space = [numpy.linspace(P_SIEMENS_6_min + P_SIEMENS_1000_min - P_PV_PROD*500/90 , P_SIEMENS_6_max + P_SIEMENS_1000_max - P_PV_PROD*500/90, 20), # carico Siemens_2, per la P faccio + e - il 10% della potenza nominale (50 kVA)
                  numpy.linspace(Q_SIEMENS_6_min + Q_SIEMENS_1000_min + Q_SIEMENS_P_min, Q_SIEMENS_6_max + Q_SIEMENS_1000_max + Q_SIEMENS_P_max, 10), # carico Siemens_2, per la Q faccio + e - il 5% della potenza nominale (50 kVA)
                  numpy.linspace(P_TRET_min , P_TRET_max, 20),  # carico Tre_T_2, per la P faccio + e - il 10% della potenza nominale(100 kVA)
                  numpy.linspace(Q_TRET_min , Q_TRET_max, 10), # carico Tre_T_2, per la Q faccio + e - il 5% della potenza nominale(100 kVA)
                  numpy.linspace(P_FDP_min, P_FDP_max, 20), # carico Fontana_di_polo_2, per la P faccio + e - il 10% della potenza nominale(160 kVA)
                  numpy.linspace(Q_FDP_min, Q_FDP_max, 10), # carico Fontana_di_polo_2, per la Q faccio + e - il 5% della potenza nominale(100 kVA)
                  numpy.linspace(P_TECHNO_min, P_TECHNO_max, 20), # carico Technomultiservice, per la P faccio + e - il 10% della potenza nominale(160 kVA)
                  numpy.linspace(Q_TECHNO_min, Q_TECHNO_max, 10), # carico  Technomultiservice, per la Q faccio + e - il 5% della potenza nominale(100 kVA)
                  numpy.linspace(P_ANGELINI_min, P_ANGELINI_max, 20), # carico Angelini, per la P faccio + e - il 10% della potenza nominale(160 kVA)
                  numpy.linspace(Q_ANGELINI_min, Q_ANGELINI_max, 10), # carico Angelini, per la Q faccio + e - il 5% della potenza nominale(100 kVA)
                  numpy.linspace(0.89, 1.11, 20)
                  ]
    parent_selection_type = "sss"
    keep_parents = 1
    crossover_type = "single_point"
    mutation_type = "random"
    mutation_percent_genes = 50
    stop_criteria="reach_4" #Tolleranza 0.25 V

    def on_generation(ga_instance):
        print(f"Generation = {ga_instance.generations_completed}")
        print(f"Fitness    = {ga_instance.best_solution(pop_fitness=ga_instance.last_generation_fitness)[1]}")

    ga_instance = pygad.GA(num_generations=num_generations,
                           on_generation=on_generation,
                           num_parents_mating=num_parents_mating,
                           fitness_func=fitness_function,
                           sol_per_pop=sol_per_pop,
                           stop_criteria=stop_criteria,
                           num_genes=num_genes,
                           gene_space=gene_space,
                           parent_selection_type=parent_selection_type,
                           keep_parents=keep_parents,
                           crossover_type=crossover_type,
                           mutation_type=mutation_type,
                           mutation_percent_genes=mutation_percent_genes,
                           initial_population=initial_population)

    start = time.time()
    ga_instance.run()
    end = time.time()

    

    o = open(r"KPI_GA_Execution_Time.csv.txt", "a")
    o.write("\n"+ f"[{ora_attuale}];" +str(end - start))
    o.close()

    solution, solution_fitness, solution_idx = ga_instance.best_solution()
    initial_population = [solution, solution, solution, solution, solution, solution, solution, solution, solution, solution]

    o = open(r"GA_Fitness.csv.txt", "a")
    o.write("\n" + f"[{ora_attuale}];" + str(1 / solution_fitness))
    o.close()

    ora_attuale = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%fZ')[:-3]

    ## CALCOLO I RISULTATI E LI MOSTRO
    for i in range(len(carichiSE)-1):
        net.load.p_mw.at[pp.get_element_index(net, "load", carichiSE[i])] = float(solution[2 * i])
        net.load.q_mvar.at[pp.get_element_index(net, "load", carichiSE[i])] = float(solution[2 * i +1])
    df.loc[0, 'net.ext_grid.vm_pu'] =float(solution[2*len(carichiSE)])
    pp.runpp(net,numba=False)
    
    for i in range(len(carichiSE)-1):
        net.load.p_mw.at[pp.get_element_index(net, "load", carichiSE[i])] = float(solution[2 * i]) #fuction example for pandapower
        net.load.q_mvar.at[pp.get_element_index(net, "load", carichiSE[i])] = float(solution[2 * i +1])
        #Publishing on MQTT
        json_object["d"] = solution[2 * i]
        json_object["ts"] = ora_attuale
        json_message = json.dumps(json_object, indent=4)
        client.publish("A2MQTT/" + carichiSE[i] + "/Power_P_1_7_0/Cv", json_message)
        json_object["d"] = solution[2 * i + 1]
        json_object["ts"] = ora_attuale
        json_message = json.dumps(json_object, indent=4)
        client.publish("A2MQTT/" + carichiSE[i] + "/Power_Q_3_7_0/Cv", json_message)
        #client.publish("A2MQTT/" + carichiSE[i] + "/Power_P_1_7_0/Cv","{\"d\":" + str(solution[2 * i]) + ",\"dt\":4,\"ts\":" + ora_attuale + "Z,\"q\":192}")
        #client.publish("A2MQTT/" + carichiSE[i] + "/Power_Q_3_7_0/Cv","{\"d\":" + str(solution[2 * i + 1]) + ",\"dt\":4,\"ts\":" + ora_attuale + "Z,\"q\":192}")
    pp.runpp(net,numba=False) #execution of power flow

#####Pubblicazione Tensioni
    tensioni_calc, delta = [], []
    for i in range(len(nodi_noti)-1):
        tensione = net.res_bus.vm_pu.at[float(nodi_noti[i])]
        tensioni_calc.append(tensione)
        json_object["d"] = float(misure[i] - tensioni_calc[i]*230)
        json_object["ts"] = ora_attuale
        json_message = json.dumps(json_object, indent=4)
        client.publish("A2MQTT/" + nodi_noti[i] + "/Voltage_Error_U_32_7_0/Cv", json_message)
        json_object["d"] = tensioni_calc[i]
        json_object["ts"] = ora_attuale
        json_message = json.dumps(json_object, indent=4)
        client.publish("A2MQTT/" + nodi_noti[i] + "/Voltage_Calc_U_32_7_0/Cv", json_message)
    #dss.circuit_set_active_element(f"Load.{nodi_noti[i]}")




# #### LF RESULTS HANDLING #####
    ora_attuale = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
 
    print(ora_attuale)

# # EXPORT POWER REQUIRED BY EACH LOAD (USEFUL FOR FLEXIBILITY OPTIMIZATION)
    potenza_SE = open(r".\potenza_SE.txt", "a")
    potenza_SE.write(f"[{ora_attuale}]; ")
    potenza_SE.close()
        
    for i in range(len(carichiSE)-1):
        pot_attiva= net.load.p_mw.at[pp.get_element_index(net, "load", carichiSE[i])]
        pot_reattiva = net.load.q_mvar.at[pp.get_element_index(net, "load", carichiSE[i])]
        pot=[pot_attiva, pot_reattiva]
        potenza_SE = open("potenza_SE.txt", "a")
        potenza_SE.write(f"{pot}; ")
        potenza_SE.close()
    potenza_SE = open(r"potenza_SE.txt", "a")
    potenza_SE.write("\n")
    potenza_SE.close()
    #Task: try to transfer from DSS to pandapower
    # # EXPORT VOLTAGE PU IN THE PRIMARY SUBSTATION (USEFUL FOR FLEXIBILITY OPTIMIZATION)
    tensione_pu = open(r"tensione_master_SE.txt", "a")
    tensione_pu.write(f"[{ora_attuale}]; ")
    voltage_pu = net.res_bus.vm_pu.at[17]  # OBJECT PROGRAMMING - net: 
    print(voltage_pu)
    tensione_pu.write(f"{voltage_pu}; ")
    tensione_pu.write("\n")

    # EXPORT VOLTAGE RESULTS FOR EACH LOADp_mw
    voltage= open(r"tensioni_SE.txt", "a")
    voltage.write(f"[{ora_attuale}]; ")
    voltage.close()
    for i in range(17):
        tensione = net.res_bus.vm_pu.at[float(i)]
        voltage= open(r"tensioni_SE.txt", "a")
        voltage.write(f"{tensione}"+";")
        voltage.close()
    voltage = open(r"tensioni_SE.txt", "a")
    voltage.write("\n")
    voltage.close()
    
    # EXPORT VOLTAGE ERRORS FOR EACH MBT
    voltage= open(r"tensioni_ERROR.txt", "a")
    voltage.write(f"[{ora_attuale}]; ")
    voltage.close()
    for i in range(len(nodi_noti)-1):
        tensione = float(misure[i] - net.res_bus.vm_pu.at[float(nodi_noti[i])]*230)
        voltage= open(r"tensioni_ERROR.txt", "a")
        voltage.write(f"{tensione}"+";")
        voltage.close()
    voltage = open(r"tensioni_ERROR.txt", "a")
    voltage.write("\n")
    voltage.close()

    # # EXPORT CURRENT RESULTS FOR EACH LINE
    current = open(r"correnti.txt", "a")
    current.write(f"[{ora_attuale}]; ")
    current.close()
    for j in range(19):
        current_mag = net.res_line.i_from_ka.at[float(j)]  # Replace element_name with the actual line name
        current = open(r"correnti_SE.txt", "a")
        current.write(f"{current_mag}; ")
        current.close()
    current = open(r"correnti_SE.txt", "a")
    current.write("\n")
    current.close()

    # # EXPORT REVERSE POWER FLOW RESULTS
    reverse = open(r"RPF_SE.txt", "a")
    rpf = net.res_ext_grid.p_mw.at[0]*1000
    reverse.write(f"[{ora_attuale}]; {rpf}; \n")    # scrivo la potenza che passa nel trasformatore EXSIT, è negativa se è RPF, positiva se va verso il carico.
    reverse.close()

    o = open(r"ANGELINI_ESTIMATED.txt", "a")
    o.write("\n" + f"[{ora_attuale}];" + str(solution[8]))
    o.close()
# #######################################################################################################################
# #######################################################################################################################
# #######################################################################################################################
    # # DA QUI IN POI EFFETTUO LO STUDIO SFRUTTANDO LA FLESSIBILITà
    # # FROM HERE, FLEXIBIITY MECHANISM IS ADDRESSED
    # study storage in pandapwoer, then include storage in the network only for ASM, then transfer the script to pandapower
    # Include the PMU of COMSENSUS
    # Aim of script: set set points of previous thresholds. There were many storages (batterie in line 318), but now we do with only one.
# #######################################################################################################################
# #######################################################################################################################
# #######################################################################################################################
    if attivo_flessibilita==True:
#         valori_flusso=[]
# 
#         reverse= open("RPF.txt", "r")
#             for riga in reverse:
#                 valori_flusso.append(float(riga[1]))

        # I recalculate these values continuously, so the more the program runs, the more accurate it is,
        # I can, however, put it before the while which thus saves some time.
#         val_10=np.percentile(valori_flusso, 10)
#         val_20=np.percentile(valori_flusso, 20)
#         val_30=np.percentile(valori_flusso, 30)
#         val_40=np.percentile(valori_flusso, 40)
#         val_60=np.percentile(valori_flusso, 60)
#         val_70=np.percentile(valori_flusso, 70)
#         val_80=np.percentile(valori_flusso, 80)
#         val_90=np.percentile(valori_flusso, 90)
# 
#         print("il flusso in cabina primaria rpf è", str(rpf))
        
        # utilizzo lo stato di carica che avevo lasciato dalla iterazione precedente
        batterie = ["BEMS", "Celi", "Mazzocchio", "Croci", "Scov", "Slow", "Fast"]
        
        ##Charging Stations
#         for i in range(7):
#             # Modify the storage values using Pandapower
#             pp.runpp(net)  # Run power flow before modifying storage values
#             net.storage.loc[batterie[i], "p_mw"] = prossimi_kWh_stored[i]
#             pp.runpp(net)  # Run power flow after modifying storage values
# 
# 
#         # Check if there are electric vehicles and enable them for flexibility if their load is greater than 3 MW
#         enabled_Slow = net.load.loc["Slow", "p_mw"]
#         if enabled_Slow > 3:
#             # Enable the storage element
#             net.storage.loc["Slow", "in_service"] = True
#         else:
#             # Disable the storage element and set the state of charge to 100%
#             net.storage.loc["Slow", "in_service"] = False
#             net.storage.loc["Slow", "p_mw"] = 0  # Set power output to 0
#             net.storage.loc["Slow", "max_p_mw"] = 0  # Set maximum power output to 0
#             net.storage.loc["Slow", "min_p_mw"] = 0  # Set minimum power output to 0
#             net.storage.loc["Slow", "q_mvar"] = 0  # Set reactive power output to 0
#             net.storage.loc["Slow", "soc_percent"] = 100  # Set state of charge to 100%
# 
#         enabled_Fast = net.load.loc["Fast", "p_mw"]
#         if enabled_Fast > 3:
#             # Enable the storage element
#             net.storage.loc["Fast", "in_service"] = True
#         else:
#             # Disable the storage element and set the state of charge to 100%
#             net.storage.loc["Fast", "in_service"] = False
#             net.storage.loc["Fast", "p_mw"] = 0  # Set power output to 0
#             net.storage.loc["Fast", "max_p_mw"] = 0  # Set maximum power output to 0
#             net.storage.loc["Fast", "min_p_mw"] = 0  # Set minimum power output to 0
#             net.storage.loc["Fast", "q_mvar"] = 0  # Set reactive power output to 0
#             net.storage.loc["Fast", "soc_percent"] = 100  # Set state of charge to 100%

#         # Run power flow calculation
#         pp.runpp(net)

        # Check RPF and set storage element states and charge levels accordingly
        if rpf <= soglia[0]:
            net.storage.p_mw.at[1] = net.storage.max_e_mwh.at[1]
        elif rpf <= soglia[1]:
            net.storage.p_mw.at[1] = net.storage.max_e_mwh.at[1]*0.75
        elif rpf <= soglia[2]:
            net.storage.p_mw.at[1] = net.storage.max_e_mwh.at[1]*0.5
        elif rpf <= soglia[3]:
            net.storage.p_mw.at[1] = net.storage.max_e_mwh.at[1]*0.25
        elif rpf <= soglia[4]:
            net.storage.p_mw.at[1] = net.storage.min_e_mwh.at[1]  # Set to None for IDLING state
        elif rpf <= soglia[5]:
            net.storage.p_mw.at[1] = -net.storage.max_e_mwh.at[1]*0.25    
        elif rpf <= soglia[6]:
            net.storage.p_mw.at[1] = -net.storage.max_e_mwh.at[1]*0.5
        elif rpf <= soglia[7]:
            net.storage.p_mw.at[1] = -net.storage.max_e_mwh.at[1]*0.75
        else:
            net.storage.p_mw.at[1] = -net.storage.max_e_mwh.at[1]

        # Update the storage elements' states and charge levels
        for batteria in batterie:
            net.storage.loc[batteria, "in_service"] = True  # Enable the storage element
            if charge_level is None:
                net.storage.loc[batteria, "in_service"] = False  # Disable the storage element
            else:
                net.storage.loc[batteria, "p_mw"] = charge_level  # Set the charge level

    # #### LF RESULTS HANDLING #####
        # EXPORT VOLTAGE RESULTS FOR EACH LOAD
        voltage= open(r"tensioni_DR.txt", "a")
        voltage.write(f"[{ora_attuale}]; ")
        voltage.close()
        for i in range(7):
            print(i)
            tensione = net.res_bus.vm_pu.at[float(i)]
            voltage= open(r"tensioni_DR.txt", "a")
            voltage.write(f"{tensione}"+";")
            voltage.close()
        voltage = open(r"tensioni_DR.txt", "a")
        voltage.write("\n")
        voltage.close()

        # EXPORT CURRENT RESULTS FOR EACH LINE
        current = open(r"correnti_DR.txt", "a")
        current.write(f"[{ora_attuale}]; ")
        current.close()
        for j in range(6):
            print(j)
            current_mag = net.res_line.i_from_ka.at[float(j)]  # Replace element_name with the actual line name
            print(current_mag)
            current = open(r"correnti_DR.txt", "a")
            current.write(f"{current_mag}; ")
            current.close()
        current = open(r"correnti_DR.txt", "a")
        current.write("\n")
        current.close()

        # EXPORT SOC RESULTS FOR EACH LINE
        state_of_charge = open(r"SOC_DR.txt", "w")
        state_of_charge.write(f"[{ora_attuale}]; ")
        state_of_charge.close()
        potenza = open(r"P_storage.txt", "a")
        potenza.write(f"[{ora_attuale}]; ")
        potenza.close()
        prossimi_kWh_stored=[]
        for elemento in batterie:
            soc = net.storage.at[elemento, "p_mw"]
            prossimi_kWh_stored.append(soc)
            p = net.storage.at[elemento, "p_mw"]
            
            state_of_charge_data[elemento] = soc
            power_data[elemento] = p
            
            state_of_charge = open(r"SOC_DR.txt", "w")
            state_of_charge.write(f"[{ora_attuale}]; {rpf}; \n")
            state_of_charge.close()
            potenza = open(r"P_storage.txt", "a")
            potenza.write(f"{P}; ")
            potenza.close()
        state_of_charge = open(r"SOC_DR.txt", "a")
        state_of_charge.write("\n")
        state_of_charge.close()
        potenza = open(r"P_storage.txt", "a")
        potenza.write("\n")
        potenza.close()
        

        ### or instead of 12 previous lines---->ask Tommaso
#         state_of_charge_df = pd.DataFrame(state_of_charge_data)
#         state_of_charge_df.to_csv(r"SOC_DR.txt", mode="a", sep=";", index=False)
#         power_df = pd.DataFrame(power_data)
#         power_df.to_csv(r"P_storage.txt", mode="a", sep=";", index=False)

        # EXPORT REVERSE POWER FLOW RESULTS
        reverse = open(r"RPF_DR.txt", "a")
        rpf = net.res_ext_grid.p_mw.at[0]
        reverse.write(f"[{ora_attuale}]; {rpf}; \n")    # scrivo la potenza che passa nel trasformatore EXSIT, è negativa se è RPF, positiva se va verso il carico.
        reverse.close()
        
        fine = time.time()
        durata = fine - inizio

    if inizio - time.time() < MAX_TIME:     # impongo che il tempo totale sia uguale a 20s
        time.sleep(MAX_TIME-(inizio - time.time()))
    #if fine - inizio < MAX_TIME:
    #time.sleep(MAX_TIME - (fine - inizio))



#     # Load data from JSON files  NO VALUE IS DISPLAYED
#     with open('W4_P.json', 'r') as f:
#         w4p_data = json.load(f)
#     with open('W4_Q.json', 'r') as f:
#         w4q_data = json.load(f)
#     # Load data from other JSON files in a similar manner
#     # Extract x and y values from the data
#     d_value = w4p_data['d']
#     dt_value = w4p_data['dt']
#     ts_value = w4p_data['ts']
#     q_value = w4p_data['q']
#     print(w4p_data['d'])
#     print(w4p_data['dt'])
#     print(w4p_data['ts'])
#     print(w4p_data['q'])
# 
#     # Extract x and y values from other data in a similar manner
#     # Plot the data
#     x_values = w4p_data['d']
#     w4p_values = w4p_data['q']
# 
#     plt.figure(figsize=(10, 6))
#     plt.plot(x_values, w4p_values, label='W4_P')
#     # Plot other data in a similar manner
#     # Customize the plot
#     plt.xlabel('Time')
#     plt.ylabel('Power')
#     plt.title('Power Data')
#     plt.legend()
#     # Show the plot
#     plt.show()
    
    # import csv  # THERE IS A BIG VALUE IN THE RESULT FILE
    # from datetime import datetime
    # import matplotlib.pyplot as plt
    # 
    # # Define the path to the result file
    # file_path = "KPI_GA_Execution_Time.csv.txt"
    # 
    # # Create empty lists to store the data
    # dates = []
    # values = []
    # 
    # # Read the CSV file
    # try:
    #     with open(file_path, "r") as csv_file:
    #         csv_reader = csv.reader(csv_file, delimiter=";")
    #         next(csv_reader)  # Skip the header row
    #         
    #         # Iterate over each row in the CSV file
    #         for row in csv_reader:
    #             if len(row) >= 2:
    #                 datetime_str = row[0].strip("[]")
    #                 value = float(row[1])
    #                 
    #                 date = datetime.strptime(datetime_str, "%Y-%m-%d %H:%M:%S")
    #                 
    #                 dates.append(date)
    #                 values.append(value)
    #             else:
    #                 print(f"Ignoring row: {row}")
    # except FileNotFoundError:
    #     print(f"File not found: {file_path}")
    # except ValueError:
    #     print("Error occurred while parsing the value.")
    #     
    # # Plotting the values
    # plt.plot(dates, values)
    # plt.title("Values Over Time")
    # plt.xlabel("Date and Time")
    # plt.ylabel("Value")
    # plt.xticks(rotation=45)
    # plt.show()

#     import csv  # REMOVED BIG VALUE FROM THE FILE.
#     from datetime import datetime
#     import matplotlib.pyplot as plt
# 
#     # Define the path to the result file
#     file_path = "KPI_GA_Execution_Time.csv.txt"
# 
#     # Create empty lists to store the data
#     dates = []
#     values = []
# 
#     # Read the CSV file
#     try:
#         with open(file_path, "r") as csv_file:
#             csv_reader = csv.reader(csv_file, delimiter=";")
#             next(csv_reader)  # Skip the header row
#             
#             # Iterate over each row in the CSV file
#             for row in csv_reader:
#                 datetime_str = row[0].strip("[]")
#                 value = float(row[1])
#                 
#                 if datetime_str != '[2023-06-15 11:44:28]' and value <= 1000:  # Skip row 312 and exclude values over 1000
#                     date = datetime.strptime(datetime_str, "%Y-%m-%d %H:%M:%S")
#                     
#                     dates.append(date)
#                     values.append(value)
#         
#         # Plotting the values
#         plt.plot(dates, values)
#         plt.title("Values Over Time")
#         plt.xlabel("Date and Time")
#         plt.ylabel("Value")
#         plt.xticks(rotation=45)
#         plt.show()
# 
#     except FileNotFoundError:
#         print(f"File not found: {file_path}")
#     except ValueError:
#         print("Error occurred while parsing the value.")

#     Define the path to the result file
    ########### MIDDLE OF THE CODE###################

    import numpy as np
    import matplotlib.pyplot as plt
    import ast

    # Common timestamps for all sections
    timestamps = np.linspace(0, 168, 168)

    # First Section
    y0 = []
    data = np.genfromtxt("potenza_SE.txt", delimiter=';', dtype=str, usecols=np.arange(0, 5))
    print(data.shape[0])

    # Ensure that the length of the data is at least 168
    data_length = min(168, data.shape[0])

    for i in range(data_length):
        value_list = ast.literal_eval(data[data.shape[0] - data_length + i][1])
        values = float(value_list[0])
        y0.append(values)

    # Second Section
    y1 = []
    data_1 = np.genfromtxt("GA_Fitness.csv.txt", delimiter=';', dtype=None, encoding=None)
    print(data_1.shape)
    last_168_rows_1 = data_1[-168:]
    y1 = [float(row[1]) for row in last_168_rows_1]

    # Third Section
    y2 = []
    data_2 = np.genfromtxt("RPF.txt", delimiter=';', dtype=None, encoding=None)
    print(data_2.shape)
    last_168_rows_2 = data_2[-168:]
    y2 = [float(row[1]) for row in last_168_rows_2]

    # Print the lengths for debugging
    print(len(timestamps), len(y0), len(y1), len(y2))

    # Now, you can use the timestamps array in your plotting function.
    update_plot()
        
#     y=[]
#     data = numpy.genfromtxt("SOC_DR.txt", delimiter=';', dtype=None, encoding=None)
#     print(data.shape)
#     last_20_rows = data[-20:]
#     y = [float(row[1]) for row in last_20_rows]
#     x=numpy.linspace(0,20,20)
#     plt.xlabel("Timestamp")  # Set the x-axis label
#     plt.ylabel("SOC")  # Set the y-axis label
#     update_plot()
    
    # include RPF
    # plot current SOC: last 20 values OR srat real-time
    # modify x,y labels in the plot section, and scales
    # 
     
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




