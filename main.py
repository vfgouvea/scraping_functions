import functions_framework
from google.cloud import pubsub_v1

publisher = pubsub_v1.PublisherClient()


@functions_framework.cloud_event
def start_scraping(cloud_event):
    topic_path = "projects/scraping-3f03b/topics/doScraping"
    product_list = ["Camisa Corinthians", "Boné Vai Corinthians", "Chaveiro Timao"]
    for product_name in product_list:
        try:
            future = publisher.publish(topic_path, product_name.encode("utf-8"))
            print(future.result())
            print(f"Published {product_name} to {topic_path}.")
        except Exception as e:
            print(e)
