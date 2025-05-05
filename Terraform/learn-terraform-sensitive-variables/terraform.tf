# Copyright (c) HashiCorp, Inc.
# SPDX-License-Identifier: MPL-2.0

terraform {
#Uncomment this block to use Terraform Cloud for this tutorial
cloud {
    organization = "hashicorps-codecamp"
    workspaces {
      name = "learn-terraform-sensitive-variables"
    }
}

required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.55.0"
    }
  }
  required_version = "~> 1.5.7"
}