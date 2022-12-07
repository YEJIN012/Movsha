<template>
  <div> 
    <b-container class="review-text align-items-center">
      <b-row
      @click="goToReviewDetail"
      style="cursor:pointer"
      align-h="between">      
        <b-col md="4">
          <span>
            {{ review.movie.title }}
          </span>
        </b-col>
        <b-col md="5">
          <span>
            {{ review.title }}
          </span>
        </b-col>
        <b-col md="3">
          <span>
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
</style>