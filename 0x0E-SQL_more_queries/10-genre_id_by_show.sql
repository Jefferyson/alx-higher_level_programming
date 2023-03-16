-- Script that lists all all shows contained in hbtn_0d_tvshows that have at least one genre linked
SELECT tv_show.title, tv_show_genres_genre_id
    FROM tv_shows
    INNER JOIN tv_show_genres
    ON tv_shows.id = tv_show_genres.show_id
    ORDER BY tv_shows.title, tv_sjow_genres.genre_id ASC;
