<template>
  <div id="wrapper" class="home">
    <MovieListComp v-if="token"/>
    <SignUpComp v-if="token === ''"/>
  </div>
</template>

<script>
import MovieListComp from '@/components/MovieListComp.vue'
import SignUpComp from '@/components/SignUpComp'

export default {
  name: 'HomeView',
  components: {
    MovieListComp,
    SignUpComp,
  },
  computed: {
    token() {
      return this.$store.state.token
    },
  }
}
</script>

<style lang="css" scoped>
.home{
  flex: 1;
  height: 100%;
  background-color: rgb(34, 34, 34);
}
</style>