from google.cloud import pubsub_v1

publisher = pubsub_v1.PublisherClient()


def publicar(topic_path, product_name):
    try:
        future = publisher.publish(topic_path, product_name.encode("utf-8"))
        print(future.result())
        print(f"Published {product_name} to {topic_path}.")
    except Exception as e:
        print(e)
