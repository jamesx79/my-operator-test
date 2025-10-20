#!/usr/bin/env python3
"""
Kubernetes Operator built with kopf framework.
This operator manages custom resources in Kubernetes.
"""

import kopf
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@kopf.on.create('example.com', 'v1', 'myresources')
def create_fn(spec, name, namespace, logger, **kwargs):
    """
    Handler for when a MyResource custom resource is created.
    
    Args:
        spec: The spec section of the custom resource
        name: The name of the custom resource
        namespace: The namespace of the custom resource
        logger: Logger instance
        **kwargs: Additional keyword arguments from kopf
    """
    logger.info(f"Creating MyResource: {name} in namespace: {namespace}")
    logger.info(f"Spec: {spec}")
    
    # Add your resource creation logic here
    # For example, create a ConfigMap, Deployment, Service, etc.
    
    return {'message': f'MyResource {name} created successfully'}


@kopf.on.update('example.com', 'v1', 'myresources')
def update_fn(spec, name, namespace, logger, **kwargs):
    """
    Handler for when a MyResource custom resource is updated.
    
    Args:
        spec: The spec section of the custom resource
        name: The name of the custom resource
        namespace: The namespace of the custom resource
        logger: Logger instance
        **kwargs: Additional keyword arguments from kopf
    """
    logger.info(f"Updating MyResource: {name} in namespace: {namespace}")
    logger.info(f"New spec: {spec}")
    
    # Add your resource update logic here
    
    return {'message': f'MyResource {name} updated successfully'}


@kopf.on.delete('example.com', 'v1', 'myresources')
def delete_fn(spec, name, namespace, logger, **kwargs):
    """
    Handler for when a MyResource custom resource is deleted.
    
    Args:
        spec: The spec section of the custom resource
        name: The name of the custom resource
        namespace: The namespace of the custom resource
        logger: Logger instance
        **kwargs: Additional keyword arguments from kopf
    """
    logger.info(f"Deleting MyResource: {name} in namespace: {namespace}")
    
    # Add your resource cleanup logic here
    
    return {'message': f'MyResource {name} deleted successfully'}


@kopf.on.startup()
def startup_fn(logger, **kwargs):
    """
    Handler for operator startup.
    """
    logger.info("Operator is starting up")


@kopf.on.cleanup()
def cleanup_fn(logger, **kwargs):
    """
    Handler for operator cleanup.
    """
    logger.info("Operator is shutting down")


if __name__ == '__main__':
    # Run the operator
    kopf.run()
