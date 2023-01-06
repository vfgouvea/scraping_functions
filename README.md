
gcloud projects list -> checar projetos tenho

Instalar python

criar diretorio do projeto

criar arquivo main.py no diretorio -> cloud functions por default ja procura por functions deployaveis no arquivo main.py

criar documento de dependecias requirements.txt no mesmo diretorio do main.py -> para baixar as dependencias : py -m pip install -r requirements.txt

setar o projeto para deployar a funçao -> gcloud config set project scraping-3f03b


Para http trigger:

deployar a funçao com http request como trigger -> gcloud functions deploy startscraping --gen2 --runtime=python310 --source=. --entry-point=start_scraping --trigger-http --allow-unauthenticated



Para Pub/Sub trigger:

criar Pub/Sub topic -> gcloud pubsub topics create startScrapingProcess

deployar a funçao com evento como trigger -> gcloud functions deploy start-scraping --gen2 --runtime=python310 --source=. --entry-point=start_scraping --trigger-topic=startScrapingProcess --allow-unauthenticated 
                                             gcloud functions deploy do-scraping --gen2 --runtime=python310 --source=. --entry-point=do_scraping --trigger-topic=doScraping --allow-unauthenticated

criar o scheduler -> processo feito manualmente no Cloud Scheduler, simples e apenas seleciona e quer http ou pub/sub e selecionar o endereço ou topico

Teste: publicar uma menssagem no topico -> gcloud pubsub topics publish startScrapingProcess --message="Friend"

ver o log da funçao -> gcloud beta functions logs read start-scraping --gen2



criar topico -> gcloud pubsub topics create my-topic

criar subscription -> gcloud pubsub subscriptions create my-sub --topic my-topic

deletar ->
gcloud pubsub subscriptions delete my-sub
gcloud pubsub topics delete my-topic




CRIAR PROJETO

Criar projeto python para deployar na cloud function gcp:


Criar arquivo main.py ( contem as funçoes ) na raiz de um projeto criado


Criar arquivo requirements.txt no mesmo diretorio do arquivo main.py -> TODAS DEPENDENCIAS DEVEM ESTAR NESSE ARQUIVO


instalar todas dependencias -> py -m pip install -r requirements.txt
instalar individual -> install --upgrade google-cloud-pubsub 


