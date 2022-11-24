<template>
  <div id="app">
    <header>
      <HeaderComp/>
    </header>
    <main>
      <router-view/>
    </main>
    <footer>
      <hr>
      <div class="footer-div">
        <span>
          본 사이트의 콘텐츠는 저작권법의 보호를 받는 바 무단 전재, 복사, 배포 등을 금합니다.
        </span>
        <br>
        <span>
          Copyright © JINJIN All Rights Reserved.
        </span>
      </div>
    </footer>
  </div>
</template>

<script>
import HeaderComp from '@/components/HeaderComp.vue'

export default {
  components: {
    HeaderComp,
  },
}
</script>

<style>
* {
  font-family: 'Noto Sans KR', sans-serif;
}
#app {
  height: auto;
  min-height: 100vh;
  background-color: rgb(34, 34, 34);
  color: white;
  display: grid;
  grid-template-rows: 0.5fr 8.2fr 0.8fr
}
main {
  margin-left: 27%;
  margin-right: 27%;
  margin-top: 2%;
}
.footer-div {
  margin-left: 15px;
  padding-bottom: 15px;
  font-size: small;
  color: rgb(132, 132, 132);
  text-align: center;
}
hr {
  background-color: rgb(132, 132, 132);
}
</style>