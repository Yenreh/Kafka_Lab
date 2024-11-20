#!/bin/bash
docker exec -it kafka-broker-1 kafka-topics --bootstrap-server kafka-broker-1:9092 --list
