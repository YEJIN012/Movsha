<template>
  <div>
    <div v-if="followings.length === 0" class="no-following">
      <h1>{{ userNickname }} 님의 팔로잉</h1>
      <h2>팔로잉이 없습니다.</h2>
    </div>
    <div v-else class="following">
      <h1>{{ userNickname }} 님의 팔로잉</h1>
      <div class="follow-item">
        <FollowItemComp
          v-for="(following, idx) in followings"
          :key="idx"
          :follow="following"
        />
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import FollowItemComp from "@/components/FollowItemComp.vue";

export default {
  name: "FollowingListView",
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
    followings() {
      return this.profiledetail.followings;
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
        console.log(response.data);
        this.profiledetail = response.data;
      }
    },
  },
};
</script>

<style scoped>
.follow-item {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr 1fr 1fr;
  row-gap: 70px;
  column-gap: 60px;
  margin-top: 40px;
  text-align: center;
}
.no-following {
  text-align: center;
  margin-top: 30px;
}
.following {
  text-align: center;
}
h2 {
  margin-top: 50px;
}
</style>