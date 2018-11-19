# web_coding_challenge

## project dependencies 
```
docker
```

## deploy script in dev mod
```
sudo sh dev_deploy_project.sh
```

## project architecture
```
The project follow the microservices architecture: we have two microservices, shopify and shopify_auth, each with its own database.
    - Shopify_auth microservice used for user authentication.
    - Shopify microservice handle the business requirements of the applicaton.
    - Shops are retrieved from GOOGLE API.
    - Databases are containerized with docker.
```

## TODO
```
	- Containerize the whole project
	- Add Front-End microservice with React and Reduce
	- Use Celery for async jobs
```