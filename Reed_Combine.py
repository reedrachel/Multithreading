#Reed_Combine



import csv, threading, json, os

with open('ccombine.csv', 'w', newline='\n', encoding='utf-8') as f:
    f.write("prod_id,prod_sku,prod_cat,prod_name\n")
    temp = []
    for root,dirs, files in os.walk('Output'):
        #print(root,dirs,files)
        path = root.split(os.sep)
        for fn in files:
            fp = root+os.sep+fn

            file = open(fp, 'r')
            print(fp)
            for line in file:
                if "prod_id" in line:
                    l = json.loads(line)["data"]
                    f.write(str(l["prod_id"]) + "," + str(l["prod_sku"]) + "," + str(l["prod_cat"])  + "," + str(l["prod_name"]) + "\n")
