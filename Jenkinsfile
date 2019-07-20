def admintoken = "1147655d74720ae967e1be190d4d31990f"

node('master'){
    stage('Creating Ec2 Instance') {
        cd ${WORKSPACE}/terradetails
        terraform init                      // Initiating terraform
        terraform plan                      // Getting a pre-approval / check the resources to be applied to
        terraform apply --auto-approve      // Applying the terraform file
        terraform output instance_ip_addr   // Capturing the state after applying the changes and IP Address
    }

    stage('Jenkins CLI to add the slave entry') {
        sh '''
        cat <<EOF | java -jar jenkins-cli.jar -s http://10.40.73.106:8000 -auth admin:1147655d74720ae967e1be190d4d31990f create-node appserver 
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
        '''
    }
}
