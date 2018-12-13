<!--suppress ALL -->
<template>
  <v-container>

    <v-layout mb-2>
      <v-carousel>
        <v-carousel-item v-for="(picture,index) in pictures" :key="index" :src="picture.src"></v-carousel-item>
      </v-carousel>
    </v-layout>


    <v-layout class="second-main-title">
    <h1>我们的优势</h1>
  </v-layout>
    <v-layout align-center justify-center row fill-height class="second-main">
      <v-layout align-center justify-center column fill-height class="second-main-card">
        <v-img src="/image/gengu.png" width="100"/>
        <h1>自主创新研发</h1>
        <h4>公司依托于南京信息工程大学（原南京气象学院）国内一流的气象学科和庞大的气象专业团队.</h4>
      </v-layout>
      <v-layout align-center justify-center column fill-height class="second-main-card">
        <v-img src="/image/gengu.png" width="100"/>
        <h1>专业气象团队</h1>
        <h4>团队凭借雄厚的科研积淀、技术积累，专注于科研成果的技术转化，拥有的核心技术都是我国军、地各类气象部门业务现代化建设中急需的关键性技术，具有国际先进水平。</h4>
      </v-layout>
      <v-layout align-center justify-center column fill-height class="second-main-card">
        <v-img src="/image/gengu.png" width="100"/>
        <h1>科研成果转化</h1>
        <h4> 公司成立以来通过引进和吸收国内外新技术，自主创新开发了一系列气象新技术和新产品.</h4>
      </v-layout>
    </v-layout>

    <v-layout class="mb-2" >
      <v-parallax src="https://cdn.vuetifyjs.com/images/carousel/planet.jpg" style="width:100%;">
        <v-layout align-center column justify-center>
          <h1 class="display-2  mb-3">南京亘古科技公司</h1>
          <h1 class="mb-3 font-weight-thin">科技服务社会</h1>
          <h4 class="subheading">面对持续发展、迅速增长的海内外卫星应用服务市场，宏图人将不断坚持技术创新，全面提高企业的核心竞争力!</h4>
        </v-layout>
      </v-parallax>
    </v-layout>
    <v-layout>

      <v-flex xs6 sm6 md6 lg6 xl6 mr-2>
        <v-card color="#aed8f5">
          <v-card-title class="white--text">
            <h1>行业相关</h1>
          </v-card-title>
        </v-card>
        <v-card flat tile>
          <v-layout column>
            <v-flex v-for="message in messages" :key="message.id">
              <v-card flat tile>
                <v-card-text class="message-info">
                  <a>{{message.title}}</a>
                  <span>2018-10-1</span>
                </v-card-text>
              </v-card>
            </v-flex>
          </v-layout>
        </v-card>
      </v-flex>

      <v-flex xs6 sm6 md6 lg6 xl6 ml-2>

        <v-card color="#aed8f5">
          <v-card-title  class="white--text">
            <h1>热门产品</h1>
          </v-card-title>
        </v-card>

        <v-card class="goods-card">
          <v-img src="image/goods/1.jpg" aspect-ratio="2.75"></v-img>
          <v-card-title primary-title>
            <div>
              <h3 class="headline mb-0">基于北斗定位的微型厘米波段降水探空监测仪</h3>
            </div>
          </v-card-title>
          <v-card-text>大气边界层的气象要素与人们的生活息息相关，通过对边界层的气象要素进行探测，人们可以准确判断实时的气象条件，为人工影响天气的作业以及气象环境的监测提供可靠的数据支持。本系统通过多个无人机携带气象环境监测传感器，可以实现对边界层区域网的风速，风向，温度，湿度，压强，pm2.5进行探测。携带的北斗模块和无线传输模块不仅可以实时把边界层的各气象要素发送的到地面接收端，而且可以利用北斗模块准确地反映经纬度以及各个点的气象要，绘制成网格图，这样可以直观地测量以及读取区域的各个气象要素</v-card-text>
          <v-card-actions>
            <v-btn flat color="orange">查看详情</v-btn>
            <v-btn flat color="orange">立即购买</v-btn>
          </v-card-actions>
        </v-card>

        <v-card>
          <v-img src="image/goods/4.jpg" aspect-ratio="2.75"></v-img>
          <v-card-title primary-title>
            <div>
              <h3 class="headline mb-0">基于北斗定位的无人机高空气象探测系统</h3>
            </div>
          </v-card-title>
          <v-card-text>本设计将北斗定位技术结合探空气球、FPGA、射频电路技术、电磁散射理论、气溶胶物理学、大气探测技术等设计一个厘米波段降水探空监测仪，该仪器能够实时监测不同海拔高度的大气中降水粒子的大小、形状、谱分布等微观物理特性，为检测该地区降水时空分布的业务人员或者其他科研人员提供可靠的数据支撑，可推广应用至高校、气象局、环保局、海洋局、宇航局等科研院所</v-card-text>
          <v-card-actions>
            <v-btn flat color="orange">查看详情</v-btn>
            <v-btn flat color="orange">立即购买</v-btn>
          </v-card-actions>
        </v-card>

      </v-flex>

    </v-layout>
  </v-container>
</template>

<script>
export default {
  data() {
    return {
      messages: [
        {
          id: 0,
          title: '冰雹自动检测系统',
        },
        {
          id: 1,
          title: '基于北斗定位的无人机大气边界层气象探测系统',
        },
        {
          id: 2,
          title: '冰雪探测雷达',
        },
        {
          id: 3,
          title: '大气环境六要素监测仪',
        },
        {
          id: 4,
          title: '微型降水探空雷达',
        },
        {
          id: 5,
          title: '大气负氧离子监测仪',
        }
      ],
      pictures: [
        {
          src: "/image/active/banner.png"
        },
        {
          src: "/image/active/bdb.png"
        },
        {
          src: "/image/active/noc.png"
        },
        {
          src: "/image/active/bdb.png"
        }
      ]
    };
  }
};
</script>

<style lang="stylus" scoped>
.message-info
  display flex
  align-items center
  justify-content space-between
  border-bottom 1px solid #f9f9f9
.goods-card
  margin-bottom 15px
.second-main-title
  margin-top  60px
  margin-bottom  70px
.second-main
  margin-bottom  170px
.second-main-card
  border-left: 1px solid #e0e0e0;
  border-right: 1px solid #e0e0e0;
  padding 0px 18px
</style>
