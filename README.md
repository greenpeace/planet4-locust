# Deploy a swarm of locusts on your servers!

![](https://media.giphy.com/media/dcubXtnbck0RG/giphy.gif)

[Locust](https://locust.io) - An open source load testing tool

## Master / Slave configuration on Kubernetes:

Requirements for the full GKE install:

Google Cloud SDK: https://cloud.google.com/sdk/downloads

Helm: https://docs.helm.sh/using_helm/

Examples for the Greenpeace Planet4 Project:
```
# Setup environment
gcloud config set project planet-4-151612
gcloud config set compute zone europe-west4

# Create cluster (or skip these steps if re-using an existing cluster)
gcloud container clusters create locust-load-tester

# Get kubectl credentials
gcloud container clusters get-credentials locust-load-tester

# Install Helm (Download from https://helm.sh)
helm init

# Install Traefik ingress controller from helm chart
helm install --name ingress-controller --namespace kube-system stable/traefik

# Create the Locust master deployment and service
kubectl apply -f k8s/locust.dev.p4.greenpeace.org/locust-master.yaml

# Create the Locust slave deployment and horizontal autoscaler
kubectl apply -f k8s/locust.dev.p4.greenpeace.org/locust-slave.yaml

# Check to see the deployment completes successfully
kubectl rollout status deployment locust-slave

# Open your browser to the web interface
open http://locust.dev.p4.greenpeace.org

# Attack!
```

## Standalone command-line load testing:

```
docker run -e TARGET_URL="https://example.com" -e LOCUST_OPTIONS="-c 1000 -r 100" gcr.io/planet-4-151612/locust:0.0.2
```

Where `-c` specifies number of clients, and `-r` specifies the hatch rate (number of users to spawn per second). See https://docs.locust.io/en/latest/running-locust-without-web-ui.html for options.

---

Idea borrowed from [hakobera/docker-locust](https://github.com/hakobera/docker-locust)
