<template>
  <div id="app">
    <div id="nav" class="navbar sticky-top navbar-light">
      <span v-if="isLogin">
          <router-link class="mx-3" :to="{ name: 'Home' }"><b class="my-tc">Home</b></router-link> 
          <router-link class="mx-3" :to="{ name: 'MyPage' }"><b class="my-tc">MyPage</b></router-link> 
          <router-link class="mx-3" :to="{ name: 'Community' }"><b class="my-tc">Community</b></router-link> 
          <router-link class="logout" @click.native="logout" to="#"><b class="my-tc">Logout</b></router-link>
      </span>
      <span v-else>
        <router-link :to="{ name: 'SignUp' }">Signup</router-link> |
        <router-link :to="{ name: 'Login' }">Login</router-link>
      </span>
    </div>
    <router-view @login="isLogin = true"/>
    <footer>
      <div class="footer">
      </div>
    </footer>
  </div>
</template>

<script>
export default {
  name: 'App',
  data: function () {
    return {
      isLogin: false,
    }
  },
  methods: {
    logout: function () {
      this.isLogin = false
      localStorage.removeItem('jwt')
      this.$router.push({ name: 'Login' })
    }
  },
  created: function () {
    const token = localStorage.getItem('jwt')
    if (token) {
      this.isLogin = true
    }
    else {
      this.$router.push({ name: 'Login' })
    }

    
  }
}
</script>
<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  background-color: rgb(15, 15, 22);
}

#nav {
  padding: 30px;
  background-color: rgb(24, 28, 43);
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}

.my-tc {
  color:rgb(131, 131, 185)
}
.footer {
  height: 300px;
}
.logout {
  position: absolute;
  right: 50px;
}
</style>
