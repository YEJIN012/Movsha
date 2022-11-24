<template>
  <div>
    <h3>좋아요한 영화</h3>
    <div class="likemovies-item">
      <LikeMoviesItemComp
        v-for="(likemovie, idx) in like_movies"
        :key="idx"
        :likemovie_pk="likemovie"
      />
    </div>
  </div>
</template>

<script>
import LikeMoviesItemComp from '@/components/LikeMoviesItemComp.vue'

export default {
    name: 'LikeMoviesComp',
    components: {
      LikeMoviesItemComp,
    },
    data() {
      return {
      }
    },
    props: ['like_movies'],
}
</script>

<style scoped>
  .likemovies-item {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr 1fr 1fr;
  }

</style>