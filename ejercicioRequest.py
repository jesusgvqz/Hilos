import requests

##data = {"id": "tt7975244", "image": "https://m.media-amazon.com/images/M/MV5BOTVjMmFiMDUtOWQ4My00YzhmLWE3MzEtODM1NDFjMWEwZTRkXkEyXkFqcGdeQXVyMTkxNjUyNQ@@._V1_Ratio0.6837_AL_.jpg","title": "Jumanji: The Next Level","description": "(2019)","runtimeStr": "123 min","genreList": [{"key": "Action","value": "Action"},{"key": "Adventure","value": "Adventure"},{"key": "Comedy","value": "Comedy"}],"contentRating": "PG-13","imDbRating": "6.7","imDbRatingVotes": "247970","metacriticRating": "58","plot": "In Jumanji: The Next Level, the gang is back but the game has changed. As they return to rescue one of their own, the players will have to brave parts unknown from arid deserts to snowy mountains, to escape the worlds most dangerous game.","starList": [{"id": "tt7975244","name": "Jake Kasdan"},{"id": "tt7975244","name": "Dwayne Johnson"},{"id": "tt7975244","name": "Jack Black"},{"id": "tt7975244","name": "Kevin Hart"}, {"id": "tt7975244","name": "Karen Gillan"}]}
##url_image = data['image']

r = requests.get('https://clandestina-hds.com/movies/title?search=shrek')
data = r.json()

