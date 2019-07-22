resource "aws_security_group" "elb_sg" {
  name        = "elb_sg"
  description = "SG for AppServer"
  vpc_id      = "${data.aws_vpc.environment_api.id}"

  ingress {
    # TLS (change to whatever ports you need)
    from_port   = 80
    to_port     = 80
    protocol    = "TCP"
    cidr_blocks = ["0.0.0.0/0"]
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


