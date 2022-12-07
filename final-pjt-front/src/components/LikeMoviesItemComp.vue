<template>
  <div>
    <b-card
      no-body
      @click="goToDetail"
      style="cursor:pointer"
      >
      <img :src="likemovie.poster_path" alt="poster" height="200rem" width="133.33">
    </b-card>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  data() {
    return {
      likemovie: {},
    }
  },
  props: [
    'likemovie_pk',
  ],
  created() {
    this.getMovieDetail()
  },
  methods: {
    async getMovieDetail() {
      try {
        const response = await axios({
          method: 'get',
          url: `${this.$store.state.API_URL}api/v1/movies/${this.likemovie_pk}/`,
          headers: {
            Authorization: `Token ${this.$store.state.token}`
          },
        })
        if (response.data) {
          this.likemovie = response.data
        }
      } catch (error) {
        console.log(error)
      }
    },
    goToDetail() {
      // console.log(this.movie)
      this.$router.push({ name: 'movie', params: {id: this.likemovie_pk} })
    },
  }

}
</script>

<style scoped>
* {
  display: grid;
}

</style>