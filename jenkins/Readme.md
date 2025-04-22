# Jenkins

Run the following commands for jenkins:

```bash
# This command installs the jenkins and run it locally, you can access it via `localhost:808`
# It asks you about the password which you get from logs of 'jenkins' running container like a hashed form string
# As like this e.g., 4f91e958bdac4d91b6b52d95354b6dc8
docker run -d -p 8081:8080 --name jenkins jenkins/jenkins
```
