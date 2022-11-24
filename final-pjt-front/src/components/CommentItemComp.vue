<template>
  <div class="comment-item">
    <b-container>
      <b-row align-h="between">
        <b-col cols="3">
          <span v-if="comment.user.profile_image">
            <img class="profile-img"  @click="goToUserProfile" :src="profileImageOfComment" height="25">
          </span>
          <span v-else>
            <img class="profile-img"  @click="goToUserProfile" src="@/assets/images/anonymoususer.jpg" height="25">
          </span>
          &nbsp;&nbsp;
          <span class="comment-nickname">
            {{ comment.user.nickname }}
          </span>
        </b-col>
        <b-col cols="4">
          <span class="comment-createdat">
            {{ comment.created_at|moment('YYYY-MM-DD HH:mm') }}
          </span>
          <span v-if="comment.user.id === userId">
            &nbsp;&nbsp;&nbsp;<b-icon icon="trash" @click="deleteComment"></b-icon>
          </span>
        </b-col>
      </b-row>
    </b-container>
      <div class="review-title">
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        {{ comment.content }}
      </div>
      <hr style="width:100%;height:1px;border:none;background-color:grey;">
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'CommentItemComp',
  props: ['comment', 'reviewId'],
  computed: {
    profileImageOfComment() {
      return `http://localhost:8000${this.comment.user.profile_image}`
    },
    userId() {
      return this.$store.state.userinfo.id
    },
    commentId() {
      return this.comment.id
    }
  },
  methods: {
    goToUserProfile() {
      this.$router.push({ name: 'profile', params: {id: this.comment.user.id }})
    },
    async deleteComment() {
      try {
        const response = await axios({
          method: 'delete',
          url: `${this.$store.state.API_URL}api/v1/comments/${this.commentId}/`,
          headers: {
            Authorization: `Token ${this.$store.state.token}`
          }
        })
        if (!response.data) {
          this.$emit('emit')
        }
      } catch(err) {
        console.log(err)
      }
    },
  },

}
</script>

<style scoped>
  .profile-img {
    border-radius: 10px;
    border: 1px solid rgb(107, 107, 107);
  }
  .comment-item {
    margin-top: 6px;
  }
  .comment-profile-img {
    border-radius: 10px;
    border: 1px solid rgb(107, 107, 107);
  }
  .comment-createdat {
    margin-left: 30%;
  }
  .review-title {
    margin-right: 2%;
  }

</style>