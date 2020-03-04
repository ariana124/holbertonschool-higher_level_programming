-- Lists all shows contained in the database 'hbtn_0d_tvshows' that have at least 1 genre linked

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
JOIN tv_show_genres
ON tv_show_genres.show_id = tv_shows.id
ORDER by 1, 2;
