variable "region" {
  description = "AWS region"
  type        = string
  default     = "us-east-1"
}

variable "project_name" {
  description = "project name"
  type        = string
  default     = "btc-edc-m3"
}

locals {
  cluster_name = "${var.project_name}-eks"
}
