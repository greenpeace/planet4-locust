# Deploy a swarm of locusts on P4 servers!

![](https://media.giphy.com/media/dcubXtnbck0RG/giphy.gif)

[Locust](https://locust.io) - An open source load testing tool

```
# Setup environment
gcloud config set project planet-4-151612
gcloud config set compute zone us-central1-b

# Create cluster
gcloud container clusters create p4-locust-load-tester

# Get credentials (happens automatically?)
gcloud container clusters get-credentials p4-locust-load-tester

# Create the Locust master
kubectl apply -f k8s/locust-master-deployment.yaml
kubectl rollout status deployment locust

# Create the load balancer, pointing to the master
kubectl apply -f k8s/locust-service.yaml

# Create the Locust slave deployment
kubectl apply -f k8s/locust-slave-deployment.yaml
kubectl rollout status deployment locust-slave

# Open your browser (OSX only?)
open http:/$(kubectl get svc locust -o jsonpath="{.status.loadBalancer.ingress[*].ip}"):8089

# Attack!
```


---

Idea borrowed from [hakobera/docker-locust](https://github.com/hakobera/docker-locust)
