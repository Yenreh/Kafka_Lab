#!/bin/bash
kubectl exec -it kafka-broker-1 -- bash -c "kafka-topics --bootstrap-server kafka-broker-1:9092 --list"