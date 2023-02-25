# GKE cluster
resource "google_container_cluster" "primary" {
  name               = "${var.project_name}-gke"
  location           = var.zone
  min_master_version = "1.22"

  remove_default_node_pool = true
  initial_node_count       = 1

  network    = google_compute_network.vpc.name
  subnetwork = google_compute_subnetwork.subnet.name
}

# Separately Managed Node Pool
resource "google_container_node_pool" "primary_nodes" {
  name       = google_container_cluster.primary.name
  version    = "1.22"
  location   = var.zone
  cluster    = google_container_cluster.primary.name
  node_count = var.gke_num_nodes

  node_config {
    labels = var.common_labels

    spot         = true
    machine_type = "e2-standard-2"
  }
}
