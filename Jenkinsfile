pipeline {
  agent { label "master" 
  }

  environment {
    APP_NAME = "expense_splitter"
    RELEASE = "1.0.0"
    DOCKER_USER = "tobbeee"
    DOCKER_PASS = "dockerhub"
    IMAGE_NAME = "${DOCKER_USER}" + "/" + "${APP_NAME}"
    IMAGE_TAG = "${RELEASE}-${BUILD_NUMBER}"  
    }
  
  stages {
    stage("Cleanup Workspace") {
      steps {
        cleanWs()
      }
    }

    stage("Checkout from SCM") {
      steps {
        git branch: "remove_pablo", credentialsId: "github", url:"https://github.com/tobbeee/expense-splitter"
      }
    }

    stage("Build environment") {
      steps {
        sh "ls -l"
        sh "python3 -m pip install -r requirements.txt"
      }
    }

    stage("Build Application") {
      steps {
        sh "python3 expense_splitter.py"
      }
    }

    stage("Test Application") {
      steps {
        sh "python3 test_expense_splitter.py"
      }
    }

    stage("Build and Push Docker Image") {
      steps {
        script {
          docker.withRegistry("",DOCKER_PASS) {
              docker_image = docker.build "${IMAGE_NAME}"
          }

          docker.withRegistry("",DOCKER_PASS) {
              docker_image.push("${IMAGE_TAG}")
              docker_image.push("latest")
          }
        }
      }
    }
  }
}