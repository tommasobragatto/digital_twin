# import pandapower as pp #import pandapower
# import numba
# import json
# 
# def fdipolo_network():
# 
#     net = pp.create_empty_network() #create an empty network
# 
#     # create the buses
#     bus1 = pp.create_bus(net, vn_kv=20, name="INT0723A1_0722A1_2", geodata=(42.57069445366638, 12.587663886588158), type='b', in_service=True, max_vm_pu=1.1, min_vm_pu=0.9)
#     bus2 = pp.create_bus(net, vn_kv=20, name="00102000723A1", geodata=(42.57165583, 12.58597006), type='b', in_service=True, max_vm_pu=1.1, min_vm_pu=0.9)
#     bus3 = pp.create_bus(net, vn_kv=20, name="INT0723A1_0722A1_3", geodata=(42.56657239561523, 12.592446945516475), type='b', in_service=True, max_vm_pu=1.1, min_vm_pu=0.9)
#     bus4 = pp.create_bus(net, vn_kv=20, name="INT0723A1_0722A1_0", geodata=(42.576777640961765, 12.59165620494046), type='b', in_service=True, max_vm_pu=1.1, min_vm_pu=0.9)
#     bus5 = pp.create_bus(net, vn_kv=20, name="INT0723A1_0722A1_1", geodata=(42.59155878367046, 12.594687963796105), type='b', in_service=True, max_vm_pu=1.1, min_vm_pu=0.9)
#     bus6 = pp.create_bus(net, vn_kv=20, name="00102000827A1", geodata=(42.56587048, 12.58831038), type='b', in_service=True, max_vm_pu=1.1, min_vm_pu=0.9)
#     bus7 = pp.create_bus(net, vn_kv=20, name="00102000722A1", geodata=(42.59163941, 12.59406697), type='b', in_service=True, max_vm_pu=1.1, min_vm_pu=0.9)
#     bus8 = pp.create_bus(net, vn_kv=20, name="100000336", geodata=(42.562806023499064, 12.60568432070056), type='b', in_service=True, max_vm_pu=1.1, min_vm_pu=0.9)
#     bus9 = pp.create_bus(net, vn_kv=20, name="INT001737_000336_1", geodata=(42.56153542478011, 12.605596903756808), type='b', in_service=True, max_vm_pu=1.1, min_vm_pu=0.9)
#     bus10 = pp.create_bus(net, vn_kv=20, name="INT001737_000336_0", geodata=(42.56524604642435, 12.593271129007814), type='b', in_service=True, max_vm_pu=1.1, min_vm_pu=0.9)
#     bus11 = pp.create_bus(net, vn_kv=20, name="INT0724A1_0764A1_0", geodata=(42.566642675302425, 12.590104267201315), type='b', in_service=True, max_vm_pu=1.1, min_vm_pu=0.9)
#     bus12 = pp.create_bus(net, vn_kv=20, name="00102000764A1", geodata=(42.56799926, 12.58852029), type='b', in_service=True, max_vm_pu=1.1, min_vm_pu=0.9)
#     bus13 = pp.create_bus(net, vn_kv=20, name="00102000724A1", geodata=(42.56738887, 12.59435605), type='b', in_service=True, max_vm_pu=1.1, min_vm_pu=0.9)
#     bus14 = pp.create_bus(net, vn_kv=20, name="00102000725A1", geodata=(42.56725771, 12.59443875), type='b', in_service=True, max_vm_pu=1.1, min_vm_pu=0.9)
#     bus15 = pp.create_bus(net, vn_kv=20, name="INT0459A1_0725A1_1", geodata=(42.56730938927409, 12.594034922229612), type='b', in_service=True, max_vm_pu=1.1, min_vm_pu=0.9)
#     bus16 = pp.create_bus(net, vn_kv=20, name="INT0459A1_0725A1_0", geodata=(42.565244826989684, 12.593283815186203), type='b', in_service=True, max_vm_pu=1.1, min_vm_pu=0.9)
#     bus17 = pp.create_bus(net, vn_kv=20, name="00102000459A1", geodata=(42.56470751, 12.59332143), type='b', in_service=True, max_vm_pu=1.1, min_vm_pu=0.9)
#     bus18 = pp.create_bus(net, vn_kv=20, name="100001737", geodata=(42.562806023499064, 12.60568432070056), type='b', in_service=True, max_vm_pu=1.1, min_vm_pu=0.9)
#     # LV BUS
#     bus19 = pp.create_bus(net, vn_kv=0.4, name="00102000459A1_LV", geodata=(42.56470751, 12.59332143), type='b', in_service=True, max_vm_pu=1.1, min_vm_pu=0.9)
#     bus20 = pp.create_bus(net, vn_kv=0.4, name="00102000722A1_LV", geodata=(42.59163941, 12.59406697), type='b', in_service=True, max_vm_pu=1.1, min_vm_pu=0.9)
#     bus21 = pp.create_bus(net, vn_kv=0.4, name="00102000723A1_LV", geodata=(42.57165583, 12.58597006), type='b', in_service=True, max_vm_pu=1.1, min_vm_pu=0.9)
#     bus22 = pp.create_bus(net, vn_kv=0.4, name="00102000725A1_LV", geodata=(42.56725771, 12.59443875), type='b', in_service=True, max_vm_pu=1.1, min_vm_pu=0.9)
#     bus23 = pp.create_bus(net, vn_kv=0.4, name="00102000827A1_LV", geodata=(42.56587048, 12.58831038), type='b', in_service=True, max_vm_pu=1.1, min_vm_pu=0.9)
#     bus24 = pp.create_bus(net, vn_kv=0.4, name="00102000724A1_LV", geodata=(42.56738887, 12.59435605), type='b', in_service=True, max_vm_pu=1.1, min_vm_pu=0.9)
#     bus25 = pp.create_bus(net, vn_kv=0.4, name="00102000764A1_LV", geodata=(42.56799926, 12.58852029), type='b', in_service=True, max_vm_pu=1.1, min_vm_pu=0.9)
# 
#     # bus18 = pp.create_bus(net, vn_kv=20, name="ns0492_000", geodata=(12.63418, 42.526908), type='b', in_service=True, max_vm_pu=1.1, min_vm_pu=0.9)
#     # bus19 = pp.create_bus(net, vn_kv=20, name="nd0103_000", geodata=(12.622921, 42.531), type='b', in_service=True, max_vm_pu=1.1, min_vm_pu=0.9)
#     # bus20 = pp.create_bus(net, vn_kv=20, name="nd0103_001", geodata=(12.627205, 42.529751), type='b', in_service=True, max_vm_pu=1.1, min_vm_pu=0.9)
#     # bus21 = pp.create_bus(net, vn_kv=20, name="ns0749_000", geodata=(12.621205, 42.529751), type='b', in_service=True, max_vm_pu=1.1, min_vm_pu=0.9)
#     # bus22 = pp.create_bus(net, vn_kv=20, name="ns0493_000", geodata=(12.620421, 42.524806), type='b', in_service=True, max_vm_pu=1.1, min_vm_pu=0.9)
#     # bus23 = pp.create_bus(net, vn_kv=20, name="ns0494_000", geodata=(12.623494, 42.520911), type='b', in_service=True, max_vm_pu=1.1, min_vm_pu=0.9)
#     # bus24 = pp.create_bus(net, vn_kv=20, name="nm0970_001", geodata=(12.623594, 42.518011), type='b', in_service=True, max_vm_pu=1.1, min_vm_pu=0.9)
#     # bus25 = pp.create_bus(net, vn_kv=20, name="ns0747_000", geodata=(12.623702, 42.513762), type='b', in_service=True, max_vm_pu=1.1, min_vm_pu=0.9)
#     # bus26 = pp.create_bus(net, vn_kv=20, name="nd0104_001", geodata=(12.6183, 42.5213), type='b', in_service=True, max_vm_pu=1.1, min_vm_pu=0.9)
#     # bus27 = pp.create_bus(net, vn_kv=20, name="ns0495_000", geodata=(12.614082, 42.522281), type='b', in_service=True, max_vm_pu=1.1, min_vm_pu=0.9)
#     # bus28 = pp.create_bus(net, vn_kv=20, name="nd0105_000", geodata=(12.621339, 42.519436), type='b', in_service=True, max_vm_pu=1.1, min_vm_pu=0.9)
#     # bus29 = pp.create_bus(net, vn_kv=20, name="ns0496_000", geodata=(12.620339, 42.517436), type='b', in_service=True, max_vm_pu=1.1, min_vm_pu=0.9)
#     # bus30 = pp.create_bus(net, vn_kv=20, name="nm0971_001", geodata=(12.6173, 42.5173), type='b', in_service=True, max_vm_pu=1.1, min_vm_pu=0.9)
#     # bus31 = pp.create_bus(net, vn_kv=20, name="ns0748_000", geodata=(12.615794, 42.513827), type='b', in_service=True, max_vm_pu=1.1, min_vm_pu=0.9)
#     # bus32 = pp.create_bus(net, vn_kv=20, name="nd0104_000", geodata=(12.618, 42.521611), type='b', in_service=True, max_vm_pu=1.1, min_vm_pu=0.9)
# 
#     # create the external grid connection
#     pp.create_ext_grid(net, bus=17, vm_pu=1.0, va_degree=0.0, name="ASM_Grid", in_service=True, s_sc_max_mva=31000, rx_max=0.125, r0x0_max=0.25)
# 
#     # create the linecodes
#     pp.create_std_type(net, data={"r_ohm_per_km":0.23, "x_ohm_per_km":0.323, "c_nf_per_km":11.2, "max_i_ka":335, "type":"cs"}, name="A_AL_160", element='line', overwrite=True, check_required=True)
#     pp.create_std_type(net, data={"r_ohm_per_km":0.164, "x_ohm_per_km":0.101, "c_nf_per_km":315, "max_i_ka":360, "type":"cs"}, name="C_CU_185", element='line', overwrite=True, check_required=True)
#     pp.create_std_type(net, data={"r_ohm_per_km":0.125, "x_ohm_per_km":0.097, "c_nf_per_km":352, "max_i_ka":440, "type":"cs"}, name="C_AL_240", element='line', overwrite=True, check_required=True)
# 
#     # create the lines
#     line1 = pp.create_line(net, from_bus=pp.get_element_index(net, "bus", "INT0723A1_0722A1_2"), to_bus=pp.get_element_index(net, "bus", "00102000723A1"), length_km=0.514, std_type="C_CU_185", name="00102000723A1_INT0723A1_0722A1_0")
#     line2 = pp.create_line(net, from_bus=pp.get_element_index(net, "bus", "INT0723A1_0722A1_3"), to_bus=pp.get_element_index(net, "bus", "INT0723A1_0722A1_2"), length_km=1.298, std_type="A_AL_160", name="INT0723A1_0722A1_0_INT0723A1_0722A1_1")
#     line3 = pp.create_line(net, from_bus=pp.get_element_index(net, "bus", "00102000827A1"), to_bus=pp.get_element_index(net, "bus", "INT0723A1_0722A1_3"), length_km=0.175, std_type="C_AL_240", name="INT0723A1_0722A1_1_00102000722A1")
#     line4 = pp.create_line(net, from_bus=pp.get_element_index(net, "bus", "00102000723A1"), to_bus=pp.get_element_index(net, "bus", "INT0723A1_0722A1_0"), length_km=0.514, std_type="C_CU_185", name="00102000723A1_INT0723A1_0722A1_0")
#     line5 = pp.create_line(net, from_bus=pp.get_element_index(net, "bus", "INT0723A1_0722A1_0"), to_bus=pp.get_element_index(net, "bus", "INT0723A1_0722A1_1"), length_km=1.8, std_type="A_AL_160", name="INT0723A1_0722A1_0_INT0723A1_0722A1_1")
#     line6 = pp.create_line(net, from_bus=pp.get_element_index(net, "bus", "INT0723A1_0722A1_1"), to_bus=pp.get_element_index(net, "bus", "00102000722A1"), length_km=0.175, std_type="C_CU_185", name="INT0723A1_0722A1_1_00102000722A1")
#     line7 = pp.create_line(net, from_bus=pp.get_element_index(net, "bus", "00102000722A1"), to_bus=pp.get_element_index(net, "bus", "100000336"), length_km=1.088, std_type="C_CU_185", name="00102000722A1_100000336")
#     line8 = pp.create_line(net, from_bus=pp.get_element_index(net, "bus", "INT001737_000336_1"), to_bus=pp.get_element_index(net, "bus", "100000336"), length_km=0.107, std_type="C_CU_185", name="INT001737_000336_1_100000336")
#     line9 = pp.create_line(net, from_bus=pp.get_element_index(net, "bus", "INT001737_000336_0"), to_bus=pp.get_element_index(net, "bus", "INT001737_000336_1"), length_km=2.446, std_type="A_AL_160", name="INT001737_000336_0_INT001737_000336_1")
#     line10 = pp.create_line(net, from_bus=pp.get_element_index(net, "bus", "100001737"), to_bus=pp.get_element_index(net, "bus", "INT001737_000336_0"), length_km=0.773, std_type="C_CU_185", name="100001737_INT001737_000336_0")
#     line11 = pp.create_line(net, from_bus=pp.get_element_index(net, "bus", "INT001737_000336_1"), to_bus=pp.get_element_index(net, "bus", "100000336"), length_km=0.107, std_type="C_CU_185", name="INT001737_000336_1_100000336")
#     line12 = pp.create_line(net, from_bus=pp.get_element_index(net, "bus", "INT001737_000336_0"), to_bus=pp.get_element_index(net, "bus", "INT001737_000336_1"), length_km=2.446, std_type="A_AL_160", name="INT001737_000336_0_INT001737_000336_1")
#     line13 = pp.create_line(net, from_bus=pp.get_element_index(net, "bus", "100001737"), to_bus=pp.get_element_index(net, "bus", "INT001737_000336_0"), length_km=0.773, std_type="C_CU_185", name="100001737_INT001737_000336_0")
#     line14 = pp.create_line(net, from_bus=pp.get_element_index(net, "bus", "00102000764A1"), to_bus=pp.get_element_index(net, "bus", "00102000827A1"), length_km=0.573, std_type="C_AL_240", name="00102000764A1_00102000827A1")
#     line15 = pp.create_line(net, from_bus=pp.get_element_index(net, "bus", "INT0724A1_0764A1_0"), to_bus=pp.get_element_index(net, "bus", "00102000764A1"), length_km=0.171, std_type="C_AL_240", name="INT0724A1_0764A1_0_00102000764A1")
#     line16 = pp.create_line(net, from_bus=pp.get_element_index(net, "bus", "00102000724A1"), to_bus=pp.get_element_index(net, "bus", "INT0724A1_0764A1_0"), length_km=0.368, std_type="C_CU_185", name="00102000724A1_INT0724A1_0764A1_0")
#     line17 = pp.create_line(net, from_bus=pp.get_element_index(net, "bus", "00102000725A1"), to_bus=pp.get_element_index(net, "bus", "00102000724A1"), length_km=0.016, std_type="C_CU_185", name="00102000724A1_00102000725A1")
#     line18 = pp.create_line(net, from_bus=pp.get_element_index(net, "bus", "INT0459A1_0725A1_1"), to_bus=pp.get_element_index(net, "bus", "00102000725A1"), length_km=0.06, std_type="C_CU_185", name="INT0459A1_0725A1_1_00102000725A1")
#     line19 = pp.create_line(net, from_bus=pp.get_element_index(net, "bus", "INT0459A1_0725A1_0"), to_bus=pp.get_element_index(net, "bus", "INT0459A1_0725A1_1"), length_km=0.121, std_type="A_AL_160", name="INT0459A1_0725A1_0_INT0459A1_0725A1_1")
#     line20 = pp.create_line(net, from_bus=pp.get_element_index(net, "bus", "00102000459A1"), to_bus=pp.get_element_index(net, "bus", "INT0459A1_0725A1_0"), length_km=0.325, std_type="C_CU_185", name="00102000459A1_INT0459A1_0725A1_0")
#     
#     # create transformer codes https://pandapower.readthedocs.io/en/latest/std_types/manage.html
#     pp.create_std_type(net, {"sn_mva": 0.16,
#         "vn_hv_kv": 20,
#         "vn_lv_kv": 0.4,
#         "vk_percent": 6,
#         "vkr_percent": (2.3-0.65)/160,
#         "pfe_kw": 0.65,
#         "i0_percent": 2.3,
#         "shift_degree": 0,
#         "vector_group": 'Dyn',
#         "tap_side": "lv",
#         "tap_neutral": 0,
#         "tap_min": -2,
#         "tap_max": 2,
#         "tap_step_degree": 0,
#         "tap_step_percent": 2.5,
#         "tap_phase_shifter":False}, name='SIEMENS_TR_160kVA', element="trafo", overwrite=True, check_required=True)
#         
#     pp.create_std_type(net, {"sn_mva": 0.1,
#         "vn_hv_kv": 20,
#         "vn_lv_kv": 0.4,
#         "vk_percent": 6,
#         "vkr_percent": (1.8-0.46)/100,
#         "pfe_kw": 0.46,
#         "i0_percent": 2.5,
#         "shift_degree": 0,
#         "vector_group": 'Dyn',
#         "tap_side": "lv",
#         "tap_neutral": 0,
#         "tap_min": -2,
#         "tap_max": 2,
#         "tap_step_degree": 0,
#         "tap_step_percent": 2.5, "tap_phase_shifter":False}, name='FDIPOLO_TR_100kVA', element="trafo", overwrite=True, check_required=True)
#     
#     pp.create_std_type(net, {"sn_mva": 0.4,
#         "vn_hv_kv": 20,
#         "vn_lv_kv": 0.4,
#         "vk_percent": 6,
#         "vkr_percent": (4.8-1.2)/400,
#         "pfe_kw": 1.2,
#         "i0_percent": 1.5,
#         "shift_degree": 0,
#         "vector_group": 'Dyn',
#         "tap_side": "lv",
#         "tap_neutral": 0,
#         "tap_min": -2,
#         "tap_max": 2,
#         "tap_step_degree": 0,
#         "tap_step_percent": 2.5, "tap_phase_shifter":False}, name='AVIOSUPERFICIE_TR_400kVA', element="trafo", overwrite=True, check_required=True)
#     
#     
#     pp.create_std_type(net, {"sn_mva": 0.25,
#         "vn_hv_kv": 20,
#         "vn_lv_kv": 0.4,
#         "vk_percent": 6,
#         "vkr_percent": (3.4-0.88)/250,
#         "pfe_kw": 0.88,
#         "i0_percent": 2,
#         "shift_degree": 0,
#         "vector_group": 'Dyn',
#         "tap_side": "lv",
#         "tap_neutral": 0,
#         "tap_min": -2,
#         "tap_max": 2,
#         "tap_step_degree": 0,
#         "si0_hv_partial": 0.9, "tap_phase_shifter":False}, name='ANGELINI_TR_250kVA', element="trafo", overwrite=True, check_required=True)
#     
#     # create transfomermers
#     tr1 = pp.create_transformer(net, hv_bus=pp.get_element_index(net, "bus", "00102000459A1"), lv_bus=pp.get_element_index(net, "bus", "00102000459A1_LV"), std_type="SIEMENS_TR_160kVA", name="SIEMENS_TR", in_service=True, parallel=1)
#     tr2 = pp.create_transformer(net, hv_bus=pp.get_element_index(net, "bus","00102000722A1"), lv_bus=pp.get_element_index(net, "bus","00102000722A1_LV"), std_type="FDIPOLO_TR_100kVA", name="FDIPOLO_TR", in_service=True, parallel=1)
#     tr3 = pp.create_transformer(net, hv_bus=pp.get_element_index(net, "bus", "00102000723A1"), lv_bus=pp.get_element_index(net, "bus","00102000723A1_LV"), std_type="AVIOSUPERFICIE_TR_400kVA", name="AVIOSUPERFICIE_TR", in_service=True, parallel=1)
#     tr4 = pp.create_transformer(net, hv_bus=pp.get_element_index(net,  "bus","00102000725A1"), lv_bus=pp.get_element_index(net, "bus","00102000725A1_LV"), std_type="SIEMENS_TR_160kVA", name="TRE_T_TR", in_service=True, parallel=1)
#     tr5 = pp.create_transformer(net, hv_bus=pp.get_element_index(net, "bus", "00102000827A1"), lv_bus=pp.get_element_index(net, "bus","00102000827A1_LV"), std_type="ANGELINI_TR_250kVA", name="ANGELINI_TR", in_service=True, parallel=1)
# #     tr7 = pp.create_transformer(net, "00102000724A1", "00102000724A1_LV", std_type, name="TECHNOMULTISERVICE_TR", in_service=True, parallel=1) THERE IS NO TRANSF. 
#     tr6 = pp.create_transformer(net, hv_bus=pp.get_element_index(net,  "bus","00102000764A1"), lv_bus=pp.get_element_index(net, "bus","00102000764A1_LV"), std_type="ANGELINI_TR_250kVA", name="ARCHIMEDE_TR", in_service=True, parallel=1)
# 
# 
#     # create loads
#     pp.create_load(net, bus=pp.get_element_index(net, "bus", "00102000459A1_LV"), p_mw=0.000525, q_mvar=-0.001888, name="Siemens_1", scaling=1.0, in_service=True, type='wye')
#     pp.create_load(net, bus=pp.get_element_index(net, "bus", "00102000459A1_LV"), p_mw=0.000100, q_mvar=0.000100, name="Siemens_2", scaling=1.0, in_service=True, type='wye')
# 
#     pp.create_load(net, bus=pp.get_element_index(net, "bus", "00102000722A1_LV"), p_mw=0.016710, q_mvar=-0.025789, name="Fontana_di_polo_1", scaling=1.0, in_service=True, type='wye')
#     pp.create_load(net, bus=pp.get_element_index(net, "bus", "00102000722A1_LV"), p_mw=0.000100, q_mvar=0.000100, name="Fontana_di_polo_2", scaling=1.0, in_service=True, type='wye')
#     
#     pp.create_load(net, bus=pp.get_element_index(net, "bus", "00102000723A1_LV"), p_mw=-0.058715, q_mvar=-0.082985, name="Aviosuperficie", scaling=1.0, in_service=True, type='wye')
# 
#     pp.create_load(net, bus=pp.get_element_index(net, "bus", "00102000725A1_LV"), p_mw=-0.002880, q_mvar=-0.008816, name="Tre_T_1", scaling=1.0, in_service=True, type='wye')
#     pp.create_load(net, bus=pp.get_element_index(net, "bus", "00102000725A1_LV"), p_mw=0.000100, q_mvar=0.000100, name="Tre_T_2", scaling=1.0, in_service=True, type='wye')
#     
#     pp.create_load(net, bus=pp.get_element_index(net, "bus", "00102000827A1_LV"), p_mw=0.0, q_mvar=0, name="Angelini", scaling=1.0, in_service=True, type='wye')
#     pp.create_load(net, bus=pp.get_element_index(net, "bus", "00102000724A1_LV"), p_mw=0.000100, q_mvar=0.000100, name="Tecnomultiservice", scaling=1.0, in_service=True, type='wye')
#     pp.create_load(net, bus=pp.get_element_index(net, "bus", "00102000764A1_LV"), p_mw=0.000706, q_mvar=-0.008028, name="Archimede", scaling=1.0, in_service=True, type='wye')
#  
# 
#     # 
# #     pp.create_sgen(net, bus=pp.get_element_index(net, "bus", "00102000459A1"), p_mw=0.050, q_mvar=0, name="PV_459_0")
# #     pp.create_sgen(net, bus=pp.get_element_index(net, "bus", "00102000722A1"), p_mw=0.050, q_mvar=0, name="PV_722_0")
# #     pp.create_sgen(net, bus=pp.get_element_index(net, "bus", "00102000722A1"), p_mw=0.050, q_mvar=0, name="PV_722_1")
# #     pp.create_sgen(net, bus=pp.get_element_index(net, "bus", "00102000723A1"), p_mw=0.050, q_mvar=0, name="PV_723_0")
# #     pp.create_sgen(net, bus=pp.get_element_index(net, "bus", "00102000723A1"), p_mw=0.050, q_mvar=0, name="PV_723_1")
# #     pp.create_sgen(net, bus=pp.get_element_index(net, "bus", "00102000723A1"), p_mw=0.050, q_mvar=0, name="PV_723_2")
# #     pp.create_sgen(net, bus=pp.get_element_index(net, "bus", "00102000723A1"), p_mw=0.050, q_mvar=0, name="PV_723_3")
# #     pp.create_sgen(net, bus=pp.get_element_index(net, "bus", "00102000725A1"), p_mw=0.050, q_mvar=0, name="PV_725_0")
# #     pp.create_sgen(net, bus=pp.get_element_index(net, "bus", "00102000725A1"), p_mw=0.050, q_mvar=0, name="PV_725_1")
# #     pp.create_sgen(net, bus=pp.get_element_index(net, "bus", "00102000827A1"), p_mw=0.050, q_mvar=0, name="PV_827_0")
# #     pp.create_sgen(net, bus=pp.get_element_index(net, "bus", "00102000764A1"), p_mw=0.050, q_mvar=0, name="PV_764_0")
# #     pp.create_sgen(net, bus=pp.get_element_index(net, "bus", "00102000764A1"), p_mw=0.050, q_mvar=0, name="PV_764_1")
# #     pp.create_sgen(net, bus=pp.get_element_index(net, "bus", "00102000764A1"), p_mw=0.050, q_mvar=0, name="PV_764_2")
# #     pp.create_sgen(net, bus=pp.get_element_index(net, "bus", "00102000764A1"), p_mw=0.050, q_mvar=0, name="PV_764_3")
# 
#     return net
#     
# 
#

