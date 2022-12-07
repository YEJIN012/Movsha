<template>
  <div>
    <h1>{{ profileDetail.nickname }} 님의 프로필</h1>
    <span v-if="profileDetail.profile_image">
      <img class="profile-image" :src="profileImage" height="150">
    </span>
    <span v-else>
      <img class="profile-image" src="@/assets/images/anonymoususer.jpg" height="150">
    </span>
    <div v-if="profileDetail.username === userInfo.username">
      <label for="imgFile" class="upload-profile-img" style="cursor:pointer">프로필 사진 업로드</label>
      <input type="file" accept="image/jpeg, image/jpg, image/png" id="imgFile" v-on:change="selectImage" style="display:none">
      <span class="update-btn" v-if="selectedimage" v-on:click="changeImage">수정</span>
    </div>
    <div class="followers-followings">
      <span @click="goToFollowerList" style="cursor:pointer"> 팔로워 {{ followersCount }} |</span>
      <span @click="goToFollowingList" style="cursor:pointer"> 팔로잉 {{ followingsCount }}</span>
    </div>
    
    <div v-if="profileDetail.username !== this.$store.state.userinfo.username" class="follow-btn">
      <b-button v-if="profileDetail.followers?.includes(userInfo.id)" @click="follow" style="cursor:pointer">언팔로우 &nbsp;<b-icon icon="person-check-fill"/></b-button>
      <b-button v-if="!profileDetail.followers?.includes(userInfo.id)" @click="follow" style="cursor:pointer">팔로우 &nbsp;<b-icon icon="person"/></b-button>
    </div>

    <br>
    <hr>
    <br>
    <LikeMoviesComp :like_movies="likeMovies"/>
    <br>
    <hr>
    <br>
    <h3 v-if="profileDetail.username === userInfo.username">내가 쓴 리뷰 {{ writereviews?.length }}</h3>
    <h3 v-if="profileDetail.username !== userInfo.username">{{ profileDetail.nickname }} 님의 리뷰 {{writereviews?.length }}</h3>
    <div class="review-list-wrapper">
      <WriteReviewsItemComp 
        v-for="review in writereviews" 
        :key="review.id" 
        :review="review"
      />
    </div>
  </div>
</template>


<script>
import LikeMoviesComp from "@/components/LikeMoviesComp.vue"
import WriteReviewsItemComp from "@/components/WriteReviewsItemComp.vue"
import arrayShuffle from 'array-shuffle';
import axios from 'axios'
import swal from 'sweetalert'

export default {
    name: 'ProfileDetailComp',
    data() {
      return {
        profiledetail : {},
        selectedimage : '',
        likemovies : {},
        writereviews : {},
      }
    },
    components : {
      LikeMoviesComp,
      WriteReviewsItemComp,
    },
    created() {
      this.getProfile()
    }
    ,
    computed: {
      profileImage() {
        return `http://localhost:8000${this.profiledetail.profile_image}`
      },
      profileDetail() {
        return this.profiledetail
      },
      userInfo() {
        return this.$store.state.userinfo
      },
      followersCount() {
        return this.profiledetail.followers?.length
      },
      followingsCount() {
        return this.profiledetail.followings?.length
      },
      // 배열
      likeMovies() {
        return this.likemovies
      },
      writeReviews() {
        return this.writereviews
      },
    },
    methods: {
      async getProfile() {
      const response = await axios({
        method: 'get',
        url: `${this.$store.state.API_URL}api/v1/profile/${this.$route.params.id}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        },
      })
      if (response.data) {
        this.profiledetail = response.data
        // like_movies는 movie_PK 순서대로 배열 받아와짐...
        this.likemovies = arrayShuffle(this.profiledetail.like_movies)
        // 최신 댓글순
        this.writereviews = this.profiledetail.review_set.reverse()
      }
    },
      selectImage(event) {
        if (event.target.files[0] != "") {
          let filename = event.target.files[0].name
          console.log(filename)
          let file_format = filename.slice(filename.lastIndexOf(".") + 1).toLowerCase();
          if (!(file_format === "jpeg" || file_format === "jpg" || file_format === "png")) {
            this.selectedimage = ''
            swal('경고!', '이미지 파일은 jpg, jpeg, png 만 업로드 가능합니다.', 'warning');
            return
          } else {
            let formData = new FormData()
            formData.append("profile_image", event.target.files[0])
            this.selectedimage = formData
          } 
        }

      },
      async changeImage() {
        try {
          const response = await axios({
            method: 'put',
            url: `${this.$store.state.API_URL}api/v2/profile/${this.$route.params.id}/update_image/`,
            headers: {
              Authorization: `Token ${this.$store.state.token}`
            },
            data: this.selectedimage,
          })
          if (response.data) {
            // console.log(response.data)
            this.getProfile()
            this.selectedimage=''
          }
        } catch (error) {
          console.log(error)
        }
      },
      goToFollowerList() {
        this.$router.push({ name: 'followerlist', params: { id: this.$route.params.id } })
      },
      goToFollowingList() {
        this.$router.push({ name: 'followinglist', params: { id: this.$route.params.id }})
      },
      async follow() {
        try {
        const response = await axios({
          method: 'post',
          url: `${this.$store.state.API_URL}api/v2/${this.$route.params.id}/follow/`,
          headers: {
            Authorization: `Token ${this.$store.state.token}`
          },
        })
        if (response.data) {
          // console.log(response.data)
          const updateprofile = await axios({
          method: 'get',
          url: `${this.$store.state.API_URL}api/v1/profile/${this.$route.params.id}/`,
          headers: {
            Authorization: `Token ${this.$store.state.token}`
          },
        })
        if (updateprofile.data) {
          this.profiledetail = updateprofile.data
          // console.log(this.profileDetail)
          // console.log(this.profileDetail.followers)
          // console.log(this.profileDetail.followings)
          this.$store.dispatch('getuserinfo')
        }
        }
      } catch (error) {
        console.log(error)
      }
      },
    },
} 
</script>
  

<style scoped>
  .review-list-wrapper {
    background-color: rgb(136, 136, 138);
    border: 1px solid rgb(87, 87, 90);
    border-radius: 6px;
  }
  .profile-image {
    border-radius: 50%;
    margin-top: 20px;
  }
  .follower-following {
    margin-top: 30px;
  }
  .upload-profile-img {
    border: 1px solid grey;
    border-radius: 5px;
    padding: 7px;
    margin-top: 20px;
    margin-left: 3px;
  }
  .upload-profile-img:hover {
    background-color: rgba(100, 98, 98, 0.6);
  }
  .followers-followings {
    margin-left: 8px;
    margin-top: 10px;
  }
  .follow-btn {
    margin-top: 20px;
  }
  .update-btn {
    border: 1px solid grey;
    border-radius: 5px;
    padding: 7px;
    margin-top: 20px;
    margin-left: 8px;
  }
  .update-btn:hover {
    background-color: rgba(100, 98, 98, 0.6);
  }
</style>