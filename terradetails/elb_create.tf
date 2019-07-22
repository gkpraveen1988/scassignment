# Create a new load balancer
resource "aws_lb" "appserver" {
  depends_on	      = ["aws_security_group.elb_sg"]
  name                = "appserverelb"
  subnets             = "${var.elb_subnet_ids}"
  load_balancer_type  = "application"
  security_groups     = ["${aws_security_group.elb_sg.id}"]
  tags = {
    Name = "${var.taginfo}"
  }
}
