# ECS Deployment Notes

- Create an ECS Cluster (Fargate) and one Service per microservice with a Task Definition that references the image:
  `ghcr.io/<ORG>/{svc}:<TAG>`
- The GitHub Actions workflow can call `aws ecs update-service --force-new-deployment`
  to roll tasks to the new image tag.

Required GitHub Secrets (if you want ECS deployment from CI):
- AWS_REGION
- ECS_CLUSTER
- (Optional) AWS_ACCESS_KEY_ID / AWS_SECRET_ACCESS_KEY if not using OIDC
