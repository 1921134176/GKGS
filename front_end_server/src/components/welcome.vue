<template>
    <div>
        <el-carousel height="100%" direction="vertical" :autoplay="true" >
            <el-carousel-item>
                <div class="page1">
                    <div style="text-align:center;">
                        <div style="font-weight: 900; font-size: 50px; margin: 20px 0 20px 0;; color: white;">
                            地学知识图谱服务平台(GKGS)
                        </div>
                        <div style="font-weight: 500; font-size: 30px; margin: 40px 0 20px 0;; color: white;">
                            Knowledge based geographic information service platform
                        </div>
                        <div style="font-weight: 500; font-size: 25px; margin: 20px 0 20px 0; color: white;">
                            数据处理+知识驱动+知识服务
                        </div>
                    </div>
                    <div class="page1-footer">
                        <div id='earth'></div>
                        <div class="avatar1" @click="urlPush('/1')">
                            <el-popover
                                placement="left"
                                title="知识管理"
                                width="200"
                                trigger="hover"
                                content="主要用于知识图谱的可视化增删查改。">
                                <el-avatar :size="60" :src="circleUrl1" fit="cover" slot="reference"></el-avatar>
                            </el-popover>
                        </div>
                        <div class="avatar2" @click="urlPush('/2')">
                            <el-popover
                                placement="left"
                                title="知识图谱"
                                width="200"
                                trigger="hover"
                                content="中文通用知识图谱与地学知识图谱的结合，可进行可视化交互。">
                                <el-avatar :size="60" :src="circleUrl2" fit="cover" slot="reference"></el-avatar>
                            </el-popover>
                        </div>
                        <div class="avatar3" @click="urlPush('/3')">
                            <el-popover
                                placement="left"
                                title="智能问答"
                                width="200"
                                trigger="hover"
                                content="以知识图谱作为知识图库，问答结果简洁、准确、丰富。">
                                <el-avatar :size="60" :src="circleUrl3" fit="cover" slot="reference"></el-avatar>
                            </el-popover>
                        </div>
                        <div class="avatar4" @click="urlPush('/4')">
                            <el-popover
                                placement="right"
                                title="数据推荐"
                                width="200"
                                trigger="hover"
                                content="数据产品知识图谱辅助的推荐，推荐结果准确、丰富、可交互。">
                                <el-avatar :size="60" :src="circleUrl4" fit="cover" slot="reference"></el-avatar>
                            </el-popover>
                        </div>
                        <div class="avatar5" @click="urlPush('/5-1')">
                            <el-popover
                                placement="right"
                                title="国土领域"
                                width="200"
                                trigger="hover"
                                content="国土领域知识图谱，创新的国土数据管理、获取与挖掘平台。">
                                <el-avatar :size="60" :src="circleUrl5" fit="cover" slot="reference"></el-avatar>
                            </el-popover>
                        </div>
                    </div>
                </div>
            </el-carousel-item>
            <el-carousel-item>
                <div>
                    <el-row>
                        <el-col :span="2">
                            <div class="page2-title">
                                地学领域共享平台导航页
                            </div>
                        </el-col>
                        <el-col :span="22">
                            <div style="margin: 50px 20px 20px 0px;">
                                <my-card-list :data="data" :columns="columns">
                                    <el-card slot-scope="{item}" :body-style="{ padding: '0px' }" shadow="hover">
                                        <a :href="item[1]">
                                            <el-image
                                            :src="item[0]"
                                            fit="scale-down">
                                            </el-image>
                                        </a>
                                    </el-card>
                                </my-card-list>
                            </div>
                        </el-col>
                    </el-row>
                </div>
            </el-carousel-item>
            <el-carousel-item>
                <el-carousel height="100%">
                    <el-carousel-item class="subcarousel">
                        <div class="page3-1">
                            <div style="text-align:center; position: absolute; top:200px; left: 23%;">
                                <div style="font-weight: 900; font-size: 50px; margin: 20px 0 20px 0;; color: white;">
                                    地像天图课题组(Sky Earth)
                                </div>
                                <div style="font-weight: 500; font-size: 30px; margin: 40px 0 20px 0;; color: white;">
                                    School of Remote Sensing and Information Engineering, Wuhan University
                                </div>
                                <div style="font-weight: 500; font-size: 25px; margin: 20px 0 20px 0; color: white;">
                                    遥感影像处理+LiDAR数据处理+知识图谱服务
                                    <a href="https://skyearth.org/">
                                        <i class="el-icon-arrow-right"></i>
                                    </a>
                                </div>
                            </div>
                        </div>
                    </el-carousel-item>
                    <el-carousel-item class="subcarousel">
                        <div class="page3-2">
                            <el-row>
                                <el-col :span="8">
                                    <my-description  title="标题居中" :width="100" top align="center">
                                        <el-image slot="title" :src="page32aSrc" fit="cover" style="height:400px"></el-image>
                                        <div style="text-align:center;">
                                            <div style="font-weight: 600; font-size: 20px; margin: 20px 0 20px 0;; color: white;">
                                                超大范围多源遥感卫星影像联合智能处理与地物信息提取理论方法
                                            </div>
                                            <div style="font-weight: 400; font-size: 20px; margin: 20px 0 20px 0;; color: white;">
                                                School of Remote Sensing and Information Engineering, Wuhan University
                                            </div>
                                            <div style="font-weight: 300; font-size: 18px; margin: 20px 0 20px 0; padding: 0 20px; color: white;">
                                                卫星遥感具有实时性强、覆盖范围广、信息量丰富等优势，但是遥感信息的生产和服务能 力严重滞后，多源遥感卫星影像联合处理应用是地球系统观测和多源数据融合的核心科学问题 。针对遥感对地观测领域的世界科技前沿热点和国家重大工程的迫切需求，立足二十年多源遥 感影像多特征一体化处理研究积累，提出超大范围多源遥感卫星影像联合智能处理与地物信息 提取理论方法的创新研究设想。重点围绕多模态遥感卫星影像高可靠性匹配、多星多载荷一体 化联合在轨几何检校、混合区域网平差、多时相影像合成、基于深度学习的地物信息智能提取 及全链路不确定性分析等前沿科学问题展开理论探索和算法研究，形成“理论架构－联合处理 －信息提取－不确定性分析”有机整合的研究范式，充分发挥每颗卫星、每个波段、每个有效 像元的作用，以期突破美国新一轮遥感领域技术封锁，为全球地理信息资源建设、一带一路倡 议、突发灾害应急响应、自然资源监测等重大工程提供国际一流技术支撑。
                                                <a href="https://skyearth.org/projects/">
                                                    <i class="el-icon-arrow-right"></i>
                                                </a>
                                            </div>
                                        </div>
                                    </my-description> 
                                </el-col>
                                <el-col :span="8">
                                    <my-description  title="标题居中" :width="100" top align="center">
                                        <el-image slot="title" :src="page32bSrc" fit="cover" style="height:400px"></el-image>
                                        <div style="text-align:center;">
                                            <div style="font-weight: 600; font-size: 20px; margin: 20px 0 20px 0;; color: white;">
                                                结合LiDAR点云和多视角航空影像的建筑物结构化模型重建理论与方法
                                            </div>
                                            <div style="font-weight: 400; font-size: 20px; margin: 20px 0 20px 0;; color: white;">
                                                School of Remote Sensing and Information Engineering, Wuhan University
                                            </div>
                                            <div style="font-weight: 300; font-size: 18px; margin: 20px 0 20px 0; padding: 0 20px; color: white;">
                                                LiDAR点云与航空影像联合进行建筑物三维重建相比单一数据源的传统方法有突出优势。 本项目率先提出结合机载LiDAR点云和多视角航空影像的建筑物结构化模型重建理论与方法， 创造性地提出线框与三角网混合的矢量模型构建思想，基于线面特征互约束机制，利用点云精 确三维几何信息提取平面特征和影像丰富纹理信息提取直线特征，共同构建带有精细纹理且包 含建筑物角点间拓扑关系的结构化矢量模型。重点围绕基于线面特征的三维点云表面重建、基 于影像纹理识别的建筑物立面修复、保证纹理映射最优的两步法模型简化、线框与三角网混合 的建筑物矢量模型提取等核心问题展开系统深入的理论探索和算法研究，并研发基于机载LiDA R点云与多视角航空影像的建筑物结构化三维重建原型系统，验证相关理论和算法的正确性和 有效性。研究成果可为通用化矢量模型重建提供有效的解决方案，并为智能建筑、新型智慧城 市、城市三维数据库等应用奠定坚实的理论和技术基础。
                                                <a href="https://skyearth.org/projects/">
                                                    <i class="el-icon-arrow-right"></i>
                                                </a>
                                            </div>
                                        </div>
                                    </my-description> 
                                </el-col>
                                <el-col :span="8">
                                    <my-description  title="标题居中" :width="100" top align="center">
                                        <el-image slot="title" :src="page32cSrc" fit="cover" style="height:400px"></el-image>
                                        <div style="text-align:center;">
                                            <div style="font-weight: 600; font-size: 20px; margin: 20px 0 20px 0; color: white;">
                                                人工智能驱动的领域知识建模与深度共享服务
                                            </div>
                                            <div style="font-weight: 400; font-size: 20px; margin: 20px 0 20px 0;; color: white;">
                                                School of Remote Sensing and Information Engineering, Wuhan University
                                            </div>
                                            <div style="font-weight: 300; font-size: 18px; margin: 20px 0 20px 0; padding: 0 20px; color: white;">
                                                针对我国现有遥感观测成果知识化建模和智能化知识服务能力较弱，未能为国家重大战略应用提供有力决策支持的现状，本项目将重点开展领域知识建模、深度共享与服务加速技术的研究，解决全球综合观测成果领域知识高可信知识建模、需求驱动的知识服务以及高效深度共享服务等问题。具体包括：研究遥感对象解译和“推理-验证”协同的领域知识本体迭代建模方法，设计和创建国土、海洋、测绘、气象和环境五大领域的本体知识库；研究需求驱动的智能知识服务框架，发展面向五大领域专业分析模型和人工智能分析模型的领域模型知识库；构建五大领域知识图谱和面向应用场景的语义单元，研究十大典型应用场景知识的自动化构建，结合领域本体和模型知识库共同形成“中国遥感应用智库”知识支撑；研究涵盖知识建模、推理与服务的多粒度计算服务加速方法技术，实现知识化服务全流程加速；研究知识图谱检索和基于图谱推理的场景决策方法，设计用户知识获取与推送反馈环路，构筑决策知识深度共享模式。
                                                <a href="https://skyearth.org/projects/">
                                                    <i class="el-icon-arrow-right"></i>
                                                </a>
                                            </div>
                                        </div>
                                    </my-description> 
                                </el-col>
                            </el-row>
                        </div>
                    </el-carousel-item>
                </el-carousel>
            </el-carousel-item>
            <el-carousel-item>
                <div class="page4">
                    <my-map 
                    :zoom="17" 
                    :center="[114.353, 30.528]"
                    height="100%">
                        <my-map-scatter 
                        :coordinate="[114.3567, 30.5278]"
                        fill="red"
                        :radius="10"
                        :stroke="{width:4, color:'#fff'}">
                        </my-map-scatter>
                        <my-map-placement placement="left-center">
                            <el-card>
                                <table style="font-weight: 300; font-size: 15px;">
                                    <tr>
                                        <td>电子邮件: </td>
                                        <td>chengxin_w@whu.edu.cn</td>
                                    </tr>
                                    <tr>
                                        <td>通讯地址: </td>
                                        <td>武汉市珞喻路129号武汉大学遥感信息工程学院</td>
                                    </tr>
                                    <tr>
                                        <td>邮政编码: </td>
                                        <td>430079</td>
                                    </tr>
                                </table>
                            </el-card>
                        </my-map-placement>
                    </my-map>
                </div>
            </el-carousel-item>
        </el-carousel>
    </div>
