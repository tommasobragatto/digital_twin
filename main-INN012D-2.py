import pandapower as pp
import json
import network_function_FdiPOLO_with_correct_coordinations2
import time
import pygad
import numpy
import time
import csv
import matplotlib.pyplot as plt
from datetime import datetime
# import numba
# import network_function_FdiPOLO_with_correct_coordinations2
import subprocess

fig, ax = plt.subplots(3, 1, sharex=True)  # Create a figure with 3 subplots (3 rows, 1 column)

timestamps = numpy.linspace(0, 2 * numpy.pi, 100)
y = numpy.sin(timestamps)

line1, = ax[0].plot(timestamps, y)
line2, = ax[1].plot(timestamps, y)
line3, = ax[2].plot(timestamps, y)
ax[0].set_xlabel('X-axis')
ax[0].set_ylabel('Y-axis')

ax[0].set_title("Power....")
ax[1].set_title("Power....")
ax[2].set_title("Power....")


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

net = network_function_FdiPOLO_with_correct_coordinations2.fdipolo_network()
initial_population=[[1,1,1,1,1,1,1],[1,1,1,1,1,1,1],[1,1,1,1,1,1,1],[1,1,1,1,1,1,1],[1,1,1,1,1,1,1]] #TODO


while True:
    inizio = time.time()
### INDIVIDUAL METERS ARE INVOKED IN ORDER TO COLLECT DATA ###
     subprocess.call(['python', "testMain.py"])
    

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
    ############################################    ## COLLECTION OF THE VOLTAGES FOR THE STATE ESTIMATION
    misure = [data_1["Lines"][0]["V"]["Value"][0], data_4["Lines"][0]["V"]["Value"][0], data_5["Lines"][0]["V"]["Value"][0], data_6["Lines"][0]["V"]["Value"][0], data_7["Lines"][0]["V"]["Value"][0]]

