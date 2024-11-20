#!/bin/bash
docker exec -it kafka-broker-1 kafka-console-producer --bootstrap-server kafka-broker-1:9092 --topic univalle-ideas
