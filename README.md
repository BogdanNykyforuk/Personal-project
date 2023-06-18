# Personal-project
login: qwerty, password: qwerty12
SafeRoute overlays a map with a danger level heatmap based on crime data.
The application is built using FastAPI/MongoDB on the backend and React on frontend. API runs in Docker, deployed on AWS Lambda, and main app is deployed on AWS Amplify.

Installation
To deploy project you will need to:

1. Clone the SafeRoute repository to your local machine.
2. Change uri in mongo_db file.
3. Build and deploy lambda_func container to AWS Lambda.
4. Via amplfy init connect frontend to your account.
5. Deploy frontend to AWS amplify.
6. Add to env variables MongoDB Atlas MONGODB_URI_PSW and GoogleMapsApi key.
To update map:

1. Install requirements in requirements.txt
2. Change uri in mongo_db.py file.
3. Add .env variables (MONGODB_URI_PSW, GEOCODE_API_KEY Geocodio key))
4. Change settings in mongo_db.py and start it.
 Stack
Python - simple and readable programming language, widely used in web development.
FastAPI - modern, fast (high-performance) web framework for building APIs with Python, based on standard Python type hints.
TensorFlow - open-source machine learning framework for building and deploying ML models.
AWS Amplify - development platform provided by Amazon Web Services (AWS) that enables frontend web and mobile developers to build full-stack applications.
AWS Lambda - serverless computing service provided by AWS that lets you run your code without provisioning or managing servers.
MongoDB Atlas - fully managed cloud database service for MongoDB.
Docker - platform that allows automatic the deployment of applications inside containers, providing an efficient and consistent environment for running applications.
React - JavaScript library for building user interfaces.
