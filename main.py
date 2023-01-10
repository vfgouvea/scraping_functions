import functions_framework
from Pubsub import Publisher, Subscriber
import Firestore


@functions_framework.cloud_event
def start_scraping(cloud_event):
    topic_path = "projects/scraping-3f03b/topics/doScraping"
    product_list = ["Camisa Corinthians", "Boné Vai Corinthians", "Chaveiro Timao"]
    for product_name in product_list:
        Publisher.publicar(topic_path, product_name)


@functions_framework.cloud_event
def do_scraping(cloud_event):
    subcription_name = "projects/scraping-3f03b/subscriptions/doScraping-sub"
    Subscriber.lerNomeProduto(subcription_name, Firestore.write)
