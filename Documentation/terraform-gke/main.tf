variable "GCP_SA_KEY_FILE" {
  description = "Path to Google Cloud Service Account JSON key file"
  type        = string
}

provider "google" {
  credentials = file(var.GCP_SA_KEY_FILE)
  project     = "finel_project-web"
  region      = "us-central1"
}

data "google_client_config" "default" {}

data "google_container_cluster" "primary" {
  name     = "flask-cluster"
  location = "us-central1-a"
}

provider "kubernetes" {
  host                   = "https://${data.google_container_cluster.primary.endpoint}"
  cluster_ca_certificate = base64decode(data.google_container_cluster.primary.master_auth.0.cluster_ca_certificate)
  token                  = data.google_client_config.default.access_token
}

output "cluster_endpoint" {
  value = data.google_container_cluster.primary.endpoint
}

output "cluster_ca_certificate" {
  value     = data.google_container_cluster.primary.master_auth.0.cluster_ca_certificate
  sensitive = true
}

output "access_token" {
  value     = data.google_client_config.default.access_token
  sensitive = true
}
