<template>
  <div> 
    <b-container class="review-text">
      <b-row align-h="between">      
        <b-col cols="4">
          <span @click="goToReviewDetail" class="review-title">
            {{ review.movie.title }}
          </span>
        </b-col>
        <b-col cols="5">
          <span @click="goToReviewDetail" class="review-title">
            {{ review.title }}
          </span>
        </b-col>
        <b-col cols="3">
          <span @click="goToReviewDetail" class="review-createdate">
            {{ review.created_at|moment('YYYY-MM-DD HH:mm') }}
          </span>
        </b-col>
      </b-row>
    </b-container>
    
  </div>
</template>

<script>
export default {
    name: 'WriteReviewsItemComp',
    props: ['review'],
    data() {
      return {
        reviewId: this.review.id,
      }
    },
    methods: {
      goToReviewDetail() {
        console.log('clicked')
        console.log(this.reviewId)
        this.$router.push({ name: 'review', params: { id: this.reviewId } })
      }
    }
}
</script>

<style scoped>
  .review-text:hover {
    background-color: rgb(107, 104, 104);
  }
  .review-text {
    margin-top: 8px;
    margin-bottom: 8px;
  }
  .review-createdate {
    margin-left: 50px;
  }
</style>