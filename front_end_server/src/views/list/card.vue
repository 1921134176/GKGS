<template>
  <div>
    <!-- 搜索框 -->
    <div class="search">
      <el-input
          placeholder="数据名称、关键字(如：土地覆盖)..."
          prefix-icon="el-icon-search"
          v-model="search_input"
          clearable>
          <i slot="suffix" class="el-input__icon el-icon-right" @click="search"></i>
      </el-input>
      <!-- <my-search-box placeholder="数据名称、关键字..." @search="search"></my-search-box> -->
    </div>
    <div class="datacard">
      <el-row>
        <!-- 数据卡片区域 -->
        <el-col :span="18">
          <div>
            <my-card-list :data="data" :columns="columns">
              <el-card slot-scope="{item}" shadow="hover" :body-style="{ padding: '0px' }">
                <!-- 弹出框来显示数据描述 -->
                <el-popover
                  placement="right-end"
                  title="数据简介"
                  width="225"
                  trigger="hover"
                  :content="item[4]">
                  <el-image
                   :src="item[1]"
                    class="image"
                    lazy
                    @mouseenter="enter(item[4])" 
                    @mouseleave="leave" slot="reference" 
                    @click="imageClick(item[6])">
                  <!-- 加载失败采样默认图像 -->
                    <div slot="error" class="image-slot">
                      <img src="https://data.casearth.cn/resources/storedataimages/defaultdata.png">
                    </div>
                  </el-image>
                </el-popover>
                <div style="padding: 5px;">
                  <!-- 数据集名称，文字过长则滚动显示 -->
                  <div style="height: 50px; overflow: auto;">
                    <span style="font-size: 14px; font-weight: 550; font-family: Microsoft YaHei;">
                      {{item[0]}}
                    </span>
                  </div>
                  <div class="bottom clearfix">
                    <time class="time" @click="descClick(item[0],item[5])">{{ item[2] }}</time>
                    <span class="dataform" :title="item[3]">{{ item[3] }}</span>
                    <el-button type="text" class="button" @click="descClick2(item[0],item[5])">详情</el-button>
                  </div>
                </div>
              </el-card>
            </my-card-list>
            <!-- 点击详情弹出的数据详情对话框 -->
            <el-dialog :title="dialogTitle" :visible.sync="dialogVisible" top="10px" center>
              <carddatadesc :url="dataDescUrl"></carddatadesc>
            </el-dialog>
            <!-- 点击详情弹出的数据详情对话框 这个对话框内容是自定义的-->
            <el-dialog :title="dialogTitle" :visible.sync="dialogVisible2" top="10px" center>
              <carddatadescform :sdoid="datasdoid"></carddatadescform>
            </el-dialog>
          </div>
        </el-col>
        <!-- 数据详情区域 -->
        <el-col :span="6">
          <div class="datadec">
            <el-row>
              <el-col :span="24">
                <!-- 标签云 -->
                <div style="height: 200px;">
                  <my-panel title="标签云" theme="border-left" fit>
                      <my-tag-canvas ref="tag" :data="tags" :options="options"></my-tag-canvas>
                  </my-panel>
                </div>
              </el-col>
            </el-row>
            <el-row>
              <el-col :span="24">
                <div style="height: 325px;">
                  <my-panel title="知识图谱" theme="border-left" fit>
                    <template v-slot:handle>
                      <el-switch
                        v-model="compareValue"
                        active-color="#13ce66"
                        inactive-color="#ff4949"
                        active-text="compare">
                      </el-switch>
                    </template>
                    <kgecharts :options="kgoptions1" :width="kgwidth" :height="kgheight" @clickNode="clickNode1"></kgecharts>
                  </my-panel>
                </div>
              </el-col>
            </el-row>
            <el-row>
              <el-col :span="24">
                <div style="height: 325px;">
                  <my-panel title="数据推荐" theme="border-left" fit>
                    <template v-slot:handle>
                      <el-switch
                        v-model="showValue"
                        active-color="#13ce66"
                        inactive-color="#ff4949"
                        active-text="show"
                        @change="recommendationView">
                      </el-switch>
                    </template>
                      <kgecharts :options="kgoptions2" :width="kgwidth" :height="kgheight" @clickNode="clickNode2"></kgecharts>
                  </my-panel>
                </div>
              </el-col>
            </el-row>
          </div>
          <el-dialog title="推荐数据详情" :visible.sync="recommendatonKgClickDialogVisible" center width="400px">
            <el-card>
              <el-image
              :src="recommendationItem[1]"
              class="image"
              @click="imageClick(recommendationItem[6])">
              <!-- 加载失败采样默认图像 -->
                <div slot="error" class="image-slot">
                  <img src="https://data.casearth.cn/resources/storedataimages/defaultdata.png">
                </div>
              </el-image>
              <div style="padding: 5px;">
              <!-- 数据集名称，文字过长则滚动显示 -->
                  <div style="height: 50px; overflow: auto;">
                      <span style="font-size: 14px; font-weight: 550; font-family: Microsoft YaHei;">
                        {{recommendationItem[0]}}
                      </span>
                  </div>
                  <div class="bottom clearfix">
                    <time class="time" @click="descClick(recommendationItem[0],recommendationItem[5])">{{ recommendationItem[2] }}</time>
                    <span class="dataform" :title="recommendationItem[3]">{{ recommendationItem[3] }}</span>
                    <el-button type="text" class="button" @click="descClick2(recommendationItem[0],recommendationItem[5])">详情</el-button>
                  </div>
              </div>
            </el-card>
          </el-dialog>
        </el-col>
      </el-row>
    </div>
  </div>
