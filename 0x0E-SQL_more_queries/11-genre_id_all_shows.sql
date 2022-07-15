-- Write a script that lists all shows contained in the database hbtn_0d_tvshows.
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows AS ts
LEFT JOIN tv_show_genres ON ts.id = tv_shows_genres.show_id
ORDER BY ts.title, tv_show_genres.genre_id;
