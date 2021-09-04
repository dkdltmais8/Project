<template>
  <div>
    <h1 class="m-100">게시물 디테일</h1>
    <div class="container">
      <div class="row">
        <div class="col-1"></div>
        <div class="col-10 bg-light p-5" align="left">
          <b-button class="right mx-4" @click="back" variant="secondary">목록</b-button>
          <b-button class="right" @click="onUpdate" variant="primary">수정하기</b-button>
          <h1>{{ review.title }}</h1>
          <div class="left">{{ review.user }}</div>
          <div align="right">{{ review.created_at }}</div>
          <hr>
          <div class="min-h">{{ review.content }}</div>
          <form @submit.prevent="onSubmit" align="left">
            <input class="width" v-model="content" placeholder="댓글을 작성하세요" required />
            <b-button type="submit" variant="primary">확인</b-button>
            <ul v-for="(comment, i) in comments" :key="i">
              <li><b>{{ comment.user }}</b></li>
              <button type="button" @click="comment_pk=comment.id, ondelete()" class="btn-sm btn-outline-dark right">x</button>
              <div class="fs-4">{{ comment.content }}</div>
              <li class="text-secondary"><small>{{ comment.created_at }}</small></li>
              <hr>
            </ul>
          </form>
        </div>
        <div class="col-1"></div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from'axios'
export default {
  name: 'ReviewDetail',
  data: function () {
    return {
      iswriter: false,
      review_pk: '',
      review: {},
      comments: [],
      content: '',
      comment_pk: '',
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
    getReview: function () {
      this.review_pk = this.$route.params.review_pk
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/community/${this.review_pk}/`,
        headers: this.setToken()
      })
      .then((response) => {
        this.review = response.data
      })
    },
    getComments: function () {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/community/${this.review_pk}/comments/`,
        headers: this.setToken()
      })
      .then((response) => {
        this.comments = response.data
      })
      console.log(this.comments);
    },
    onSubmit: function () {
      this.review_pk = this.$route.params.review_pk
      axios({
        method: 'post',
        url: `http://127.0.0.1:8000/community/${this.review_pk}/comments/`,
        data: {
          content: this.content,
          },
        headers: this.setToken()
      })
      .then(() => {
        this.comments = this.getComments()
        this.content = ''
      })
    },
    ondelete: function () {
      axios({
        method: 'DELETE',
        url: `http://127.0.0.1:8000/community/${this.review_pk}/comments/${this.comment_pk}/`,
        headers: this.setToken()
      })
      this.comments = this.getComments()
    },
    onUpdate: function () {
      this.$router.push({ name: 'UpdateReview', params: {review_pk: this.review_pk}})
    },
    back: function () {
      this.$router.push({ name: 'Community',})
    }
  },
  created: function () {
    this.getReview()
    this.getComments()
  }
}
</script>

<style scoped>
.m-100 {
  margin: 100px;
}
.left {
  float: left;
}
.right {
  float: right;
}
.min-h {
  min-height: 400px;
  padding: 50px 0 50px 0;
}
.width {
  left: 0px;
  width: 85%;
  height: 40px;
  margin: 20px 20px 20px 0;
}
ul {
  list-style: none;
  width: 92%;
}
li {
  height: 20px;
}

</style>