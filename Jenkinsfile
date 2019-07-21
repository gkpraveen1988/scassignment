def admintoken = "1147655d74720ae967e1be190d4d31990f"

node('master'){
    stage('Checking out code') {
        checkout scm
    }
    
    stage('Constructing Ansible inventory_file') {
        sh """
            mkdir ${env.WORKSPACE}/ansible_deploy; cd ${env.WORKSPACE}/ansible_deploy
            cp /instance1.pem ${env.WORKSPACE}/ansible_deploy
            ipaddress = terraform output instance_ip_addr
            echo '[application]' > hosts
            echo ${ipaddress} ansible_connection=ssh ansible_user=ec2-user" >> hosts
            echo '[local_instance:vars]' >> hosts
            echo 'ansible_ssh_private_key_file=instance1.pem' >> hosts
            echo "Ansible host file constructed" 
            cat /ansible_deploy/hosts            
        """
    }
}
