# Copyright (c) HashiCorp, Inc.
# SPDX-License-Identifier: MPL-2.0

terraform {
  required_version = ">= 1.5.7"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "5.7.0"
    }
    random = {
      source  = "hashicorp/random"
      version = "3.5.1"
    }
    time = {
      source  = "hashicorp/time"
      version = "0.9.1"
    }
  }
  #Uncomment this block to use Terraform Cloud for this tutorial
  cloud {
    organization = "hashicorps-codecamp"
    workspaces {
      name = "learn-terraform-apply"
    }
  }
}
