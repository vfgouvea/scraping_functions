

Habilitar pub sub na gcp

DEPENDENCIAS
Toda dependencia deve estar no arquivo requirements.txt localizado na msm pasta do arquivo main.py

instalar todas dependencias -> py -m pip install -r requirements.txt
instalar individual -> install --upgrade google-cloud-pubsub 

criar topico -> gcloud pubsub topics create my-topic

criar subscription -> gcloud pubsub subscriptions create my-sub --topic my-topic

deletar:
gcloud pubsub subscriptions delete my-sub
gcloud pubsub topics delete my-topic
