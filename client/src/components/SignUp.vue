<template>
  <div>
    <h1 class="my-tc">Signup</h1>


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
            <p>비밀번호 확인</p>
            <b-form-input type="password" v-model="credentials.passwordConfirmation" required />
            <p></p>
            <b-button @click="signup" variant="primary">회원가입</b-button>
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
  name: 'Signup',
  data: function () {
    return {
      credentials: {
        username: null,
        password: null,
        passwordConfirmation: null,
      }
    }
  },
  methods: {
    signup: function () {
      axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/users/signup/',
        data: this.credentials,
      })
      .then(() => {
        this.$router.push({ name: 'Login' })
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