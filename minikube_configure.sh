#!/bin/bash

minikube start

eval $(minikube docker-env)

docker build -t product:v1 services/product

kubectl create -f services/product/product.yaml
kubectl create -f services/ingress/ingress.yaml
