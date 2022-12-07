<template>
  <div class="review-detail">
    <b-container align-v="center" fluid="lg">
      <b-card no-body class="overflow-hidden review-wrapper " img-right>
        <b-card-body>
          <b-row>
            <b-col cols="8">
              <b-card-text>
                <h5>
                {{ review.movie?.title }}
                </h5>
                <div>
                  {{ review.movie?.release_date }}
                </div>
                <hr>
                <b-media>
                    <span v-if="review.user?.profile_image">
                      <img
                      class="profile-image"
                      @click="goToUserProfile"
                      style="cursor:pointer"
                      :src="profileImageOfReview"
                      height="25">
                    </span>
                    <span v-else>
                      <img
                      class="profile-image"
                      @click="goToUserProfile"
                      style="cursor:pointer"
                      src="@/assets/images/anonymoususer.jpg"
                      height="25">
                    </span>
                    &nbsp;
                    <span
                    class="mt-0"
                    @click="goToUserProfile"
                    style="cursor:pointer">&nbsp;&nbsp;&nbsp;{{ review.user?.nickname }}</span>
                  <div class="tmp">
                    <div
                      class="star"
                      v-for="index in 5"
                      :key="index"
                    >
                      <span v-if="index <= review.rank"><b-icon icon="star-fill"/>&nbsp;</span>
                    </div>
                  </div>              
                  <p class="mt-3 mb-0">
                  {{ review.title }}
                  </p>
                  <p class="mt-1">
                    {{ review.content }}
                  </p>
                  <div v-if="userId !== reviewUserId" class="mt-4">
                    <b-button v-if="!userLikeReviews.includes(reviewId)" @click="likeReview" variant="outline-primary"><b-icon icon="hand-thumbs-up"/>좋아요</b-button>
                    <b-button v-if="userLikeReviews.includes(reviewId)" @click="likeReview" variant="primary"><b-icon icon="hand-thumbs-up"/>좋아요</b-button>
                  </div>
                  <div v-else>
                    <b-button @click="deleteReview" variant="outline-primary"><b-icon icon="trash"/>&nbsp;삭제</b-button>
                  </div>
                </b-media>        
              </b-card-text>
            </b-col>
            <b-col cols="4" v-if="large_width">
              <b-card-img
                :src="review.movie?.poster_path" alt="poster" img-right>
              </b-card-img>
            </b-col>
          </b-row>
        </b-card-body>
      </b-card>
    </b-container>
    
    
    <CommentCreateComp class="comment-create" :reviewId="reviewId" @emit="getReviewDetail"/>
    <div class="comment-list-wrapper">
      <CommentItemComp 
        class="comment-item"
        v-for="comment in review.comments"
        :key="comment?.id"
        :comment="comment"
        @emit="getReviewDetail"
      />
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import CommentItemComp from '@/components/CommentItemComp.vue'
import CommentCreateComp from '@/components/CommentCreateComp.vue'

export default {
  name: 'ReviewDetailView',
  data() {
    return {
      review: '',
      movieId: '',
      windowWidth: window.innerWidth,
    }
  },
  components: {
    CommentItemComp,
    CommentCreateComp,
  },
  mounted() {
      window.addEventListener('resize', () => {
        this.windowWidth = window.innerWidth
      })
  },
  created() {
    this.getReviewDetail()
  },
  computed: {
    profileImageOfReview() {
      return `http://localhost:8000${this.review.user.profile_image}`
    },
    userLikeReviews() {
      return this.$store.state.userinfo.like_reviews
    },
    reviewId() {
      return this.review?.id
    },
    reviewUserId() {
      return this.review.user?.id
    },
    userId() {
      return this.$store.state.userinfo.id
    },
    large_width() {
        return this.windowWidth >= 768
    },
  },
  methods: {
    async getReviewDetail() {
      try {
        const response = await axios({
          method: 'get',
          url: `${this.$store.state.API_URL}api/v1/reviews/${this.$route.params.id}/`,
          headers: {
            Authorization: `Token ${this.$store.state.token}`
          }
        })
        if (response.data) {
          this.review = response.data
          this.movieId = this.review.movie.id
        }
      } catch(err) {
        console.log(err)
      }
    },
    async deleteReview() {
      try {
        const response = await axios({
          method: 'delete',
          url: `${this.$store.state.API_URL}api/v1/reviews/${this.$route.params.id}/`,
          headers: {
            Authorization: `Token ${this.$store.state.token}`
          }
        })
        if (!response.data) {
          this.$router.push({ name: 'movie', params: { id: this.movieId }})
        }
      } catch(err) {
        console.log(err)
      }
    },
    async likeReview() {
      try {
        const response = await axios({
          method: 'post',
          url: `${this.$store.state.API_URL}api/v2/${this.reviewId}/like_review/`,
          headers: {
            Authorization: `Token ${this.$store.state.token}`
          },
        })
        if (response.data) {
          this.$store.dispatch('getuserinfo')
        }
      } catch (error) {
        console.log(error)
      }
    },
    goToUserProfile() {
      this.$router.push({ name: 'profile', params: {id: this.review.user.id }})
    },

  }
}
</script>

<style scoped>
/* .review-detail {
  margin-left: 10%;
  margin-right: 10%;
} */
.review-wrapper {
  margin: 25px;
  color: rgb(58, 58, 59);
}
.comments-count {
  margin-left: 5%;
}

.profile-image {
  border-radius: 10px;
}
.comment-text {
  margin-top: 15px;
  margin-left: 25px;
}
.comment-create {
  margin: 25px;
  margin-top: 13px;
}
.comment-list-wrapper {
  background-color: rgb(136, 136, 138);
  border: 1px solid rgb(87, 87, 90);
  border-radius: 6px;
  margin: 25px;
  padding: 8px;
}
.movie-poster {
  width: 80%;
}
.poster {
  display: flex;
  justify-content: right;
}
.tmp {
  display: flex;
}
</style>