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
            </my-panel>
        </el-col>
        <el-col class="box" :span="8">
            <my-panel title="数据挖掘" theme="flag" shadow="always" icon="el-icon-menu" fit>
              <kgecharts :options="kgoptions2" :width="kgwidth" :height="kgheight" @clickNode="clickNode2"></kgecharts>
              <template v-slot:handle>
                <el-button-group>
                  <el-popover
                    placement="bottom"
                    width="150"
                    trigger="hover"
                    content="查看影像">
                    <el-button slot="reference" icon="el-icon-picture"  size="mini" @click="productImgShow"></el-button>
                  </el-popover>
                  <el-popover
                    placement="bottom"
                    width="150"
                    trigger="hover"
                    content="异常检测">
                    <el-button slot="reference" icon="el-icon-warning" size="mini" @click="kgErrorDialogShow"></el-button>
                  </el-popover>
                </el-button-group>
              </template>
            </my-panel>
        </el-col>
        <el-col class="box" :span="8">
            <my-panel title="知识卡片" theme="flag" shadow="always" icon="el-icon-menu" fit>
                <my-key-val-list :column="nodecolumn" :data="nodedata" border :columns="1"> </my-key-val-list>
            </my-panel>
        </el-col>
      </el-row>
    </my-map-drawer>
    <el-dialog :title="dialogTitle" top="2vh" :visible.sync="dialogProductImgVisible">
      <el-row>
        <el-col :span="6">
          <div>
            <el-image
            :src="imageSrcList[0]"
            :fit="imageFit"
            @click="downImg(0)"
            @error="imageLoadError"
            @load="imageLoadSuccess">
            </el-image>
            <div style="margin: 0 auto; text-align: center ">
              <span style="font-size: 14px; font-weight: 550; font-family: Microsoft YaHei;">
                GLC_FCS30-1985
              </span>
            </div>
          </div>
        </el-col>
        <el-col :span="6">
          <div>
            <el-image
            :src="imageSrcList[1]"
            :fit="imageFit"
            @click="downImg(1)">
            </el-image>
            <div style="margin: 0 auto; text-align: center ">
              <span style="font-size: 14px; font-weight: 550; font-family: Microsoft YaHei;">
                GLC_FCS30-1990
              </span>
            </div>
          </div>
        </el-col>
        <el-col :span="6">
          <div>
            <el-image
            :src="imageSrcList[2]"
            :fit="imageFit"
            @click="downImg(2)">
            </el-image>
            <div style="margin: 0 auto; text-align: center ">
              <span style="font-size: 14px; font-weight: 550; font-family: Microsoft YaHei;">
                GLC_FCS30-1995
              </span>
            </div>
          </div>
        </el-col>
        <el-col :span="6">
          <div>
            <el-image
            :src="imageSrcList[3]"
            :fit="imageFit"
            @click="downImg(3)">
            </el-image>
            <div style="margin: 0 auto; text-align: center ">
              <span style="font-size: 14px; font-weight: 550; font-family: Microsoft YaHei;">
                GLC_FCS30-2000
              </span>
            </div>
          </div>
        </el-col>
      </el-row>
      <el-row>
        <el-col :span="6">
          <div>
            <el-image
            :src="imageSrcList[4]"
            :fit="imageFit"
            @click="downImg(4)">
            </el-image>
            <div style="margin: 0 auto; text-align: center ">
              <span style="font-size: 14px; font-weight: 550; font-family: Microsoft YaHei;">
                GLC_FCS30-2005
              </span>
            </div>
          </div>
        </el-col>
        <el-col :span="6">
          <div>
            <el-image
            :src="imageSrcList[5]"
            :fit="imageFit"
            @click="downImg(5)">
            </el-image>
            <div style="margin: 0 auto; text-align: center ">
              <span style="font-size: 14px; font-weight: 550; font-family: Microsoft YaHei;">
                GLC_FCS30-2010
              </span>
            </div>
          </div>
        </el-col>
        <el-col :span="6">
         <div>
            <el-image
            :src="imageSrcList[6]"
            :fit="imageFit"
            @click="downImg(6)">
            </el-image>
            <div style="margin: 0 auto; text-align: center ">
              <span style="font-size: 14px; font-weight: 550; font-family: Microsoft YaHei;">
                GLC_FCS30-2015
              </span>
            </div>
          </div>
        </el-col>
        <el-col :span="6">
          <div>
            <el-image
            :src="imageSrcList[7]"
            :fit="imageFit"
            @click="downImg(7)">
            </el-image>
            <div style="margin: 0 auto; text-align: center ">
              <span style="font-size: 14px; font-weight: 550; font-family: Microsoft YaHei;">
                GLC_FCS30-2020
              </span>
            </div>
          </div>
        </el-col>
      </el-row>
      <el-row>
        <el-col :span="6">
          <div>
            <el-image
            :src="imageSrcList[8]"
            :fit="imageFit"
            @click="downImg(8)">
            </el-image>
            <div style="margin: 0 auto; text-align: center ">
              <span style="font-size: 14px; font-weight: 550; font-family: Microsoft YaHei;">
                GlobaLand30_2000
              </span>
            </div>
          </div>
        </el-col>
        <el-col :span="6">
          <div>
            <el-image
            :src="imageSrcList[9]"
            :fit="imageFit"
            @click="downImg(9)">
            </el-image>
            <div style="margin: 0 auto; text-align: center ">
              <span style="font-size: 14px; font-weight: 550; font-family: Microsoft YaHei;">
                GlobaLand30_2010
              </span>
            </div>
          </div>
        </el-col>
        <el-col :span="6">
          <div>
            <el-image
            :src="imageSrcList[10]"
            :fit="imageFit"
            @click="downImg(10)">
            </el-image>
            <div style="margin: 0 auto; text-align: center ">
              <span style="font-size: 14px; font-weight: 550; font-family: Microsoft YaHei;">
                GlobaLand30_2020
              </span>
            </div>
          </div>
        </el-col>
        <el-col :span="6">
          <div>
            <el-image
            :src="imageSrcList[11]"
            :fit="imageFit"
            @click="downImg(11)">
            </el-image>
            <div style="margin: 0 auto; text-align: center ">
              <span style="font-size: 14px; font-weight: 550; font-family: Microsoft YaHei;">
                FROM-GLC10_2017
              </span>
            </div>
          </div>
        </el-col>
      </el-row>
      <el-button slot="footer" type="primary" @click="computeButtonClick" :disabled="computeButtonDisabled">图计算获取</el-button>
    </el-dialog>
    <el-dialog title="图计算流" top="5vh" :visible.sync="dialogKgComputeVisible">
      <div style="height: 600px">
        <kgecharts :options="kgoptions3" :width="kgwidth" :height="kgheight" v-loading="loading"></kgecharts>
      </div>
      <el-button slot="footer" type="primary" @click="subComputeButtonClick" v-loading="loading">计算</el-button>
    </el-dialog>
    <el-dialog :title="errorDialogTitle" top="5vh" :visible.sync="dialogKgErrorVisible">
      <div style="height: 600px">
        <kgecharts :options="kgoptions4" :width="kgwidth" :height="kgheight" v-loading="loading"></kgecharts>
        <span slot="footer">数据异常阈值参考：皮尔森相关系数(Ｒ) &lt; 60% 、 总体一致性系数(N) &lt; 60%、百分比不一致性(PD) &gt; 40%、 不同地类的一致性系数(Mi) &lt; 60%</span>
      </div>
    </el-dialog>
  </my-map>
