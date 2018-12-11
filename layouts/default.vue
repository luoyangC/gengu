<template>
  <v-app>
    <v-toolbar app color="#fff" height="64">
      <v-toolbar-title class="app-toolbar-title">
        <v-img width="36" height="36" src="/image/gengu.ico"></v-img>
        <v-flex>南京亘古科技公司</v-flex>
      </v-toolbar-title>
      <v-btn flat small nuxt to="/">首页</v-btn>
      <v-btn flat small nuxt to="/goods">产品</v-btn>
      <v-btn flat small nuxt to="/about">关于</v-btn>
      <v-spacer></v-spacer>
    </v-toolbar>
    <v-content app>
      <nuxt/>
      <v-btn fab bottom right color="light-blue" dark fixed>
        <v-icon>vertical_align_top</v-icon>
      </v-btn>
      <v-footer app height="auto">
        <v-card class="flex" flat tile>
          <v-card-actions class="justify-center">
            &copy;2018 — <strong>njggkj.com</strong>
          </v-card-actions>
        </v-card>
      </v-footer>
    </v-content>
  </v-app>
</template>

<script>
  export default {
  }
</script>

<style lang="stylus">
  .app-toolbar-title
    display flex
    align-items center
    justify-content center
</style>

