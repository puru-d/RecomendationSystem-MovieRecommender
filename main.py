from flask import Flask
from flask import request
from movie_recommender import rec_movie_lst

rec_movie_str = ""
app = Flask(__name__)
@app.route("/")
def index():
	titlename = request.args.get("titlename", "")
	recommended_movies = rec_movie_lst(titlename)
	rec_movie_str = "\n".join(recommended_movies)
	return ( 
		"""<form action="" method="get">
			<input type="text" name="titlename">
			<input type="submit" value="Recommend">
		</form>"""
		+ "Recommended Movies:"
		+ "\n"
		+ rec_movie_str
		)


if __name__ == "__main__":
	app.run(host="127.0.0.1", port=8080, debug=True)
