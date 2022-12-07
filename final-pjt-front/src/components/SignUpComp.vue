<template>
  <div class="signup-comp">
    <img 
      src="@/assets/images/MovSha_shadow.png" 
      width="100%"
      style="margin-top:80px"
    >
    <h3>
      "무샤" 와 함께 영화를 나누세요
    </h3>
    <b-button
      size="lg"
      pill
      variant="primary"
      class="signup-btn"
      @click="goSignUp">
      회원가입
    </b-button>
  </div>
</template>

<script>
export default {
  name: 'SignUpComp',
  methods: {
    goSignUp() {
        this.$router.push( {name : 'signup'} )
    },
  }
}
</script>

<style scoped>
  .signup-comp {
    display: flex;
    flex-direction: column;
    justify-items: center;
    text-align: center;
  }
  h3 {
    margin-top: 30px;
  }
  .signup-btn {
    display: flex;
    margin-top: 5rem;
    margin-left: auto;
    margin-right: auto;
    padding-left: 4%;
    padding-right: 4%;
    padding-top: 1.3%;
    padding-bottom: 1.3%;
  }

</style>