output "instance_ip_addr" {
  value = "${aws_instance.appserver.private_ip}"
}

output "applicationelb" {
  value = "${aws_lb.appserver.dns_name}"
}
