<template>
  <div class="margin-x">
    <b-container class="bv-example-row">
      <b-row>
        <b-col cols="8" align="left">
          <hr>
          <div>
            <h2 class="my-tc bg-myColor"><p>오늘 구독한 배우</p></h2>
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
              <vueper-slide v-for="(actor, i) in newActors" :key="i">
                <template v-slot:content>
                  <div align="center">
                    <p><img :src="actor.profile_path" alt="img" height="150"></p>
                    <div class="text-wrap fs-6 actor-name">{{ actor.actor_name }}</div>
                  </div>
                </template>
              </vueper-slide>
            </vueper-slides>
          </div>
          <hr>
          <div>
            <h2 class="my-tc"><p>나의 배우들</p></h2>
            <vueper-slides
              class="no-shadow br"
              :style="'background-color: rgb(15, 15, 15)'"
              :touchable="false"
              :bullets="false"
              :visible-slides="5"
              slide-multiple
              :gap="3"
              :slide-ratio="1 / 4">
              <vueper-slide v-for="(actor, i) in oldActors" :key="i">
                <template v-slot:content>
                  <div align="center" class="fs-small">
                    <p><img :src="actor.profile_path" alt="img" width="100"></p>
                    <div class="text-wrap fs-6 actor-name">{{ actor.actor_name }}</div>
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
  name: "MyActors",
  components: {
    VueperSlides, VueperSlide,
  },
  props: {
    actors: {
      type: Array,
    }
  },
  data: function () {
    return {
      Month: ['', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
      newActors: [],
      oldActors: [],
    }
  },
  methods: {
    divideActors: function () {
      const today = new Date()
      const date = String(today).split(" ")
      this.newActors = this.actors.filter((actor) => {
        const subscribeAt = actor.created_at.split(" ")
        const subscribeDate = subscribeAt[0].split("-")
        if (parseInt(date[2])===parseInt(subscribeDate[2]) && date[1]===this.Month[parseInt(subscribeDate[1])] && parseInt(date[3])===parseInt(subscribeDate[0]) ){
          return true
        }
        this.oldActors.push(actor)
        return false
      })
      this.newActors.sort(function (a, b) {
        if (b.created_at > a.created_at) return 1
        else return -1
      })
    }
  },
  watch: {
    actors: function () {
      this.divideActors()
    }
  },
  created: function () {
      this.divideActors()
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