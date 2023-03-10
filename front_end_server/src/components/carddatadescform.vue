<!-- eslint-disable no-tabs -->
<template>
    <div>
        <el-row>
            <el-col :span="2">
                <div class="grid-content bg-purple">
                    <label>数据简介：</label>
                </div>
            </el-col>
            <el-col :span="22">
                <div class="grid-content bg-purple-light">
                    <span>
                        {{desData.desc}}
                    </span>
                </div>
            </el-col>
        </el-row>
        <el-row>
            <el-col :span="12">
                <el-row>
                    <el-col :span="4">
                        <div class="grid-content bg-purple">
                            <label>下载地址：</label>
                        </div>
                    </el-col>
                    <el-col :span="20">
                        <div class="grid-content bg-purple-light">
                            <a :href="desData.objectUrl" target="_blank">
                                {{desData.objectUrl}}
                            </a>
                        </div>
                    </el-col>
                </el-row>
            </el-col>
            <el-col :span="12">
                <el-row>
                    <el-col :span="4">
                        <div class="grid-content bg-purple">
                            <label>学科分类：</label>
                        </div>
                    </el-col>
                    <el-col :span="20">
                        <div class="grid-content bg-purple-light">
                            <span>
                                {{desData.taxonomy}}
                            </span>
                        </div>
                    </el-col>
                </el-row>
            </el-col>
        </el-row>
        <el-row>
            <el-col :span="12">
                <el-row>
                    <el-col :span="4">
                        <div class="grid-content bg-purple">
                            <label>开始时间：</label>
                        </div>
                    </el-col>
                    <el-col :span="20">
                        <div class="grid-content bg-purple-light">
                            <span>
                                {{desData.startTime}}
                            </span>
                        </div>
                    </el-col>
                </el-row>
            </el-col>
            <el-col :span="12">
                <el-row>
                    <el-col :span="4">
                        <div class="grid-content bg-purple">
                            <label>结束时间：</label>
                        </div>
                    </el-col>
                    <el-col :span="20">
                        <div class="grid-content bg-purple-light">
                            <span>
                                {{desData.endTime}}
                            </span>
                        </div>
                    </el-col>
                </el-row>
            </el-col>
        </el-row>
        <el-row>
            <el-col :span="12">
                <el-row>
                    <el-col :span="5">
                        <div class="grid-content bg-purple">
                            <label>空间分辨率：</label>
                        </div>
                    </el-col>
                    <el-col :span="19">
                        <div class="grid-content bg-purple-light">
                            <span>
                                {{desData.spatialResolution}}
                            </span>
                        </div>
                    </el-col>
                </el-row>
            </el-col>
            <el-col :span="12">
                <el-row>
                    <el-col :span="5">
                        <div class="grid-content bg-purple">
                            <label>时间分辨率：</label>
                        </div>
                    </el-col>
                    <el-col :span="19">
                        <div class="grid-content bg-purple-light">
                            <span>
                                {{desData.timeResolution}}
                            </span>
                        </div>
                    </el-col>
                </el-row>
            </el-col>
        </el-row>
        <el-row>
            <el-col :span="12">
                <el-row>
                    <el-col :span="4">
                        <div class="grid-content bg-purple">
                            <label>地域范围：</label>
                        </div>
                    </el-col>
                    <el-col :span="20">
                        <div class="grid-content bg-purple-light">
                            <span>
                                {{desData.rangeDescription}}
                            </span>
                        </div>
                    </el-col>
                </el-row>
            </el-col>
            <el-col :span="12">
                <el-row>
                    <el-col :span="4">
                        <div class="grid-content bg-purple">
                            <label>共享方式：</label>
                        </div>
                    </el-col>
                    <el-col :span="20">
                        <div class="grid-content bg-purple-light">
                            <span>
                                {{desData.shareMethod}}
                            </span>
                        </div>
                    </el-col>
                </el-row>
            </el-col>
        </el-row>
        <el-row>
            <el-col :span="12">
                <el-row>
                    <el-col :span="4">
                        <div class="grid-content bg-purple">
                            <label>产品编号：</label>
                        </div>
                    </el-col>
                    <el-col :span="20">
                        <div class="grid-content bg-purple-light">
                            <span>
                                {{desData.productSN}}
                            </span>
                        </div>
                    </el-col>
                </el-row>
            </el-col>
            <el-col :span="12">
                <el-row>
                    <el-col :span="4">
                        <div class="grid-content bg-purple">
                            <label>创建机构：</label>
                        </div>
                    </el-col>
                    <el-col :span="20">
                        <div class="grid-content bg-purple-light">
                            <span>
                                {{desData.publishDepartment}}
                            </span>
                        </div>
                    </el-col>
                </el-row>
            </el-col>
        </el-row>
        <el-row>
            <el-col :span="12">
                <el-row>
                    <el-col :span="4">
                        <div class="grid-content bg-purple">
                            <label>创建人员：</label>
                        </div>
                    </el-col>
                    <el-col :span="20">
                        <div class="grid-content bg-purple-light">
                            <span>
                                {{desData.publisher}}
                            </span>
                        </div>
                    </el-col>
                </el-row>
            </el-col>
            <el-col :span="12">
                <el-row>
                    <el-col :span="4">
                        <div class="grid-content bg-purple">
                            <label>发布日期：</label>
                        </div>
                    </el-col>
                    <el-col :span="20">
                        <div class="grid-content bg-purple-light">
                            <span>
                                {{desData.releaseDate}}
                            </span>
                        </div>
                    </el-col>
                </el-row>
            </el-col>
        </el-row>
        <el-row>
            <el-col :span="12">
                <el-row>
                    <el-col :span="4">
                        <div class="grid-content bg-purple">
                            <label>文件量：</label>
                        </div>
                    </el-col>
                    <el-col :span="20">
                        <div class="grid-content bg-purple-light">
                            <span>
                                {{desData.filesNumber}}
                            </span>
                        </div>
                    </el-col>
                </el-row>
            </el-col>
            <el-col :span="12">
                <el-row>
                    <el-col :span="4">
                        <div class="grid-content bg-purple">
                            <label>存储量：</label>
                        </div>
                    </el-col>
                    <el-col :span="20">
                        <div class="grid-content bg-purple-light">
                            <span>
                                {{desData.mSize}}
                            </span>
                        </div>
                    </el-col>
                </el-row>
            </el-col>
        </el-row>
        <el-row>
            <el-col :span="12">
                <el-row>
                    <el-col :span="4">
                        <div class="grid-content bg-purple">
                            <label>浏览量：</label>
                        </div>
                    </el-col>
                    <el-col :span="20">
                        <div class="grid-content bg-purple-light">
                            <span>
                                {{desData.visitCount}}
                            </span>
                        </div>
                    </el-col>
                </el-row>
            </el-col>
            <el-col :span="12">
                <el-row>
                    <el-col :span="4">
                        <div class="grid-content bg-purple">
                            <label>下载量：</label>
                        </div>
                    </el-col>
                    <el-col :span="20">
                        <div class="grid-content bg-purple-light">
                            <span>
                                {{desData.downloadCount}}
                            </span>
                        </div>
                    </el-col>
                </el-row>
            </el-col>
        </el-row>
        <el-row>
            <el-col :span="12">
                <el-row>
                    <el-col :span="4">
                        <div class="grid-content bg-purple">
                            <label>数据格式：</label>
                        </div>
                    </el-col>
                    <el-col :span="20">
                        <div class="grid-content bg-purple-light">
                            <span>
                                {{desData.dataFormat}}
                            </span>
                        </div>
                    </el-col>
                </el-row>
            </el-col>
            <el-col :span="12">
                <el-row>
                    <el-col :span="4">
                        <div class="grid-content bg-purple">
                            <label>数据类型：</label>
                        </div>
                    </el-col>
                    <el-col :span="20">
                        <div class="grid-content bg-purple-light">
                            <span>
                                {{desData.datatype}}
                            </span>
                        </div>
                    </el-col>
                </el-row>
            </el-col>
        </el-row>
        <el-row>
            <el-col :span="2">
                <div class="grid-content bg-purple">
                    <label>关键字：</label>
                </div>
            </el-col>
            <el-col :span="22">
                <div class="grid-content bg-purple-light">
                    <el-tag
                        v-for="word in desData.keyword.split(';')"
                        :key="word">
                        {{word}}
                    </el-tag>
                </div>
            </el-col>
        </el-row>
        <el-row>
            <el-col :span="2">
                <div class="grid-content bg-purple">
                    <label>用户标签：</label>
                </div>
            </el-col>
            <el-col :span="22">
                <div class="grid-content bg-purple-light">
                    <el-tag
                        v-for="word in desData.tagStr.split(',')"
                        :key="word">
                        {{word}}
                    </el-tag>
                </div>
            </el-col>
        </el-row>
    </div>
