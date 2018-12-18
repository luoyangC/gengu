<template>
  <v-layout>
    <v-flex text-xs-center>
      {{title}}
    </v-flex>
  </v-layout>
</template>

<script>
export default {
  validate({params}){
    return /^\d+$/.test(params.id)
  },
  asyncData ({ params }) {
    const dataList = [
      {
        id: 1,
        title: '激光雷达的产品研发及数据应用',
        content: ''
      },{
        id: 2,
        title: '厘米波雷达的产品研发及数据应用',
        content: ''
      },{
        id: 3,
        title: '毫米波雷达的产品研发及数据应用',
        content: ''
      },{
        id: 4,
        title: '雷电探测技术的产品研发及数据应用',
        content: ''
      },{
        id: 5,
        title: '风廓线雷达的产品研发及数据应用',
        content: ''
      },{
        id: 6,
        title: '卫星反演的产品研发及数据应用',
        content: ''
      },{
        id: 7,
        title: '微波辐射计的产品研发及数据应用',
        content: ''
      },{
        id: 8,
        title: '新型探测设备的设计与研发',
        content: ''
      },{
        id: 9,
        title: '人工智能及VR虚拟技术在气象中的应用',
        content: ''
      },
    ]
    return dataList[parseInt(params.id)-1]
  }
}
</script>

<style>

</style>