</template>

<script>
    import axios from '$ui/utils/axios'
    import dataServerIp from '../assets/js/dataserverip'
    axios.defaults.baseURL = dataServerIp.dataServerIp
    export default {
        data () {
            return {
                circleUrl1: dataServerIp.dataServerIp + '/welcome/page1/01.png',
                circleUrl2: dataServerIp.dataServerIp + '/welcome/page1/02.png',
                circleUrl3: dataServerIp.dataServerIp + '/welcome/page1/03.png',
                circleUrl4: dataServerIp.dataServerIp + '/welcome/page1/04.png',
                circleUrl5: dataServerIp.dataServerIp + '/welcome/page1/05.png',
                data: null,
                columns: {
                    xxl: 8,
                    xl: 5,
                    lg: 4,
                    md: 3,
                    sm: 2,
                    xs: 1
                    },
                page32aSrc: dataServerIp.dataServerIp + '/welcome/page1/page3-2.jpg',
                page32bSrc: dataServerIp.dataServerIp + '/welcome/page1/page3-2b.jpg',
                page32cSrc: dataServerIp.dataServerIp + '/welcome/page1/page3-2c.jpg'
            }
        },
        methods: {
            urlPush(url) {
                // this.$message(url)
                this.$router.push(url)
            }
        },
        created() {
            axios.get('/welcome/page2')
            .then((response) => {
                this.data = response.data.data
                // console.log(response)
            })
            .catch(function (error) {
                console.log(error);
            })
        }

    }
