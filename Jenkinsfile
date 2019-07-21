def admintoken = "1147655d74720ae967e1be190d4d31990f"

node('appserver'){
    stage('Checking out code') {
        checkout scm
    }
    
    stage('Display all files') {
        sh """
        ls -ltr ${env.WORKSPACE}           
        """
    }
}
