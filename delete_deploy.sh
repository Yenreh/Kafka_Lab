#!/bin/bash
kubectl delete -f kubernetes/kafka-cluster.yml
kubectl delete -f kubernetes/producer-deployment.yml
kubectl delete -f kubernetes/consumer-deployment.yml
