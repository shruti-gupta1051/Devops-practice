pipeline
{
  agent{
    label "ec2"
  }
    stages{
      stage("deployment to prod env"){
        steps{
          sh "docker run -dit --name webos -p 80:80 shrutipp/gfgcicd
        }
      }
    }
}
