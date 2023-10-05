# python-docker-app
## To build the docker image in current directory
```
sudo docker build -t python-flask-app .
```
## To run the docker image 
```
sudo docker run -d -p 6000:6000 <imgname>
```
## Expose the application using public Ip
```
<publicIp>:6000
```
