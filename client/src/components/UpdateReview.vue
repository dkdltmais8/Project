<template>
  <div>
    <h1>게시물 수정</h1>
    <div class="container">
      <div class="row">
        <div class="col-1"></div>
        <div class="col-10 bg-light p-5" align="left">
          <b-form @submit="onSubmit" align="left">
            <p>제목</p>
            <b-form-input maxlength='20' v-model="form.title" value="review.title" placeholder="Enter title" required />
            <hr>
            <p>내용</p>
            <b-form-textarea v-model="form.content" placeholder="Enter something..." rows="15" max-rows="10" required />
            <p></p>
            <b-button type="submit" variant="primary">확인</b-button>
            <b-button @click="onDelete" variant="danger">글 삭제</b-button>
          </b-form>
        </div>
        <div class="col-1"></div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from'axios'
export default {
  name: 'UpdateReview',
  data: function () {
    return {
      review_pk: '',
      review: {},
      form: {
        title: '',
        content: '',
      }
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
    onSubmit: function () {
      axios({
        method: 'put',
        url: `http://127.0.0.1:8000/community/${this.review_pk}/update/`,
        data: this.form,
        headers: this.setToken()
      })
      this.$router.push({ name: 'ReviewDetail', params: {review_pk: this.review.id}})
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
        this.form.title = this.review.title
        this.form.content = this.review.content
      })
    },
    onDelete: function () {      
      axios({
        method: 'delete',
        url: `http://127.0.0.1:8000/community/${this.review_pk}/delete/`,
        headers: this.setToken()
      })
      this.$router.push({ name: 'Community',})
    }
  },
  created: function () {
    this.getReview()
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
</style>