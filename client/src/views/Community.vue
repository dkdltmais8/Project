<template>
  <div class="container">
    <h1 class="my-tc">게시글 목록</h1>
    <div class="row">
      <div class="col-1"></div>
      <div class="col-10">
        <b-button @click="writeReview" variant="light">글쓰기</b-button>
        <table class="table bg-light">
          <thead class="table-primary">
            <tr>
              <th scope="col">#</th>
              <th scope="col">글쓴이</th>
              <th scope="col">제목</th>
              <th scope="col">조회수</th>
            </tr>
          </thead>
          <tbody v-for="(article, i) in articles" :key="i">
            <tr class="bb" :class="{black:article.mouseOn}">
              <th scope="row">{{ article.id }}</th>
              <td>{{ article.user }}</td>
              <td class="left overflow-hidden title " 
              @click="review_pk=article.id, reviewDetail()"
              @mouseover="article.mouseOn=true" 
              @mouseout="article.mouseOn=false" 
              >
              {{ article.title }} 
                <b>({{ article.comment_cnt }})</b>
              </td>
              <td>{{ article.view_cnt }}</td>
            </tr>
          </tbody>
        </table>
      </div>
      <div class="col-1"></div>
    </div>
  </div>
</template>

<script>
import axios from'axios'
export default {
  name: 'Community',
  data: function () {
    return {
      articles: [],
      review_pk: '',
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
    getArticles: function () {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/community/',
        headers: this.setToken()
      })
      .then((response) => {
        this.articles = response.data.map(({user,title,id,comment_cnt,view_cnt})=>({ 
          id,user,title,comment_cnt,view_cnt,mouseOn:false
        
        }))
        console.log(this.articles);
      })
    },
    writeReview: function () {
      this.$router.push({ name: 'WriteReview' })
    },
    reviewDetail: function () {
      this.$router.push({ name: 'ReviewDetail', params: {review_pk: this.review_pk}})
    },
    selectArticle() {
      this.mouseOn = !this.mouseOn
    }
  },
  mounted: function () {
    this.getArticles()
  }
}
</script>

<style scoped>
h1 {
  margin: 100px;
}
button {
  float: right;
  margin: 10px;
}
.left {
  text-align: left;
}
.title {
  width:600px;
  overflow:hidden;
  text-overflow:ellipsis;
}
.black {
  border : 2px solid rgb(131, 131, 185)
}
.bb {
  box-sizing: border-box;
}
</style>