resource "aws_lb_target_group" "appservergrp" {
  name     = "appservertg"
  port     = 80
  protocol = "HTTP"
  vpc_id   = "${var.vpc_id}"
  tags = {
    Name = "${var.taginfo}"
  }
}

resource "aws_lb_listener" "appserverlist" {
  depends_on        = ["aws_lb.appserver"]
  load_balancer_arn = "${aws_lb.appserver.arn}"
  port              = "80"
  protocol          = "HTTP"

  default_action {
    type             = "forward"
    target_group_arn = "${aws_lb_target_group.appservergrp.arn}"
  }
}

resource "aws_lb_target_group_attachment" "appserverattachment" {
  depends_on	   = ["aws_lb_listener.appserverlist"]
  target_group_arn = "${aws_lb_target_group.appservergrp.arn}"
  target_id        = "${aws_instance.appserver.id}"
  port             = 7000
}

