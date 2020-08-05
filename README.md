# Docker Compose Validator
## Idea
When we are using docker-compose, we may make silly mistakes. This tool helps you avoid making such mistakes!
<br />For example:
``` yaml
version: '3'

services:
    app:
        build: .
        image: takacsmark/flask-redis:1.0
        environment:
          - FLASK_ENV=development
        ports:
          - "4999-5005:4999-5005"
    redis:
        image: redis:4.0.11-alpine
```
This is a docker-compose that works correctly!
But imagine that you need more services. More services means complicated our docker-compose template! And at this point, human mistakes will probably show up! Say, we add more services, and at this point, we forgot that two of them share the same name, but <b>THEY ARE NOT THE SAME SERVICE!</b>
<br />Simply I'll lose one of my services!

``` yaml
version: '3'

services:

  service1:
    /* Some stuff */

  service2:
    /* Some other stuff */
    
    
    ************ OTHER SERVICES ************
    
    service-n:
        /* Some stuff */
    
    service2:   <---------------- DUPLICATE SERVICE! ----------------
        /* Some stuff */    
    
```
<br />
<br />
<br />


Another example:
Imagine you are new to docker-compose, and your template looks like this:
``` yaml
version: '3'

services:

  service1:
    /* Some stuff */

  service2:
    /* Some other stuff */
    
volumes:   <---------------- NOT IN A GOOD PLACE! ----------------
  db-data:


networks:
  something:
    external: true
    
```
Well this might happened to every newcomer with docker-compose!<br />

## How to use it

1. virtualenv venv
2. pip wheel .
3. install wheel wherever you feel like. it provides the command dcvalidate


## Can I contribute?
<b>YES!</b> <br />
Feel free to add some features!

## Note
This tool extends the [label consistency checker](https://github.com/serviceprototypinglab/label-consistency) which targets Docker Compose and Kubernetes/OpenShift YAML files.
It emerged from [research on microservice quality](https://mao-mao-research.github.io/) at Service Prototyping Lab, Zurich University of Applied Sciences.
