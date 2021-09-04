<template>
  <div>
    <input type="text" class="margin-50" @input="makeWord" placeholder=" 배우의 이름을 검색하세요." size=40>
    <PersonList :my-word="myWord" />
  </div>
</template>

<script>
import PersonList from '@/components/PersonList'

export default {
  name: 'Search',
  components: {
    PersonList,
  },
  data: function () {
    return {
      myWord: "",
      page: 1,
    }
  },
  methods: {
    makeWord: function (event) {
      this.myWord = event.target.value
    },
  },
}
</script>

<style scoped>
.margin-50 {
  margin-top: 50px;
  line-height: 30px
}
</style>