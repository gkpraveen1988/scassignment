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
        def ipaddress = sh "terraform output instance_ip_addr"
        //def ipaddress = '10.40.73.82'
        sh """
            cd ${env.WORKSPACE}/ansibleplay
            cp /instance1.pem ${env.WORKSPACE}/ansibleplay
            echo '[local_instance]' > hosts
            echo "${ipaddress} ansible_connection=ssh ansible_user=ec2-user" >> hosts
            echo '' >> hosts
            echo '[local_instance:vars]' >> hosts
            echo 'ansible_ssh_private_key_file=instance1.pem' >> hosts
            echo "Ansible host file constructed" 
            cat ${env.WORKSPACE}/ansibleplay/hosts            
        """
    }
    
    stage('Applying ansible files') {
        sh """
            cd ${env.WORKSPACE}/ansibleplay
            ansible-playbook -i hosts installPackages.yml
            echo "Ansible yaml successfully applied"
        """
    }
}
