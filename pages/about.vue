<template>
  <v-container>
    <v-layout row>
      <v-flex md4 lg3 xl2 text-xs-center align-self-start mt-5 class="hidden-sm-and-down">
        <v-navigation-drawer permanent class="grey lighten-4">
          <v-toolbar flat class="display-1">关于我们</v-toolbar>
          <v-list two-line>
            <v-list-tile exact-active-class='nav-activity' v-for="item in items" :key="item.title" nuxt :to="item.src">
              <v-list-tile-action>
                <v-icon>{{ item.icon }}</v-icon>
              </v-list-tile-action>
              <v-list-tile-content>
                <v-list-tile-title>{{ item.title }}</v-list-tile-title>
              </v-list-tile-content>
            </v-list-tile>
          </v-list>
        </v-navigation-drawer>
      </v-flex>
      <v-flex xs12 sm12 md8 lg9 xl10 mt-5>
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
          { title: '公司介绍', icon: 'iconfont icon-apps', src: '/about/company' },
          { title: '成员介绍', icon: 'iconfont icon-friend', src: '/about/member' },
          { title: '联系我们', icon: 'iconfont icon-community', src: '/about/developer' }
        ]
    }
  }
};
</script>

<style lang="stylus">
.nav-activity
  background-color #81D4FA
</style>