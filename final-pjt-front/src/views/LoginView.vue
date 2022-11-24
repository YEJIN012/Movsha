<template>
  <div class="login-wrapper">
    <h2>로그인</h2>

    <b-form @submit.prevent="login" class="login-form">
      <b-form-group class="login-id">
        <b-form-input
          id="input-1"
          v-model="form.userid"
          placeholder="ID를 입력하세요"
          required
        ></b-form-input>
      </b-form-group>

      <b-form-group class="login-pw">
        <b-form-input
          id="input-2"
          v-model="form.userpw"
          type="password"
          placeholder="비밀번호를 입력하세요"
          required
        ></b-form-input>
      </b-form-group>

      <b-button class="submit-btn" type="submit" variant="primary">Submit</b-button>


    </b-form>
  </div>
</template>

<script>
import swal from 'sweetalert'

export default {
  name: "LoginView",
  data() {
    return {
      form: {
        userid: "",
        userpw: "",
      },
      URL: "http://localhost:8000/",
      TOKEN: "",
    };
  },
  methods: {
    async login() {
      try {
        const flag = await this.$store.dispatch("login", {
        username: this.form.userid,
        password: this.form.userpw,
        });
        console.log(flag)
        if (flag === false) {
          swal('로그인 실패!', '가입된 정보가 없습니다.', 'error')
        } else {
          this.$router.push({ name : 'home' })
        }
      } catch (error) {
        console.log(error)
      }
      
    },
  },
}
</script>

<style scoped>
.login-wrapper {
  border: 1px solid rgb(95, 96, 100);
  border-radius: 10px;
  background-color: rgb(61, 61, 63);
  margin-left: 20%;
  margin-right: 20%;
  margin-top: 10%;
  padding: 5%;
  padding-right: 10%;
  padding-left: 10%;
}
.login-form {
  margin-top: 10%;
}
.login-pw {
  margin-top: 30px;
}
.submit-btn {
  margin-top: 15px;
  margin-left: 77%;
}
</style>