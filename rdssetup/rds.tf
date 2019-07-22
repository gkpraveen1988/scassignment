# To fetching the VPC details
data "aws_vpc" "environment_api" {
  id = "${var.vpc_id}"
}

variable "dbsubnetname" {
  default = "dbsubnet"
}

resource "aws_security_group" "rds_sg" {
  name        = "rds_sg"
  description = "SG for RDS"
  vpc_id      = "${data.aws_vpc.environment_api.id}"

  ingress {
    # TLS (change to whatever ports you need)
    from_port   = 3306
    to_port     = 3306
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

resource "aws_db_instance" "appdb" {
  depends_on    = ["aws_security_group.rds_sg"]
  allocated_storage    = 10
  storage_type         = "gp2"
  engine               = "mysql"
  engine_version       = "5.7"
  instance_class       = "db.t2.micro"
  db_subnet_group_name = "${var.dbsubnetname}"
  name                 = "appserverrds"
  username             = "appadminuser"
  password             = ""
  identifier           = "appserverrds"
  vpc_security_group_ids = ["${aws_security_group.rds_sg.id}"]
  tags = {
    Name = "${var.taginfo}"
  }
}

output "rds_instance_endpoint" {
  value = "${aws_db_instance.appdb.endpoint}"
}

