import random
class Model: 
    def __init__(self): 
        self._model=["The Wedding Planner", "The Dove", "The Lincoln Lawyer", "Waterboys", "The Kentuckian", "Saw", "Saw V", "The Purge", "The Purge: Anarchy", "The Treasure Hunter", "The A-Team", "The Earthling", "John Wick", "Free Willy", "Tarzan the Fearless", "Operation Dumbo", "The Black Stallion", "War and Peace", "Highlander", "Kronk's New Groove", "Turbulence", "The Texas Chainsaw Massacre", "Black Snake Moan", "Glee: The Concert Movie", "Murder Party", "Happy Feet Two", "The Matrix", "Aces High", "Teenage Mutant Ninja Turtles III", "The Karate Kid", "American Reunion", "Despicable Me 2"]
    def predict(self, X): 
        output = random.choices(self._model, k=5)
        return output
