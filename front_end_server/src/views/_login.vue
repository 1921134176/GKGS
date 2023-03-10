<template>
  <div class="bg">
    <my-login center pki :logo="logo" :login="login" :title="title" @success="handleSuccess" @pki="register">
      <div slot="extra">
            <!-- <el-checkbox>记住密码</el-checkbox> -->
      </div>
      <div slot="footer" style="text-align: right">
            <el-link type="primary" @click="loginHelp">登录帮助</el-link>
      </div>
    </my-login>
    <Wave width="100%" height="100%"></Wave>
  </div>
</template>

<script>
  import axios from '$ui/utils/axios'
  import dataServerIp from '../assets/js/dataserverip'
  axios.defaults.baseURL = dataServerIp.dataServerIp

  export default {
    components: {
      Wave: () => import('$ui/components/my-wave')
    },
    props: {
      // url查询参数名称
      urlQueryName: {
        type: String,
        default: 'url'
      },
      // 默认登录成功跳转页面地址
      defaultUrl: {
        type: String,
        default: '/layout'
      }
    },
    data() {
      return {
        title: '地学知识图谱应用平台',
        logo: require('../assets/logo03.png'),
        keyMap: {
          account: null,
          paaaword: null
        }
        } 
    },
    methods: {
      // login({account, password}) {
      //   // todo: 根据业务实现对接登录接口
      //   // this.$message(account + password)
      //   this.keyMap = {
      //     account: account,
      //     paaaword: password
      //   }   
      //   return new Promise((resolve, reject) => {
      //     axios.post('/login', {
      //       username: account,
      //       password: password
      //     })
      //     .then(function (response) {
      //       if(response.data.code === 200) {
      //         resolve({
      //             id: account,
      //             token: password
      //           }
      //         )
      //       } else {
      //         reject(response.data)
      //       }
      //       // console.log(response.data.msg)
      //     })
      //     .catch(function (error) {
      //       // console.log(error)
      //       reject(error)
      //     }) 
      //   })
      // },
      login({account, password}) {
        // todo: 根据业务实现对接登录接口
        // this.$message(account + password)
        this.keyMap = {
          account: account,
          paaaword: password
        }   
        return new Promise((resolve, reject) => {
          axios.post('/login', {
            username: account,
            password: password
          })
          .then(response => {
            if(response.data.code === 200) {
              resolve({
                  id: account,
                  token: password
                }
              )
            } else {
              reject(response.data)
            }
          })
          .catch(function (error) {
            console.log(error)
          }) 
        }) 
      },
      handleSuccess(res) {
        // 在此记录登录信息和跳转
        console.log(res)
        if (!this.$access) return
        this.$access.login(res)
        this.redirect()
        window.localStorage.setItem('username', res.id)
      },
      isSelf(url) {
        const {fullPath, path} = this.$route
        return url === fullPath || url === path || url === window.location.href
      },
      redirect() {
        const redirectUrl = this.$route.query[this.urlQueryName] || this.defaultUrl
        const path = decodeURIComponent(redirectUrl)
        // 如果准备要跳转的地址就是页面本身，不需要处理
        if (this.isSelf(path)) return
        const regex = /^http(s)?:\/\/.+/
        if (regex.test(path)) {
          window.location.href = path
        } else {
          this.$router.push(path)
        }
      },
      register() {
        if(this.keyMap.account === null || this.keyMap.paaaword === null) {
          this.$message.warning('请先尝试登录，提示用户不存在时点击注册！')
        } else {
          axios.post('/register', {
            username: this.keyMap.account,
            password: this.keyMap.paaaword
          })
          .then(response => {
            if(response.data.code === 200) {
              this.$message.success(response.data.msg)
            } else {
              this.$message.error(response.data.msg)
            }
          })
          .catch(function (error) {
            console.log(error);
          })
        }
        console.log(this.keyMap)
      },
      loginHelp() {
        this.$alert('先输入用户名和密码，点击登录，若提示用户不存在，再点击注册，注册成功会有消息提示。', '登录帮助', {
          confirmButtonText: '确定',
          center: true,
          type: 'info',
          callback: action => {
          }
        })
      }
    },
    created() {
      // 如果已经是登录状态，跳转到首页或指定页面
      if (this.$access && this.$access.isLogin()) {
        this.redirect()
      }
    }
  }
</script>

<style lang="scss" scoped>
  .bg {
    position: relative;
    width: 100%;
    height: 100%;
    background: url("../assets/kg02.png") center center;
  }

  .my-login {
    z-index: 3;
  }

  .my-wave {
    position: absolute;
    left: 0;
    bottom: 0;
  }
</style>