import pandapower as pp #import pandapower
import numba
import json

def fdipolo_network():

    net = pp.create_empty_network() #create an empty network

    # create the buses
    bus1 = pp.create_bus(net, vn_kv=20, name="INT0723A1_0722A1_2", geodata=(42.57069445366638, 12.587663886588158), type='b', in_service=True, max_vm_pu=1.1, min_vm_pu=0.9)
    bus2 = pp.create_bus(net, vn_kv=20, name="00102000723A1", geodata=(42.57165583, 12.58597006), type='b', in_service=True, max_vm_pu=1.1, min_vm_pu=0.9)
    bus3 = pp.create_bus(net, vn_kv=20, name="INT0723A1_0722A1_3", geodata=(42.56657239561523, 12.592446945516475), type='b', in_service=True, max_vm_pu=1.1, min_vm_pu=0.9)
    bus4 = pp.create_bus(net, vn_kv=20, name="INT0723A1_0722A1_0", geodata=(42.576777640961765, 12.59165620494046), type='b', in_service=True, max_vm_pu=1.1, min_vm_pu=0.9)
    bus5 = pp.create_bus(net, vn_kv=20, name="INT0723A1_0722A1_1", geodata=(42.59155878367046, 12.594687963796105), type='b', in_service=True, max_vm_pu=1.1, min_vm_pu=0.9)
    bus6 = pp.create_bus(net, vn_kv=20, name="00102000827A1", geodata=(42.56587048, 12.58831038), type='b', in_service=True, max_vm_pu=1.1, min_vm_pu=0.9)
    bus7 = pp.create_bus(net, vn_kv=20, name="00102000722A1", geodata=(42.59163941, 12.59406697), type='b', in_service=True, max_vm_pu=1.1, min_vm_pu=0.9)
    bus8 = pp.create_bus(net, vn_kv=20, name="100000336", geodata=(42.562806023499064, 12.60568432070056), type='b', in_service=True, max_vm_pu=1.1, min_vm_pu=0.9)
    bus9 = pp.create_bus(net, vn_kv=20, name="INT001737_000336_1", geodata=(42.56153542478011, 12.605596903756808), type='b', in_service=True, max_vm_pu=1.1, min_vm_pu=0.9)
    bus10 = pp.create_bus(net, vn_kv=20, name="INT001737_000336_0", geodata=(42.56524604642435, 12.593271129007814), type='b', in_service=True, max_vm_pu=1.1, min_vm_pu=0.9)
    bus11 = pp.create_bus(net, vn_kv=20, name="INT0724A1_0764A1_0", geodata=(42.566642675302425, 12.590104267201315), type='b', in_service=True, max_vm_pu=1.1, min_vm_pu=0.9)
    bus12 = pp.create_bus(net, vn_kv=20, name="00102000764A1", geodata=(42.56799926, 12.58852029), type='b', in_service=True, max_vm_pu=1.1, min_vm_pu=0.9)
    bus13 = pp.create_bus(net, vn_kv=20, name="00102000724A1", geodata=(42.56738887, 12.59435605), type='b', in_service=True, max_vm_pu=1.1, min_vm_pu=0.9)
    bus14 = pp.create_bus(net, vn_kv=20, name="00102000725A1", geodata=(42.56725771, 12.59443875), type='b', in_service=True, max_vm_pu=1.1, min_vm_pu=0.9)
    bus15 = pp.create_bus(net, vn_kv=20, name="INT0459A1_0725A1_1", geodata=(42.56730938927409, 12.594034922229612), type='b', in_service=True, max_vm_pu=1.1, min_vm_pu=0.9)
    bus16 = pp.create_bus(net, vn_kv=20, name="INT0459A1_0725A1_0", geodata=(42.565244826989684, 12.593283815186203), type='b', in_service=True, max_vm_pu=1.1, min_vm_pu=0.9)
    bus17 = pp.create_bus(net, vn_kv=20, name="00102000459A1", geodata=(42.56470751, 12.59332143), type='b', in_service=True, max_vm_pu=1.1, min_vm_pu=0.9)
    bus18 = pp.create_bus(net, vn_kv=20, name="100001737", geodata=(42.562806023499064, 12.60568432070056), type='b', in_service=True, max_vm_pu=1.1, min_vm_pu=0.9)
    # LV BUS
    bus19 = pp.create_bus(net, vn_kv=0.4, name="00102000459A1_LV", geodata=(42.56470751, 12.59332143), type='b', in_service=True, max_vm_pu=1.1, min_vm_pu=0.9)
    bus20 = pp.create_bus(net, vn_kv=0.4, name="00102000722A1_LV", geodata=(42.59163941, 12.59406697), type='b', in_service=True, max_vm_pu=1.1, min_vm_pu=0.9)
    bus21 = pp.create_bus(net, vn_kv=0.4, name="00102000723A1_LV", geodata=(42.57165583, 12.58597006), type='b', in_service=True, max_vm_pu=1.1, min_vm_pu=0.9)
    bus22 = pp.create_bus(net, vn_kv=0.4, name="00102000725A1_LV", geodata=(42.56725771, 12.59443875), type='b', in_service=True, max_vm_pu=1.1, min_vm_pu=0.9)
    bus23 = pp.create_bus(net, vn_kv=0.4, name="00102000827A1_LV", geodata=(42.56587048, 12.58831038), type='b', in_service=True, max_vm_pu=1.1, min_vm_pu=0.9)
    bus24 = pp.create_bus(net, vn_kv=0.4, name="00102000724A1_LV", geodata=(42.56738887, 12.59435605), type='b', in_service=True, max_vm_pu=1.1, min_vm_pu=0.9)
    bus25 = pp.create_bus(net, vn_kv=0.4, name="00102000764A1_LV", geodata=(42.56799926, 12.58852029), type='b', in_service=True, max_vm_pu=1.1, min_vm_pu=0.9)

    # bus18 = pp.create_bus(net, vn_kv=20, name="ns0492_000", geodata=(12.63418, 42.526908), type='b', in_service=True, max_vm_pu=1.1, min_vm_pu=0.9)
    # bus19 = pp.create_bus(net, vn_kv=20, name="nd0103_000", geodata=(12.622921, 42.531), type='b', in_service=True, max_vm_pu=1.1, min_vm_pu=0.9)
    # bus20 = pp.create_bus(net, vn_kv=20, name="nd0103_001", geodata=(12.627205, 42.529751), type='b', in_service=True, max_vm_pu=1.1, min_vm_pu=0.9)
    # bus21 = pp.create_bus(net, vn_kv=20, name="ns0749_000", geodata=(12.621205, 42.529751), type='b', in_service=True, max_vm_pu=1.1, min_vm_pu=0.9)
    # bus22 = pp.create_bus(net, vn_kv=20, name="ns0493_000", geodata=(12.620421, 42.524806), type='b', in_service=True, max_vm_pu=1.1, min_vm_pu=0.9)
    # bus23 = pp.create_bus(net, vn_kv=20, name="ns0494_000", geodata=(12.623494, 42.520911), type='b', in_service=True, max_vm_pu=1.1, min_vm_pu=0.9)
    # bus24 = pp.create_bus(net, vn_kv=20, name="nm0970_001", geodata=(12.623594, 42.518011), type='b', in_service=True, max_vm_pu=1.1, min_vm_pu=0.9)
    # bus25 = pp.create_bus(net, vn_kv=20, name="ns0747_000", geodata=(12.623702, 42.513762), type='b', in_service=True, max_vm_pu=1.1, min_vm_pu=0.9)
    # bus26 = pp.create_bus(net, vn_kv=20, name="nd0104_001", geodata=(12.6183, 42.5213), type='b', in_service=True, max_vm_pu=1.1, min_vm_pu=0.9)
    # bus27 = pp.create_bus(net, vn_kv=20, name="ns0495_000", geodata=(12.614082, 42.522281), type='b', in_service=True, max_vm_pu=1.1, min_vm_pu=0.9)
    # bus28 = pp.create_bus(net, vn_kv=20, name="nd0105_000", geodata=(12.621339, 42.519436), type='b', in_service=True, max_vm_pu=1.1, min_vm_pu=0.9)
    # bus29 = pp.create_bus(net, vn_kv=20, name="ns0496_000", geodata=(12.620339, 42.517436), type='b', in_service=True, max_vm_pu=1.1, min_vm_pu=0.9)
    # bus30 = pp.create_bus(net, vn_kv=20, name="nm0971_001", geodata=(12.6173, 42.5173), type='b', in_service=True, max_vm_pu=1.1, min_vm_pu=0.9)
    # bus31 = pp.create_bus(net, vn_kv=20, name="ns0748_000", geodata=(12.615794, 42.513827), type='b', in_service=True, max_vm_pu=1.1, min_vm_pu=0.9)
    # bus32 = pp.create_bus(net, vn_kv=20, name="nd0104_000", geodata=(12.618, 42.521611), type='b', in_service=True, max_vm_pu=1.1, min_vm_pu=0.9)

    # create the external grid connection
    pp.create_ext_grid(net, bus=17, vm_pu=1.0, va_degree=0.0, name="ASM_Grid", in_service=True, s_sc_max_mva=31000, rx_max=0.125, r0x0_max=0.25)

    # create the linecodes
    pp.create_std_type(net, data={"r_ohm_per_km":0.23, "x_ohm_per_km":0.323, "c_nf_per_km":11.2, "max_i_ka":335, "type":"cs"}, name="A_AL_160", element='line', overwrite=True, check_required=True)
    pp.create_std_type(net, data={"r_ohm_per_km":0.164, "x_ohm_per_km":0.101, "c_nf_per_km":315, "max_i_ka":360, "type":"cs"}, name="C_CU_185", element='line', overwrite=True, check_required=True)
    pp.create_std_type(net, data={"r_ohm_per_km":0.125, "x_ohm_per_km":0.097, "c_nf_per_km":352, "max_i_ka":440, "type":"cs"}, name="C_AL_240", element='line', overwrite=True, check_required=True)

    # create the lines
    line1 = pp.create_line(net, from_bus=pp.get_element_index(net, "bus", "INT0723A1_0722A1_2"), to_bus=pp.get_element_index(net, "bus", "00102000723A1"), length_km=0.514, std_type="C_CU_185", name="00102000723A1_INT0723A1_0722A1_0")
    line2 = pp.create_line(net, from_bus=pp.get_element_index(net, "bus", "INT0723A1_0722A1_3"), to_bus=pp.get_element_index(net, "bus", "INT0723A1_0722A1_2"), length_km=1.298, std_type="A_AL_160", name="INT0723A1_0722A1_0_INT0723A1_0722A1_1")
    line3 = pp.create_line(net, from_bus=pp.get_element_index(net, "bus", "00102000827A1"), to_bus=pp.get_element_index(net, "bus", "INT0723A1_0722A1_3"), length_km=0.175, std_type="C_AL_240", name="INT0723A1_0722A1_1_00102000722A1")
    line4 = pp.create_line(net, from_bus=pp.get_element_index(net, "bus", "00102000723A1"), to_bus=pp.get_element_index(net, "bus", "INT0723A1_0722A1_0"), length_km=0.514, std_type="C_CU_185", name="00102000723A1_INT0723A1_0722A1_0")
    line5 = pp.create_line(net, from_bus=pp.get_element_index(net, "bus", "INT0723A1_0722A1_0"), to_bus=pp.get_element_index(net, "bus", "INT0723A1_0722A1_1"), length_km=1.8, std_type="A_AL_160", name="INT0723A1_0722A1_0_INT0723A1_0722A1_1")
    line6 = pp.create_line(net, from_bus=pp.get_element_index(net, "bus", "INT0723A1_0722A1_1"), to_bus=pp.get_element_index(net, "bus", "00102000722A1"), length_km=0.175, std_type="C_CU_185", name="INT0723A1_0722A1_1_00102000722A1")
    line7 = pp.create_line(net, from_bus=pp.get_element_index(net, "bus", "00102000722A1"), to_bus=pp.get_element_index(net, "bus", "100000336"), length_km=1.088, std_type="C_CU_185", name="00102000722A1_100000336")
    line8 = pp.create_line(net, from_bus=pp.get_element_index(net, "bus", "INT001737_000336_1"), to_bus=pp.get_element_index(net, "bus", "100000336"), length_km=0.107, std_type="C_CU_185", name="INT001737_000336_1_100000336")
    line9 = pp.create_line(net, from_bus=pp.get_element_index(net, "bus", "INT001737_000336_0"), to_bus=pp.get_element_index(net, "bus", "INT001737_000336_1"), length_km=2.446, std_type="A_AL_160", name="INT001737_000336_0_INT001737_000336_1")
    line10 = pp.create_line(net, from_bus=pp.get_element_index(net, "bus", "100001737"), to_bus=pp.get_element_index(net, "bus", "INT001737_000336_0"), length_km=0.773, std_type="C_CU_185", name="100001737_INT001737_000336_0")
    line11 = pp.create_line(net, from_bus=pp.get_element_index(net, "bus", "INT001737_000336_1"), to_bus=pp.get_element_index(net, "bus", "100000336"), length_km=0.107, std_type="C_CU_185", name="INT001737_000336_1_100000336")
    line12 = pp.create_line(net, from_bus=pp.get_element_index(net, "bus", "INT001737_000336_0"), to_bus=pp.get_element_index(net, "bus", "INT001737_000336_1"), length_km=2.446, std_type="A_AL_160", name="INT001737_000336_0_INT001737_000336_1")
    line13 = pp.create_line(net, from_bus=pp.get_element_index(net, "bus", "100001737"), to_bus=pp.get_element_index(net, "bus", "INT001737_000336_0"), length_km=0.773, std_type="C_CU_185", name="100001737_INT001737_000336_0")
    line14 = pp.create_line(net, from_bus=pp.get_element_index(net, "bus", "00102000764A1"), to_bus=pp.get_element_index(net, "bus", "00102000827A1"), length_km=0.573, std_type="C_AL_240", name="00102000764A1_00102000827A1")
    line15 = pp.create_line(net, from_bus=pp.get_element_index(net, "bus", "INT0724A1_0764A1_0"), to_bus=pp.get_element_index(net, "bus", "00102000764A1"), length_km=0.171, std_type="C_AL_240", name="INT0724A1_0764A1_0_00102000764A1")
    line16 = pp.create_line(net, from_bus=pp.get_element_index(net, "bus", "00102000724A1"), to_bus=pp.get_element_index(net, "bus", "INT0724A1_0764A1_0"), length_km=0.368, std_type="C_CU_185", name="00102000724A1_INT0724A1_0764A1_0")
    line17 = pp.create_line(net, from_bus=pp.get_element_index(net, "bus", "00102000725A1"), to_bus=pp.get_element_index(net, "bus", "00102000724A1"), length_km=0.016, std_type="C_CU_185", name="00102000724A1_00102000725A1")
    line18 = pp.create_line(net, from_bus=pp.get_element_index(net, "bus", "INT0459A1_0725A1_1"), to_bus=pp.get_element_index(net, "bus", "00102000725A1"), length_km=0.06, std_type="C_CU_185", name="INT0459A1_0725A1_1_00102000725A1")
    line19 = pp.create_line(net, from_bus=pp.get_element_index(net, "bus", "INT0459A1_0725A1_0"), to_bus=pp.get_element_index(net, "bus", "INT0459A1_0725A1_1"), length_km=0.121, std_type="A_AL_160", name="INT0459A1_0725A1_0_INT0459A1_0725A1_1")
    line20 = pp.create_line(net, from_bus=pp.get_element_index(net, "bus", "00102000459A1"), to_bus=pp.get_element_index(net, "bus", "INT0459A1_0725A1_0"), length_km=0.325, std_type="C_CU_185", name="00102000459A1_INT0459A1_0725A1_0")
   
    # create transformer codes https://pandapower.readthedocs.io/en/latest/std_types/manage.html
    pp.create_std_type(net, {"sn_mva": 0.16,
        "vn_hv_kv": 20,
        "vn_lv_kv": 0.4,
        "vk_percent": 6,
        "vkr_percent": (2.3-0.65)/160,
        "pfe_kw": 0.65,
        "i0_percent": 2.3,
        "shift_degree": 0,
        "vector_group": 'Dyn',
        "tap_side": "lv",
        "tap_neutral": 0,
        "tap_min": -2,
        "tap_max": 2,
        "tap_step_degree": 0,
        "tap_step_percent": 2.5,
        "tap_phase_shifter":False}, name='SIEMENS_TR_160kVA', element="trafo", overwrite=True, check_required=True)
       
    pp.create_std_type(net, {"sn_mva": 0.1,
        "vn_hv_kv": 20,
        "vn_lv_kv": 0.4,
        "vk_percent": 6,
        "vkr_percent": (1.8-0.46)/100,
        "pfe_kw": 0.46,
        "i0_percent": 2.5,
        "shift_degree": 0,
        "vector_group": 'Dyn',
        "tap_side": "lv",
        "tap_neutral": 0,
        "tap_min": -2,
        "tap_max": 2,
        "tap_step_degree": 0,
        "tap_step_percent": 2.5, "tap_phase_shifter":False}, name='FDIPOLO_TR_100kVA', element="trafo", overwrite=True, check_required=True)
   
    pp.create_std_type(net, {"sn_mva": 0.4,
        "vn_hv_kv": 20,
        "vn_lv_kv": 0.4,
        "vk_percent": 6,
        "vkr_percent": (4.8-1.2)/400,
        "pfe_kw": 1.2,
        "i0_percent": 1.5,
        "shift_degree": 0,
        "vector_group": 'Dyn',
        "tap_side": "lv",
        "tap_neutral": 0,
        "tap_min": -2,
        "tap_max": 2,
        "tap_step_degree": 0,
        "tap_step_percent": 2.5, "tap_phase_shifter":False}, name='AVIOSUPERFICIE_TR_400kVA', element="trafo", overwrite=True, check_required=True)
   
   
    pp.create_std_type(net, {"sn_mva": 0.25,
        "vn_hv_kv": 20,
        "vn_lv_kv": 0.4,
        "vk_percent": 6,
        "vkr_percent": (3.4-0.88)/250,
        "pfe_kw": 0.88,
        "i0_percent": 2,
        "shift_degree": 0,
        "vector_group": 'Dyn',
        "tap_side": "lv",
        "tap_neutral": 0,
        "tap_min": -2,
        "tap_max": 2,
        "tap_step_degree": 0,
        "si0_hv_partial": 0.9, "tap_phase_shifter":False}, name='ANGELINI_TR_250kVA', element="trafo", overwrite=True, check_required=True)
   
    # create transfomermers
    tr1 = pp.create_transformer(net, hv_bus=pp.get_element_index(net, "bus", "00102000459A1"), lv_bus=pp.get_element_index(net, "bus", "00102000459A1_LV"), std_type="SIEMENS_TR_160kVA", name="SIEMENS_TR", in_service=True, parallel=1)
    tr2 = pp.create_transformer(net, hv_bus=pp.get_element_index(net, "bus","00102000722A1"), lv_bus=pp.get_element_index(net, "bus","00102000722A1_LV"), std_type="FDIPOLO_TR_100kVA", name="FDIPOLO_TR", in_service=True, parallel=1)
    tr3 = pp.create_transformer(net, hv_bus=pp.get_element_index(net, "bus", "00102000723A1"), lv_bus=pp.get_element_index(net, "bus","00102000723A1_LV"), std_type="AVIOSUPERFICIE_TR_400kVA", name="AVIOSUPERFICIE_TR", in_service=True, parallel=1)
    tr4 = pp.create_transformer(net, hv_bus=pp.get_element_index(net,  "bus","00102000725A1"), lv_bus=pp.get_element_index(net, "bus","00102000725A1_LV"), std_type="SIEMENS_TR_160kVA", name="TRE_T_TR", in_service=True, parallel=1)
    tr5 = pp.create_transformer(net, hv_bus=pp.get_element_index(net, "bus", "00102000827A1"), lv_bus=pp.get_element_index(net, "bus","00102000827A1_LV"), std_type="ANGELINI_TR_250kVA", name="ANGELINI_TR", in_service=True, parallel=1)
    tr7 = pp.create_transformer(net, hv_bus=pp.get_element_index(net, "bus", "00102000724A1"), lv_bus=pp.get_element_index(net, "bus","00102000724A1_LV"), std_type="ANGELINI_TR_250kVA", name="ANGELINI_TR", in_service=True, parallel=1)
    tr6 = pp.create_transformer(net, hv_bus=pp.get_element_index(net,  "bus","00102000764A1"), lv_bus=pp.get_element_index(net, "bus","00102000764A1_LV"), std_type="ANGELINI_TR_250kVA", name="ARCHIMEDE_TR", in_service=True, parallel=1)


    # create loads
    pp.create_load(net, bus=pp.get_element_index(net, "bus", "00102000459A1_LV"), p_mw=0.000525, q_mvar=-0.001888, name="Siemens_1", scaling=1.0, in_service=True, type='wye')
    pp.create_load(net, bus=pp.get_element_index(net, "bus", "00102000459A1_LV"), p_mw=0.000100, q_mvar=0.000100, name="Siemens_2", scaling=1.0, in_service=True, type='wye')

    pp.create_load(net, bus=pp.get_element_index(net, "bus", "00102000722A1_LV"), p_mw=0.016710, q_mvar=-0.025789, name="Fontana_di_polo_1", scaling=1.0, in_service=True, type='wye')
    pp.create_load(net, bus=pp.get_element_index(net, "bus", "00102000722A1_LV"), p_mw=0.000100, q_mvar=0.000100, name="Fontana_di_polo_2", scaling=1.0, in_service=True, type='wye')
   
    pp.create_load(net, bus=pp.get_element_index(net, "bus", "00102000723A1_LV"), p_mw=-0.058715, q_mvar=-0.082985, name="Aviosuperficie", scaling=1.0, in_service=True, type='wye')

    pp.create_load(net, bus=pp.get_element_index(net, "bus", "00102000725A1_LV"), p_mw=-0.002880, q_mvar=-0.008816, name="Tre_T_1", scaling=1.0, in_service=True, type='wye')
    pp.create_load(net, bus=pp.get_element_index(net, "bus", "00102000725A1_LV"), p_mw=0.000100, q_mvar=0.000100, name="Tre_T_2", scaling=1.0, in_service=True, type='wye')
   
    pp.create_load(net, bus=pp.get_element_index(net, "bus", "00102000827A1_LV"), p_mw=0.0, q_mvar=0, name="Angelini", scaling=1.0, in_service=True, type='wye')
    pp.create_load(net, bus=pp.get_element_index(net, "bus", "00102000724A1_LV"), p_mw=0.000100, q_mvar=0.000100, name="Tecnomultiservice", scaling=1.0, in_service=True, type='wye')
    pp.create_load(net, bus=pp.get_element_index(net, "bus", "00102000764A1_LV"), p_mw=0.000706, q_mvar=-0.008028, name="Archimede", scaling=1.0, in_service=True, type='wye')
 

    #
