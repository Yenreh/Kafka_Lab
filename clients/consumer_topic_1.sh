#!/bin/bash
docker exec -it kafka-broker-1 kafka-console-consumer --bootstrap-server kafka-broker-1:9092 --topic univalle-ideas --from-beginning
