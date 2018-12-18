<template>
  <v-layout justify-center wrap>
    <v-flex xs12 sm12>
      <v-card>
        <v-card-title class="display-3 font-weight-bold justify-center">中科芯杯二等奖</v-card-title>
        <v-container grid-list-sm fluid>
          <v-layout row wrap>
            <v-flex v-for="i in 4" :key="i" xs4 d-flex>
              <v-card flat tile class="d-flex">
                <v-img :src="`https://gengu.oss-cn-shanghai.aliyuncs.com/static/image/certificate/zkx2 (${i}).png`" aspect-ratio="1.4" class="grey lighten-2">
                  <v-layout slot="placeholder" fill-height align-center justify-center ma-0>
                    <v-progress-circular indeterminate color="grey lighten-5"></v-progress-circular>
                  </v-layout>
                </v-img>
              </v-card>
            </v-flex>
          </v-layout>
        </v-container>
      </v-card>
    </v-flex>
    <v-flex xs12 sm12>
      <v-card>
        <v-card-title class="display-3 font-weight-bold justify-center">中科芯杯优秀奖</v-card-title>
        <v-container grid-list-sm fluid>
          <v-layout row wrap>
            <v-flex v-for="i in 11" :key="i" xs4 d-flex>
              <v-card flat tile class="d-flex">
                <v-img :src="`https://gengu.oss-cn-shanghai.aliyuncs.com/static/image/certificate/zkx (${i}).png`" aspect-ratio="1.4" class="grey lighten-2">
                  <v-layout slot="placeholder" fill-height align-center justify-center ma-0>
                    <v-progress-circular indeterminate color="grey lighten-5"></v-progress-circular>
                  </v-layout>
                </v-img>
              </v-card>
            </v-flex>
          </v-layout>
        </v-container>
      </v-card>
    </v-flex>
    <v-flex xs12 sm12>
      <v-card>
        <v-card-title class="display-3 font-weight-bold justify-center">NOC获奖证数</v-card-title>
        <v-container grid-list-sm fluid>
          <v-layout row wrap>
            <v-flex v-for="i in 2" :key="i" xs4 d-flex>
              <v-card flat tile class="d-flex">
                <v-img :src="`https://gengu.oss-cn-shanghai.aliyuncs.com/static/image/certificate/noc (${i}).png`" aspect-ratio="0.6" class="grey lighten-2">
                  <v-layout slot="placeholder" fill-height align-center justify-center ma-0>
                    <v-progress-circular indeterminate color="grey lighten-5"></v-progress-circular>
                  </v-layout>
                </v-img>
              </v-card>
            </v-flex>
          </v-layout>
        </v-container>
      </v-card>
    </v-flex>
    <v-flex xs12 sm12>
      <v-card>
        <v-card-title class="display-3 font-weight-bold justify-center">其他证书</v-card-title>
        <v-container grid-list-sm fluid>
          <v-layout row wrap>
            <v-flex v-for="i in imageList" :key="i.id" xs4 d-flex>
              <v-card flat tile class="d-flex">
                <v-img :src="i.src" aspect-ratio="1.4" class="grey lighten-2">
                  <v-layout slot="placeholder" fill-height align-center justify-center ma-0>
                    <v-progress-circular indeterminate color="grey lighten-5"></v-progress-circular>
                  </v-layout>
                </v-img>
              </v-card>
            </v-flex>
          </v-layout>
        </v-container>
      </v-card>
    </v-flex>
  </v-layout>
</template>

<script>
export default {
  data() {
    return {
      imageList: [
        {id: 0, src: 'https://gengu.oss-cn-shanghai.aliyuncs.com/static/image/certificate/bdb.png'},
        {id: 1, src: 'https://gengu.oss-cn-shanghai.aliyuncs.com/static/image/certificate/bd%2B.png'},
        {id: 2, src: 'https://gengu.oss-cn-shanghai.aliyuncs.com/static/image/certificate/hlw.png'},
        {id: 3, src: 'https://gengu.oss-cn-shanghai.aliyuncs.com/static/image/certificate/fpga.png'},
      ]
    }
  }
}
</script>
