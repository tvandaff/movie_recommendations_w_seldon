# Movie Recommendations with Seldon

 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; I decided to test out the functionality of Seldon Core for model deployment. I ran an example for demonstration purposes from my local machine. For this example, I used a movie recommendation model and served it user id queries, returning movie recommendations in response to each query. I installed Seldon in conjunction with Istio, but the lack of documentation on this relationship led me to continue the search for a better user interface tool that could provide model visibility. I finally decided on Fusion.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; I built the model using S2I or source to image, which packaged my custom python model into an image that was ready to be containerized. I deployed the image with Docker with simple tagging and pushing commands on my local machine.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Once the model was deployed to my repository on Docker Hub, I ran the microservice locally through port 5000. From this point on I was able to curl my model and receive predictions with a given data input. You can see the simple model deployment files at my GitHub link. This will show you not only how I trained the model, but also how I saved the model to a pickle file, and uploaded it using a Python Wrapper into the Seldon Image.  

## The Files: 
- Seldonmodel folder: contains the seldon deployment files from my experiments
    - canary.yaml: code for deploying two models to receive incoming requests (20% of requests sent to canary model) 
    - deployment.yaml: code for deploying a single Seldon model
    - environment: commandline variables for Seldon execution
    - Model.py: Simple baseline model execution code
    - Model2.py: SVD model execution code
    - requirements.txt: dependencies for containerizing Model2.py
    - user_rating.pickle: pickled user data loaded into the init of Model2.py 
- Various screenshots: show the commands I executed to run the deployment files from an Ubuntu terminal
- SVD_movie_rec_model.ipynb: model training code for Model2.py
- user_ratings.pickle: pickled user data for model training
- finalized_model.sav: pickled model produced by training code

## The Problem Seldon Solves
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; The problem Seldon solves is quite simple. It is an abstraction of the microservice development process for models. Seldon simplifies this microservice deployment process and publishes the microservice to an endpoint. This endpoint can serve requests with the model predictions. Seldon did not stop at model deployment but includes additional functionality for model metrics record keeping, A/B testing, and canary deployments. Besides the model deployment itself, because Seldon sits on top of Kubernetes, it is capable of autoscaling your model to meet demand, given the proper configuration files. 
