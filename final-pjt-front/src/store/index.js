import axios from "axios";
import Vue from "vue";
import Vuex from "vuex";
import vueMoment from "vue-moment";
import swal from 'sweetalert';
Vue.use(vueMoment);
Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    token: '',
    userinfo: '',
    API_URL: "http://localhost:8000/",
    movies: [],  

  },
  mutations: {
    CHANGE_TOKEN(state, newToken) {
      state.token = newToken;
    },
    CHANGE_USERINFO(state, newUserinfo) {
      state.userinfo = newUserinfo
    },
    // CHANGE_PROFILEIMAGE(state, newUsername) {
    //   state.username = newUsername
    // },
  },
  actions: {
    
    async login(context, userdata) {
      console.log(context.state.token)
      console.log(context.state.userinfo)
      try {
        // 로그인하고 토큰 저장하기
        const response = await axios.post(
          context.state.API_URL + "accounts/login/",
          userdata
        );
        if (response.data) {
          context.commit("CHANGE_TOKEN", response.data.key);
          // this.getUserInfo()
          console.log(context.state.token)
        }
        // 현재 토큰으로 user_pk 받기 
        if (context.state.token) {
          const getuser = await axios({
            method: 'get',
            url: `${context.state.API_URL}accounts/user/`,
            headers: {
              Authorization: `Token ${context.state.token}`
            }
          })
          console.log(getuser.data)
          // 찾은 user_pk로 userprofiledetail 받기
          if (getuser.data) {
            const userinfo = await axios({
              method: 'get',
              url: `${context.state.API_URL}api/v1/profile/${getuser.data.pk}/`,
              headers: {
                Authorization: `Token ${context.state.token}`
              },
            })
            if (userinfo.data) {
              context.commit("CHANGE_USERINFO", userinfo.data)
              context.state.userinfo = userinfo.data
              console.log(context.state.userinfo)
            }
          }
        }
        return true;
      } catch (error) {
        console.log(error);
        return false;
      }
    },
    async getuserinfo(context) {
      const userinfo = await axios({
        method: 'get',
        url: `${context.state.API_URL}api/v1/profile/${context.state.userinfo.id}/`,
        headers: {
          Authorization: `Token ${context.state.token}`
        },
      })
      if (userinfo.data) {
        context.commit("CHANGE_USERINFO", userinfo.data)
        context.state.userinfo = userinfo.data
      }
    },
    async signup(context, userdata) {
      try {
        const response = await axios({
          method: "post",
          url: `${context.state.API_URL}accounts/signup/`,
          data: userdata,
          headers: {
            "Content-Type": 'application/json',
          }
        });
        if (response.data) {
          swal('가입 성공!', '로그인하세요', 'success')
          .then(function() {
            location.href = 'http://localhost:8080/login/'
          })
        }
      } catch (err) {
        console.log(err)
        if (err) {
          swal('가입 실패!', '다른 ID나 닉네임을 사용하세요.', 'error')
          .then(function() {
            location.href = 'http://localhost:8080/signup/'
          })
        }
      }
    },
    logout(context, deletedToken) {
      context.commit("CHANGE_TOKEN", deletedToken)
      context.commit("CHANGE_USERINFO", deletedToken)
    },
    async searchInput(context, userInput) {
      try {
        const response = await axios({
          method: 'get',
          url: 'http://localhost:8000/api/v1/movies/',
          headers: {
            Authorization: `Token ${context.state.token}`
          },
        })
        if (response.data) {
          context.state.movies = []
          for(let i = 0; i<response.data.length; i++) {
            if(response.data[i].title.includes(userInput)) {
              context.state.movies.push(response.data[i])
            }
          } 
        }
      } catch(err) {
        console.log(err)
      }
    },
  },
});