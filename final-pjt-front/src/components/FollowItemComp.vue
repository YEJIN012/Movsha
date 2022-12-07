<template>
  <b-col>
    <span v-if="profileDetail.profile_image">
      <img
      class="profile-img"
      @click="goToUserProfile"
      style="cursor:pointer"
      :src="profileImg"
      height="150">
    </span>
    <span v-else>
      <img
      class="profile-img"
      @click="goToUserProfile"
      style="cursor:pointer"
      src="@/assets/images/anonymoususer.jpg"
      height="150">
    </span>
    <h4
      class="mt-3"
      @click="goToUserProfile"
      style="cursor:pointer">
      {{ profileDetail.nickname }}
    </h4>
  </b-col>
</template>

<script>
import axios from "axios";

export default {
  name: "FollowItemComp",
  data() {
    return {
      profileDetail: {},
    };
  },
  props: ["follow",],
  created() {
    this.getProfile();
  },
  computed: {
    profileImg() {
      return `http://localhost:8000${this.profileDetail.profile_image}`
    }
  },
  methods: {
    async getProfile() {
      const response = await axios({
        method: "get",
        url: `${this.$store.state.API_URL}api/v1/profile/${this.follow}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      });
      if (response.data) {
        // console.log(response.data)
        this.profileDetail = response.data;
        // console.log(this.profileDetail)
      }
    },
    goToUserProfile() {
      this.$router.push({ name: 'profile', params: {id: this.follow }})
    },
  },
};
</script>

<style scoped>
  .profile-img {
      border-radius: 50%;
      border: 1px solid rgb(107, 107, 107);
    }
</style>