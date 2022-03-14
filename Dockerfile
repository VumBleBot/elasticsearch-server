FROM docker.elastic.co/elasticsearch/elasticsearch:7.9.1

RUN apt-get install python3 && python3-pip

COPY . server/

RUN pip install -r requirements.txt

RUN sh bulk_create_lyrics_data.sh
EXPOSE 9200 9300
