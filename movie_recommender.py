import turicreate as tc
load_best_model = True

rating_movie = tc.SFrame("./rating_movie.sframe")
unique = rating_movie['userId'].unique()

train_data, test_data = rating_movie.random_split(.8)
if not load_best_model:
	movie_model = tc.item_similarity_recommender.create(train_data,
                                                    user_id = 'userId',
                                                    item_id = 'title')
	movie_model.save("./best_movie_model")
else:
	movie_model = tc.load_model("./best_movie_model")

unique_title = rating_movie['title'].unique()

def rec_movie_lst(title_search):
    title_search_list = []
    for itm in unique_title:
        alpha_title_lst = []
        if len(title_search.split(" ")) <= 1:
            words = itm.lower().split(" ")
            for word in words:
                alpha_word = ''.join(c for c in word if c.isalpha() or c.isdigit())
                if title_search.lower() == alpha_word:
                    title_search_list.append(itm)    
        else:
            words = itm.lower().split(" ")
            for word in words:
                alpha_word = ''.join(c for c in word if c.isalpha() or c.isdigit())
                alpha_title_lst.append(alpha_word)
            alpha_title = ' '.join(w for w in alpha_title_lst)
            if title_search.lower() in alpha_title:
                title_search_list.append(itm)
    return movie_model.get_similar_items(title_search_list,k=4)['similar']
