<template>
  <div class="recommend-view">
    <h1>{{ userNickname }} 님을 위한 영화 추천</h1>
    <br>
    <b-row class="row-gap">
      <RecommendItemComp
        v-for="(movie_pk, idx) in recommend_movies"
        :key="idx"
        :movie_pk="movie_pk"
      />
    </b-row>
  </div>
</template>


<script>
import axios from 'axios'
import RecommendItemComp from '@/components/RecommendItemComp.vue'
import swal from 'sweetalert'

export default {
    name: 'RecommendView',
    components: {
      RecommendItemComp,
    },
    data() {
      return {
        recommend_movies : '',
      }
    },
    created() {
      this.recommend()
    },
    computed: {
      userNickname() {
        return this.$store.state.userinfo.nickname
      }
    },
    methods: {
      async recommend() {
        try {
          const response = await axios({
            method: 'get',
            url: 'http://localhost:8000/api/v1/movies/',
            headers: {
              Authorization: `Token ${this.$store.state.token}`
            },
          })
          if (response.data) {
            let x = response.data.length
            let myfollowings = this.$store.state.userinfo.followings
            let myfollowingsnum = myfollowings.length
            // console.log(myfollowingsnum)
            if (myfollowingsnum === 0) {
              swal('팔로잉 정보가 없습니다!', '비슷한 취향의 유저를 팔로우하세요.', 'warning')
              return
            } else {
              let count_list = Array(x+1).fill(0)
              for (let i=0; i<myfollowingsnum; i++) {
                let following_pk = myfollowings[i]
                try {
                  const response = await axios({
                    method: 'get',
                    url: `${this.$store.state.API_URL}api/v1/profile/${following_pk}/`,
                    headers: {
                      Authorization: `Token ${this.$store.state.token}`
                    },
                  })
                  if (response.data) {
                    let following_reviews = response.data.review_set
                    for (let i=0; i<following_reviews.length; i++) {
                    let review_movie = following_reviews[i].movie
                    count_list[review_movie.id] = count_list[review_movie.id] + (-(3-following_reviews[i].rank))
                    }
                  }
                } catch (err) {
                  console.log(err)
                }
              }
              // console.log(count_list)
              let sorted_index_list = Array.from(Array(count_list.length).keys())
                .sort((a, b) => count_list[b] < count_list[a] ? -1 : (count_list[b] < count_list[a]) | 0)
              for (let i=0; i<10; i++) {
                if (sorted_index_list[i] === 0) {
                  sorted_index_list.splice(i,1)
                }
              }
              this.recommend_movies = sorted_index_list.slice(0,10)
            }
            // console.log(this.recommend_movies)
          }
        } catch(err) {
        console.log(err)
        }
      }
    }
}
</script>


<style scoped>
  .recommend-view {
    text-align: center;
    margin-bottom: 50px;
  }
  .row-gap {
    row-gap: 50px;
    margin-top: 30px;
  }
</style>

