<template>
  <div>
    <h1 class="padding-50 my-tc">POPULAR</h1>
    <vueper-slides
    :autoplay="autoplay"
    infinite
    class="no-shadow"
    :touchable="false"
    :visible-slides="6"
    :arrows="false"
    :slide-ratio="1 / 4"
    :gap="3"
    >
      <vueper-slide v-for="(actor, i) in actors" :key="i" :image="actor.profile_path" :duration="3000"
        @click.native="actorId=actor.id, $bvModal.show('modal')"
        @mouseover.native="actor.mouse_over=true"
        @mouseout.native="actor.mouse_over=false"
        :class="{borderMouse: actor.mouse_over, cp: actor.mouse_over}">
        <template v-slot:content>
          <div class="badge bg-secondary text-wrap fs-5 actor-name" style="width: 12rem;">
            {{actor.name}}
          </div>
        </template>
      </vueper-slide>
    </vueper-slides>

    <b-modal id="modal" centered size="lg" hide-header-close>
      <template #modal-title> 배우 설명</template>
      <div class="d-block">
        <img :src="actor.profile_path" alt="img" height="400" align="left">
        <div align="center">
          <h3><b>{{ actor.name }}</b></h3>
          <p><b>국적</b> : {{ actor.place_of_birth }}</p>
          <p><b>출생일</b> : {{ actor.birthday }}</p>
          <div class="crollbar">{{ actor.biography }} </div>
          <button class="bottom" v-if="isSubscriber" @click="actorSubscribe()">구독 취소</button>
          <button class="bottom" v-if="!isSubscriber" @click="actorSubscribe()">구독 하기</button>
        </div>
      </div>
      <template #modal-footer align="center">
        <div class="padding w-100">
          <vueper-slides
            class="no-shadow"
            slide-multiple
            :touchable="false"
            :bullets="false"
            :visible-slides="3"
            :slide-ratio="1 / 3">
            <vueper-slide v-for="(movie, i) in movies" :key="i">
              <template v-slot:content>
                <div align="center" class="fs-small">
                  <img :src="movie.poster_path" @click="[movieId=movie.id, movieIdx=movie.index, movieSubscribe()]" v-bind:class="{borderRed: movie.subscribe}" alt="img" width="100">
                  <div><b>{{ movie.title }}</b></div>
                  <div v-if="movie.date"><b>({{ movie.date }})</b></div>
                </div>
              </template>
            </vueper-slide>
          </vueper-slides>
        </div>
      </template>
    </b-modal>

  </div>
</template>

<script>
import axios from'axios'
import {VueperSlides, VueperSlide} from 'vueperslides'
import 'vueperslides/dist/vueperslides.css'

export default {
  name: 'PersonList',
  components: {
    VueperSlides, VueperSlide
  },
  props: {
    myWord: {
      type: String,
    }
  },
  data: function () {
    return {
      actors: [],
      actorId: '',
      actor: {},
      movies: {},
      movieId: '',
      movieIdx: '',
      isSubscriber: false,
      autoplay: true,
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
    getPerson: function () {
      axios({
        method: 'get',
        url: 'https://api.themoviedb.org/3/person/popular?api_key=33b865b38e340385996befbfd40fadd0',
      })
      .then((response) => {
        this.actors = response.data.results.map(({name, profile_path, popularity, id}) => ({
          name, popularity, 
          profile_path: `https://image.tmdb.org/t/p/original${profile_path}`, 
          id,
          mouse_over: false
        }))
      })
    },
     actorSubscribe: function () {
      axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/subscribe/actors/',
        data: {
          actor_id: this.actorId,
          actor_name: this.actor.name,
          profile_path: this.actor.profile_path,
        },
        headers: this.setToken()
      })
      .then((response) => {
        if (response.data['subscribe']) {
          this.isSubscriber = true
        }
        else {
          this.isSubscriber = false
        }
      })
    },
    movieSubscribe: function () {
      axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/subscribe/movies/',
        data: {
          movie_id: this.movieId,
          movie_title: this.movies[this.movieIdx].title,
          poster_path: this.movies[this.movieIdx].poster_path,
        },
        headers: this.setToken()
      })
      .then((response) => {
        if (response.data['subscribe']) {
          this.movies[this.movieIdx]['subscribe'] = true
        }
        else {
          this.movies[this.movieIdx]['subscribe'] = false
        }
      })
    },
  },
  watch: {
    actorId: function () {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/subscribe/actors/',
        headers: this.setToken()
      })
      .then((response) => {
        this.isSubscriber = false
        for (const actor of response.data) {
          if (actor['actor_id']==this.actorId) {
            this.isSubscriber = true
          }
        }
      })

      axios({
        method: 'get',
        url: `https://api.themoviedb.org/3/person/${this.actorId}?api_key=33b865b38e340385996befbfd40fadd0`,
      })
      .then((response) => {
        const tmp = response.data
        const places = tmp.place_of_birth.split(',')
        const place_of_birth = places[places.length-1]
        this.actor = {
          id: tmp.id,
          name: tmp.name,
          birthday: tmp.birthday,
          place_of_birth,
          profile_path: `https://image.tmdb.org/t/p/original${tmp.profile_path}`,
          biography: tmp.biography,
        }
      })

      axios({
        method: 'get',
        url: `https://api.themoviedb.org/3/person/${this.actorId}/movie_credits?api_key=33b865b38e340385996befbfd40fadd0`,
      })
      .then((response) => {
        this.movies = response.data.cast.map(({id, title, poster_path, release_date}, index) => ({
          id, title, date: release_date,
          poster_path: `https://image.tmdb.org/t/p/original${poster_path}`,
          index,
          subscribe: false
        }))
      })

      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/subscribe/movies/',
        headers: this.setToken()
      })
      .then((response) => {
        for (const movie of this.movies) {
          if (response.data.some(function (a) { return movie.id === parseInt(a.movie_id) })) {
            movie.subscribe = true
          }
        }
      })
    },
    myWord: function () {
      const isWord = /^[가-힣|ㄱ-ㅎ|ㅏ-ㅣ|a-z|A-Z|0-9|\s]/.test(this.myWord)
      if (isWord) {
        axios({
          method: 'get',
          url: `https://api.themoviedb.org/3/search/person?api_key=33b865b38e340385996befbfd40fadd0&query=${this.myWord}&page=${this.page}`,
        })
        .then((response) => {
          this.autoplay = false
          const searchList = response.data.results.map(({id, name, profile_path, popularity}, index) => ({
            id, name, index, popularity,
            profile_path:`https://image.tmdb.org/t/p/original${profile_path}`,
            mouse_over: false
          }))
          this.actors = searchList.sort(function (a, b) {
            return b.popularity-a.popularity
          })
        })
      }
      else {
        console.log("리셋");
        this.myWord = ''
        this.autoplay = true
        this.actors = this.getPerson()
      }
    }
  },
  created: function (){
    this.getPerson()
  }
}
</script>

<style scoped>
.borderMouse {
  border:3px solid white;
}
.vueperslide__inner {
  width: 200;
}
.crollbar {
  overflow:scroll; 
  overflow-x:hidden;
  width:400px; 
  height:200px;
}
.padding {
  padding: 0px 80px;
}
.bottom {
  position: absolute;
  right: 60px;
  bottom: 0px;
  margin: 20px;
}
.fs-small {
  font-size: x-small;
}
.borderRed {
  border:3px solid #1cff07;
}
.padding-50 {
  padding: 50px;
}
.cp {
  cursor:pointer;
}
ul {
  list-style:none;
}
.actor-name {
  margin-top: 150%;
  opacity: 0.8;
}
</style>