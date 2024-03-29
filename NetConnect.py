import network, time, socket


class NetTools(object):
    def __init__(self, essid, passwd):
        self.essid = essid
        self.passwd = passwd
        self.client = None
        
        # connect wifi
        self.wlan = network.WLAN(network.STA_IF)
        self.wlan.active(True)
        
        if not self.wlan.isconnected():
            print('connecting to network...')
            self.wlan.connect(self.essid, self.passwd)
            while not wlan.isconnected():
                print("connecting to network...")
                time.sleep(1)
        self.ipconfig = self.wlan.ifconfig()
        
    def SendTCP(self, target_IP,target_port, message):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            
        self.client.connect((target_IP, target_port))
        self.client.send(message.encode('utf-8'))
        recv_data = self.client.recv(1024)
        print(recv_data)
        self.client.close()
        


if __name__ == "__main__":
    net1 = NetTools("MianNMN_Net", "12345678")
    print(net1.ipconfig)
    net1.SendTCP("192.168.43.252", 8080, "test message (client)")
    