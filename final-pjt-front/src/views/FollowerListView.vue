<template>
  <div>
    <div v-if="followers?.length === 0" class="no-follower">
      <h1>{{ userNickname }} 님의 팔로워</h1>
      <h2>팔로워가 없습니다.</h2>
    </div>
    <div v-else class="follower">
      <h1>{{ userNickname }} 님의 팔로워</h1>
      <b-row>
        <FollowItemComp
          v-for="(follower, idx) in followers"
          :key="idx"
          :follow="follower"
        />
      </b-row>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import FollowItemComp from "@/components/FollowItemComp.vue";

export default {
  name: "FollowerListView",
  data() {
    return {
      profiledetail: {},
    };
  },
  components: {
    FollowItemComp,
  },
  created() {
    this.getProfile();
  },
  computed: {
    followers() {
      return this.profiledetail.followers;
    },
    userNickname() {
      return this.profiledetail.nickname
    }
  },
  methods: {
    async getProfile() {
      const response = await axios({
        method: "get",
        url: `${this.$store.state.API_URL}api/v1/profile/${this.$route.params.id}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      });
      if (response.data) {
        // console.log(response.data);
        this.profiledetail = response.data;
      }
    },
  },
};
</script>

<style scoped>
h1 {
  text-align: center;
}
.no-follower {
  text-align: center;
  margin-top: 30px;
}
.follower {
  text-align: center;
}
h2 {
  margin-top: 50px;
}
</style>