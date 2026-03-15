from quixstreams import Application
from fakeData import createFakeDeliveryAgent
import time



def main():

    """
    Main function to produce fake delivery agent data to a Kafka topic.

    This function creates a Quix Streams application, produces fake delivery agent data using the createFakeDeliveryAgent function, 
    and publishes it to a Kafka topic named "demo_test" with a key of "Delivery Agent". The data is produced in an infinite loop 
    with a 5-second delay between each message.

    Parameters:
    None

    Returns:
    None
    
    """


    app = Application(broker_address="localhost:9092")

    topics = ["testmul_1", "testmul_2", "testmul_3"]  # List of topics
    
    with app.get_producer() as producer:
        while True:
            for topic in topics:
                message = createFakeDeliveryAgent()  # Create a message for each topic
                producer.produce(
                    topic=topic,
                    key="Delivery Agent",
                    value=message
                )
                print(f"Pushed to topic {topic}")

            time.sleep(2)  # Add delay between pushes


if __name__=="__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass

