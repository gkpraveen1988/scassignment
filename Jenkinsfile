def admintoken = "1147655d74720ae967e1be190d4d31990f"

node('master'){
    stage('Checking out code') {
        checkout scm
    }
    
    stage('Jenkins CLI to add the slave entry') {
        sh """
        wget http://10.40.73.106:8000/jnlpJars/jenkins-cli.jar -o /tmp/jenkins-cli.jar
        cd /tmp
        cat <<EOF | java -jar jenkins-cli.jar -s http://10.40.73.106:8000 -auth admin:$admintoken create-node appserver 
            <slave>
              <name>10.40.73.106</name>
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
}
