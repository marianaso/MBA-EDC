variable "gke_num_nodes" {
  default     = 3
  description = "number of gke nodes"
}

variable "project_id" {
  description = "project id"
  default     = "<YOUR-PROJECT-ID>"
}

variable "project_name" {
  description = "project name"
  default     = "btc-edc-m3"
}

variable "region" {
  description = "region"
  default     = "us-central1"
}

variable "zone" {
  description = "zone"
  default     = "us-central1-a"
}


variable "common_labels" {
  description = "project common labels"
  default = {
    Environment  = "development"
    Project      = "btc_edc"
    Organization = "xp_educacao"
  }

}
