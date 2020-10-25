/*
 * tcp.h
 * shinchokuer: tari
 *
 * DESCRIPTION
 *  This is for using WLAN-TCP feature of duck controller.
 *
 * DEPENDENCIES
 *  This header file needs WiFi.h, standard library, and additional
 *  header file to define connection info.
 *
 * usage:
 * init_tcp(int port, char* addr)
 *   port: port number, remote hosts.
 *   addr: IP address, remote hosts.
 * send_tcp(content_send)
 *   content_send: a character you want to send to the remote host.
 */

#include <WiFi.h>

extern void disp_string(char*);
extern void disp_stringln(char*);

extern int MODE_NETWORK_CLIENT;

extern WiFiClient client;
extern WiFiServer server;  //Port番号

extern const int port_tcp_remote;
extern const char* addr_ip_remote;

//static WiFiUDP wifiUdp;

void init_tcp() {
    Serial.println("FUNCTION    > INIT_TCP");
    int count_retry = 0;
    char str[50];
    Serial.println("INIT SRVC   > TCP");
    if(MODE_NETWORK_CLIENT){
        Serial.println("START SRVC  > TCP SUCCESS");
        disp_string("RM ADDR: ");
        sprintf(str,"%s",addr_ip_remote);
        disp_stringln(str);
        disp_string("RM PORT: ");
        sprintf(str,"%d",port_tcp_remote);
        disp_stringln(str);
        disp_string("Try: ");
        for(count_retry = 0 ; count_retry <= 5 ; count_retry++){
          disp_string("* ");
          //if()
            if(client.connect(addr_ip_remote, port_tcp_remote)){
                Serial.println("START SRVC  > TCP CL SUCCESS");
                Serial.println("TASK STATUS > DONE SUCCESS");
                disp_stringln(" ");
                return;
            };
        }
    }
    else{
        server.begin();
        Serial.println("START SRVC  > TCP SV SUCCESS");
        Serial.println("TASK STATUS > DONE SUCCESS");
        return;
    }
    Serial.println("START SRVC  > TCP FAILE∏");
    Serial.println("TASK STATUS > FAILE∏");
}

void send_tcp(char* content_send) {
    Serial.println("FUNCTION    > SEND_TCP");
    Serial.print("SEND CHAR   > ");
    Serial.println(content_send);
    client.print(content_send);
    //client.readStringUntil('\r');
    Serial.println("TASK STATUS > DONE SUCCESS");
}
