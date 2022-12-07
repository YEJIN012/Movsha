<template>
    <b-carousel-slide
      :img-src="poster_path"
      class="carousel"
    > 
    <div class="card">
      <b-row
      @click="goToDetail"
      
      style="cursor:pointer"
      >
          <b-col v-if="large_width" xl="3" align-self="center">
            <img :src="poster_path" alt="Image" class="card_img">
          </b-col>
          <b-col xl="1"><br></b-col>
          <b-col xl="8" class="text-center">
              <h5>
                {{ title }}
              </h5>
                평점: {{ vote_average }}
                <br>
                <br>
              <div
              v-if="movie.overview">
                {{ overview }}
              </div>
          </b-col>
      </b-row>
    </div>
    </b-carousel-slide>
</template>



<script>
export default {
    name: 'PopularItemComp',
    data() {
      return {
        slide: 0,
        sliding: null,
        windowWidth: window.innerWidth,
      }
    },
    props: ['movie',],
    mounted() {
      window.addEventListener('resize', () => {
        this.windowWidth = window.innerWidth
      })
    },
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
      },
      large_width() {
        return this.windowWidth >= 1200
      }
    },
    
    methods: {
      goToDetail() {
        this.$router.push({ name: 'movie', params:{id:this.movie.id} })
      },
    }
}
</script>



<style scoped>
  .carousel {
    width: 100%;
    height: 40vh;
    padding-bottom: 100px;
  }
  .card-img-wrapper {
    display:flex;
  }
  .card_img {
    scale: 100%;
    max-width: 160px;
    height: 25vh;
    border-radius: 8px;
    align-items: center;
  }
  .card {
    height: 30vh;
    background-color: rgba(0,0,0,0.8);
    overflow: hidden;
    padding: 2vh;
    padding-bottom: 2vh;
    display: grid;
    align-items: center;
  }
  .text-center {
    margin: auto;
  }

</style>