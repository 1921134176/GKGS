<template>
  <my-map height="100%"
          :adapter="defaultAdapter"
          :zoom="zoom"
          :center="center"
          @click="handleClickmap"
          @dblclick="dcmap"
          :key="keymap"
          ref="map">
    <!-- 通过改变key，组件会重新渲染 -->
    <my-map-geo :key="key" :json="geo" :stroke="stroke" :fill="fill" :text="text" :hover-style="hoverStyle" @click="handleClick"></my-map-geo>
    <my-map-layers :placement="placement" :layers="layers" :margin="10" @change="redrawgeo"></my-map-layers>
    <my-map-overview :collapsed="false" ></my-map-overview>
    <!-- 左侧显示 -->
    <!-- <my-map-drawer title="知识图谱可视化分析面板" width="450px" collapsed placement="left">
      <el-row>
        <el-col>
            <my-panel title="容器标题" theme="flag" shadow="always" icon="el-icon-menu" fit>
                <Diagram  height="400px" :nodes="nodes" :highlight-mode="'adjoin'" :links="links" :options="options"></Diagram>
                <template v-slot:footer>
                    <el-button size="small" type="primary">提交</el-button>
                    <el-button size="small">取消</el-button>
                </template>
            </my-panel>
        </el-col>
      </el-row>
      <el-row>
        <el-col>
            <my-panel title="容器标题" theme="flag" shadow="always">
                <Diagram  height="400px" :nodes="nodes" :highlight-mode="'adjoin'" :links="links" :options="options"></Diagram>
            </my-panel>
        </el-col>
      </el-row>
      <el-row>
        <el-col>
            <my-panel title="容器标题" theme="flag" shadow="always">
                <Diagram  height="400px" :nodes="nodes" :highlight-mode="'adjoin'" :links="links" :options="options"></Diagram>
            </my-panel>
        </el-col>
      </el-row>
    </my-map-drawer> -->
    <!-- 顶部显示 -->
    <my-map-drawer collapsed placement="top">
      <el-row>
        <el-col class="box" :span="8">
            <my-panel title="知识图谱" theme="flag" shadow="always" icon="el-icon-menu" fit>
              <kgecharts :options="kgoptions1" :width="kgwidth" :height="kgheight" @clickNode="clickNode"></kgecharts>
              <template v-slot:handle>
                <el-button-group>
                  <el-button icon="el-icon-edit"  size="mini"></el-button>
                  <el-button icon="el-icon-share"  size="mini"></el-button>
                  <el-button icon="el-icon-delete" size="mini"></el-button>
              </el-button-group>
              </template>
            </my-panel>
        </el-col>
        <el-col class="box" :span="8">
            <my-panel title="数据挖掘" theme="flag" shadow="always" fit>
              <kgecharts :options="kgoptions2" :width="kgwidth" :height="kgheight" @clickNode="clickNode2"></kgecharts>
            </my-panel>
        </el-col>
        <el-col class="box" :span="8">
            <my-panel title="知识卡片" theme="flag" shadow="always" fit>
                <my-key-val-list :column="nodecolumn" :data="nodedata" border :columns="1"> </my-key-val-list>
            </my-panel>
        </el-col>
      </el-row>
    </my-map-drawer>
  </my-map>
</template>

