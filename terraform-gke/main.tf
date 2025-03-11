provider "google" {
  project = "finel-project-web"  # ודאי שהשם נכון
  region  = "us-central1"        # ניתן לשנות לאזור אחר
}

resource "google_container_cluster" "primary" {
  name     = "gke-cluster"
  location = "us-central1"

  remove_default_node_pool = true
  initial_node_count       = 1

  network    = "default"
}

resource "google_container_node_pool" "primary_nodes" {
  name       = "node-pool"
  location   = google_container_cluster.primary.location
  cluster    = google_container_cluster.primary.name
  node_count = 2

  node_config {
    preemptible  = true
    machine_type = "e2-medium"
    disk_size_gb = 50  # עדכון ל-50GB לכל Node כדי להתאים ל-Quota
    oauth_scopes = [
      "https://www.googleapis.com/auth/cloud-platform"
    ]
  }
}
