-- Lists all genres and shows linked to a show from the database 'hbtn_0d_tvshows'

SELECT tv_shows.title, tv_genres.name
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
ORDER by 1, 2 ASC;
