<template>
  <div bg-dark class="bg-myColor">
    <h1 class="padding-100 my-tc">MyPage</h1>
    <MyActors :actors="actors"/>
    <MyMovies :movies="movies"/>
  </div>
</template>

<script>
import axios from'axios'
import MyActors from '@/components/MyActors'
import MyMovies from '@/components/MyMovies'

export default {
  name: 'MyPage',
  components: {
    MyActors, MyMovies,
  },
  data: function () {
    return {
      actors: [],
      movies: [],
    }
  },
  methods: {    
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    getActors: function () {
      axios({
        method: 'get',
        url : 'http://127.0.0.1:8000/subscribe/actors/',
        headers : this.setToken()
      })
      .then(res=>{
        this.actors = res.data
      })
    },
    getMovies: function () {
      axios({
        method: 'get',
        url : 'http://127.0.0.1:8000/subscribe/movies/',
        headers : this.setToken()
      })
      .then(res=>{
        this.movies = res.data
      })
    }
  },
  created() {
    this.getActors()
    this.getMovies()
  }
}
</script>

<style scoped>
.bg-color {
  background-color: rgb(73, 38, 38);
}
.padding-100 {
  padding: 100px;
}
.bg-myColor {
  background-color: rgb(15, 15, 15);
}
</style>