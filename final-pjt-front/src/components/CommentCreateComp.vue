<template>
  <div>
    <b-form v-on:submit.prevent="createComment">
      <b-form-input
        id="input-1"
        v-model="form.comment.content"
        placeholder="댓글을 입력하세요"
        required
      ></b-form-input>
    </b-form>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'CommentCreateComp',
  data() {
    return {
      form: {
        comment: {
          content: null,
        }
      }
    }
  },
  props: ['reviewId',],
  methods: {
    async createComment() {
      const content = this.form.comment.content
      const data = {
        content,
      }
      try {
        const response = await axios({
          method: 'post',
          url: `${this.$store.state.API_URL}api/v1/reviews/${this.reviewId}/comments/`,
          data: data,
          headers: {
            Authorization: `Token ${this.$store.state.token}`
          }
        })
        if (response.data) {
          // console.log(response.data)
          this.form.comment.content = null
          this.$emit('emit')
        }
      } catch(err) {
        console.log(err)
      }
    }
  }
}
</script>

<style>

</style>