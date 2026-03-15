from quixstreams import Application
import json

def main():

    """
    Consumes messages from the 'demo_test' topic using the Quix Streams Kafka consumer.

    This function creates a Quix Streams application, subscribes to the 'demo_test' topic,
    and continuously polls for new messages. If a message is received, it decodes the key,
    parses the value as JSON, and prints the offset, key, and value. If an error occurs,
    it prints the error message.

    Parameters:
    None

    Returns:
    None
    """

    app =Application(
        broker_address="localhost:9092",
        consumer_group="delivery_agent_details_reader",
        auto_offset_reset="latest"
    )

    with app.get_consumer() as consumer:
        # print(consumer.list_topics()) 
        consumer.subscribe(["testmul_1"])

        while True:
            msg = consumer.poll(1)
            if msg is None:
                print("Waiting....")
            elif msg.error() is not None:
                print(f"Error: {msg.error()}")
                raise Exception(msg.error())
            else:
                key=msg.key().decode("utf-8")
                value=json.loads(msg.value())
                offset=msg.offset()

                print(f"{offset} {key} {value}")
                consumer.store_offsets(msg)



if __name__=="__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
    


