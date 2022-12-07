<template>
  <b-col sm="6" md="4">
    <a href="#" class="banner_img" @click="goToDetail">
      <img :src="movie.poster_path">
      <div class="hover_text">
        <p>{{ movie.title }}</p>
        <p>{{ movie.vote_average }}</p>
      </div>
    </a>
  </b-col>
</template>

<script>
export default {
  name: 'SearchItemComp',
  props: [
    'movie',
    'userInput',
  ],
  methods: {
    goToDetail() {
      this.$router.push({ name: 'movie', params: {id: this.movie.id} })
    }
  }

}
</script>

<style scoped>
img {
  vertical-align: top;
}
.banner_img{
  display:inline-block;
  position: relative;
}
.banner_img:hover:after,.banner_img:hover > .hover_text{
  display:block;
}
.banner_img:after,.hover_text{
  display:none;
}
.banner_img:after{
  content:'';
  position: absolute;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  background: rgba(0, 0, 0, 0.3);
  z-index: 10;
}
.banner_img {
  overflow: hidden;
}
.banner_img img{
  height: 340px;
}
.banner_img:hover img{
  transform: scale(1.2);
  transition: 1s;
}
.hover_text {
  position: absolute;
  top: 140px;
  left: 25px;
  color: #fff;
  z-index: 20;
  font-weight: 600;
  font-size: 20px;
}

</style>