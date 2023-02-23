# Python Round-Robin Load Balancer

This is a Python project that demonstrates how to implement a load balancer using socket package. It consists of a client, a main server, and three processing servers. The client sends information to the main server, which then implements round-robin logic to distribute the load between the processing servers.

## Installation
To run this project, you will need to have Python 3.x installed on your machine. Clone the repository to your local machine using the following command:
```
git clone https://github.com/MrRique15/roundRobin-client-server.git
```

It uses only native packages, so you don´t need installing any requirements.

## Usage
To use the load balancer and run the simulation, you need to start the processing servers first, followed by the main server, and then the client. Here are the steps to do this:

1. Open three terminal windows and navigate to the project directory in each one.

2. In the first terminal window, start the S1 server by running the following command:
```
python s1_socket_s.py
```
3. In the second terminal window, start the S2 server by running the following command:
```
python s2_socket_s.py
```
4. In the third terminal window, start the S3 server by running the following command:
```
5. python s3_socket_s.py
```
6. In another terminal window, start the main server by running the following command:
```
python main_socket_s.py
```
7. Finally, in another terminal window, start the client by running the following command:
```
python c1_socket_c.py
```

### Simulation Flow
The client will automatically send three messages to the servers, which will be distributed using the round-robin logic implemented by the main server. After the processing of these three messages, the client will wait for user input to send new messages.