.PHONY: help install run build push deploy clean test

help:
	@echo "Available targets:"
	@echo "  install     - Install Python dependencies"
	@echo "  run         - Run the operator locally"
	@echo "  build       - Build the Docker image"
	@echo "  push        - Push the Docker image to registry"
	@echo "  deploy      - Deploy the operator to Kubernetes"
	@echo "  clean       - Clean up resources"
	@echo "  test        - Run tests"

install:
	pip install -r requirements.txt

run:
	python operator.py

build:
	docker build -t my-operator:v1.0.0 .

push:
	@echo "Please tag and push to your registry:"
	@echo "  docker tag my-operator:v1.0.0 <your-registry>/my-operator:v1.0.0"
	@echo "  docker push <your-registry>/my-operator:v1.0.0"

deploy:
	kubectl apply -f manifests/crd.yaml
	kubectl apply -f manifests/rbac.yaml
	kubectl apply -f manifests/deployment.yaml

clean:
	kubectl delete -f manifests/deployment.yaml --ignore-not-found
	kubectl delete -f manifests/rbac.yaml --ignore-not-found
	kubectl delete -f manifests/crd.yaml --ignore-not-found
	rm -rf __pycache__

test:
	python -m pytest -v
