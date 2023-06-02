## Build infrastructure for a real application including AWS Application Load Balancer + Auto Scaling Group + Relational Database Service using Terraform Module include Root module, Autoscaling module, Networking module and Database module.

### Build steps:

- cd ./terrafrom-project
- terraform init (init terraform repo)
- terraform plan (view before deploy)                   
- terraform apply --auto-approve (deploy terraform) 
- terraform destroy --auto-approve (destroy infra)  

# django setup deploy

**2)** `initial-setup.sh` - This file is the first file to look at when setting up this project. It installs the required packages to make this project work such as Nginx, Jenkins, Python etc. Refer to the youtube video to see how and when it is used.

**3)** `Jenkinsfile` - This file contains the definition of the stages in the pipeline. The stages in this project's pipeline are `Setup Python Virtual Environment`, `Setup gunicorn service` and `Setup Nginx`. The stages in this pipeline just does two things. First it makes a file executable and then runs the file. The file carries out the commands that is described by the stage description.

**4)** `envsetup.sh` - This file sets up the python virtual environment, installs the python packages and then creates log files that will be used by Nginx. 

**5)** `gunicorn.sh` - This file runs some Django management commands like migration commands and static files collection commands. It also sets up the gunicorn service that will be running the gunicorn server in the background.

**6)** `nginx.sh` - This file sets up Nginx with a configuration file that points Nginx to the gunicorn service that is running our application. This allows Nginx serve our application. I have followed a digital ocean article to setup this file. You can go through the video once to replicate sites-available and sites-enabled scanerio. 

**7)** `app.conf` - This is an Nginx server configuration file. This file is used to setup Nginx as proxy server to gunicorn. For this configuration to work, change the value of `server_name` to the IP address or domain name of your server. 

**8)** `gunicorn.service` - This is a Systemd Service configuration file. This configures the gunicorn server to run in the background as a service. It also sets the path to the gunicorn sock file. At the end of the `ExecStart` value, change it to the path of the `wsgi` file of the Django Project. Also set the User to the one that owns the project folder according to the configuration from the youtube video. 