</script>

<style lang="scss" scoped>
  .el-carousel {
    position: absolute;
    width: 100%;
    top: 0;
    left: 0;
    bottom: 0;
  }

  .page1 {
    display: flex;
    flex-direction: column;
    justify-content: space-around;
    align-items: center;
    background: url(../assets/bg4.png) no-repeat;
    top: 0;
    left: 0;
    width:100%;
    height:100%;
    background-size: cover;
    -webkit-background-size: cover;
    -o-background-size: cover;
    background-position: center 0;
  }

  .page1-footer {
    // display: flex;
    // flex-direction: row;
    // justify-content: space-around;
    // align-items: center;
    // width: 70%;
    position: relative;
    // background-color: aliceblue;
  }

  #earth {
    border-radius: 50%;
    width: 330px;
    height: 330px;
    background: url(../assets/dq_bg_3.png);
  }

  .avatar1 {
    position: absolute;
    top: 50%;
    left: -70px;
    transform: translate(0, -50%);
    width: 60px;
    height: 60px;
    // background-color: red;
    border-radius: 50%;
  }

  .avatar2 {
    position: absolute;
    top: 282px;
    left: -12px;
    // transform: translate(-50%, -50%);
    // transform: rotate(45deg);
    width: 60px;
    height: 60px;
    // background-color: red;
    border-radius: 50%;
  }

  .avatar3 {
    position: absolute;
    top: 340px;
    left: 165px;
    transform: translate(-50%, 0);
    width: 60px;
    height: 60px;
    // background-color: red;
    border-radius: 50%;
  }

  .avatar4 {
    position: absolute;
    top: 282px;
    left: 282px;
    // transform: translate(-50%, -50%);
    // transform: rotate(45deg);
    width: 60px;
    height: 60px;
    // background-color: red;
    border-radius: 50%;
  }

  .avatar5 {
    position: absolute;
    top: 50%;
    left: 340px;
    transform: translate(0, -50%);
    width: 60px;
    height: 60px;
    // background-color: red;
    border-radius: 50%;
  }

  .page2-card {
    display: flex;
    flex-direction: row;
    justify-content: space-around;
    flex-wrap: wrap;
    align-items: center;
  }

  .page2-title {
    font-family: STFangsong;
    font-weight: 900; 
    font-size:55px; 
    margin: 40px auto;
    color: rgb(15, 3, 119);
    writing-mode:vertical-rl;
  }

  .page3-1 {
    background: url(../assets/free_bg.png) no-repeat;
    width:100%;
    height:100%;
    top: 0;
    left: 0;
    background-size: cover;
    -webkit-background-size: cover;
    -o-background-size: cover;
    background-position: center 0;
  }

  .page3-2 {
    width:100%;
    height:100%;
    padding: 20px;
    top: 0;
    left: 0;
    background-size: cover;
    -webkit-background-size: cover;
    -o-background-size: cover;
    background-position: center 0;
  }

  .page4 {
    width:100%;
    height:100%;
    padding: 0 15px 0 0;
    background-color: #d3d5d6;;
    top: 0;
    left: 0;
    background-size: cover;
    -webkit-background-size: cover;
    -o-background-size: cover;
    background-position: center 0;
  }

  .image {
    width: 100%;
    display: block;
  }

  .button {
    padding: 0px 0px 10px 0px;
    float: right;
  }

  .bottom {
    margin-top: 13px;
    line-height: 12px;
  }
  
