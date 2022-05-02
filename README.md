# cloud-run-test
This is a repository that takes a pickled model and deploys it to the GCP service that I set up to run the model. The model will be capable of doing some machine learning on URLS that given to it.


## hosted pickle
The pickle model is [hosted on the professor website ](phish-model-1649995335.cloudpickle).


## Docker compose
It is possible to use docker-compose on this repo using the following command:

```bash
docker-compose up
#use this to run the docker. 
```
```bash
docker-compose exec web python make-request.py
#this is the command for the routes within the flask app
```
