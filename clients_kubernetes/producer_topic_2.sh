#!/bin/bash
kubectl exec -it kafka-broker-1 -- bash -c "kafka-console-producer --bootstrap-server kafka-broker-1:9092 --topic cosas-misteriosas"
