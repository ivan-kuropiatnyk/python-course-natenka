'''
Python for network engineers Natasha Samoilenko
'''
# Page range 114-118
#TASK = 5.2, 5.2a
ip_address_mask = input("Please input IP address in a format: 10.1.1.0/24 :")
#ip_address_mask = "10.1.1.1/24"

#--------Part for IP calculation
ip_add = list(ip_address_mask.split("/"))[0]
ip_add_spl = list(list(ip_address_mask.split("/"))[0].split("."))
ip_add_1oct = int(ip_add_spl[0])
ip_add_2oct = int(ip_add_spl[1])
ip_add_3oct = int(ip_add_spl[2])
ip_add_4oct = int(ip_add_spl[3])
ip_add_print = f'''
                IP ADDRESS = {ip_add}
                IN DECIMELS:
                {ip_add_1oct:03}  {ip_add_2oct:03}  {ip_add_3oct:03}  {ip_add_4oct:03}
                IN BINARIES:
                {ip_add_1oct:08b} {ip_add_2oct:08b} {ip_add_3oct:08b} {ip_add_4oct:08b}
                '''
#----------Part for mask calculation
mask = list(ip_address_mask.split("/"))[1]#took mask from text
qnul = 32 - int(mask)#quontity of zeroes
qone = 32 - qnul#quontity of ones
mask_qone_qnul = ("1"*qone)+("0"*qnul)
mask_o1 = mask_qone_qnul[0:8]#chunk 1 of 32 bits, 4 chunks in total by 8 bits
mask_o2 = mask_qone_qnul[8:16]
mask_o3 = mask_qone_qnul[16:24]
mask_o4 = mask_qone_qnul[24:]
mask_o1_i = int(mask_o1,2)#convert from binary to integer
mask_o2_i = int(mask_o2,2)
mask_o3_i = int(mask_o3,2)
mask_o4_i = int(mask_o4,2)
mask_print = f'''
                Mask entered = {mask}
                Mask IN DECIMELS:
                {mask_o1_i} {mask_o2_i:8} {mask_o3_i:8} {mask_o4_i:8}
                Mask IN BINARIES:
                {mask_o1} {mask_o2} {mask_o3} {mask_o4}
                '''
#------------IP of the network
ip_add_net = f"{ip_add_1oct:08b}{ip_add_2oct:08b}{ip_add_3oct:08b}{ip_add_4oct:08b}"
ip_add_net = list(ip_add_net)
del ip_add_net [qone:]
ip_add_net = ','.join(ip_add_net).replace(",","")
ip_qnul = "0"*qnul
ip_add_net = ip_add_net + ip_qnul
ip_add_net_o1 = ip_add_net[0:8]#chunk 1 of 32 bits, 4 chunks in total by 8 bits
ip_add_net_o2 = ip_add_net[8:16]
ip_add_net_o3 = ip_add_net[16:24]
ip_add_net_o4 = ip_add_net[24:]
ip_add_net_o1_i = int(ip_add_net_o1,2)#convert from binary to integer
ip_add_net_o2_i = int(ip_add_net_o2,2)
ip_add_net_o3_i = int(ip_add_net_o3,2)
ip_add_net_o4_i = int(ip_add_net_o4,2)
ip_add_net_print = f'''
                Network address in dec:
                {ip_add_net_o1_i} {ip_add_net_o2_i:8} {ip_add_net_o3_i:8} {ip_add_net_o4_i:8}
                Network address in binaries:
                {ip_add_net_o1}   {ip_add_net_o2}     {ip_add_net_o3}     {ip_add_net_o4}
                '''
print(ip_add_print)
print(mask_print)
print(ip_add_net_print)