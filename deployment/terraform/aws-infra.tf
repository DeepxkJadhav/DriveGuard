#############################
# DriveGuard AWS Infrastructure
#############################

terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
  required_version = ">= 1.3.0"
}

provider "aws" {
  region = var.region
}

#############################
# Variables
#############################

variable "region" {
  default = "ap-south-1"
}

variable "project_name" {
  default = "driveguard"
}

#############################
# S3 Bucket for Dataset & Models
#############################

resource "aws_s3_bucket" "data_bucket" {
  bucket = "${var.project_name}-data-bucket"
  acl    = "private"

  tags = {
    Name        = "DriveGuard Data Bucket"
    Environment = "Dev"
  }
}

#############################
# ECR Repository for Docker Images
#############################

resource "aws_ecr_repository" "driveguard_repo" {
  name = "${var.project_name}-repo"
  image_scanning_configuration {
    scan_on_push = true
  }

  tags = {
    Project = var.project_name
  }
}

#############################
# EC2 Instance (Backend)
#############################

resource "aws_instance" "backend_server" {
  ami           = "ami-0c94855ba95c71c99" # Amazon Linux 2
  instance_type = "t3.micro"
  key_name      = "driveguard-key"

  tags = {
    Name = "DriveGuard Backend"
  }

  user_data = <<-EOF
    #!/bin/bash
    yum update -y
    amazon-linux-extras install docker -y
    service docker start
    docker run -d -p 8000:8000 driveguard/backend:latest
  EOF
}

#############################
# Output
#############################

output "backend_public_ip" {
  value = aws_instance.backend_server.public_ip
  description = "Public IP of the DriveGuard Backend Server"
}

output "s3_bucket_name" {
  value = aws_s3_bucket.data_bucket.bucket
}
