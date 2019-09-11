#! /bin/bash
eksctl create cluster \
--name bootcamp-webinar \
--version 1.14 \
--nodes-min 2 \
--nodes-max 3 \
--nodes 2 \
--auto-kubeconfig \
--full-ecr-access \
--region=us-east-1 --zones=us-east-1a,us-east-1b,us-east-1c,us-east-1d \

export KUBECONFIG=~/.kube/eksctl/clusters/bootcamp-webinar