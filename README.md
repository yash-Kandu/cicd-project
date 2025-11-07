# CI/CD for 5 Microservices (Mono-Repo, Independent Pipelines)

This repo demonstrates a path-filtered mono-repo where **each microservice is built, tested, and deployed independently** via GitHub Actions and container images (GHCR).

## Microservices
- svc-users svc-orders svc-inventory svc-payments svc-notifications

## Repo Structure
```
cicd-project/
  /svc-users//svc-orders//svc-inventory//svc-payments//svc-notifications/.github/workflows/
  deploy/ecs/
  deploy/k8s/
```
(Each service has `app.py`, `requirements.txt`, `test_ok.py`, `Dockerfile`.)

## CI/CD Flow
1. Developer commits under `svc-*/` folder.
2. Path-filtered GitHub Action for that service runs:
   - Install deps, run tests
   - Build & push Docker image to GHCR
   - (Optional) Trigger ECS rolling update
3. Kubernetes/ECS pulls new image and rolls out without downtime.

## Diagram
See `docs/architecture.png` (also included below as ASCII).

```
Developer ─► GitHub Repo
              └─► GitHub Actions (per service: path filters)
                    ├─ Test (pytest)
                    ├─ Build (Docker)
                    ├─ Push (GHCR)
                    └─ Deploy (ECS/K8s - rolling)
                                   │
                        ┌──────────┴──────────┐
                        │                     │
                    AWS ECS               Kubernetes
                (1 service/task)      (Deployment/Service)
```

## Why Mono-repo is NOT Monolithic
- Each service has **its own workflow** triggered only by changes in its folder.
- Each service builds **its own image** and is deployed **independently**.
- Integration tests can be added as a separate workflow on PRs to `main`.

## Running Locally
```
cd svc-users
pip install -r requirements.txt
uvicorn app:app --reload
```

## K8s Manifests
Edit images under `deploy/k8s/*.yaml`: replace `ORG` and `TAG` with your ghcr org and commit SHA.

## ECS
Create an ECS service per microservice. CI step `aws ecs update-service --force-new-deployment` will roll it.

## Secrets Needed (CI)
- For GHCR push: `GITHUB_TOKEN` (provided automatically)
- For ECS (optional): `AWS_REGION`, `ECS_CLUSTER`, and AWS credentials or OIDC

## Notes
- Add cross-service integration tests later in a separate workflow.
- Use commit SHA tags for traceability; `latest` for convenience.
