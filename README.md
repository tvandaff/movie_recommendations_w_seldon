# Movie Recommendations with Seldon

  I decided to test out the functionality of Seldon Core for model deployment. I ran an example for demonstration purposes from my local machine. For this example, I used a movie recommendation model and served it user id queries, returning movie recommendations in response to each query. I installed Seldon in conjunction with Istio, but the lack of documentation on this relationship led me to continue the search for a better user interface tool that could provide model visibility. I finally decided on Fusion. 
  I built the model using S2I or source to image, which packaged my custom python model into an image that was ready to be containerized. I deployed the image with Docker with simple tagging and pushing commands on my local machine. 
  Once the model was deployed to my repository on Docker Hub, I ran the microservice locally through port 5000. From this point on I was able to curl my model and receive predictions with a given data input. You can see the simple model deployment files at my GitHub link. This will show you not only how I trained the model, but also how I saved the model to a pickle file, and uploaded it using a Python Wrapper into the Seldon Image.  

## The Files: 
- Seldonmodel folder 
    - canary.yaml
    - deployment.yaml
    - environment
    - Model.py
    - Model2.py
    - requirements.txt
    - user_rating.pickle
- Various screenshots: 
- SVD_movie_rec_model.ipynb: 
- user_ratings.pickle: 
- finalized_model.sav

## The Problem Seldon Solves
  The problem Seldon solves is quite simple. It is an abstraction of the microservice development process for models. Seldon simplifies this microservice deployment process and publishes the microservice to an endpoint. This endpoint can serve requests with the model predictions. Seldon did not stop at model deployment but includes additional functionality for model metrics record keeping, A/B testing, and canary deployments. Besides the model deployment itself, because Seldon sits on top of Kubernetes, it is capable of autoscaling your model to meet demand, given the proper configuration files. 
