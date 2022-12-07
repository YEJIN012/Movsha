<template>
  <div class="signup-wrapper">
    <h2>회원가입</h2>

    <b-form v-on:submit.prevent="signUp" class="signup-form">
      <b-form-group class="signup-id">
        <b-form-input
          v-model="form.username"
          placeholder="아이디"
          required
        ></b-form-input>
      </b-form-group>

      <b-form-group class="signup-nickname">
        <b-form-input
          v-model="form.nickname"
          placeholder="닉네임(10자 이하)"
          required
        ></b-form-input>
      </b-form-group>

      <b-form-group class="signup-pw1">
        <b-form-input
          v-model="form.password1"
          type="password"
          placeholder="비밀번호(8자 이상)"
          required
        ></b-form-input>
      </b-form-group>

      <b-form-group class="signup-pw2">
        <b-form-input
          v-model="form.password2"
          type="password"
          placeholder="비밀번호 재입력"
          required
        ></b-form-input>
      </b-form-group>

      <b-button class="float-right submit-btn" type="submit" variant="primary">Submit</b-button>


    </b-form>
  </div>
</template>

<script>
import swal from 'sweetalert'

export default {
  name: 'SignupView',
  data() {
    return {
      form: {
        username: null,
        nickname: null,
        password1: null,
        password2: null,
      }
    }
  },
  methods: {
    async signUp() {
      const username = this.form.username
      const nickname = this.form.nickname
      const password1 = this.form.password1
      const password2 = this.form.password2

      if (password1 !== password2) {
        swal('가입 실패!', '비밀번호가 같지 않습니다.', 'error')
        return
      }
      const data = {
        username,
        nickname,
        password1,
        password2,
      }
      await this.$store.dispatch('signup', data)
      this.$router.push({ name: 'home' })
    },
  }
}
</script>

<style scoped>
  .signup-wrapper {
    border: 1px solid rgb(95, 96, 100);
    border-radius: 10px;
    background-color: rgb(61, 61, 63);
    margin-left: 20%;
    margin-right: 20%;
    margin-top: 10%;
    padding: 5%;
    padding-bottom: 85px;
    padding-left: 10%;
    padding-right: 10%;
  }
  .signup-form {
    margin-top: 10%;
  }
  .signup-nickname {
    margin-top: 30px;
  }
  .signup-pw1 {
    margin-top: 30px;
  }
  .signup-pw2 {
    margin-top: 30px;
  }
  .submit-btn {
    margin-top: 15px;
  }
</style>