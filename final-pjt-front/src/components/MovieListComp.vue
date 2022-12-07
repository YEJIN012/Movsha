<template>
  <div>
    <div class="recent-movies">
      <h3 class="recent-movies-text">Hot 최신 개봉작</h3>
      <b-carousel
        id="carousel-1"
        v-model="slide1"
        :interval="3000"
        controls
        indicators
        width="1024"
        height="480"
        background="#ababab"

        @sliding-start="onSlideStart"
        @sliding-end="onSlideEnd"
      >
        <PopularItemComp 
            v-for="(movie, index) in lastest_movies" 
            :key="index"
            :movie="movie"/>
      </b-carousel>
    </div>
    <div class="user-choice">
      <h3 class="user-choice-text">유저들의 선택</h3>
      <b-carousel
        id="carousel-1"
        v-model="slide2"
        :interval="3000"
        controls
        indicators
        width="1024"
        height="480"
        background="#ababab"
        @sliding-start="onSlideStart"
        @sliding-end="onSlideEnd"
      >
        <PopularItemComp 
            v-for="(movie, index) in mostlikes_movies" 
            :key="index"
            :movie="movie"/>
      </b-carousel>
    </div>
  </div>
  
</template>



<script>
import PopularItemComp from '@/components/PopularItemComp.vue'
import axios from 'axios'

export default {
    name: 'MovieListComp',
    components: {
        PopularItemComp,
    },
    data() {
      return {
        movies : [],
        lastest_movies : [],
        mostlikes_movies : [],
        slide1: 0,
        slide2: 0,
        sliding: null,
      }
    },
    created() {
      this.getMovieList()
    },
    methods: {
      lastestMovies() {
        let newlist = this.movies.sort((a,b)=>{
          return new Date(b.release_date) - new Date(a.release_date)
        })
        let newlist2 = newlist.slice(0,50)
        let newlist3 = newlist2.sort((a,b)=>{
          return b.vote_average - a.vote_average 
        })
        this.lastest_movies = newlist3.slice(0,10)
      },
      mostlikesMovies() {
        let newlist = this.movies.sort((a,b)=>{
          return b.like_users.length - a.like_users.length
        })
        this.mostlikes_movies = newlist.slice(0,10)
      },
      async getMovieList() {
        try {
          const response = await axios({
            method: 'get',
            url: `${this.$store.state.API_URL}api/v1/movies/`,
            headers: {
              Authorization: `Token ${this.$store.state.token}`
            },
          })
          if (response.data) {
            this.movies = response.data
            this.lastestMovies()
            this.mostlikesMovies()
          }
        } catch (error) {
          console.log(error)
        }
      },
      onSlideStart() {
        this.sliding = true
      },
      onSlideEnd() {
        this.sliding = false
      }
    }

  }
</script>



<style scoped>
  .recent-movies-text {
    margin-bottom: 3%;
  }
  .user-choice {
    margin-top: 5%;
    margin-bottom: 5%
  }
  .user-choice-text {
    margin-bottom: 3%;
  }
  .movie-item {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    row-gap: 50px;
    column-gap: 30px;
    margin-top: 40px;
    margin-left: 30px;
    margin-right: 30px;
  }

  .carousel-control-prev-icon,
  .carousel-control-next-icon {
    display: none;
  }
</style>