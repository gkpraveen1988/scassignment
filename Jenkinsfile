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

    stage('Jenkins CLI to add the slave entry') {
        sh """
        cat <<EOF | java -jar jenkins-cli.jar -s http://10.40.73.106:8000 -auth admin:$admintoken create-node appserver
            <slave>
              <name>appserver</name>
              <description></description>
              <remoteFS>/home/jenkins/agent</remoteFS>
              <numExecutors>1</numExecutors>
              <mode>NORMAL</mode>
              <retentionStrategy class="hudson.slaves.RetentionStrategy\$Always"/>
              <launcher class="hudson.slaves.JNLPLauncher">
                <workDirSettings>
                  <disabled>false</disabled>
                  <internalDir>remoting</internalDir>
                  <failIfWorkDirIsMissing>false</failIfWorkDirIsMissing>
                </workDirSettings>
              </launcher>
              <label></label>
              <nodeProperties/>
              <userId>jenkins</userId>
            </slave>
            EOF
        """
    }
    
    stage('Constructing Ansible inventory_file') {
        def ipaddress = sh (returnStdout: true, script: """
	    cd ${env.WORKSPACE}/terradetails; terraform output instance_ip_addr
	""").trim()
        sh """
            cd ${env.WORKSPACE}/ansibleplay
            cp /instance1.pem ${env.WORKSPACE}/ansibleplay
            echo '[local_instance]' > hosts
            echo "${ipaddress} ansible_connection=ssh ansible_user=ec2-user" >> hosts
            echo '' >> hosts
            echo '[local_instance:vars]' >> hosts
            echo 'ansible_ssh_private_key_file=instance1.pem' >> hosts
	    ssh -oStrictHostKeyChecking=no -i instance1.pem ec2-user@${ipaddress} uptime
            echo "Ansible host file constructed" 
            cat ${env.WORKSPACE}/ansibleplay/hosts            
        """
    }
    
    stage('Applying ansible files') {
        sh """
            cd ${env.WORKSPACE}/ansibleplay
            ansible-playbook -i hosts installPackages.yml --ssh-common-args='-o "StrictHostKeyChecking no"'
            echo "Ansible yaml successfully applied"
        """
    }
    
}
