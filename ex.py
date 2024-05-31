not_found_movie = ['Nehlle Pe Dehlla', 'Darling', 'Speed', 'Jannat', 'Ek: The Power of One', 'Tum Mile', 'Kucch Luv Jaisaa', 'Bodyguard', 'Barfi!', 'Yeh Jawaani Hai Deewani', 'Dhoom 3', 'Ae Dil Hai Mushkil', 'Dangal', 'Jagga Jasoos', 'Jab Harry Met Sejal', 'Kalank', 'The Sky Is Pink', 'The Forgotten Army - Azaadi Ke Liye', 'Ludo', '83', 'Brahmāstra: Part One – Shiva', 'Tu Jhoothi Main Makkaar', 'Animal', 'Dunki', 'Anees Bazmee', 'Shashank Khaitan']

for nf_movie in not_found_movie:
        list = [word for word in nf_movie.split()]
        nf_movie_url = "https://en.wikipedia.org/wiki/" + '_'.join(list) + "_(soundtrack)"
        print(nf_movie_url)
        