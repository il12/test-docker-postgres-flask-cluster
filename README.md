# For using web application in cluster mode use follow this guideline:

Create registry where your application will be published.
```bash
docker service create --name registry --publish published=5000,target=5000 registry:2
```

Build all images to be sure that they exist
```bash
docker-compose up -d
```

Push your application to registry created before
```bash
docker-compose push
```

Deploy your application
```bash
docker stack deploy --compose-file docker-compose.yml 13112020
```

Check that all worked correctly and all services and all replicas were deployed
```bash
docker stack services 13112020
```