<script>
  import ChinaOnlineCommunity from '$ui/map/sources/preview/ChinaOnlineCommunity.png'
  import ChinaRSTDT from '../assets/RSTDT.png'
  import china from '$ui/charts/geo/china.json'
  import index from '../assets/id_index.json'
  import kgecharts from './kgecharts.vue'
  import {options1, options2} from '../assets/js/utilkg'
  import axios from '$ui/utils/axios'
  import dataServerIp from '../assets/js/dataserverip'
  axios.defaults.baseURL = dataServerIp.dataServerIp
  // axios.defaults.baseURL = 'http://127.0.0.1:5000'

  const map = new Map(Object.entries(index))

  export default {
    components: {
      kgecharts
    },
    data() {
      return {
        zoom: 5,
        center: [108.683729, 31.166113],
        keymap: 1,
        key: 1,
        placement: 'right-bottom',
        layers: null,
        defaultAdapter: null,
        geo: null,
        stroke: {
          width: 1,
          color: 'blue'
        },
        fill: 'rgba(0, 0, 0, 0)',
        text: {
          fill: 'rgba(0, 0, 0, 0)',
          font: '16px',
          scale: '0.8'
        },
        hoverStyle: {
          fill: 'rgba(0, 0, 0, 0)',
          stroke: {
            color: '#000',
            width: 3
          },
          text: {
            fill: 'red'
          }
        },
        // echarts知识图谱数据
        kgoptions1: options1,
        kgoptions2: options2,
        kgwidth: '100%',
        kgheight: '100%',
        kgIdList: new Set(),
        kgEdgeIdSet: new Set(),
        // 知识卡片数据
        nodecolumn: [],
        nodedata: {}
      }
    },
    methods: {
        createLayers() {
            const mapLayers = [
                {
                    title: '天地图',
                    adapter: 'Baidu', // Baidu
                    preview: ChinaOnlineCommunity
                },
                {
                    title: '影像地图',
                    adapter: {
                    type: 'XYZ',
                    url: 'http://t0.tianditu.gov.cn/img_w/wmts?SERVICE=WMTS&REQUEST=GetTile&VERSION=1.0.0&LAYER=img&STYLE=default&TILEMATRIXSET=w&FORMAT=tiles&TILEMATRIX={z}&TILEROW={y}&TILECOL={x}&tk=1e6e1db34020461896ee2fecf5f54dad'
                    },
                    preview: ChinaRSTDT
                }]
            return mapLayers
      },
      // map点击事件
      handleClickmap() {
        // console.log(this.$refs.map.getLayer())
      },
      // map双击事件: 返回视图全局
      dcmap() {
        this.geo = china
        this.$refs.map.moveTo([108.683729, 31.166113])
        this.$refs.map.zoomTo(5)
        this.key = -this.key
        this.getOneSubKg(this.kgoptions1, 'country', '中华人民共和国-country')
      },
      // geo点击事件
      handleClick(e, feature) {
        try {
          this.geo = require((`$ui/charts/geo/${map.get(feature.id_).geo}`))
          this.$refs.map.moveTo(feature.values_.cp)
          const path = map.get(feature.id_).geo
          if (path.search('province') !== -1) {
            this.$refs.map.zoomTo(7)
          } else {
            this.$refs.map.zoomTo(9)
          }
          // 重新绘图
          this.key = -this.key
        } catch (error) {
          // console.log(error)
        }
        // 更新知识图谱
        // console.log(feature)
        // this.$message(feature.get('name'))
        this.getOneSubKgFromGeoName(this.kgoptions1, feature.get('name'))
        // console.log(this.kgoptions1.series[0])
      },
      redrawmap() {
        this.keymap = -this.keymap
      },
      // 点击图层切换
      redrawgeo() {
        // 重新加载geo,确保位于最上方图层
        this.key = -this.key
        // 控制文字图层显示与否
        if(this.key === -1) {
          if(this.$refs.map.getLayer().sourceChangeKey_.target.projection_.code_ === 'baidu') {
            this.text = {
                fill: 'blue',
                font: '16px',
                scale: '0.8'
            }
          } else {
            this.text = {
                fill: 'yellow',
                font: '16px',
                scale: '0.8'
            }
          }
        } else {
            this.text = {
                fill: 'rgba(0, 0, 0, 0)',
                font: '16px',
                scale: '0.8'
            }
        }
      },
      // 利用label,name(alias)获取一阶子图
      getOneSubKg(option, label, name) {
        axios.get('/guotu/kg/init', {
        params: {
          label: label,
          name: name
        }
        })
        .then((response) => {
          option.series[0].data = response.data.data
          option.series[0].links = response.data.links
          // console.log(response)
        })
        .catch(function (error) {
          console.log(error);
        })
      },
      // 从geo获取的name中获取一阶子图
      getOneSubKgFromGeoName(option, name) {
        axios.get('/guotu/kg/update_from_geo', {
        params: {
          name: name
        }
        })
        .then((response) => {
          option.series[0].data = response.data.data
          option.series[0].links = response.data.links
        })
        .catch(function (error) {
          console.log(error);
        })
      },
      // 根据id获取一阶子图
      getOneSubKgFromNodeId(option, id) {
        axios.get('/guotu/kg/update_from_nodeid', {
        params: {
          id: id
        }
        })
        .then((response) => {
          option.series[0].data = []
          option.series[0].links = []
          // for in 遍历的key为索引值
          for (const key1 of response.data.data) {
            if (this.kgIdList.has(key1.id) === false) {
                this.kgIdList.add(key1.id)
                option.series[0].data.push(key1)
            }
          }
          for (const key2 of response.data.links) {
            if (this.kgEdgeIdSet.has(key2.id) === false) {
                this.kgEdgeIdSet.add(key2.id)
                option.series[0].links.push(key2)
            }
          }
          // option.series[0].data = response.data.data
          // option.series[0].links = response.data.links
        })
        .catch(function (error) {
          console.log(error);
        })
      },
      // 知识图谱节点展开接口
      kgAddNodes(option, id) {
        axios.get('/guotu/kg/update_from_nodeid', {
        params: {
          id: id
        }
        })
        .then((response) => {
          // for in 遍历的key为索引值
          for (const key1 of response.data.data.slice(1)) {
            if (this.kgIdList.has(key1.id) === false) {
                this.kgIdList.add(key1.id)
                option.series[0].data.push(key1)
            }
          }
          for (const key2 of response.data.links) {
            if (this.kgEdgeIdSet.has(key2.id) === false) {
                this.kgEdgeIdSet.add(key2.id)
                option.series[0].links.push(key2)
            }
          }
        })
        .catch(function (error) {
          console.log(error);
        })
      },
      // 知识图谱点击事件
      clickNode(nodeData) {
        this.kgIdList.clear()
        this.kgEdgeIdSet.clear()
        this.getOneSubKgFromNodeId(this.kgoptions2, nodeData.data.id)
        if (nodeData.dataType === 'node') {
          this.kgCardUpdate(nodeData.data.id)
            } else {
              axios.get('/manage/kg/getRelationshipInformation', {
              params: {
                relationshipId: nodeData.data.id,
                relationshipType: nodeData.data.value
              }
              })
              .then((response) => {
                this.nodedata = response.data.data
                this.nodecolumn = response.data.column
              })
              .catch(function (error) {
                console.log(error);
              })
            } 
      },
      // 数据挖掘点击事件
      clickNode2(nodeData) {
        this.kgAddNodes(this.kgoptions2, nodeData.data.id)
        console.log(nodeData)
        if (nodeData.dataType === 'node') {
          this.kgCardUpdate(nodeData.data.id)
            } else {
              axios.get('/manage/kg/getRelationshipInformation', {
              params: {
                relationshipId: nodeData.data.id,
                relationshipType: nodeData.data.value
              }
              })
              .then((response) => {
                this.nodedata = response.data.data
                this.nodecolumn = response.data.column
              })
              .catch(function (error) {
                console.log(error);
              })
            }
      },
      // 知识卡片数据获取与更新
      kgCardUpdate(nodeId) {
        axios.get('/guotu/kg/kgCardUpdate', {
        params: {
          id: nodeId
        }
        })
        .then((response) => {
          this.nodedata = response.data.data
          this.nodecolumn = response.data.column
          if (this.nodecolumn.length === 0) {
            axios.get('/manage/kg/getNodeInformation', {
              params: {
                nodeid: nodeId
              }
              })
              .then((response) => {
                this.nodedata = response.data.data
                this.nodecolumn = response.data.column
              })
              .catch(function (error) {
                console.log(error);
              })
          } 
        })
        .catch(function (error) {
          console.log(error);
        })
      }
    },
    created() {
      this.layers = this.createLayers()
      this.defaultAdapter = this.layers[0].adapter
      this.geo = china
      // 初始化知识图谱
      this.getOneSubKg(this.kgoptions1, 'country', '中华人民共和国-country')
      this.getOneSubKg(this.kgoptions2, 'country', '中华人民共和国-country')
    },
    mounted() {
      // this.key_kg = -this.key_kg
    }
  }
</script>

<style lang="scss" scoped>
  .el-row {
    margin-bottom: 5px;
    &:last-child {
      margin-bottom: 0;
    }
  }
  .el-col {
    border-radius: 4px;
  }
  .bg-purple {
    background: #a88585;
  }
  .grid-content {
    border-radius: 4px;
    min-height: 36px;
  }
  .row-bg {
    padding: 10px 0;
    background-color: #f9fafc;
  }
  .box {
    height:350px;
  }
  .my-panel {
    margin-bottom: 2rem;
  }
</style>