</template>

<script>
  import axios from '$ui/utils/axios'
  import dataServerIp from '../assets/js/dataserverip'
  axios.defaults.baseURL = dataServerIp.dataServerIp
//   axios.defaults.baseURL = 'http://127.0.0.1:5000'
export default {
    props: {
        sdoid: {
            type: String,
            default: null
            }
    },

    watch: {
        sdoid(a, b) {
            axios.get('/datarecommendation/descDialog', {
                params: {
                sdoid: this.sdoid
                }
            })
            .then((response) => {
                this.desData = response.data.data
                // console.log(this.desData)
            })
            .catch(function (error) {
                console.log(error);
            });
        }
    },

    data() {
        return {
            desData: null
        }
    },
    created() {
      // 根据productSN请求数据
      axios.get('/datarecommendation/descDialog', {
        params: {
        sdoid: this.sdoid
        }
      })
      .then((response) => {
        this.desData = response.data.data
        console.log(this.desData)
      })
      .catch(function (error) {
        console.log(error);
      });
    } 
}
</script>

<style lang="scss" scoped>
    label {
        font-family: Microsoft YaHei; 
        font-size: 14px; 
        font-weight: 550; 
        font-style: normal; 
        color: blue; 
    }

    span {
        font-family: STKaiti; 
        font-size: 16px; 
        font-weight: 500; 
        font-style: normal; 
        color: black;
    }

  .el-row {
    margin-bottom: 20px;
    &:last-child {
      margin-bottom: 0;
    }
  }
  .el-col {
    border-radius: 4px;
  }
  .bg-purple-dark {
    background: white;
  }
  .bg-purple {
    background: white;
  }
  .bg-purple-light {
    background: white;
  }
  .grid-content {
    border-radius: 4px;
    min-height: 36px;
  }
  .row-bg {
    padding: 10px 0;
    background-color: #f9fafc;
  }
</style>
