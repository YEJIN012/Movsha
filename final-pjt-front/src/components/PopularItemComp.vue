<template>
  <div>
    
    <b-carousel-slide
      :img-src="poster_path"
      class="carousel_back"
    >
      <b-card @click="goToDetail" class="overflow-hidden">
        <b-row no-gutters>
          <b-col md="5" class="card-image-wrapper">
            <img :src="poster_path"  alt="Image" class="card_img" height="254">
          </b-col>
          <b-col md="6">
            <b-card-body :title="title">
              <b-card-text >
                평점: {{ vote_average }}
              </b-card-text>
              <b-card-text class="mt-2" v-if="movie.overview">
                {{ overview }}
              </b-card-text>
            </b-card-body>
          </b-col>
        </b-row>
      </b-card>
    </b-carousel-slide>
  </div>
</template>



<script>
export default {
    name: 'PopularItemComp',
    data() {
      return {
        slide: 0,
        sliding: null
      }
    },
    props: ['movie',],
    computed: {
      poster_path() {
        return this.movie.poster_path
      },
      title() {
        return this.movie.title
      },
      vote_average() {
        return this.movie.vote_average
      },
      like_users() {
        return this.movie.like_users.length
      },
      overview() {
        return this.movie.overview.substring(50, 0) + '...'
      }
    },
    methods: {
      goToDetail() {
        console.log(this.movie.id)
        this.$router.push({ name: 'movie', params:{id:this.movie.id} })
      },
    }
}
</script>



<style scoped>
  .carousel_back {
    width: 100%;
    height: 40vh;
  }
  .card-img-wrapper {
    display:flex;
  }
  .card_img {
    /* height: 252px;
    width: 240px; */
    border-radius: 8px;
    justify-content: center;
    align-items: center;
  }
  .card {
    height: 30vh;
    background-color: rgba(0,0,0,0.8);

  }

</style>