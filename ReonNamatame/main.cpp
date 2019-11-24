#include "mbed.h"
#include "EthernetInterface.h"

//DigitalOut myled(LED1);
//Serial pc(USBTX, USBRX);
 
int main() {
    Serial pc(USBTX, USBRX);

    //pc.printf("aaaa\n");
    EthernetInterface eth;
    int result = eth.EthernetInterface::init(); //Use DHCP
    
    //wait(1);
    pc.printf("aiueo");
    
    if(result < 0){
        pc.printf("cannot init.\n");
    }
    pc.printf("bbbb\n");
    
    if(eth.EthernetInterface::connect() < 0){
        pc.printf("connection error.\n");
    }
    pc.printf("cccc\n");
    
    pc.printf("IP Address is %s\n", eth.getIPAddress());
    
    TCPSocketConnection sock;
    sock.connect("mbed.org", 80);
    
    char http_cmd[] = "GET /media/uploads/mbed_official/hello.txt HTTP/1.0\n\n";
    sock.send_all(http_cmd, sizeof(http_cmd)-1);
    
    char buffer[300];
    int ret;
    
    while (true) {
        ret = sock.receive(buffer, sizeof(buffer)-1);
        if (ret <= 0)
            break;
        buffer[ret] = '\0';
        pc.printf("Received %d chars from server:\n%s\n", ret, buffer);
    }
      
    sock.close();
    
    eth.disconnect();
    while(1) {}
}