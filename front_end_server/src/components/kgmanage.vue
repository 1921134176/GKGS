<template>
  <!-- <div>
    <iframe
      src="https://kg.ownthink.com/knowledge.html"
      id="mobsf"
      frameborder="0"
      style="position: absolute"
    ></iframe>
  </div> -->
  <!-- 直接拿三方网页嵌入的知识管理页面 -->
  <div align="center" style="margin:0 auto;">
    <div style="width:100%;height:907px;overflow:hidden;border:0px"> 
      <div style="margin:0px 0px 0px 0px;position:relative">
        <iframe src="https://graphxr.kineviz.com/Projects" id="mobsf" scrolling="no" frameborder="0"
          style="position:absolute;  //这里的position = acsolute也是必须的
          width: 100%;
          height: 1118px;
          display:block;
          left: 0;
          right:0;
          transform-origin: left top;
          transform: scale(1, 0.82)">
        </iframe>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {};
  },
  mounted() {
    /**
     * iframe-宽高自适应显示
     */
    function changeMobsfIframe() {
      const mobsf = document.getElementById('mobsf');
      const deviceWidth = document.body.clientWidth;
      const deviceHeight = document.body.clientHeight;
      mobsf.style.width = Number(deviceWidth) + 10 + 'px' // 数字是页面布局宽度差值
      mobsf.style.height = Number(deviceHeight) + 150 + 'px' // 数字是页面布局高度差
    }

    changeMobsfIframe();

    window.onresize = function () {
      changeMobsfIframe();
    };
  }
  
};
</script>

<style lang="scss" scoped>
</style>
