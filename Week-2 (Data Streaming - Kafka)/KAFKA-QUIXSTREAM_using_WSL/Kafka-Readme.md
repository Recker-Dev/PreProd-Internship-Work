## Data Streaming with WSL, Kafka, and Quixstreams

<br>
**READ BEFORE PROCEEDING**: The initial approach was attempted, but it ultimately failed due to network porting issues. Many of the steps in that process may no longer be relevant if using SSH tunneling with properly configured private and public keys, or by employing a different authentication method to connect to the server.

For a more streamlined approach, please refer to the **README_SIMPLE.md** file, which outlines a simplified and more effective method.
<br><br>

## Overview

This project demonstrates a data streaming process using Windows Subsystem for Linux (WSL), Kafka, and Quixstreams. We utilize Faker to generate fake custom data for this example.

## Setup and Configuration

1. Installing and Configuring WSL **(MOST IMPORTANT AND MOST DIFFICULT STEP)**

   -Install WSL2 on your system and ensure it's working. Note that this process may involve troubleshooting various bugs and using different methods found online.

2. Configuring Windows Firewall

   -In Windows Firewall, create a new inbound rule:

   - Select "Port" and customize it for TCP.
   - Specify the port as 9092.

3. Setting up Port Forwarding with netsh

   -Open PowerShell in administrator mode and run the following commands:

   - `netsh interface portproxy add v6tov4 listenport=9092 listenaddress=:: connectport=9092 connectaddress=WSL_IP_ADDR`
   - `netsh interface portproxy add v4tov4 listenport=9092 listenaddress=localhost connectport=9092 connectaddress=WSL_IP_ADDR`

     -Note:

     - To find the WSL IP address, install net-tools with `sudo apt install net-tools` and use `ifconfig` to retrieve the IP address.
     - `netsh interface portproxy reset` to reset all netsh rules.

4. Downloading and Installing Kafka

   - We need the latest binary link and download it using wget in a suitable folder inside the WSL.
   - We used `wget https://downloads.apache.org/kafka/3.8.0/kafka_2.12-3.8.0.tgz`
   - Extract the zip file using `tar xvzf "filename"`
   - Install OpenJDK-8-JDK as Kafka requires Java to run: `sudo apt-get install openjdk-8-jdk`
   - Run `sudo apt update`

5. Setting up Kafka

   - cd into the extracted Kafka directory.

6. Starting Kafka Instances

   - Start 3 instances of WSL in the Kafka directory:
     - One for ZooKeeper
     - One for the Kafka Broker
     - One to create a new topic

7. Starting Kafka Services

   - To start ZooKeeper: `./bin/zookeeper-server-start.sh config/zookeeper.properties`
   - To start the Kafka Broker: `./bin/kafka-server-start.sh config/server.properties`
   - To create a new topic: `./bin/kafka-topics.sh --bootstrap-server localhost:9092 --create --topic test --replication-factor 1 --partitions 1`

8. Setting up the Python Environment

   - Create a new folder on your Windows machine for the project.
   - Create a virtual Python environment to contain the Quixstreams and Faker dependencies.
   - Install the required dependencies; `pip install -r requirements.txt`

9. Running the Producer and Consumer

   - Create the necessary files in the folder, including producer.py and consumer.py.
   - Run the producer script: `python producer.py`
   - Run the consumer script in a new terminal window: `python consumer.py`

     Note: The consumer will not work if the producer is not already running, as it relies on the streaming data.

10. Verifying Live Data Streaming

    - If all goes well, live data streaming has been made possible using WSL, Kafka, and Quixstreams.
    - Verify that data is being produced and consumed correctly by checking the terminal outputs.
