def admintoken = "1147655d74720ae967e1be190d4d31990f"

node('master'){
    stage('Checking out code') {
        checkout scm
    }
    
    stage('Creating Ec2 Instance') {
        sh """
        cd ${env.WORKSPACE}/terradetails
        ls -ltr
        terraform init
        terraform plan
        terraform apply --auto-approve
        terraform output instance_ip_addr
        """
    }
}
