
# To fetching the VPC details
data "aws_vpc" "environment_api" {
  id = "${var.vpc_id}"
}

# To Spin up an Ec2 instance
resource "aws_instance" "appserver" {
  depends_on    = ["aws_security_group.allow_tls"]
  ami           = "${var.amiinfo}"
  instance_type = "t2.micro"
  availability_zone = "us-east-1a"
  subnet_id     = "${var.ec2_subnet_ids}"
  key_name      = "${var.keynm}"
  vpc_security_group_ids = [
    "${aws_security_group.allow_tls.id}"
  ]
  tags = {
    Name = "${var.taginfo}"
  }
}

# Creating Security group
resource "aws_security_group" "allow_tls" {
  name        = "appserver_sg"
  description = "SG for AppServer"
  vpc_id      = "${data.aws_vpc.environment_api.id}"

  ingress {
    # TLS (change to whatever ports you need)
    from_port   = 22
    to_port     = 22
    protocol    = "TCP"
    cidr_blocks = ["10.0.0.0/8"]
  }

  ingress {
    # TLS (change to whatever ports you need)
    from_port   = 5000
    to_port     = 5000
    protocol    = "TCP"
    cidr_blocks = ["10.0.0.0/8"]
  }

 ingress {
    # TLS (change to whatever ports you need)
    from_port   = 8000
    to_port     = 8000
    protocol    = "TCP"
    cidr_blocks = ["10.0.0.0/8"]
  }
 
 ingress {
    # TLS (change to whatever ports you need)
    from_port   = 7000
    to_port     = 7000
    protocol    = "TCP"
    cidr_blocks = ["10.0.0.0/8"]
  }

  egress {
    from_port       = 0
    to_port         = 0
    protocol        = "-1"
    cidr_blocks     = ["0.0.0.0/0"]
  }
   
  tags = {
    Name = "${var.taginfo}"
  }
}
