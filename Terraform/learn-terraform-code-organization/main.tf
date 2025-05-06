# Copyright (c) HashiCorp, Inc.
# SPDX-License-Identifier: MPL-2.0

provider "aws" {
  region = var.region
}

resource "random_pet" "petname" {
  length    = 4
  separator = "-"
}

resource "aws_s3_bucket" "bucket" {
  bucket        = "${var.prefix}-${random_pet.petname.id}"
  force_destroy = true
}

resource "aws_s3_bucket_website_configuration" "bucket" {
  bucket = aws_s3_bucket.bucket.id
  index_document { suffix = "index.html" }
  error_document { key = "error.html" }
}

resource "aws_s3_bucket_ownership_controls" "bucket" {
  # Must be created BEFORE public access block
  bucket = aws_s3_bucket.bucket.id
  rule { object_ownership = "BucketOwnerEnforced" }
}

resource "aws_s3_bucket_public_access_block" "bucket" {
  depends_on = [aws_s3_bucket_ownership_controls.bucket]
  
  bucket = aws_s3_bucket.bucket.id
  block_public_acls       = false
  block_public_policy     = false
  ignore_public_acls      = false
  restrict_public_buckets = false
}

resource "aws_s3_bucket_policy" "bucket" {
  depends_on = [
    aws_s3_bucket_public_access_block.bucket
  ]
  
  bucket = aws_s3_bucket.bucket.id
  policy = jsonencode({
    Version = "2012-10-17",
    Statement = [{
      Sid       = "PublicReadGetObject",
      Effect    = "Allow",
      Principal = "*",
      Action    = "s3:GetObject",
      Resource  = "arn:aws:s3:::${aws_s3_bucket.bucket.id}/*"
    }]
  })
}

resource "aws_s3_object" "webapp" {
  depends_on = [aws_s3_bucket_policy.bucket]
  
  bucket       = aws_s3_bucket.bucket.id
  key          = "index.html"
  content      = file("${path.module}/assets/index.html")
  content_type = "text/html"
  
  metadata = {
    cache-control = "max-age=3600"
  }
}