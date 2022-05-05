# Cloud Cooked - A CSC 468 Project

## Steps to Recreate:

1. First, using a valid Cloudlab, clone this repo into a new experiment profile
2. Next, instantiate an experiment.
3. After waiting for the experiment to finish starting, you must SSH into the HEAD node and begi the final startup
   sequence.
   This involves starting Jenkins as described in the CSC 468 CI/CD Episode.
4. Once Jenkins is up and running, you are ready to start deploying the app. If you do not want to use CI/CD, follow the
   steps below this and you are done.
   If you want to use CI/CD, continue following the steps.
    1. To setup the project without CI/CD, you must manually launch the kubernetes Deployments.
       This means running the following commands in a shell running on the head node.
    2. First, build the
       deployments: `cd /local/repository/DockerFiles;git branch flask;docker-compose build flask;docker-compose push flask`
    3. Next, deploy the containers to the local
       registry: `cd /local/repository/DockerFiles;git branch mysql;docker-compose build mysql;docker-compose push mysql`
    4. Next, apply the kubernetes deployment file for mysql `cd /local/repository;kubectl apply -f mysql.yaml`
        1. Wait for this deployment to finish starting the server before proceeding. It takes about 90 seconds.
    5. Next, apply the kubernetes deployment file for
       flask `cd /local/repository;git branch flask;kubectl apply -f flask.yaml`
    6. View the efforts of your labor by grabbing the external IP: `ip a | grep eth0` and visting that ip in your
       browser, port `350000`
5. If you are using Jenkins CI/CD, you will need two pipelines to run the project. First, fork this repository so that
   you may enable Github Webhooks. This is what triggers a Jenkins build upon a git commit/tag.
6. Next, create the two pipelines. Point each of them towards your forked repository. Then, specify the two branches in
   the two pipelines, namely flask and mysql.
7. Run the MySql pipeline first and wait for it to start, this takes about 90 seconds after the deployment step.
8. After waiting for the database to be up and running, you are ready to start the flask webserver. Run the flask
   deployment, and it should be reachable at `ip a | grep eth0`:35000
9. Lastly, test the CI/CD by pushing to your repo. If the GitHub webhooks are set up correctly, you should see Jenkins
   start a build moments after pushing to GitHub.