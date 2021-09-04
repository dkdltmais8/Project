<template>
  <div>
    <Search />
    <MovieList />
    <GenreMovieAction />
    <GenreMovieComedy />
    <GenreMovieThriller />
    <GenreMovieFantasy />
  </div>
</template>

<script>
import Search from '@/components/Search'
import MovieList from '@/components/MovieList'
import GenreMovieAction from '@/components/GenreMovieAction'
import GenreMovieComedy from '@/components/GenreMovieComedy'
import GenreMovieThriller from '@/components/GenreMovieThriller'
import GenreMovieFantasy from '@/components/GenreMovieFantasy'


export default {
  name: 'Home',
  components: {
    Search,
    MovieList,
    GenreMovieAction,
    GenreMovieComedy,
    GenreMovieThriller,
    GenreMovieFantasy,
  },
}
</script>

<style>

</style>