#### STATE ESTITMATION ##########    
    def fitness_func(ga_instance, solution, solution_idx):

        carichiSE = ["Siemens_2", "Tre_T_2", "Fontana_di_polo_2"]   # Loads to be estimated
        for i in range(len(carichiSE)-1):
            net.load.p_mw.at[pp.get_element_index(net, "load", carichiSE[i])] = float(solution[2 * i])/1000
            net.load.q_mvar.at[pp.get_element_index(net, "load", carichiSE[i])] = float(solution[2 * i +1])/1000
        net.ext_grid.vm_pu[0]=float(solution[2*len(carichiSE)])
        pp.runpp(net,numba=False)

        tensioni_calc, delta = [], []
        nodi_noti = ["13", "16", "5", "1", "6"] #nodi_noti in english means nodes_known
        for i in range(len(nodi_noti)-1):
            tensione = net.res_bus.vm_pu.at[float(nodi_noti[i])]
            tensioni_calc.append(tensione)
            delta.append(float(misure[i])*50 - tensioni_calc[i])
        fitness = len(nodi_noti) / numpy.dot(delta, delta)
        return fitness


    fitness_function = fitness_func

    num_generations = 50
    num_parents_mating = 4
    sol_per_pop = 5
    num_genes = 7

    # Leggo i valori medi delle potenze che passano nei nodi 9, 10 e 11, così da fare una stima più accurata ed inserirli nel gene_space con + o - 20%
    h=time.localtime().tm_hour
    m=time.localtime().tm_min
    valoreP9=21.41749
    valoreP10=3.92556
    valoreP11=12.76311
    valoreQ9=6.44643
    valoreQ10=0.79711
    valoreQ11=0.59104

    gene_space = [numpy.linspace(valoreP10 - 5, valoreP10 + 5, 20), # carico mazzocchio, per la P faccio + e - il 10% della potenza nominale (50 kVA)
                  numpy.linspace(valoreQ10 - 2.5, valoreQ10 + 2.5, 10), # carico mazzocchio, per la Q faccio + e - il 5% della potenza nominale (50 kVA)
                  numpy.linspace(valoreP11 - 10, valoreP11 + 10, 20),  # carico celi, per la P faccio + e - il 10% della potenza nominale(100 kVA)
                  numpy.linspace(valoreQ11 - 5, valoreQ11 + 5, 10), # carico celi, per la Q faccio + e - il 5% della potenza nominale(100 kVA)
                  numpy.linspace(valoreP9 - 16, valoreP9 + 16, 20), # carico croci, per la P faccio + e - il 10% della potenza nominale(160 kVA)
                  numpy.linspace(valoreQ11 - 5, valoreQ11 + 5, 10),
                  numpy.linspace(0.9, 1.1, 10)
                  ]
    parent_selection_type = "sss"
    keep_parents = 1
    crossover_type = "single_point"
    mutation_type = "random"
    mutation_percent_genes = 50
    stop_criteria="reach_4" #Tolleranza 0.25 V

    def on_generation(ga):
        print("Generation", ga.generations_completed)
        print(ga.population)


    ga_instance = pygad.GA(num_generations=num_generations,
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

    ora_attuale = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

    o = open(r"KPI_GA_Execution_Time.csv.txt", "a")
    o.write("\n"+ f"[{ora_attuale}];" +str(end - start))
    o.close()

    solution, solution_fitness, solution_idx = ga_instance.best_solution()
    initial_population = [solution, solution, solution, solution, solution]

    o = open(r"GA_Fitness.csv.txt", "a")
    o.write("\n" + f"[{ora_attuale}];" + str(1 / solution_fitness))
    o.close()

    ora_attuale = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%fZ')[:-3]

    ## CALCOLO I RISULTATI E LI MOSTRO

    carichiSE = ["1", "2", "3", "4"]
    for i in range(len(carichiSE)-1):
        net.load.p_mw.at[float(carichiSE[i])] = float(solution[2 * i])/1000 #fuction example for pandapower
        net.load.q_mvar.at[float(carichiSE[i])] = float(solution[2 * i +1])/1000
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
    nodi_noti=["1", "6"]
    tensioni_calc, delta = [], []
    for i in range(len(nodi_noti)-1):
        tensione = tensione = net.res_bus.vm_pu.at[float(nodi_noti[i])]
        tensioni_calc.append(tensione)
        json_object["d"] = float(misure[i] - tensioni_calc[i])
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

    carichi = ["0","1", "2", "3", "4", "5"]   # carichi da stimare
        
    for i in range(len(carichiSE)-1):
        pot_attiva= net.load.p_mw.at[float(carichi[i])]/1000
        pot_reattiva = net.load.q_mvar.at[float(carichi[i])]/1000
        pot=[pot_attiva, pot_reattiva]
        potenza_SE = open("potenza_SE.txt", "a")
        potenza_SE.write(f"{pot}; ")
        potenza_SE.close()
    potenza_SE = open(r"potenza_SE.txt", "a")
    potenza_SE.write("\n")
    potenza_SE.close()
    #Task: try to transfer from DSS to pandapower
    # # EXPORT VOLTAGE PU IN THE PRIMARY SUBSTATION (USEFUL FOR FLEXIBILITY OPTIMIZATION)
    tensione_pu = open(r"tensione_master.txt", "a")
    tensione_pu.write(f"[{ora_attuale}]; ")
    voltage_pu = net.res_bus.vm_pu.at[0]  # OBJECT PROGRAMMING - net: 
    print(voltage_pu)
    tensione_pu.write(f"{voltage_pu}; ")
    tensione_pu.write("\n")

    # EXPORT VOLTAGE RESULTS FOR EACH LOADp_mw
    voltage= open(r"tensioni.txt", "a")
    voltage.write(f"[{ora_attuale}]; ")
    voltage.close()
    for i in range(7):
        print(i)
        tensione = net.res_bus.vm_pu.at[float(i)]
        voltage= open(r"tensioni.txt", "a")
        voltage.write(f"{tensione}"+";")
        voltage.close()
    voltage = open(r"tensioni.txt", "a")
    voltage.write("\n")
    voltage.close()

    # # EXPORT CURRENT RESULTS FOR EACH LINE
    current = open(r"correnti.txt", "a")
    current.write(f"[{ora_attuale}]; ")
    current.close()
    for j in range(6):
        print(j)
        current_mag = net.res_line.i_from_ka.at[float(j)]  # Replace element_name with the actual line name
        print(current_mag)
        current = open(r"correnti.txt", "a")
        current.write(f"{current_mag}; ")
        current.close()
    current = open(r"correnti.txt", "a")
    current.write("\n")
    current.close()

    # # EXPORT REVERSE POWER FLOW RESULTS
    reverse = open(r"RPF.txt", "a")
    rpf = net.res_ext_grid.p_mw.at[0]*1000
    reverse.write(f"[{ora_attuale}]; {rpf}; \n")    # scrivo la potenza che passa nel trasformatore EXSIT, è negativa se è RPF, positiva se va verso il carico.
    reverse.close()


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

    # First Section
    y0 = []
    data = np.genfromtxt("potenza_SE.txt", delimiter=';', dtype=str, usecols=np.arange(0, 5))
    timestamps = np.linspace(0, 168, 168)  # Replace this with the correct timestamps for the first section
    print(data.shape[0])
    for i in range(168):  # Interested in last 100 values
        value_list = ast.literal_eval(data[data.shape[0] - (168 - i)][1])
        values = float(value_list[0])
        y0.append(values)


    # Second Section
    y1 = []
    data = np.genfromtxt("GA_Fitness.csv.txt", delimiter=';', dtype=None, encoding=None)
    timestamps = np.linspace(0, 168, 168)  # Replace this with the correct timestamps for the second section
    print(data.shape)
    last_168_rows = data[-168:]
    y1 = [float(row[1]) for row in last_168_rows]


    # Third Section
    y2 = []
    data = np.genfromtxt("RPF.txt", delimiter=';', dtype=None, encoding=None)
    timestamps = np.linspace(0, 168, 168)  # Replace this with the correct timestamps for the third section
    print(data.shape)
    last_168_rows = data[-168:]
    y2 = [float(row[1]) for row in last_168_rows]

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





