<template>
  <div>
    <b-container class="movie-card" align-v="center" fluid="lg">
      <b-card no-body class="overflow-hidden movie-card-detail">
        <b-row no-gutters>
          <b-col md="6">
            <b-card-img :src="movie.poster_path" alt="Image" class="rounded-0"></b-card-img>
          </b-col>
          <b-col md="6">
            <b-card-body :title="movie.title">
              <b-card-text>
                <div>
                  개봉일 : {{ movie.release_date}}
                </div>
                <div>
                  평점 : {{ movie.vote_average }}
                </div>
                <div class="thumb-icon">
                  <b-icon v-if="userLikeMovies.includes(movieId)" @click="likeMovie" icon="hand-thumbs-up-fill" scale="1.5"/>
                  <span v-if="userLikeMovies.includes(movieId)" class="likes-length">{{ movie.like_users?.length }}</span> 
                  <b-icon v-if="!userLikeMovies.includes(movieId)" @click="likeMovie" icon="hand-thumbs-up" scale="1.5"/>
                  <span v-if="!userLikeMovies.includes(movieId)" class="likes-length">{{ movie.like_users?.length }}</span> 
                  <b-icon icon="chat-dots" scale="1.5" class="reviews-icon"/>
                  <span class="reviews-length">{{ movie.reviews_count }}</span> 
                </div>
                <div v-if="movie.overview" class="overview">
                  {{ overview }}
                </div>
              </b-card-text>
            </b-card-body>
          </b-col>
        </b-row>
      </b-card>
    </b-container>
    <h4 class="review-text">리뷰</h4>
    <ReviewCreateComp class="review-create" :movieId="movieId" @emit="getMovieDetail"/>
    <div class="review-list-wrapper">
      <ReviewItemComp 
        class="review-item" 
        v-for="review in reviews" 
        :key="review.id" 
        :review="review"
        @emit="getMovieDetail"
      />
    </div>

  </div>
</template>

<script>
import axios from 'axios'
import ReviewItemComp from '@/components/ReviewItemComp.vue'
import ReviewCreateComp from '@/components/ReviewCreateComp.vue'

export default {
  name: 'MovieDetailView',
  components: {
    ReviewItemComp,
    ReviewCreateComp,
  },
  data() {
    return {
      movie: [],
    }
  },
  computed: {
    reviews () {
      return this.movie.reviews
    },
    movieId() {
      return this.movie.id
    },
    userLikeMovies() {
      return this.$store.state.userinfo.like_movies
    },
    overview() {
      return this.movie.overview.substring(440, 0) + '...'
    },
    movieLikeUsersNum() {
      return this.movie.like_users.length
    }
  },
  created() {
    this.getMovieDetail()
  },
  methods: {
    async getMovieDetail() {
      try {
        const response = await axios({
          method: 'get',
          url: `${this.$store.state.API_URL}api/v1/movies/${this.$route.params.id}/`,
          headers: {
            Authorization: `Token ${this.$store.state.token}`
          },
        })
        if (response.data) {
          console.log(response.data)
          this.movie = response.data
        }
      } catch (error) {
        console.log(error)
      }
    },
    async likeMovie() {
      try {
        const response = await axios({
          method: 'post',
          url: `${this.$store.state.API_URL}api/v2/${this.$route.params.id}/like_movie/`,
          headers: {
            Authorization: `Token ${this.$store.state.token}`
          },
        })
        if (response.data) {
          this.$store.dispatch('getuserinfo')
          this.getMovieDetail()
        }
      } catch (error) {
        console.log(error)
      }
    }

    
  }
}
</script>

<style scoped>
  .movie-card {
    color: rgb(58, 58, 59);
  }
  .movie-card-detail {
    background-color: white;
    border: 1px solid rgb(102, 102, 102)
  }
  .likes-length {
    margin-left: 3%;
  }
  .reviews-icon {
    margin-left: 6%;
  }
  .reviews-length {
    margin-left: 3%;
  }
  .review-text {
    margin-top: 15px;
    margin-left: 15px;

  }
  .review-list-wrapper {
    background-color: rgb(136, 136, 138);
    border: 1px solid rgb(87, 87, 90);
    border-radius: 6px;
    padding: 13px;
    padding-bottom: 13px;
  }
  .review-create {
    margin: 15px;
  }
  .thumb-icon {
    margin-top: 20px;
  }
  .overview {
    margin-top: 20px;
  }
  .review-item:hover {
    background-color: rgba(100, 98, 98, 0.6);
  }
</style>