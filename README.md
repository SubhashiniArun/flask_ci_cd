# APP

Setting up app template
-> set up flask app
-> set up config and load the config into app
-> set up error handler globally for the app by defining logger(logging for application, logging into logfile)  
-> initialize extensions - DB (SQLAlchemy)
-> set up blueprint to register the routes

1. create User models in models file
2. use SQLAlchemy ORM to interact with MySQL Database
3. create RESFTful APIS to add, get, update and delete the resources. used blueprint to register the APIs
4. add unit tests to test the APIs
5. implement microservice architecture to call API from other service
6. set up logger functionality
7. deep dive into database connectivity (separating DB from APIs) and MySQL queries (join table)
8. including AWS EC2, Serverless lambda, S3, 
9. RabbitMQ queue, aysnc/background processing
9. deployed using CI/CD (Github Actions) to kubernetes 

Developed and containerized a microservice using Docker, and deployed it on Kubernetes with CI/CD pipelines (GitHub Actions), automating build, test, and deployment processes to accelerate release cycles and enhance system reliability.

