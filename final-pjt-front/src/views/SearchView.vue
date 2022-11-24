<template>
  <div>
    <div class="search-item" v-if="searchMovies !== 0">
      <SearchItemComp
        v-for="(movie, idx) in movies"
        :key="idx"
        :movie="movie"
      />
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
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    row-gap: 70px;
    column-gap: 60px;
    margin-top: 40px;
  }

</style>