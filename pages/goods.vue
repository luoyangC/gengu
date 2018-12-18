<template>
  <v-container>
    <v-layout>
      <v-flex xs2 text-xs-center align-self-start mt-5>
        <v-navigation-drawer permanent class="grey lighten-4">
          <v-toolbar flat class="display-1 text-xs-center">产品应用</v-toolbar>
          <v-list two-line>
            <v-list-tile exact-active-class='nav-activity' v-for="item in items" :key="item.title" nuxt :to="item.src">
              <v-list-tile-action>
                <v-icon>view_stream</v-icon>
              </v-list-tile-action>
              <v-list-tile-content>
                <v-list-tile-title>{{ item.title }}</v-list-tile-title>
              </v-list-tile-content>
            </v-list-tile>
          </v-list>
        </v-navigation-drawer>
      </v-flex>
      <v-flex xs10 mt-5>
        <nuxt/>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
export default {
  data() {
    return {
      items: [
        {title: '激光雷达的产品研发及数据应用',  src: '/goods/1'},
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
  }

}
</script>

<style lang="stylus">
.nav-activity
  background-color #81D4FA
</style>
