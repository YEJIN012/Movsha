<template>
  <div>
    <b-container class="review-item">
      <b-row>
        <b-col md="10">
          <b-row
          @click="goToReviewDetail"
          style="cursor:pointer">
            <b-col md="3">
              <span v-if="review.user.profile_image">
                <img class="profile-img" :src="profileImageOfReview" height="25">
              </span>
              <span v-else>
                <img class="profile-img" src="@/assets/images/anonymoususer.jpg" height="25">
              </span>
              &nbsp;
              <span class="review-nickname">
                {{ review.user.nickname }}
              </span>
            </b-col>
            <b-col md="5">
              <span>
                {{ review.title }}
              </span>
            </b-col>
            <b-col md="4">
              <span class="review-createdate">
                {{ review.created_at|moment('YYYY-MM-DD HH:mm') }}
              </span>
            </b-col>
          </b-row>
        </b-col>
        
        <b-col md="2">
          <span class="like-btn">
            <b-icon v-if="userLikeReviews.includes(reviewId)" @click="likeReview" style="cursor:pointer" icon="hand-thumbs-up-fill"></b-icon>
            <b-icon v-if="!userLikeReviews.includes(reviewId)" @click="likeReview" style="cursor:pointer" icon="hand-thumbs-up"></b-icon>
          </span>
          <span>{{ likesOfReview }}</span>
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
  computed: {
    userLikeReviews() {
      return this.$store.state.userinfo.like_reviews
    },
    profileImageOfReview() {
      return `http://localhost:8000${this.review.user.profile_image}`
    },
    likesOfReview() {
      return this.review.like_users.length
    }
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
          // console.log(response.data)
          this.$store.dispatch('getuserinfo')
          // console.log(this.review)
          this.$emit('emit')
        }
      } catch (error) {
        console.log(error)
      }
    },
    goToReviewDetail() {
      this.$router.push({ name: 'review', params: { id: this.reviewId } })
    }
  }
}
</script>

<style scoped>
  .review-text:hover {
    background-color: rgb(107, 104, 104);
  }
  .profile-img {
    border: 1px solid rgb(129, 129, 129);
    border-radius: 10px;

  }
  .like-btn {
    margin-right: 7px;
  }
  .review-item {
    padding: 4px;
  }
</style>