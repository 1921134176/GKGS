# 地学知识图谱服务平台(GKGS)

## 简介

地学知识图谱服务平台(GKGS)是一种将知识图谱可视化与地学数据可视化相结合的Web平台。近些年，人工智能的发展使得学者们愈发重视知识对于人工智能系统的重要性，知识图谱成为人工智能的一个重要研究分支。应用方面，学者们也尝试将知识图谱与不同领域相结合，构建领域知识图谱，并利用领域知识图谱解决领域问题，提升领域的智能化水平。在地学领域，近些年也涌现了一些诸如城市知识图谱、环境知识图谱等领域知识图谱应用，但据本人所知，目前任然缺乏从地学领域数据获取到知识图谱构建到知识图谱可视化到知识图谱应用的完整研究。

![平台架构图](https://gitee.com/CHENGXIN0219/gkgsframe/blob/master/img/平台架构图.png)

GKGS就是在这样的背景下所诞生的想法，研究希望构建一个具有知识图谱管理、知识图谱应用等功能于一体的平台，来提供领域知识服务，提升领域的智能化水平。同时，平台必须具备操作简单优雅的特点，能可视化知识图谱并且能与之交互。地学知识图谱服务平台整体采用了B/S架构，且前后端分离，这种结构跨平台且有利于后期更新维护。

## 前端

**前端工具：** Nodejs14、Vue2.9.6、Echarts、ElementUI、MyWebUI等

**主要页面：**

1. **欢迎页(welcome.vue)**

   平台简介与快速导航。

   ![平台欢迎页](https://gitee.com/CHENGXIN0219/gkgsframe/blob/master/img/平台欢迎页.PNG)

2. **知识管理页(kgmanage_self.vue)**

   知识图谱的可视化创建、修改、查询与批处理。

   ![平台知识管理](https://gitee.com/CHENGXIN0219/gkgsframe/blob/master/img/平台知识管理.PNG)

3. **知识图谱页(tongyong.vue)**

   通用知识图谱的可视化查询与知识探索。

   ![平台知识图谱](https://gitee.com/CHENGXIN0219/gkgsframe/blob/master/img/平台知识图谱.PNG)

4. **智能问答页(qachatbot.vue)**

   知识图谱支持的问答系统，提供多模态返回结果。

   ![平台智能问答](https://gitee.com/CHENGXIN0219/gkgsframe/blob/master/img/平台智能问答.PNG)

5. **数据推荐页(view\list\card.vue)**

   知识图谱支持的推荐系统，基于产品节点间相似度进行推荐。

   ![平台数据推荐](https://gitee.com/CHENGXIN0219/gkgsframe/blob/master/img/平台数据推荐.PNG)

6. **领域共享页(guotu,vue)**

   知识图谱与遥感领域的结合。

   ![平台领域共享](https://gitee.com/CHENGXIN0219/gkgsframe/blob/master/img/平台领域共享.PNG)
   
   ![平台领域共享](https://gitee.com/CHENGXIN0219/gkgsframe/blob/master/img/数据获取.PNG)
   
   ![平台领域共享](https://gitee.com/CHENGXIN0219/gkgsframe/blob/master/img/异常数据检测.PNG)

**安装与运行：**

```text
npm install
npm run serve
```

## 后端

**后端工具：** python3.8、flask2.0.3、py2neo、geopandas0.9.0等

**安装与运行：**

```python3
python main.py
```

## 数据库

1、Neo4j4.3.2

知识图谱构建参考《[利用知识图谱的国土资源数据管理与检索研究](https://link.zhihu.com/?target=http%3A//ch.whu.edu.cn/cn/article/doi/10.13203/j.whugis20210714)》

2、SQLit

## 联系

**Email：** 1921134176@qq.com
