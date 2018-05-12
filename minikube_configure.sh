#!/bin/bash

minikube start

eval $(minikube docker-env)

docker build -t product:v1 services/product
docker build -t price:v1 services/price

kubectl create -f services/product/product.yaml
kubectl create -f services/price/price.yaml
kubectl create -f services/ingress/ingress.yaml
