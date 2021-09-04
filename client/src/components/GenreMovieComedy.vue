<template >
<div class='black'>
  <h1 class="my-tc">Comedy</h1>
  <div style="padding-200px;">

  <vueper-slides 
  :arrows-outside = "true" 
  :bullets-outside = "true"
  class="no-shadow"
  :visible-slides="6"
  slide-multiple
  :gap="3"
  :fixed-height="true"
  :dragging-distance="200"

  >

  <vueper-slide 
  v-for="(movie,i) in movies" 
  
  :key="i" 
  :image="movie.poster_path" 
  id="Show-btn" 
  @click.native="$bvModal.show('modal3'), chooseId=movie.id"
  @mouseover.native="movie.mouse_over=true"
  @mouseout.native="movie.mouse_over=false"
  :class="{borderMouse: movie.mouse_over}"
  >
    
    </vueper-slide>           
  
  </vueper-slides>
  </div>

  <b-modal id="modal3" centered size="lg" hide-header-close>
      <template #modal-title>영화설명</template>
      <div class="d-block">
        <div align='middle'>
        <iframe 
      width="600" 
      height="400" 
      :src="videoUrl" 
      title="YouTube video player" 
      frameborder="0" 
      allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
      allowfullscreen></iframe>
        </div>
        <div align="left">
          <h3><b>{{ chooseMovie.title }}</b></h3>
          <br>
          <div>
            <h4>Overview</h4>
           <br>
           <div>{{ chooseMovie.overview }}</div>
          <br>
          <div><b>개봉일</b> : {{ chooseMovie.release_date }}</div>
          <br>
          <div><b>상영시간</b> : {{ chooseMovie.runtime }}분</div>
          <br>
          <div>
          <span><b>장르</b>:</span>
          <sapn v-for='(genre,i) in chooseMovie.genres' :key='i'> {{ genre.name }}</sapn>
          </div>
          <br>

          <div align="right">
            <button  v-if="!zzim" @click="onClick" >찜하기</button>
            <button  v-if="zzim" @click="onClick" >찜 취소하기</button>
          </div>
          </div>
        </div>
      </div>  
      <template #modal-footer align="center">
        <div class="padding w-100">
          <vueper-slides
            class="no-shadow"
            :bullets="true"
            :arrows-outside="false"
            :bullets-outside="true"
            :visible-slides="3"
            slide-multiple
            :touchable="false"
            :gap="5"
            :slide-ratio="1/3">
            <vueper-slide v-for="(actor, i) in actors" :key="i">
              <template v-slot:content>
                <div align="center">
                  <div v-if="actor.profile_path">
                    <img :src="actor.profile_path" @click="[ actorId=actor.id , actorIdx=actor.index, actorSubscribe()]" v-bind:class="{borderRed: actor.subscribe}" alt="사진이 없습니다." width="85">
                  </div>
                  <div ><b>이름 : {{actor.name }}</b></div>
                  <div><b>배역 : {{actor.character }}</b></div>
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
import axios from 'axios'
import { VueperSlides, VueperSlide } from 'vueperslides'
import 'vueperslides/dist/vueperslides.css'

