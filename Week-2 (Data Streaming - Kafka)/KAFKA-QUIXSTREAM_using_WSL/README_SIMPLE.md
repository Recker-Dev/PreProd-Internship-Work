# Data Streaming with WSL, Kafka, and Quixstreams

## Overview

This project demonstrates a data streaming process using Windows Subsystem for Linux (WSL), Kafka, and Quixstreams. We utilize Faker to generate fake custom data for this example.

This project also need you to be comfortable with using Command Line Interface(CLI); incase you are new to this, the project provided enough details to carry them out if followed correctly and using a bit of intuition.

## Setup and Configuration

1. Installing and Configuring WSL **(MOST IMPORTANT AND MOST DIFFICULT STEP)**

   - Install WSL2 on your system and ensure it's working. Note that this process may involve troubleshooting various bugs and need to be resolved using different methods found online.
   - https://learn.microsoft.com/en-us/windows/wsl/install use as reference material.
   - wsl version 2 is preferred and default OS of ubuntu should be enough.

2. Verify wsl is properly configured and ubuntu is up and running.

   - Run these command in powershell:
     - `wsl --status`
     - `wsl --list --verbose`
     - `wsl -d Ubuntu`

3. Run wsl by using the command `wsl` in powershell.
4. Create a seperate directory for this project inside wsl, using command `mkdir directory_name_placeholder`
5. Change directory by using the command; `cd directory_name_placeholder`
6. Downloading and Installing Kafka

   - We need the latest binary link and download it using wget in a suitable folder inside the WSL.
   - We used `wget https://downloads.apache.org/kafka/3.8.0/kafka_2.12-3.8.0.tgz`
   - Note: This was the latest binary available when the project was built, it might be changed when you are reading this; just replace the https and it should be fine.
   - See the downloaded file name using command `ls` inside the current directory.
   - Extract the zip file using `tar xvzf file_name_placeholder`
   - Example: `tar xvzf kafka_2.12-3.8.0.tgz`
   - Run: `sudo apt-get update`
   - Install OpenJDK-8-JDK as Kafka requires Java to run: `sudo apt-get install openjdk-8-jdk`
   - Run `sudo apt update`
   - Verify Java Version using: `java -version`
   - We should now have 2 directories; check using `ls`, you can delete the zipped file now using `rm -rf zipped_file_name_placeholder`
   - Example: rm -rf kafka_2.12-3.8.0.tgz

7. Setting up Kafka

   - cd into the extracted Kafka directory.

8. Starting Kafka Instances

   - Start 3 instances of WSL in the Kafka directory:
     - One for ZooKeeper
     - One for the Kafka Broker
     - One to create a new topic

9. Starting Kafka Services

   - To start ZooKeeper: `./bin/zookeeper-server-start.sh config/zookeeper.properties`
   - To start the Kafka Broker: `./bin/kafka-server-start.sh config/server.properties`
   - To create a new topic: `./bin/kafka-topics.sh --bootstrap-server localhost:9092 --create --topic test --replication-factor 1 --partitions 1`

10. **Keep the instance of Zookeeper and Kafka Broker/Server running! First run zookeeper and then the Broker.**

11. Download all the files present inside, "Kafka_Using_Single_Topic"

12. Move one level up of the kafka binary extracted directory; using `cd ..`

13. Create a new directory for Python Scripts `mkdir python_directoryname_placeholder` and cd inside it `cd python_directoryname_placeholder`

14. Copy all the files and subdirectories(if any) from "Kafka_Using_Single_Topic"; using `cp -r /path/to/source/\* .`

    - The \* . is essential for copying ALL files and sudirectories.
    - Run this command inside the python_directoryname_placeholder directory.
    - We want the files from "Kafka_Using_Single_Topic" inside the python_directoryname_placeholder directory.

15. Initialize Python and Pip inside wsl enviornment:

    - Run the following commands:

      - `sudo apt update`
      - `sudo apt install python3`
      - `sudo apt install python3-pip`

    - If all these command worked properly, python and pip are succesfully installed.

16. Install the required python packages.

    - `pip install Faker`
    - `pip install quixstreams`

17. On using command `ls`; it should show fakeData.py, producer.py, consumer.py

18. Run two wsl terminals and traverse to the python_directoryname_placeholder directory.

19. Run the two commands seperately in the two terminals:
    - `python3 consumer.py`
    - `python3 producer.py`

### Conclusion

If everything goes well, you should be able to see Data-Streaming in action! Now explore the scripts in "Kafka_Using_Multi_Topics" see the topic names, create the topics accordingly and copy the python scripts into the wsl environment and it should be working fine.

Shortcut: cd into the dowloaded Python Scripts folder using your wsl terminal. To run them without copying
