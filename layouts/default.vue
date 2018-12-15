<!--suppress ALL -->
<template>
  <v-app v-scroll="onScroll">
    <v-toolbar app color="#fff" height="80">
      <v-layout>
        <v-flex xs12 sm12 md10 offset-md1 lg10 offset-lg1 xl10 offset-xl1>
          <v-layout class="app-toolbar" justify-center>
            <v-toolbar-title class="app-toolbar-title">
              <v-img width="36" height="36" src="/image/gengu.ico"></v-img>
              <v-flex>&nbsp;南京亘古科技公司&nbsp;</v-flex>
            </v-toolbar-title>
            <v-spacer class="hidden-sm-and-down"/>
            <v-btn active-class="toobar-btn-active" class="toobar-btn hidden-sm-and-down" flat small nuxt to="/">首页</v-btn>
            <v-btn active-class="toobar-btn-active" class="toobar-btn hidden-sm-and-down" flat small nuxt to="/goods">产品应用</v-btn>
            <v-btn active-class="toobar-btn-active" class="toobar-btn hidden-sm-and-down" flat small nuxt to="/student">创新展示</v-btn>
            <v-btn active-class="toobar-btn-active" class="toobar-btn hidden-sm-and-down" flat small nuxt to="/about">关于我们</v-btn>
          </v-layout>
        </v-flex>
      </v-layout>
    </v-toolbar>
    <v-content>
      <v-layout class="app-content">
        <v-flex xs12 sm12 md10 offset-md1 lg10 offset-lg1 xl10 offset-xl1>
          <nuxt/>
        </v-flex>
      </v-layout>
      <v-btn fab bottom right color="light-blue" dark fixed>
        <v-icon>vertical_align_top</v-icon>
      </v-btn>
    </v-content>
    <v-layout class="app-foot">
      <v-flex>
        <v-footer height="auto">
          <v-card class="flex" flat tile color="#eee">
            <v-card-title class="justify-center">
              <v-layout justify-center wrap>
                <v-flex xl3>
                  <v-layout column align-end>
                    <v-layout column align-start>
                      <strong class="subheading">南京亘古科技有限公司</strong>
                      <a class="subheading">公司电话：222448888</a>
                      <a class="subheading">地址：南京信息工程大学</a>
                    </v-layout>
                  </v-layout>
                </v-flex>
                <v-flex xl3>
                  <v-layout column align-center>
                    <strong class="subheading">关于我们</strong>
                    <a class="subheading">公司介绍</a>
                    <a class="subheading">荣誉奖项</a>
                    <a class="subheading">领导风采</a>
                  </v-layout>
                </v-flex>
                <v-flex xl3>
                  <v-layout column align-start>
                    <v-layout column align-start>
                      <strong class="subheading mr-3">合作单位:</strong>
                      <a class="subheading">南京信息工程大学</a>
                      <a class="subheading">江苏省气象局</a>
                    </v-layout>
                  </v-layout>
                </v-flex>
              </v-layout>
            </v-card-title>
            <v-card-actions class="justify-center">
              &copy;2018 —
              <strong>南京亘古科技</strong>
            </v-card-actions>
          </v-card>
        </v-footer>
      </v-flex>
    </v-layout>
  </v-app>
</template>

<script>
export default {
  data() {
    return {
      offsetTop: 0
    };
  },
  methods: {
    onScroll(e) {
      this.offsetTop = window.pageYOffset || document.documentElement.scrollTop;
    }
  }
};
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

.app-content
  background-color #fff

.app-foot
  background-color #fff
</style>

