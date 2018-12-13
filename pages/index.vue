<!--suppress ALL -->
<template>
  <div>
    <div class="lunbo">
  <v-carousel>
    <v-carousel-item
      v-for="(item,i) in items"
      :key="i"
      :src="item.src"
    ></v-carousel-item>
  </v-carousel>
    </div>
    <div class="container-card">
      <v-layout align-start justify-center row fill-height>
      <div class="left-card">
        <v-layout>
          <v-flex xs12 sm12>
            <v-card>
              <v-list >
                <template v-for="(item, index) in item1">
                  <v-subheader
                    v-if="item.header"
                    :key="item.header"
                  >
                    {{ item.header }}
                  </v-subheader>

                  <v-divider
                    v-else-if="item.divider"
                    :inset="item.inset"
                    :key="index"
                  ></v-divider>

                  <v-list-tile
                    v-else
                    :key="item.title"
                    avatar
                    @click=""
                  >
                    <v-list-tile-avatar>
                      <img :src="item.avatar">
                    </v-list-tile-avatar>

                    <v-list-tile-content>
                      <v-list-tile-title v-html="item.title"></v-list-tile-title>
                      <v-list-tile-sub-title v-html="item.subtitle"></v-list-tile-sub-title>
                    </v-list-tile-content>
                  </v-list-tile>
                </template>
              </v-list>
            </v-card>
          </v-flex>
        </v-layout>
      </div>

     <v-layout align-center justify-start column fill-height>
      <div class="card">
        <v-layout>
        <v-flex xs12 sm12>
          <v-card width="530">
            <v-img
              src="image1/1.jpg"
              aspect-ratio="2.75"
            ></v-img>

            <v-card-title primary-title>
              <div>
                <h3 class="headline mb-0">2、基于北斗定位的微型厘米波段降水探空监测仪</h3>
                <div>本设计将北斗定位技术结合探空气球、FPGA、射频电路技术、电磁散射理论、气溶胶物理学、大气探测技术等设计一个厘米波段降水探空监测仪，该仪器能够实时监测不同海拔高度的大气中降水粒子的大小、形状、谱分布等微观物理特性，为检测该地区降水时空分布的业务人员或者其他科研人员提供可靠的数据支撑，可推广应用至高校、气象局、环保局、海洋局、宇航局等科研院所。</div>
              </div>
            </v-card-title>

            <v-card-actions>
              <v-btn flat color="orange">查看详情</v-btn>
              <v-btn flat color="orange">立即购买</v-btn>
            </v-card-actions>
          </v-card>
        </v-flex>
      </v-layout>
      </div>
      <div class="card">
        <v-layout>
        <v-flex xs12 sm12 >
          <v-card width="530">
            <v-img
              src="image1/4.jpg"
              aspect-ratio="2.75"
            ></v-img>

            <v-card-title primary-title>
              <div>
                <h3 class="headline mb-0">基于北斗定位的无人机高空气象探测系统</h3>
                <div>大气边界层的气象要素与人们的生活息息相关,通过对边界层的气象要素进行探测，人们可以准确判断实时的气象条件为人工影响天气的作业以及气象环境的监测提供可靠的数据支持。</div>
              </div>
            </v-card-title>

            <v-card-actions>
              <v-btn flat color="orange">查看详情</v-btn>
              <v-btn flat color="orange">立即购买</v-btn>
            </v-card-actions>
          </v-card>
        </v-flex>
      </v-layout>
      </div>
      </v-layout>
      </v-layout>
    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      cards: [
        { title: 'Pre-fab homes', src: 'https://cdn.vuetifyjs.com/images/cards/house.jpg', flex: 12 },
        { title: 'Favorite road trips', src: 'https://cdn.vuetifyjs.com/images/cards/road.jpg', flex: 6 },
        { title: 'Best airlines', src: 'https://cdn.vuetifyjs.com/images/cards/plane.jpg', flex: 6 }
      ],

      item1: [
        { header: 'Today' },
        {
          avatar: 'https://cdn.vuetifyjs.com/images/lists/1.jpg',
          title: 'Brunch this weekend?',
          subtitle: "<span class='text--primary'>Ali Connors</span> &mdash; I'll be in your neighborhood doing errands this weekend. Do you want to hang out?"
        },
        { divider: true, inset: true },
        {
          avatar: 'https://cdn.vuetifyjs.com/images/lists/2.jpg',
          title: 'Summer BBQ <span class="grey--text text--lighten-1">4</span>',
          subtitle: "<span class='text--primary'>to Alex, Scott, Jennifer</span> &mdash; Wish I could come, but I'm out of town this weekend."
        },
        { divider: true, inset: true },
        {
          avatar: 'https://cdn.vuetifyjs.com/images/lists/3.jpg',
          title: 'Oui oui',
          subtitle: "<span class='text--primary'>Sandra Adams</span> &mdash; Do you have Paris recommendations? Have you ever been?"
        }
      ],

      items: [
        {
          src: 'https://cdn.vuetifyjs.com/images/carousel/squirrel.jpg'
        },
        {
          src: 'https://cdn.vuetifyjs.com/images/carousel/sky.jpg'
        },
        {
          src: 'https://cdn.vuetifyjs.com/images/carousel/bird.jpg'
        },
        {
          src: 'https://cdn.vuetifyjs.com/images/carousel/planet.jpg'
        }
      ]
    }
  }
}
</script>

<style lang="stylus" scoped>
 .lunbo{
   margin:20px auto;
   padding:30px 10%;
 }
 .card{
   padding:0px 0px 10px 0px;
 }

 .container-card{
   padding:0px 10%;
 }
</style>
