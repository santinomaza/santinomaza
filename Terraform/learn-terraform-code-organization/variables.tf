# Copyright (c) HashiCorp, Inc.
# SPDX-License-Identifier: MPL-2.0

variable "region" {
  description = "AWS region"
  type        = string
}

#variable "dev_prefix" {
variable "prefix" {
  description = "This is the environment where your webapp is deployed. qa, prod, or dev"
  type        = string
}

#variable "prod_prefix" {
#  description = "This is the environment where your webapp is deployed. qa, prod, or dev"
#}
