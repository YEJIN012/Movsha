<template>
  <div>
    <b-form v-on:submit.prevent="createReview" class="review-form">

      <b-form-group class="star-rate">
        <div class="star-rating">
          <b-form
            class="star form-check-inline"
            v-for="index in 5"
            :key="index"
            @click="check(index)"
            v-model="form.review.rank"
          >
            <span v-if="index <= form.review.rank"><b-icon icon="star-fill" scale="1.5"/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>
            <span v-if="index > form.review.rank"><b-icon icon="star" scale="1.5"/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>
          </b-form>
        </div>
      </b-form-group>

      <b-form-group class="review-title">
        <b-form-input
          id="input-1"
          v-model="form.review.title"
          placeholder="제목을 입력하세요"
          required
        ></b-form-input>
      </b-form-group>

      <b-form-group class="review-content">
        <b-form-input
          id="input-2"
          v-model="form.review.content"
          placeholder="내용을 입력하세요"
          required
          style="height:20vh"
        ></b-form-input>
      </b-form-group>

      <div class="submit-btn">
        <b-button type="submit" variant="primary">Submit</b-button>
      </div>

    </b-form>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'ReviewCreateComp',
  data() {
    return {
      form: {
        review: {
          title: null,
          content: null,
          rank: null,
        },
      },
    }
  },
  props: [
    'movieId',
  ],
  methods: {
    async createReview() {
      console.log('create')
      const title = this.form.review.title
      const content = this.form.review.content
      const rank = Number(this.form.review.rank)
      console.log(rank)
      const data = {
        title,
        content,
        rank,
      }
      try {
        const response = await axios({
          method: 'post',
          url: `${this.$store.state.API_URL}api/v1/movies/${this.movieId}/reviews/`,
          data: data,
          headers: {
            Authorization: `Token ${this.$store.state.token}`
          },
        })
        if (response.data) {
          console.log(response.data)
          this.form.review.title = null
          this.form.review.content = null
          this.form.review.rank = null
          this.$emit('emit')
        }
      } catch (err) {
        console.log(err)
      }
    },
    check(index) {
      this.form.review.rank = index
      console.log(this.form.review.rank)
    }
  }
}
</script>

<style scoped>
.review-form {
  border: 1px solid white;
  border-radius: 8px;
  padding: 4%;
}
.star-rate {
  margin-left: 5px;
  margin-bottom: 4%;
}
.review-title {
  margin-bottom: 3%;
}
.review-content {
  margin-bottom: 3%;
}
.submit-btn {
  margin-left: 90%;
}
</style>