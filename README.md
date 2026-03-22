# Family Expense Tracker

A full-stack family expense tracking application with AWS infrastructure.

## Project Structure

```
family-expense-tracker/
├── backend/          # Lambda functions (Python)
├── frontend/         # React application
├── infra/            # AWS CDK infrastructure (Python)
└── .github/          # GitHub Actions workflows
```

## Tech Stack

- **Frontend**: React
- **Backend**: Python Lambda functions
- **Infrastructure**: AWS CDK (Python)
- **CI/CD**: GitHub Actions

## Prerequisites

- Node.js 20
- Python 3.12
- [mise](https://mise.jdx.dev/) for version management
- AWS account

## Setup

### 1. Install dependencies

```bash
# Install mise tools
mise install

# Setup infrastructure
cd infra
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 2. Configure AWS credentials

```bash
aws configure
```

### 3. Bootstrap CDK (first time only)

```bash
cdk bootstrap
```

### 4. Deploy infrastructure

```bash
cdk deploy
```

## GitHub Actions

The project uses GitHub Actions for CI/CD. On push to `main`, the workflow will:
1. Install dependencies
2. Run CDK synth
3. Deploy to AWS

### Required Secrets

Add these in GitHub repo Settings → Secrets → Actions:
- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`
- `AWS_REGION` (e.g., us-east-1)
