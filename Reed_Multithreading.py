#Multithreading

import requests,json,time,os,threading

#function call
def file_save(n):
    r = requests.get("https://clarksonmsda.org/api/get_product.php?pid=" + str(n))
    print(r.text)
    file = open('Output/file_num_' + str(n) + '.txt', 'w')
    file.write(r.text)
    file.close()

n=0
while n <= 200:
    w = threading.Thread(name='tid_' + str(n), target=file_save, args=(n,))
    w.start()
    n += 1

    
