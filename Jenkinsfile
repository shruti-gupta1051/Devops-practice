pipeline
{
agent{
  label "ec2"
}
  stages{
    stage("Deployment on PROD Env"){
      steps{
        sh "docker rm -f webos"
        sh  "docker pull shrutipp/gfgcicd:latest"
        sh "docker run -dit --name webos -p 80:80 shrutipp/gfgcicd"
      }
    }
  }
}
