output "instance_ip_addr" {
  value = "${aws_instance.appserver.private_ip}"
}