</template>

<script>
  import carddatadesc from '../../components/carddatadesc.vue'
  import carddatadescform from '../../components/carddatadescform.vue'
  import axios from '$ui/utils/axios'
  import {optionsProduct1, optionsProduct2} from '../../assets/js/utilkg'
  import kgecharts from '../../components/kgecharts.vue'
  import dataServerIp from '../../assets/js/dataserverip'
  axios.defaults.baseURL = dataServerIp.dataServerIp
  // axios.defaults.baseURL = 'http://127.0.0.1:5000'

  export default {
    components: {carddatadesc, carddatadescform, kgecharts},

    data() {
      return {
        data: [], // 卡片列表数据
        dataAll: [],
        dataRecommendation: [],
        recommendationItem: [],
        dataSearch: [],
        columns: {
          xxl: 6,
          xl: 5,
          lg: 4,
          md: 3,
          sm: 2,
          xs: 1
        },
        search_input: '', // 搜索框数据
        tags: [],
        options: {
          activeCursor: 'pointer',
          maxSpeed: 0.03,
          minSpeed: 0.01,
          textColour: null,
          textHeight: 20,
          fadeIn: 800,
          depth: 0.97,
          minBrightness: 0.2,
          wheelZoom: true,
          reverse: true,
          shuffleTags: true,
          shadowOffset: [1, 1],
          stretchX: 4.7,
          initial: [0, 0.1],
          clickToFront: 600
        },
        dialogVisible: false,
        dialogVisible2: false,
        recommendatonKgClickDialogVisible: false,
        dialogTitle: null,
        dataDescUrl: null,
        datasdoid: null, // 数据的唯一值，便于快速检索
        kgoptions1: optionsProduct1,
        kgoptions2: optionsProduct2,
        kgwidth: '100%',
        kgheight: '100%',
        kgIdList: new Set(),
        kgEdgeIdSet: new Set(),
        compareValue: false,
        showValue: false
      }
    },
    methods: {
      search() {
        if (this.search_input === '') {
          this.data = this.dataAll
          this.dataSearch = []
        } else {
          axios.get('/datarecommendation/recommendationSearch', {
            params: {
              searchText: this.search_input
            }
            })
            .then((response) => {
              this.data = response.data.data
              this.dataSearch = response.data.data
            })
            .catch(function (error) {
              console.log(error);
            })
          this.data = this.dataSearch
        }
      },
      enter(desc) {
        // this.$message(desc)
      },
      leave() {
        
      },
      descClick(title, sdoid) {
        // 用于显示iframe框架下的详情页
        this.dialogTitle = title
        this.dataDescUrl = 'https://data.casearth.cn/sdo/detail/' + sdoid
        this.dialogVisible = true
      },
      descClick2(title, sdoid) {
        this.dialogTitle = title
        this.dialogVisible2 = true
        this.datasdoid = sdoid
        // console.log(this.datasdoid)
      },
      imageClick(productSN) {
        if (!this.compareValue) {
          this.kgoptions1.series[0].data = []
          this.kgoptions1.series[0].links = []
          this.kgIdList.clear()
          this.kgEdgeIdSet.clear()
        }
        // 获取知识图谱数据
        axios.get('/datarecommendation/knowledgeGraph', {
        params: {
          productSN: productSN
        }
        })
        .then((response) => {
          // for in 遍历的key为索引值
          for (const key1 of response.data.data) {
            if (this.kgIdList.has(key1.id) === false) {
                this.kgIdList.add(key1.id)
                this.kgoptions1.series[0].data.push(key1)
            }
          }
          for (const key2 of response.data.links) {
            if (this.kgEdgeIdSet.has(key2.id) === false) {
                this.kgEdgeIdSet.add(key2.id)
                this.kgoptions1.series[0].links.push(key2)
            }
          }
        })
        .catch(function (error) {
          console.log(error);
        })
        // 获取推荐数据（排在前面的card推荐等级高）
        axios.get('/datarecommendation/reKnowledgeGraph', {
        params: {
          productSN: productSN
        }
        })
        .then((response) => {
          this.kgoptions2.series[0].data = response.data.data
          this.kgoptions2.series[0].links = response.data.links
          this.dataRecommendation = response.data.cardData
        })
        .catch(function (error) {
          console.log(error);
        })
      },
      recommendationView () {
        if (this.showValue) {
          this.data = this.dataRecommendation
        } else {
          if (this.dataSearch.length === 0) {
            this.data = this.dataAll
          } else {
            this.data = this.dataSearch
          }
        }
      },
      clickNode1 (nodeData) {
        if (nodeData.dataType === 'node') {
          axios.get('/datarecommendation/productKgClick', {
            params: {
              id: nodeData.data.id
            }
            })
            .then((response) => {
              // for in 遍历的key为索引值
              for (const key1 of response.data.data) {
                if (this.kgIdList.has(key1.id) === false) {
                    this.kgIdList.add(key1.id)
                    this.kgoptions1.series[0].data.push(key1)
                }
              }
              for (const key2 of response.data.links) {
                if (this.kgEdgeIdSet.has(key2.id) === false) {
                    this.kgEdgeIdSet.add(key2.id)
                    this.kgoptions1.series[0].links.push(key2)
                }
              }
            })
            .catch(function (error) {
              console.log(error);
            })
            }
      },
      clickNode2 (nodeData) {
        this.recommendatonKgClickDialogVisible = true
        axios.get('/datarecommendation/recommendationItem', {
        params: {
          productSN: nodeData.data.sn
        }
        })
        .then((response) => {
          this.recommendationItem = response.data.data
        })
        .catch(function (error) {
          console.log(error);
        })
      }
    },
    watch: {
      dataRecommendation () {
        if (this.showValue) {
          this.data = this.dataRecommendation
        }
      }
    },
    created() {
      axios.get('/datarecommendation/cardlist')
      .then((response) => {
        this.data = response.data.title
        this.dataAll = response.data.title
      })
      .catch(function (error) {
        console.log(error);
      });
    },
    mounted() {
      // 请求标签云数据
      axios.get('/datarecommendation/tagcloud')
      .then((response) => {
        this.tags = response.data.taglist
      })
      .catch(function (error) {
        console.log(error);
      });

    }
  }
</script>

<style lang="scss" scoped>
  .search {
    position: fixed;
    top: 7%;
    left: 38%;
    width: 400px;
    z-index: 999; 
  }

  .datacard {
    position: relative;
    margin: 10px;
    top: 45px;
  }

  .datadec {
    position: fixed;
    top: 12%;
    right: 0.5%;
    width: 25%;
    z-index: 999;
  }

  .time {
    font-size: 13px;
    color: #999;
    float: left;
  }
  
  .bottom {
    margin-top: 13px;
    line-height: 12px;
    text-align: center;
  }

  .button {
    padding: 0;
    float: right;
  }

  .image {
    height: 130px;
    width: 100%;
    display: block;
  }

  .clearfix:before,
  .clearfix:after {
      display: table;
      content: "";
  }
  
  .clearfix:after {
      clear: both
  }
  
  .dataform {
    font-family: Times New Roman; 
    font-size: 13px; 
    font-weight: 550; 
    font-style: italic; 
    color: Grey; 
    white-space:nowrap; 
    text-overflow:ellipsis; 
    overflow:hidden; 
    width: 100px; 
    display: inline-block
  }
</style>
