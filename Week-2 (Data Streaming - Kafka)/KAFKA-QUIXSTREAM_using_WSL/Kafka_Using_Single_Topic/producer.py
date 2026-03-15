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

    with app.get_producer() as producer:
        while True:
            message=createFakeDeliveryAgent()
            producer.produce(topic="demo_test",
            key="Delivery Agent",
            value=message)
            print("Pushed to Kafka")
            time.sleep(5)


if __name__=="__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass

