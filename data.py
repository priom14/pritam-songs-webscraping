import requests
from bs4 import BeautifulSoup
import csv
import time


url = 'https://en.wikipedia.org/wiki/Pritam_Chakraborty_discography'

response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

tables = soup.find_all('table', {'class': 'wikitable'})
only_movie = tables[:3]
not_found_movie = []

with open('pritam_song_details.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)

    for movie in only_movie:
        movie_details = movie.find_all('tr')
        for movie_detail in movie_details[1:]:
            movie_name_a_tag = movie_detail.find('a')
            if movie_name_a_tag and 'href' in movie_name_a_tag.attrs:
                movie_url = "https://en.wikipedia.org" + movie_name_a_tag['href']
                movie_name = movie_name_a_tag.text.strip()
                
                try:
                        inner_response = requests.get(movie_url)
                        inner_soup = BeautifulSoup(inner_response.content, 'html.parser')
                        
                        table = inner_soup.find('table', {'class': 'tracklist'})

                        if table:
                            tbody = table.find('tbody')
                            if tbody:
                                song_details = tbody.find_all('tr')
                                for song_detail in song_details[1:]:  
                                    song_detail_list = song_detail.find_all('td')
                                    song_info = [col.text.strip() for col in song_detail_list if col.text.strip()]
                                    # print(song_detail_list)
                                    
                                    writer.writerow([movie_name]+ song_info)
                                    
                                print('Success.')
                            else:
                                print(f"No <tbody> found in table at: {movie_url}")
                        else:
                            not_found_movie.append(movie_name)
                            print(f"No table with class 'tracklist' found at: {movie_url}")
                except requests.RequestException as e:
                        print(f"Failed to retrieve or parse page {movie_url}: {e}")
                        print("Failure")

            else:
                    print("No valid movie URL found in this row.")
    
    print("\n")
    print("-"*25)
    print("End of first fetching....")
    time.sleep(1)
    print("-"*25)
    print("Start of second fetching.....")
    print("-"*25)
    print("\n")
    
    tr_nf_movies = []
    tr_nf_movies_url = []
    for nf_movie in not_found_movie:
        list = [word for word in nf_movie.split()]
        nf_movie_url = "https://en.wikipedia.org/wiki/" + '_'.join(list) + "_(soundtrack)"
        movie_name = nf_movie
        try:
            inner_response_nf = requests.get(nf_movie_url)
            inner_soup_nf = BeautifulSoup(inner_response_nf.content, 'html.parser')
            
            table = inner_soup_nf.find('table', {'class': 'tracklist'})

            if table:
                tbody = table.find('tbody')
                if tbody:
                    song_details = tbody.find_all('tr')
                    for song_detail in song_details[1:]:  
                        song_detail_list = song_detail.find_all('td')
                        song_info = [col.text.strip() for col in song_detail_list if col.text.strip()]
                        # print(song_detail_list)
                        
                        writer.writerow([movie_name]+ song_info)
                        
                    print('Success.')
                else:
                    print(f"No <tbody> found in table at: {nf_movie_url}")
            else:
                tr_nf_movies.append(movie_name)
                print(f"No table with class 'tracklist' found at: {nf_movie_url}")
        except requests.RequestException as e:
                print(f"Failed to retrieve or parse page {nf_movie_url}: {e}")
                print("Failure")
    print("\n")
    print("-"*25)
    print("End of Second fetching....")
    time.sleep(1)
    print("-"*25)
    print("Start of Third fetching.....")
    print("-"*25)
    print("\n")
    
    for tr_nf_movie in tr_nf_movies:
        movie_url = [word for word in tr_nf_movie.split()]
        if movie_url[0].lower() == "jannat":
            nf_movie_url = "https://en.wikipedia.org/wiki/Jannat_(2008_film)"
        else:
            nf_movie_url = "https://en.wikipedia.org/wiki/" + '_'.join(movie_url)
        movie_name = tr_nf_movie
                
        try:
                inner_response_tr = requests.get(nf_movie_url)
                inner_soup_tr = BeautifulSoup(inner_response_tr.content, 'html.parser')
                
                table = inner_soup_tr.find('table', {'class': 'wikitable'})

                if table:
                    tbody = table.find('tbody')
                    if tbody:
                        song_details = tbody.find_all('tr')
                        for song_detail in song_details[1:]:  
                            song_detail_list = song_detail.find_all('td')
                            song_info = [col.text.strip() for col in song_detail_list if col.text.strip()]
                            # print(song_detail_list)
                            
                            writer.writerow([movie_name]+ song_info)
                            
                        print('Success.')
                    else:
                        print(f"No <tbody> found in table at: {nf_movie_url}")
                else:
                    print(f"No table with class 'wikitable' found at: {nf_movie_url}")
        except requests.RequestException as e:
                print(f"Failed to retrieve or parse page {nf_movie_url}: {e}")
                print("Failure")