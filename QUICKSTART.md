# Quick Start Guide

This guide will help you get the operator up and running quickly.

## Prerequisites

- Python 3.8+
- Docker
- Kubernetes cluster (minikube, kind, k3s, or cloud provider)
- kubectl configured

## Local Development (No Kubernetes Required)

1. Install dependencies:
```bash
make install
# or
pip install -r requirements.txt
```

2. The operator code is ready in `operator.py` with handlers for:
   - Creating resources
   - Updating resources
   - Deleting resources
   - Startup/shutdown hooks

## Deploy to Kubernetes

### Step 1: Install the CRD
```bash
kubectl apply -f manifests/crd.yaml
```

Verify:
```bash
kubectl get crd myresources.example.com
```

### Step 2: Set up RBAC
```bash
kubectl apply -f manifests/rbac.yaml
```

### Step 3: Build and Deploy the Operator

Build the image:
```bash
make build
# or
docker build -t my-operator:v1.0.0 .
```

For local clusters (minikube/kind), load the image:
```bash
# For minikube:
minikube image load my-operator:v1.0.0

# For kind:
kind load docker-image my-operator:v1.0.0
```

For remote clusters, push to registry:
```bash
docker tag my-operator:v1.0.0 <your-registry>/my-operator:v1.0.0
docker push <your-registry>/my-operator:v1.0.0
# Update manifests/deployment.yaml with your registry path
```

Deploy:
```bash
kubectl apply -f manifests/deployment.yaml
```

### Step 4: Verify Operator is Running
```bash
kubectl get pods
kubectl logs -f deployment/my-operator
```

### Step 5: Create a Custom Resource
```bash
kubectl apply -f manifests/example-resource.yaml
```

Check the operator logs to see it handling the resource:
```bash
kubectl logs -f deployment/my-operator
```

View your resource:
```bash
kubectl get myresources
kubectl describe myresource example-myresource
```

## Testing Changes

1. Modify the custom resource:
```bash
kubectl edit myresource example-myresource
```

2. Watch the operator logs to see the update handler:
```bash
kubectl logs -f deployment/my-operator
```

3. Delete the resource:
```bash
kubectl delete myresource example-myresource
```

## Cleanup

Remove everything:
```bash
make clean
# or
kubectl delete -f manifests/deployment.yaml
kubectl delete -f manifests/rbac.yaml
kubectl delete -f manifests/crd.yaml
```

## Next Steps

1. Customize the CRD schema in `manifests/crd.yaml`
2. Implement your business logic in `operator.py`
3. Add more handlers for specific fields or events
4. Set up CI/CD for automatic builds and deployments

## Troubleshooting

**Operator pod not starting:**
- Check logs: `kubectl logs deployment/my-operator`
- Verify RBAC: `kubectl get serviceaccount my-operator`
- Check image is available: `kubectl describe pod <pod-name>`

**Handlers not triggering:**
- Verify CRD is installed: `kubectl get crd`
- Check operator logs for errors
- Ensure resource namespace matches operator permissions

**Permission errors:**
- Review RBAC configuration in `manifests/rbac.yaml`
- Check service account is bound correctly
