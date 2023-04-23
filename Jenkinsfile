pipeline {
    agent {
        docker { image 'python:3.10' }
    }
    stages {
        stage('tests task') {
            steps {
                sh '''
                    python3 -m venv venv
                    source venv/bin/activate
                    pip install -r requirements.txt
                    nose2
                '''
            }
        }
    }
}