# Kubernetes Operator with kopf

A Kubernetes operator built using the [kopf](https://kopf.readthedocs.io/) framework. This operator manages custom resources in your Kubernetes cluster.

## Overview

This operator demonstrates how to build a Kubernetes operator using kopf, a Python framework for creating Kubernetes operators. The operator watches for `MyResource` custom resources and handles their lifecycle (create, update, delete).

## Features

- Custom Resource Definition (CRD) for `MyResource`
- Handlers for create, update, and delete operations
- RBAC configuration for proper permissions
- Docker containerization
- Example custom resource

## Prerequisites

- Python 3.8 or higher
- Docker (for containerization)
- Kubernetes cluster (for deployment)
- kubectl configured to access your cluster

## Project Structure

```
.
├── operator.py                    # Main operator code
├── requirements.txt               # Python dependencies
├── Dockerfile                     # Container image definition
├── manifests/
│   ├── crd.yaml                  # Custom Resource Definition
│   ├── rbac.yaml                 # RBAC resources (ServiceAccount, Role, RoleBinding)
│   ├── deployment.yaml           # Operator deployment
│   └── example-resource.yaml     # Example MyResource instance
└── README.md                     # This file
```

## Installation

### Local Development

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the operator locally (requires kubeconfig):
```bash
python operator.py
```

### Kubernetes Deployment

1. Apply the Custom Resource Definition:
```bash
kubectl apply -f manifests/crd.yaml
```

2. Apply RBAC resources:
```bash
kubectl apply -f manifests/rbac.yaml
```

3. Build and push the Docker image:
```bash
docker build -t my-operator:v1.0.0 .
# If pushing to a registry:
# docker tag my-operator:v1.0.0 <your-registry>/my-operator:v1.0.0
# docker push <your-registry>/my-operator:v1.0.0
```

4. Deploy the operator:
```bash
kubectl apply -f manifests/deployment.yaml
```

## Usage

### Creating a Custom Resource

Apply the example resource:
```bash
kubectl apply -f manifests/example-resource.yaml
```

Or create your own:
```yaml
apiVersion: example.com/v1
kind: MyResource
metadata:
  name: my-example
  namespace: default
spec:
  replicas: 3
  image: "nginx:latest"
  message: "Hello from MyResource"
```

### Viewing Resources

List all MyResource instances:
```bash
kubectl get myresources
# Or use the short name:
kubectl get mr
```

Get details of a specific resource:
```bash
kubectl describe myresource example-myresource
```

### Updating a Resource

Edit the resource:
```bash
kubectl edit myresource example-myresource
```

Or apply an updated YAML file:
```bash
kubectl apply -f manifests/example-resource.yaml
```

### Deleting a Resource

```bash
kubectl delete myresource example-myresource
```

## Monitoring

View operator logs:
```bash
kubectl logs -f deployment/my-operator
```

View events:
```bash
kubectl get events --sort-by='.lastTimestamp'
```

## Customization

To customize the operator for your use case:

1. Modify the CRD in `manifests/crd.yaml` to define your resource schema
2. Update the handlers in `operator.py` to implement your business logic
3. Add additional handlers as needed (e.g., field-specific handlers, timers)
4. Update RBAC permissions if you need to access additional Kubernetes resources

## Development

### Testing Locally

1. Ensure you have a Kubernetes cluster running (minikube, kind, or similar)
2. Apply the CRD:
```bash
kubectl apply -f manifests/crd.yaml
```
3. Run the operator locally:
```bash
python operator.py
```
4. In another terminal, create a test resource:
```bash
kubectl apply -f manifests/example-resource.yaml
```

### Debugging

Enable verbose logging by setting the log level in `operator.py`:
```python
logging.basicConfig(level=logging.DEBUG)
```

## References

- [kopf Documentation](https://kopf.readthedocs.io/)
- [Kubernetes Operators](https://kubernetes.io/docs/concepts/extend-kubernetes/operator/)
- [Custom Resource Definitions](https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definitions/)

## License

This project is provided as-is for educational and development purposes.