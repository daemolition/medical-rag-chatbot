pipeline {
    environment {

    }

    stages {
        stage('Clone Github Repo') {
            steps {
                script {
                    echo 'Cloning Github repo to Jenkins...'
                    checkout scmGit(
                        branches: [[name: '*/main']], 
                        extensions: [], 
                        userRemoteConfigs: [[
                            credentialsId: '3db88c07-d892-4b48-bd13-9cf7f19e876d', 
                            url: 'https://github.com/daemolition/medical-rag-chatbot.git']])
                }
            }
        }
    }
}