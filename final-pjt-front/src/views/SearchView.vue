<template>
  <div>
    <div class="search-item" v-if="searchMovies !== 0">
      <b-row class="row-gap">
        <SearchItemComp
          v-for="(movie, idx) in movies"
          :key="idx"
          :movie="movie"
        />
      </b-row>
    </div>
    <div v-else>
      <NoPageComp/>
    </div>
  </div>
</template>

<script>
import SearchItemComp from '@/components/SearchItemComp.vue';
import NoPageComp from '@/components/NoPageComp.vue';

export default {
  name: 'SearchView',
  components: {
    SearchItemComp,
    NoPageComp,
  },
  computed: {
    movies() {
      return this.$store.state.movies
    },
    searchMovies() {
      return this.$store.state.movies.length
    }
  },
}
</script>

<style scoped>
  .search-item {
    column-gap: 60px;
    margin-top: 40px;
  }
  .row-gap {
    row-gap: 50px;
  }
</style>