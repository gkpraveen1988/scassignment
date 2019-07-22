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
  default = "ami-035b3c7efe6d061d5"
}

variable "ec2_subnet_ids" {
  default = "subnet-49ba4463"
}

variable "elb_subnet_ids" {
  default = ["subnet-23b61e55","subnet-4cba4466"]
}
