provider "google" {
  project = "finel-project-web"
  region  = "us-central1"
}

resource "google_container_cluster" "primary" {
  name     = "gke-cluster"
  location = "us-central1"

  remove_default_node_pool = true
  initial_node_count       = 1

  release_channel {
    channel = "REGULAR"
  }
}

resource "google_container_node_pool" "primary_nodes" {
  name       = "node-pool"
  location   = "us-central1"
  cluster    = google_container_cluster.primary.name
  node_count = 2

  node_config {
    machine_type = "e2-medium"
    disk_size_gb = 50  # 👈 שיניתי ל-50GB במקום ברירת המחדל של 100GB
    oauth_scopes = [
      "https://www.googleapis.com/auth/cloud-platform"
    ]
  }
}

output "kubeconfig" {
  value = <<EOT
gcloud container clusters get-credentials gke-cluster --region us-central1 --project finel-project-web
EOT
}
