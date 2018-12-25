<!--suppress ALL -->
<template slot="items" slot-scope="props">
  <v-app v-scroll="onScroll">
    <v-toolbar app flat tile color="#fff" height="80">
      <v-layout>
        <v-flex class="app-toolbar" xs12 sm12 md10 offset-md1 lg10 offset-lg1 xl10 offset-xl1>
          <v-layout justify-center>
            <v-toolbar-title class="toolbar-title">
              <v-img width="36" height="36" src="/image/gengu.ico"></v-img>
              <v-flex class="headline font-weight-bold">&nbsp;南京亘古科技公司&nbsp;</v-flex>
            </v-toolbar-title>
            <v-spacer class="hidden-sm-and-down" @mouseenter="hiddenMenu"/>
            <v-btn active-class="toobar-btn-active" class="toobar-btn hidden-sm-and-down" flat small @mouseenter="hiddenMenu" nuxt to="/">首页</v-btn>
            <v-btn active-class="toobar-btn-active" class="toobar-btn hidden-sm-and-down" flat small @mouseenter="showMenu('goods')">产品应用</v-btn>
            <v-btn active-class="toobar-btn-active" class="toobar-btn hidden-sm-and-down" flat small @mouseenter="showMenu('stude')">高校竞赛</v-btn>
            <v-btn active-class="toobar-btn-active" class="toobar-btn hidden-sm-and-down" flat small @mouseenter="showMenu('about')">关于我们</v-btn>
          </v-layout>
          <v-layout class="toolbar-menu" wrap v-show="menuVisible" @mouseleave="hiddenMenu">
            <v-flex v-for="(item, index) in menuItem" :key="index"  xs4>
              <v-card class="menu-item" @click="hiddenMenu" v-if="item.type" :href="item.src" target="view_frame">
                <v-card-title class="subheading font-weight-bold">{{item.title}}</v-card-title>
              </v-card>
              <v-card class="menu-item" @click="hiddenMenu" v-else nuxt :to="item.src">
                <v-card-title class="subheading font-weight-bold">{{item.title}}</v-card-title>
              </v-card>
            </v-flex>
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
      <v-btn fab bottom right color="light-blue" dark fixed @click="toTop">
        <i class="iconfont icon-top" style="font-size:30px"></i>
      </v-btn>
    </v-content>
    <v-layout class="app-foot">
      <v-flex>
        <v-footer height="auto">
          <v-card class="flex" flat tile color="#eee">
            <v-card-title class="justify-center">
              <v-layout justify-center wrap>
                <v-flex xs4 sm4 md4 lg3 xl3>
                  <v-layout column align-end>
                    <v-layout column align-start>
                      <strong class="subheading">南京亘古科技有限公司</strong>
                      <a class="subheading">公司电话：222448888</a>
                      <a class="subheading">地址：南京信息工程大学</a>
                    </v-layout>
                  </v-layout>
                </v-flex>
                <v-flex xs4 sm4 md4 lg3 xl3>
                  <v-layout column align-center>
                    <strong class="subheading">关于我们</strong>
                    <a class="subheading">公司介绍</a>
                    <a class="subheading">荣誉奖项</a>
                    <a class="subheading">领导风采</a>
                  </v-layout>
                </v-flex>
                <v-flex xs4 sm4 md4 lg3 xl3>
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
  head () {
    return {
      title: '南京亘古科技',
      meta: [
        { hid: 'renderer', name: 'renderer', content: 'webkit|ie-comp|ie-stand' }
      ],
      menuItem: [],
    }
  },
  data() {
    return {
      offsetTop: 0,
      menuVisible: false,
      menuItem: []
    };
  },
  methods: {
    hiddenMenu() {
      this.menuVisible = false
    },
    showMenu(e) {
      if (e == 'goods') {
        this.menuItem = [
          {title: '激光雷达的产品研发及数据应用', src: '/goods/1'},
          {title: '厘米波雷达的产品研发及数据应用', src: '/goods/2'},
          {title: '毫米波雷达的产品研发及数据应用', src: '/goods/3'},
          {title: '雷电探测技术的产品研发及数据应用', src: '/goods/4'},
          {title: '风廓线雷达的产品研发及数据应用', src: '/goods/5'},
          {title: '卫星反演的产品研发及数据应用', src: '/goods/6'},
          {title: '微波辐射计的产品研发及数据应用', src: '/goods/7'},
          {title: '新型探测设备的设计与研发', src: '/goods/8'},
          {title: '人工智能及VR虚拟技术在气象中的应用', src: '/goods/9'},
        ]
      }
      if (e == 'stude') {
        this.menuItem = [
          {title: '“北斗杯”全国青少年科技创新大赛', src: 'http://www.bdlead.cn/', type: 'out'},
          {title: 'NOC高等学校信息技术创新与实践活动', src: 'http://www.noc.net.cn/gaoxiao/index.html', type: 'out'},
          {title: '学生荣誉奖项', src: '/competition/certificate'},
        ]
      }
      if (e == 'about') {
        this.menuItem = [
          {title: '公司介绍', src: '/about/company'},
          {title: '成员介绍', src: '/about/member'},
          {title: '联系我们', src: '/about/developer'},
        ]
      }
      this.menuVisible = true
    },
    toTop () {
      this.timer = setInterval (() => {
        let top = this.offsetTop
        document.documentElement.scrollTop = top - 60
        if (top <= 0) {
          clearInterval(this.timer)
        }
      }, 20)
    },
    onScroll(e) {
      this.offsetTop = window.pageYOffset || document.documentElement.scrollTop;
    }
  }
};
</script>

<style lang="stylus">
.app-toolbar
  position absolute
  top 0
  left 0
  width 100%
  padding 10px 24px
  .toolbar-title
    display flex
    align-items center
    justify-content center
  .toobar-btn
    color #0f0f0f
    height 50px
    padding 0 10px
  .toobar-btn-active
    color #006699
  .toolbar-menu
    width 100%
    padding 10px
    background-color rgba(250, 250, 250, .9)
    .menu-item
      margin 10px 50px
      line-height 1.5
      background-color rgba(255, 255, 255, .9)
    .menu-item:hover
      background-color #81D4FA

.app-content
  background-color #fff

.app-foot
  background-color #fff
</style>

