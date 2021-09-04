<template>
  <div>
    <h1 class="my-tc">Login</h1>

    <div class="container">
      <div class="row">
        <div class="col-3"></div>
        <div class="col-6 bg-light p-5" align="left">
          <b-form align="left">
            <p>아이디</p>
            <b-form-input v-model="credentials.username" required />
            <hr>
            <p>비밀번호</p>
            <b-form-input type="password" v-model="credentials.password" required />
            <p></p>
            <b-button @click="login" variant="primary">로그인</b-button>
          </b-form>
        </div>
        <div class="col-3"></div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'


export default {
  name: 'Login',
  data: function () {
    return {
      credentials: {
        username: null,
        password: null,
      }
    }
  },
  methods: {
    login: function () {
      axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/users/api-token-auth/',
        data: this.credentials,
      })
      .then(res => {
        console.log(res)
        localStorage.setItem('jwt', res.data.token)
        this.$emit('login')
        this.$router.push({ name: 'Home' })
      })
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