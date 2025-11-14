terraform {
  required_providers {
    hyperfabric = {
      source = "CiscoDevNet/hyperfabric"
    }
    utils = {
      source  = "netascode/utils"
      version = ">= 0.2.5"
    }
    local = {
      source  = "hashicorp/local"
      version = ">= 2.3.0"
    }
  }
}

variable "hyperfabric_token" {
}

provider "hyperfabric" {
  token = var.hyperfabric_token
}

module "hyperfabric" {
  source  = "github.com/netascode/terraform-hyperfabric-nac-hyperfabric.git"

  yaml_directories = ["data"]
}