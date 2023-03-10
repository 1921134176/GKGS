<template>
  <div :id="uuid" :style="style"></div>
</template>

<script>
import * as echarts from 'echarts'

const idGen = () => {
  return new Date().getTime()
}

export default {

  props: {

    height: {
      type: String,
      default: '400px'
    },
    width: {
      type: String,
      default: '600px'
    },

    options: {
      type: Object,
      default: null
    }

  },

  data() {
    return {
      uuid: null,
      myChart: null
    }
  },

  watch: {

    width(a, b) {
      if (this.myChart) {
        setTimeout(() => {
          this.myChart.resize({
            animation: {
              duration: 300
            }
          })
        }, 0);
      }
    },

    // options() {
    //   if (this.myChart) {
    //     this.myChart.setOption(this.options, {
    //       notMerge: true
    //     })

    //   }
    //   console.log('watch')
    // }
    options: {
      // 深度监听，否则无法监听到对象里面key里面value的变化
      deep: true,
      handler(newValue, oldValue) {
        if (this.myChart) {
          this.myChart.setOption(this.options, {
          notMerge: false // 如果设置opts.notMerge为true，那么旧的组件会被完全移除，新的组件会根据option创建。
        })
      }
      }
    }
  },

  computed: {

    style() {
      return {
        height: this.height,
        width: this.width
      }
    }

  },

  created() {
    this.uuid = idGen()
  },

  mounted() {
    // 准备实例
    this.myChart = echarts.init(document.getElementById(this.uuid));

    // 应用配置项
    this.myChart.setOption(this.options);

    // 点击事件
    this.myChart.on('click', (params) => {
      // 父组件用 @clickNode = ‘你的方法’
      this.$emit('clickNode', params);
    })

    // 双击事件
    this.myChart.on('dblclick', (params) => {
      // 父组件用 @dblclickNode = ‘你的方法’
      this.$emit('dblclickNode', params);
    })
  }
}
</script>