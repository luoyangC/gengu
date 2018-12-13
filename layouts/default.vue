<!--suppress ALL -->
<template>
  <v-app v-scroll="onScroll" >
    <v-toolbar app card color="#fff" height="80">
      <v-layout>
        <v-flex  xs12 sm12 md10 offset-md1 lg8 offset-lg2 xl8 offset-xl2>
          <v-layout class="app-toolbar">
            <v-toolbar-title class="app-toolbar-title">
              <v-img width="36" height="36" src="/image/gengu.ico"></v-img>
              <v-flex>&nbsp;南京亘古科技公司&nbsp;</v-flex>
            </v-toolbar-title>
            <v-spacer/>
            <v-btn active-class="toobar-btn-active" class="toobar-btn" flat small nuxt to="/">首页</v-btn>
            <v-btn active-class="toobar-btn-active" class="toobar-btn" flat small nuxt to="/goods">产品应用</v-btn>
            <v-btn active-class="toobar-btn-active" class="toobar-btn" flat small nuxt to="/student">创新展示</v-btn>
            <v-btn active-class="toobar-btn-active" class="toobar-btn" flat small nuxt to="/about">关于我们</v-btn>
          </v-layout>
        </v-flex>
      </v-layout>
    </v-toolbar>
    <v-content>
      <v-layout>
        <v-flex  xs12 sm12 md10 offset-md1 lg8 offset-lg2 xl8 offset-xl2>
          <nuxt/>
        </v-flex>
      </v-layout>
      <v-btn fab bottom right color="light-blue" dark fixed>
        <v-icon>vertical_align_top</v-icon>
      </v-btn>
    </v-content>
    <v-footer app height="auto">
      <v-card class="flex" flat tile>
        <v-card-actions class="justify-center">
          &copy;2018 — <strong>njggkj.com</strong>
        </v-card-actions>
      </v-card>
    </v-footer>
  </v-app>
</template>

<script>
export default {
  data() {
    return {
      offsetTop: 0
    }
  },
  methods: {
    onScroll (e) {
      this.offsetTop = window.pageYOffset || document.documentElement.scrollTop
    }
  }
}
</script>

<style lang="stylus">
.app-toolbar
  .app-toolbar-title
    display flex
    align-items center
    justify-content center
  .toobar-btn
    color #0f0f0f
    height 50px
    padding 0 10px
  .toobar-btn-active
    color #006699
    border-bottom 2px solid #006699
</style>

