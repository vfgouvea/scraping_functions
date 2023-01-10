from google.cloud import pubsub_v1

subscriber = pubsub_v1.SubscriberClient()


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