export default {
  name: 'GenreMovieAction',
  components: { 
    VueperSlides, 
    VueperSlide,
    
     },
  data () {
    return {
      movies: [],
      chooseId:'',
      chooseMovie:{},
      actors:{},
      zzim: false,
      video:'',
      videoKey:'',
      beforeclick:false,
      
  }
  },
  methods : {
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    mouseOn() {
      this.beforeclick = !this.beforeclick
    },
    actorSubscribe() {
      axios({
        method:'post',
        url:'http://127.0.0.1:8000/subscribe/actors/',
        data: {
          actor_id:this.actorId,
          actor_name: this.actors[this.actorIdx].name,
          profile_path : this.actors[this.actorIdx].profile_path,
          },
        headers : this.setToken()
      })
      .then((res)=>{
        console.log(res)
        if (res.data['subscribe']){
          this.actors[this.actorIdx]['subscribe'] = true
          }
        else {
          this.actors[this.actorIdx]['subscribe'] = false
        }
      })
      
    },
    getMovie () {
      axios ({
        method:'get',
        url: 'https://api.themoviedb.org/3/movie/popular?api_key=33b865b38e340385996befbfd40fadd0&language=ko-KR&page=2',
      })
      
      .then((response)=> {
        const tmp = response.data.results.filter((movie) => {
          return movie.genre_ids.some((genre_id)=>{
            return genre_id === 35
          })
        })

        this.movies = tmp.map(({title, popularity, genre_ids, poster_path, id}) => ({
          title, popularity, genre_ids, mouse_over: false,
          poster_path: `https://image.tmdb.org/t/p/original${poster_path}`,
          id
        }))
    })
    },

    onClick (){
      axios ({
        method : 'post',
        url: `http://127.0.0.1:8000/subscribe/movies/`,
        headers: this.setToken(),
        data :{
          movie_id : this.chooseMovie.id,
          movie_title : this.chooseMovie.title,
          poster_path : 'https://image.tmdb.org/t/p/original'+this.chooseMovie.poster_path,
        }
      })
      .then((res)=>{
        console.log(res)
        if (res.data['subscribe']) {
          this.zzim = true
        }
        else {
          this.zzim = false
        }
      })
  },
  
  },
  watch: {
    chooseId: function () {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/subscribe/movies/',
        headers: this.setToken()
      })
      .then((response) => {
        this.zzim = false
        for (const movie of response.data) {
          if (movie['movie_id']==this.chooseId) {
            this.zzim = true
          }
        }
      })

      axios({
        method: 'get',
        url: `https://api.themoviedb.org/3/movie/${this.chooseId}?api_key=33b865b38e340385996befbfd40fadd0&language=ko-KR`,
      })
      .then((response) => {
        const tmp = response.data
        console.log(tmp)
        this.chooseMovie = {
          id: tmp.id,
          title: tmp.title,
          runtime : tmp.runtime,
          overview : tmp.overview,
          genres : tmp.genres,
          release_date : tmp.release_date,
          poster_path : tmp.poster_path,
        }
      })
        axios({
          method: 'get',
          url: `https://api.themoviedb.org/3/movie/${this.chooseId}/credits?api_key=33b865b38e340385996befbfd40fadd0&language=ko-KR`,
        })
        .then((response) => {
          this.actors = response.data.cast.map(({name, character, profile_path,id},index) => ({
            name,character,id,subscribe:false,index,
            profile_path: `https://image.tmdb.org/t/p/original${profile_path}`
          }))
        })
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/subscribe/actors/',
        headers: this.setToken()
      })
      .then((response) => {
        for (const actor of this.actors) {
          console.log(response)
          if (response.data.some(function (a) { return actor.id === parseInt(a.actor_id) })) {
            actor.subscribe = true
          }
        }
      })

      axios.get(`https://api.themoviedb.org/3/movie/${this.chooseId}/videos?api_key=33b865b38e340385996befbfd40fadd0&language=ko-KR`)
          .then(response => {
            console.log(response)
            this.videoKey = response.data.results[0].key
            axios({
              method:'get',
              url :'https://www.googleapis.com/youtube/v3/search',
              params:{
                q:this.videoKey,
                part:'snippet',
                key: 'AIzaSyBxQ6qvaLLOfSrr_e0nHwPTMustGYXWmr8',
                type:'video',
              }
            })
            .then(res=>{
              console.log(res)
              this.video = res.data.items[0].id.videoId
            })
            .catch(error=>{
              console.log(error)
            })
          })
          .catch(err => {
            console.log(err)
          })
      
    },  
  },
  computed:{
    videoUrl() {
      const baseURL = 'https://www.youtube.com/embed/'
      return baseURL + this.video
    },

  },  
  
  created () {
    
    return this.getMovie()
  }
 

}
</script>

<style scoped>

.black {
  background-color: black;

}
div p {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  width: 400px;
  height: 100px;
}
.borderRed {
  border:3px solid #1cff07;
}
.borderMouse {
  border:3px solid white;
}
.vueperslides--fixed-height { height: 400px; width:100%; padding-right: 50px; padding-left: 50px;}
</style>