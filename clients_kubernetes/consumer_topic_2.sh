#!/bin/bash
kubectl exec -it kafka-broker-1 -- bash -c "kafka-console-consumer --bootstrap-server kafka-broker-1:9092 --topic cosas-misteriosas --from-beginning"