</template>

<script>
  import ChinaOnlineCommunity from '$ui/map/sources/preview/ChinaOnlineCommunity.png'
  import ChinaRSTDT from '../assets/RSTDT.png'
  import china from '$ui/charts/geo/china.json'
  import index from '../assets/id_index.json'
  import kgecharts from './kgecharts.vue'
  import {options1, options2, optionsKgCompute, optionsErrorKg} from '../assets/js/utilkg'
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
        kgoptions3: optionsKgCompute,
        kgoptions4: optionsErrorKg,
        kgwidth: '100%',
        kgheight: '100%',
        kgIdList: new Set(),
        kgEdgeIdSet: new Set(),
        // 知识卡片数据
        nodecolumn: [],
        nodedata: {},
        dialogProductImgVisible: false,
        imageFit: 'scale-down',
        imageSrcList: [],
        imageDownloadSrcList: [],
        nodeId_imageName: '',
        imageName: '',
        dialogTitle: '产品影像图',
        computeButtonDisabled: true,
        dialogKgComputeVisible: false,
        dialogKgErrorVisible: false,
        loading: false,
        errorDialogTitle: '异常数据检测'
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
        this.nodeId_imageName = nodeData.data.id
        this.dialogTitle = nodeData.data.name + '产品影像图'
        this.errorDialogTitle = nodeData.data.name + '异常数据检测'
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
        this.nodeId_imageName = nodeData.data.id
        this.dialogTitle = nodeData.data.name + '产品影像图'
        this.kgAddNodes(this.kgoptions2, nodeData.data.id)
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
      },
      productImgShow() {
        this.dialogProductImgVisible = true
        axios.get('/guotu/kg/productLocationName', {
              params: {
                nodeid: this.nodeId_imageName
              }
              })
              .then((response) => {
                this.imageName = response.data.data
                this.imageSrcList = [
                dataServerIp.dataServerIp + '/guotu/kg/GLC1985/' + response.data.data + '.png',
                dataServerIp.dataServerIp + '/guotu/kg/GLC1990/' + response.data.data + '.png',
                dataServerIp.dataServerIp + '/guotu/kg/GLC1995/' + response.data.data + '.png',
                dataServerIp.dataServerIp + '/guotu/kg/GLC2000/' + response.data.data + '.png',
                dataServerIp.dataServerIp + '/guotu/kg/GLC2005/' + response.data.data + '.png',
                dataServerIp.dataServerIp + '/guotu/kg/GLC2010/' + response.data.data + '.png',
                dataServerIp.dataServerIp + '/guotu/kg/GLC2015/' + response.data.data + '.png',
                dataServerIp.dataServerIp + '/guotu/kg/GLC2020/' + response.data.data + '.png',
                dataServerIp.dataServerIp + '/guotu/kg/GlobaLand30_2000/' + response.data.data + '.png',
                dataServerIp.dataServerIp + '/guotu/kg/GlobaLand30_2010/' + response.data.data + '.png',
                dataServerIp.dataServerIp + '/guotu/kg/GlobaLand30_2020/' + response.data.data + '.png',
                dataServerIp.dataServerIp + '/guotu/kg/GLC2017/' + response.data.data + '.png']
                this.imageDownloadSrcList = [
                dataServerIp.dataServerIp + '/guotu/kg/download/GLC1985/' + response.data.data + '.tif',
                dataServerIp.dataServerIp + '/guotu/kg/download/GLC1990/' + response.data.data + '.tif',
                dataServerIp.dataServerIp + '/guotu/kg/download/GLC1995/' + response.data.data + '.tif',
                dataServerIp.dataServerIp + '/guotu/kg/download/GLC2000/' + response.data.data + '.tif',
                dataServerIp.dataServerIp + '/guotu/kg/download/GLC2005/' + response.data.data + '.tif',
                dataServerIp.dataServerIp + '/guotu/kg/download/GLC2010/' + response.data.data + '.tif',
                dataServerIp.dataServerIp + '/guotu/kg/download/GLC2015/' + response.data.data + '.tif',
                dataServerIp.dataServerIp + '/guotu/kg/download/GLC2020/' + response.data.data + '.tif',
                dataServerIp.dataServerIp + '/guotu/kg/download/GlobaLand30_2000/' + response.data.data + '.tif',
                dataServerIp.dataServerIp + '/guotu/kg/download/GlobaLand30_2010/' + response.data.data + '.tif',
                dataServerIp.dataServerIp + '/guotu/kg/download/GlobaLand30_2020/' + response.data.data + '.tif',
                dataServerIp.dataServerIp + '/guotu/kg/download/GLC2017/' + response.data.data + '.tif']
              })
              .catch(function (error) {
                console.log(error);
              })
      },
      downImg(index) {
        const image = new Image();
        image.setAttribute('crossOrigin', 'anonymous');
        // bug：无法下载原始tif格式数据
        // image.src = this.imageDownloadSrcList[index];
        image.src = this.imageSrcList[index];
        image.onload = () => {
          const canvas = document.createElement('canvas');
          canvas.width = image.width;
          canvas.height = image.height;
          const ctx = canvas.getContext('2d');
          ctx.drawImage(image, 0, 0, image.width, image.height);
          canvas.toBlob((blob) => {
            const url = URL.createObjectURL(blob);
            const Link = document.createElement('a');
            Link.download = this.imageName;
            Link.href = url;
            Link.click();
            Link.remove();
            // 用完释放URL对象
            URL.revokeObjectURL(url);
          });
      };
      },
      imageLoadError(e) {
        
        if(this.imageName.indexOf('country') !== -1 || this.imageName.indexOf('province') !== -1 || this.imageName.indexOf('city') !== -1) {
          this.computeButtonDisabled = false
        } else {
          this.computeButtonDisabled = true
        }
      },
      imageLoadSuccess(e) {
        this.computeButtonDisabled = true
      },
      computeButtonClick() {
        this.dialogProductImgVisible = false
        this.dialogKgComputeVisible = true
        this.loading = true
        // 请求计算图
        axios.get('/guotu/kg/computeKG', {
        params: {
          id: this.nodeId_imageName
        }
        })
        .then((response) => {
          this.kgoptions3.series[0].data = response.data.data
          this.kgoptions3.series[0].links = response.data.links
          this.loading = false
          } 
        )
        .catch((error) => {
          console.log(error);
          this.loading = false
        })
      },
      subComputeButtonClick() {
        this.loading = true
        // 图像拼接代码
        axios.get('/guotu/kg/imageMosaic', {
        params: {
          id: this.nodeId_imageName
        }
        })
        .then((response) => {
          this.dialogKgComputeVisible = false;
          // this.imageSrcList滞空，不然前后没变化，不会跟新视图
          this.imageSrcList = []
          this.productImgShow(); 
          this.loading = false
          } 
        )
        .catch((error) => {
          console.log(error);
          this.loading = false
        })
        // setTimeout(() => { this.dialogKgComputeVisible = false; this.productImgShow(); this.loading = false }, 3000)
      },
      kgErrorDialogShow() {
        this.dialogKgErrorVisible = true
        this.loading = true
        // 请求异常检测数据图
        axios.get('/guotu/kg/errorKG', {
        params: {
          id: this.nodeId_imageName
        }
        })
        .then((response) => {
          this.kgoptions4.series[0].data = response.data.data
          this.kgoptions4.series[0].links = response.data.links
          this.loading = false
          } 
        )
        .catch((error) => {
          console.log(error);
          this.loading = false
        })
      }
    },
    watch: {
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
  .el-image {
    width: 200px; 
    height: 200px;
  }
</style>
