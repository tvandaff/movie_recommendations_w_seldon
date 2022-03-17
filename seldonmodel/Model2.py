import pandas as pd 
import pickle 
from surprise import SVD
from surprise import Dataset
from surprise.model_selection import cross_validate
from surprise import NormalPredictor
from surprise import Dataset
from surprise import Reader
from surprise import accuracy
from surprise.model_selection import KFold
import random
import numpy as np
from surprise.model_selection import GridSearchCV
from collections import defaultdict

def read_and_preprocess(picklefile):
      with open(picklefile, 'rb') as f:
            pickled = pd.read_pickle(f)

      #Form the Dataframe from the pickle and remove from nested dicts 
      df2 = pd.DataFrame()
      for key, value in pickled.items():
            df = pd.DataFrame(columns=['User', 'Item', 'Rating'])
            df['Rating'] = pd.Series(value.values())
            df['Item'] = pd.DataFrame(value.keys())
            df['User'] = key
            df2 = pd.concat([df2, df], axis = 0)
      df2 = df2.reset_index(drop=True)
      #transform dataset into scikit-surprise format 
      # define data reader with rating_scale param 
      reader = Reader(rating_scale=(1, 5))
      # columns must correspond to user id, item id and ratings - in order 
      data = Dataset.load_from_df(df2[['User', 'Item', 'Rating']], reader)
      return df2, data

def basic_model(data):
      # build svd model
      model = SVD(n_epochs=10)

      #split the data 
      cross_validate(model, data, measures=['RMSE', 'MAE'], cv=5, verbose=True)

      trainset = data.build_full_trainset()

      model.fit(trainset)

      return model

def top20_prediction(userid, model, data, threshold_=20): 
      movies = list(data['Item'].values)
      random.shuffle(movies)
      count = 0
      ratings = []
      movie_holder = []
      for movie in movies:
            if count >= 1500:
                  break
            else:
                  rating = model.predict(userid, movie)
                  rating2 = rating.est
                  ratings.append(rating2)
                  movie_holder.append(movie)
                  count += 1
     ratings_array = np.array(ratings)
     indices = np.argsort(ratings_array)
     sorted_movies = []
     count = 0
     #print(indices[:20])
     for i in indices:
           if count >= 20:
                 break
           if i not in sorted_movies:
                 sorted_movies.append(movie_holder[i])
                 count += 1
     #account for multiples 
     return sorted_movies

def read_and_tune(data):
      #hyperparameters to be tuned: 
      hyperparam_grid = {'n_epochs': [10,50], 'lr_all': [0.005,0.01],'reg_all':[0.02,0.1]}
      #use gridsearch to combine hyperparameters to determine optimal configuration
      gs = GridSearchCV(SVD, hyperparam_grid, measures=['rmse', 'mae'], cv=3)
      gs.fit(data)
      #use rmse to select the final hyperparameters 
      params = gs.best_params['rmse']
      #create model with tuned hyperparameters 
      modeltuned = SVD(n_epochs=params['n_epochs'],lr_all=params['lr_all'], reg_all=params['reg_all'])
      #split data into five folds and show RMSE and MAE across each iteration of training
      cross_validate(modeltuned, data, measures=['RMSE', 'MAE'], cv=5, verbose=True)
      #create a training dataset
      trainset = data.build_full_trainset()
      #train tuned model on training set 
      modeltuned.fit(trainset)

class Model:
    def __init__(self):
          filename = 'finalized_model.sav'
          self.df, self.data = read_and_preprocess('user_ratings.pickle')
          self._model = pickle.load(open(filename, 'rb'))
          
    def predict(self, X):
          output = top20_prediction(X, self._model, self.df, 20)
          return output
