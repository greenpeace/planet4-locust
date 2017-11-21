# Deploy a swarm of locusts on P4 servers!

![](https://media.giphy.com/media/dcubXtnbck0RG/giphy.gif)


```
gcloud config set project planet-4-151612
gcloud config set compute zone us-central1-b
gcloud container clusters create p4-locust-load-tester
gcloud container clusters get-credentials p4-locust-load-tester
kubectl apply -f k8s/locust-master-deployment.yaml
kubectl apply -f k8s/locust-service.yaml
kubectl apply -f k8s/locust-slave-deployment.yaml
```

---

Original idea by []
[hakobera/docker-locust](https://github.com/hakobera/docker-locust)
