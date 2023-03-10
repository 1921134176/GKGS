<template>
  <!-- <div>
    <iframe
      src="https://kg.ownthink.com/knowledge.html"
      id="mobsf"
      frameborder="0"
      style="position: absolute"
    ></iframe>
  </div> -->
  <div align="center" style="margin:0 auto;">
    <div style="width:100%;height:907px;overflow:hidden;border:0px"> 
      <div style="margin:-122px 0px 0px -10px;position:relative">
        <iframe src="https://kg.ownthink.com/knowledge.html" id="mobsf" scrolling="no" frameborder="0"
          style="position:absolute;  //这里的position = acsolute也是必须的
          width: 100%;
          height: 100vh;
          display:block;
          left: 0;
          right:0;">
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
      mobsf.style.height = Number(deviceHeight) + 100 + 'px' // 数字是页面布局高度差
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