#     pp.create_sgen(net, bus=pp.get_element_index(net, "bus", "00102000459A1"), p_mw=0.050, q_mvar=0, name="PV_459_0")
#     pp.create_sgen(net, bus=pp.get_element_index(net, "bus", "00102000722A1"), p_mw=0.050, q_mvar=0, name="PV_722_0")
#     pp.create_sgen(net, bus=pp.get_element_index(net, "bus", "00102000722A1"), p_mw=0.050, q_mvar=0, name="PV_722_1")
#     pp.create_sgen(net, bus=pp.get_element_index(net, "bus", "00102000723A1"), p_mw=0.050, q_mvar=0, name="PV_723_0")
#     pp.create_sgen(net, bus=pp.get_element_index(net, "bus", "00102000723A1"), p_mw=0.050, q_mvar=0, name="PV_723_1")
#     pp.create_sgen(net, bus=pp.get_element_index(net, "bus", "00102000723A1"), p_mw=0.050, q_mvar=0, name="PV_723_2")
#     pp.create_sgen(net, bus=pp.get_element_index(net, "bus", "00102000723A1"), p_mw=0.050, q_mvar=0, name="PV_723_3")
#     pp.create_sgen(net, bus=pp.get_element_index(net, "bus", "00102000725A1"), p_mw=0.050, q_mvar=0, name="PV_725_0")
#     pp.create_sgen(net, bus=pp.get_element_index(net, "bus", "00102000725A1"), p_mw=0.050, q_mvar=0, name="PV_725_1")
#     pp.create_sgen(net, bus=pp.get_element_index(net, "bus", "00102000827A1"), p_mw=0.050, q_mvar=0, name="PV_827_0")
#     pp.create_sgen(net, bus=pp.get_element_index(net, "bus", "00102000764A1"), p_mw=0.050, q_mvar=0, name="PV_764_0")
#     pp.create_sgen(net, bus=pp.get_element_index(net, "bus", "00102000764A1"), p_mw=0.050, q_mvar=0, name="PV_764_1")
#     pp.create_sgen(net, bus=pp.get_element_index(net, "bus", "00102000764A1"), p_mw=0.050, q_mvar=0, name="PV_764_2")
#     pp.create_sgen(net, bus=pp.get_element_index(net, "bus", "00102000764A1"), p_mw=0.050, q_mvar=0, name="PV_764_3")

    return net