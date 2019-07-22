provider "aws" {
  region = "us-east-1"
}

variable "vpc_id" {
  default = "vpc-92cfb5f6"
}

variable "taginfo" {
  default = "AppServer"
}

variable "keynm" {
  default = "Devops_testing_us_east"
}

variable "amiinfo" {
  default = "ami-0a313d6098716f372"
}

variable "ec2_subnet_ids" {
  default = "subnet-49ba4463"
}


