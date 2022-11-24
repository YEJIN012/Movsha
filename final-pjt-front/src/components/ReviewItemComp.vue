<template>
  <div class="review-text">
    <b-container>
      <b-row align-h="between">
        <b-col cols="3">
          <span v-if="review.user.profile_image">
            <img class="profile-img"  @click="goToReviewDetail" :src="profileImageOfReview" height="25">
          </span>
          <span v-else>
            <img class="profile-img"  @click="goToReviewDetail" src="@/assets/images/anonymoususer.jpg" height="25">
          </span>
          &nbsp;
          <span @click="goToReviewDetail" class="review-nickname">
            {{ review.user.nickname }}
          </span>
        </b-col>
        <b-col cols="5">
          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
          <span @click="goToReviewDetail" class="review-title">
            {{ review.title }}
          </span>
        </b-col>
        <b-col cols="3">
          <span @click="goToReviewDetail" class="review-createdate">
            {{ review.created_at|moment('YYYY-MM-DD HH:mm') }}
          </span>
        </b-col>
        <b-col cols="1">
          <span class="like-btn">
            <b-icon v-if="userLikeReviews.includes(reviewId)" @click="likeReview" icon="hand-thumbs-up-fill"></b-icon>
            <b-icon v-if="!userLikeReviews.includes(reviewId)" @click="likeReview" icon="hand-thumbs-up"></b-icon>
          </span>
        </b-col>
      </b-row>
    </b-container>



  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'ReviewItemComp',
  props: ['review',],
  data() {
    return {
      reviewId: this.review.id,
    }
  },
  // created() {
  //   this.userLikeReviews
  // },
  computed: {
    userLikeReviews() {
      return this.$store.state.userinfo.like_reviews
    },
    profileImageOfReview() {
      return `http://localhost:8000${this.review.user.profile_image}`
    },
  },
  methods: {
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
          console.log(response.data)
          this.$store.dispatch('getuserinfo')
        }
      } catch (error) {
        console.log(error)
      }
    },
    goToReviewDetail() {
      console.log('clicked')
      console.log(this.reviewId)
      this.$router.push({ name: 'review', params: { id: this.reviewId } })
    }
  }
}
</script>

<style scoped>
  .review-text {
    margin-top: 8px;
    margin-bottom: 8px;
  }
  .review-text:hover {
    background-color: rgb(107, 104, 104);
  }
  .profile-img {
    border: 1px solid rgb(129, 129, 129);
    border-radius: 10px;
    margin-left: 7px;
  }
  .like-btn {
    margin-right: 5px;
  }
</style>