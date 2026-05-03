module "vpc" {
  source  = "terraform-aws-modules/vpc/aws"
  version = "5.0.0"

  name = "haifa-devops-vpc"
  cidr = "10.0.0.0/16"

  # We use two Availability Zones for High Availability (HA)
  azs             = ["us-west-2a", "us-west-2b"]
  private_subnets = ["10.0.1.0/24", "10.0.2.0/24"]
  public_subnets  = ["10.0.101.0/24", "10.0.102.0/24"]

  # Enable NAT Gateway so private nodes can pull Docker images from the internet
  enable_nat_gateway = true
  single_nat_gateway = true # Saves money for a dev environment

  enable_dns_hostnames = true
  enable_dns_support   = true

  tags = {
    "kubernetes.io/cluster/haifa-eks-cluster" = "shared"
    Environment = "dev"
    Project     = "Hybrid-GitOps"
  }
}
