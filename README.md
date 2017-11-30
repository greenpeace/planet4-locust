# Deploy a swarm of locusts on P4 servers!

![](https://media.giphy.com/media/dcubXtnbck0RG/giphy.gif)

[Locust](https://locust.io) - An open source load testing tool

Current test environments:

http://locust.docker.p4.greenpeace.org
http://locust.dev.p4.greenpeace.org
http://locust.sysadmin-b.p4.greenpeace.org

```
# Setup environment
gcloud config set project planet-4-151612
gcloud config set compute zone us-central1-b

# Create cluster
gcloud container clusters create p4-locust-load-tester

# Get kubectl credentials
gcloud container clusters get-credentials p4-locust-load-tester

# Install Helm (Download from https://helm.sh)
helm init

# Install Traefik from helm chart
helm install --name ingress-controller --namespace kube-system --set dashboard.enabled=true,dashboard.domain=traefik.locust.p4.greenpeace.org stable/traefik

# Create the Locust master deployment and service
kubectl apply -f k8s/locust.dev.p4.greenpeace.org/locust-master.yaml
kubectl rollout status deployment locust

# Create the Locust slave deployment and horizontal scaler
kubectl apply -f k8s/locust.dev.p4.greenpeace.org/locust-slave-deployment.yaml
kubectl rollout status deployment locust-slave

# Open your browser (OSX only?)
open http://locust.dev.p4.greenpeace.org

# Attack!
```

---

Idea borrowed from [hakobera/docker-locust](https://github.com/hakobera/docker-locust)
