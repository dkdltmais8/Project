<template>
  <div>
    <h1>게시물 작성</h1>
    <div class="container">
      <div class="row">
        <div class="col-1"></div>
        <div class="col-10 bg-light p-5" align="left">
          <b-form @submit="onSubmit" align="left">
            <p>제목</p>
            <b-form-input maxlength='20' v-model="form.title" placeholder="Enter title" required />
            <hr>
            <p>내용</p>
            <b-form-textarea v-model="form.content" placeholder="Enter something..." rows="15" max-rows="10" required />
            <p></p>
            <b-button type="submit" variant="primary">확인</b-button>
            <b-button @click="onback" variant="danger">취소</b-button>
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
  name: 'WriteReview',
  data: function () {
    return {
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
        method: 'post',
        url: 'http://127.0.0.1:8000/community/',
        data: this.form,
        headers: this.setToken()
      })
      .then((response) => {
        console.log(response.data)
      })
      this.$router.push({ name: 'Community' })
    },
    onback: function () {
      this.$router.push({ name: 'Community' })
    }
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