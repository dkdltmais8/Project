<template>
  <div class="margin-x">
    <b-container class="bv-example-row">
      <b-row>
        <b-col cols="12" align="left">
          <hr>
          <div>
            <h2 class="my-tc"><p>오늘 찜한 영화</p></h2>
            <vueper-slides
              class="no-shadow br"
              :slide-image-inside="false"
              :style="'background-color: rgb(15, 15, 15)'"
              :touchable="false"
              :bullets="false"
              :visible-slides="5"
              slide-multiple
              :gap="3"
              :slide-ratio="1 / 4">
              <vueper-slide v-for="(movie, i) in newMovies" :key="i">
                <template v-slot:content>
                  <div align="center">
                    <p><img :src="movie.poster_path" alt="img" height="250"></p>
                    <div class="text-wrap fs-6 actor-name">{{ movie.movie_title }}</div>
                  </div>
                </template>
              </vueper-slide>
            </vueper-slides>
          </div>
          <hr>
          <div>
            <h2 class="my-tc bg-myColor"><p>나의 영화들</p></h2>
            <vueper-slides
              class="no-shadow br"
              :slide-image-inside="false"
              :style="'background-color: rgb(15, 15, 15)'"
              :touchable="false"
              :bullets="false"
              :visible-slides="5"
              slide-multiple
              :gap="3"
              :slide-ratio="1 / 4">
              <vueper-slide v-for="(movie, i) in oldMovies" :key="i">
                <template v-slot:content>
                  <div align="center">
                    <p><img :src="movie.poster_path" alt="img" height="250"></p>
                    <div class="text-wrap fs-6 actor-name">{{ movie.movie_title }}</div>
                  </div>
                </template>
              </vueper-slide>
            </vueper-slides>
          </div>
          </b-col>
        <b-col></b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
import {VueperSlides, VueperSlide} from 'vueperslides'
import 'vueperslides/dist/vueperslides.css'
export default {
  name: "MyMovies",
  components: {
    VueperSlides, VueperSlide,
  },
  props: {
    movies: {
      type: Array,
    }
  },
  data: function () {
    return {
      Month: ['', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
      newMovies: [],
      oldMovies: [],
    }
  },
  methods: {
    divideMovies: function () {
      const today = new Date()
      const date = String(today).split(" ")
      this.newMovies = this.movies.filter((movie) => {
        const subscribeAt = movie.created_at.split(" ")
        const subscribeDate = subscribeAt[0].split("-")
        if (parseInt(date[2])===parseInt(subscribeDate[2]) && date[1]===this.Month[parseInt(subscribeDate[1])] && parseInt(date[3])===parseInt(subscribeDate[0]) ){
          return true
        }
        this.oldMovies.push(movie)
        return false
      })
      this.newMovies.sort(function (a, b) {
        if (b.created_at > a.created_at) return 1
        else return -1
      })
    }
  },
  watch: {
    movies: function () {
      this.divideMovies()
    }
  },
  created: function () {
      this.divideMovies()
  }
}
</script>

<style scoped>
.fs-small {
  font-size: x-small;
}
.margin-x {
  margin: 0 100px 0 100px
}
.bg-myColor {
  background-color: rgb(15, 15, 15);
}
.br {
  border-radius: 30px
}
.actor-name {
  opacity: 0.8;
  color: aliceblue;
}
</style>