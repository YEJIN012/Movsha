<template>
  <div style="height:101px;">
    <nav class="nav-bar">
      <div class="signup-home" v-if="token === ''">
        <router-link to="/" class="home-router">
          <img class="signup-logo" src="@/assets/images/MovSha.png" id="logo">
        </router-link>
        <router-link to="/login" class="login-router"> 로그인 </router-link>
      </div>
      <div v-if="token" class="movie-home">
        <router-link to="/" class="home-router">
          <img class="moviehome-logo" src="@/assets/images/MovSha.png" id="logo">
        </router-link>
        <div class="right-menus">
          <router-link to="/recommend" class="recommend-router"
            >추천 영화</router-link
          >
          <b-input-group size="sm" class="search-router">
            <b-input-group-prepend is-text>
              <b-icon icon="search"></b-icon>
            </b-input-group-prepend>
            <b-form-input
              type="text"
              v-model="userInput"
              v-on:keyup.enter="searchInput"
              placeholder="영화 제목"
            ></b-form-input>
          </b-input-group>
          <b-dropdown
            split
            text="프로필"
            size="sm"
            class="m-2 profile-router"
            @click="goToProfile"
            toggle-text=""
          >
            <b-dropdown-item @click="logout" class="logout-router"
              >로그아웃</b-dropdown-item
            >
          </b-dropdown>
        </div>
      </div>
    </nav>
  </div>
</template>


<script>
export default {
  name: "HeaderComp",
  data() {
    return {
      userInput: null,
    };
  },
  computed: {
    token() {
      return this.$store.state.token;
    },
    userpk() {
      return this.$store.state.userinfo.id;
    },
  },
  methods: {
    searchInput() {
      this.$router
        .push({ name: "search", params: { userinput: this.userInput } })
        .catch(() => {});
      this.$store.dispatch("searchInput", this.userInput);
      this.userInput = null;
    },
    goToProfile() {
      this.$router.push({ name: "profile", params: { id: this.userpk } });
    },
    logout() {
      this.$store.dispatch("logout", "");
      this.$router.push({ name: "login" });
    },
  },
};
</script>


<style scoped>
.nav-bar {
  background-color: rgb(91, 91, 95);
  padding-top: 6px;
  padding-bottom: 6px;
}
.signup-home {
  display: flex;
  justify-content: space-between;
  padding-top: 8px;
  padding-bottom: 8px;
}
.signup-logo {
  margin-left: 90%;
  scale: 3;
}
.moviehome-logo {
  scale: 3;
  margin-left: 3.5%;
}
.login-router {
  text-decoration: none;
  justify-content: right;
  margin-right: 18px;
}
.movie-home {
  display: grid;
  grid-template-columns: 2fr 1fr;
  align-items: center;
}
.home-router {
  margin-left: 10px;
  text-decoration: none;
}
.right-menus {
  display: grid;
  align-items: center;
  grid-template-columns: 1fr 2fr 1fr;
}
.recommend-router {
  text-decoration: none;
}
.logout-router {
  justify-content: right;
  margin-right: 10px;
}
.search-router {
  width: 180px;
  margin-left: 30px;
}
a {
  text-decoration: none;
  color: white;
  transition: color 400ms ease-out 100ms;
}
a:hover {
  color: rgb(213, 213, 216);
}
#logo {
  height: 1rem;
}
</style>