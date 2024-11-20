#!/bin/bash
docker build -t yenreh/kafka-producer ./producer
docker build -t yenreh/kafka-consumer ./consumer
sleep 5
docker push yenreh/kafka-producer
docker push yenreh/kafka-consumer