//   .el-carousel__item:nth-child(2n) {
//     background-color: #99a9bf;
//   }
  
//   .el-carousel__item:nth-child(2n+1) {
//     background-color: #000142;
//   }
  .el-carousel__item {
    background-color: #eceef3;
  }

  .subcarousel {
    background-color: #010a22;
  }

// 华文细黑：STHeiti Light [STXihei] 
// 华文黑体：STHeiti 
// 华文楷体：STKaiti 
// 华文宋体：STSong 
// 华文仿宋：STFangsong 
// 儷黑 Pro：LiHei Pro Medium 
// 儷宋 Pro：LiSong Pro Light 
// 標楷體：BiauKai 
// 蘋果儷中黑：Apple LiGothic Medium 
// 蘋果儷細宋：Apple LiSung Light 
// Windows的一些： 
// 新細明體：PMingLiU 
// 細明體：MingLiU 
// 標楷體：DFKai-SB 
// 黑体：SimHei 
// 宋体：SimSun 
// 新宋体：NSimSun 
// 仿宋：FangSong 
// 楷体：KaiTi 
// 仿宋_GB2312：FangSong_GB2312 
// 楷体_GB2312：KaiTi_GB2312 
// 微軟正黑體：Microsoft JhengHei 
// 微软雅黑体：Microsoft YaHei 
// 装Office会生出来的一些： 

// 隶书：LiSu 
// 幼圆：YouYuan 
// 华文细黑：STXihei 
// 华文楷体：STKaiti 
// 华文宋体：STSong 
// 华文中宋：STZhongsong 
// 华文仿宋：STFangsong 
// 方正舒体：FZShuTi 
// 方正姚体：FZYaoti 
// 华文彩云：STCaiyun 
// 华文琥珀：STHupo 
// 华文隶书：STLiti 
// 华文行楷：STXingkai 
// 华文新魏：STXinwei
</style>
