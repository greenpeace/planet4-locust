# Deploy a swarm of locusts on P4 servers!

![](https://media.giphy.com/media/dcubXtnbck0RG/giphy.gif)

[Locust](https://locust.io) - An open source load testing tool

```
# Setup environment
gcloud config set project planet-4-151612
gcloud config set compute zone us-central1-b

# Create cluster
gcloud container clusters create p4-locust-load-tester

# Get kubectl credentials
gcloud container clusters get-credentials p4-locust-load-tester

# Create the Locust master deployment and service
kubectl apply -f k8s/locust.dev.p4.greenpeace.org/locust-master.yaml
kubectl rollout status deployment locust

# Create the Locust slave deployment and horizontal scaler
kubectl apply -f k8s/locust.dev.p4.greenpeace.org/locust-slave-deployment.yaml
kubectl rollout status deployment locust-slave

# Open your browser (OSX only?)
open http://$(kubectl get svc locust -o jsonpath="{.status.loadBalancer.ingress[*].ip}"):8089

# Attack!
```

---

Idea borrowed from [hakobera/docker-locust](https://github.com/hakobera/docker-locust)
