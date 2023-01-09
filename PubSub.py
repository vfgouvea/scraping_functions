from google.cloud import pubsub_v1

publisher = pubsub_v1.PublisherClient()
subscriber = pubsub_v1.SubscriberClient()


def publicar(topic_path, product_name):
    try:
        future = publisher.publish(topic_path, product_name.encode("utf-8"))
        print(future.result())
        print(f"Published {product_name} to {topic_path}.")
    except Exception as e:
        print(e)


def lerNomeProduto(subcription_name, callback):

    def subscribeCallback(message: pubsub_v1.subscriber.message.Message):
        nomeProduto = message.data.decode('utf-8')
        callback(nomeProduto)
        message.ack()

    try:
        future = subscriber.subscribe(subcription_name, subscribeCallback)
        future.result()
    except Exception as e:
        print(e)
