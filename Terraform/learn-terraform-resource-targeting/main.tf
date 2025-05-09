# Copyright (c) HashiCorp, Inc.
# SPDX-License-Identifier: MPL-2.0

provider "aws" {
  region = var.aws_region

  default_tags {
    tags = {
      hashicorp-learn = "resource-targeting"
    }
  }
}

resource "random_pet" "bucket_name" {
  #lenght    = 5
  length    = 5
  separator = "-"
  prefix    = "learning"
}

module "s3_bucket" {
  source  = "terraform-aws-modules/s3-bucket/aws"
  version = "4.1.1"

  bucket = random_pet.bucket_name.id
  acl    = "private"

  control_object_ownership = true
  object_ownership         = "BucketOwnerPreferred"

  block_public_acls       = false
  block_public_policy     = false
  ignore_public_acls      = false
  restrict_public_buckets = false
}

resource "random_pet" "object_names" {
  count = 4

  length    = 5
  separator = "_"
  #prefix    = "learning"
}

resource "aws_s3_object" "objects" {
  count = 4

  #acl          = "public-read" This is happening because AWS has recently changed its S3 bucket policies to disable ACLs by default (since April 2023). Your code is trying to create objects with acl = "public-read", but the bucket is configured to not allow ACLs.
  key          = "${random_pet.object_names[count.index].id}.txt"
  bucket       = module.s3_bucket.s3_bucket_id
  #content      = "Example object #${count.index}"
  content      = "Bucket object #${count.index}" 
  content_type = "text/plain"
}
