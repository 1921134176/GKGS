<template>
  <div class="wrapper">
    <my-pro :fixed="setting.fixed"
            :logo="logo"
            :title="title"
            :mode="setting.layout"
            :menus="menus"
            :menu-props="{router: true, uniqueOpened: true}"
            v-bind="colorTheme"
            :collapsible="setting.collapsible"
            :rainbow="setting.rainbow"
            version="1.0"
            :breadcrumb="createBreadcrumb"
            :tab="setting.tab ? createTab : null"
            :document-title="createDocumentTitle"
            sidebarTheme="light"
            navbarTheme="light"
            href="/welcome">

      <!-- 头部工具按钮 -->
      <template v-slot:actions>
        <UserAction :dropdown-items="dropdown"
                    :username="userInfo.name"
                    :extra="userInfo.role"
                    @command="handleUserCommand"
                    :avatar="{theme: 'primary'}">
        </UserAction>
        <!-- <IconAction icon="el-icon-message-solid" :badge="12"></IconAction> -->
        <!-- <IconAction icon="el-icon-info" @click="handleInfo"></IconAction> -->
        <FullScreenAction tooltip></FullScreenAction>
        <IconAction icon="icon-exit" svg  tooltip="退出" @click="handleInfo"></IconAction>
      </template>

      <!-- 加载子路由页面 -->
      <!-- 缓存的页面，缓存$route.meta.keepAlive为true的组件 -->
      <keep-alive>
        <router-view v-if="$route.meta.keepAlive && $route.name !== 'iframe'"></router-view>
        <!-- <router-view v-if="$route.meta.keepAlive"></router-view> -->
      </keep-alive>
      <!-- 不缓存的页面，不缓存$route.meta.keepAlive为false的组件 -->
      <router-view v-if="!$route.meta.keepAlive"></router-view>

      <!-- 解决iframe的缓存问题 -->
      <!-- key是为了将组件刷新一下，不然页面是乱的，并且引入firstTime变量，让页面只刷新一次 -->
      <div :key="iframeKey" v-show="$route.name === 'iframe'">
        <tongyongkg></tongyongkg>
      </div>
      
    </my-pro>
  </div>
</template>

<script>
  import logo from '../assets/logo03.png'
  import {MyPro, MyNavbar} from '$ui'
  import MockForExample from '$my/code/mixin/mock-for-example'
  import '$ui/icons/exit'
  import '$ui/icons/network-layout'
  import tongyongkg from '../components/tongyongkg'

  const {IconAction, UserAction} = MyPro
  const {FullScreenAction} = MyNavbar
  export default {
    mixins: [MockForExample],
    components: {
      MyPro,
      IconAction,
      UserAction,
      FullScreenAction,
      tongyongkg
    },
    data() {
      return {
        userInfo: {
          name: 'Admin',
          role: '普通用户'
        },
        setting: {
          skin: 'default',
          layout: 'navbar', // sidebar, navbar, both
          color: 'pro',
          fixed: true,
          collapsible: true,
          tab: false,
          breadcrumb: false,
          rainbow: true,
          invert: false
        },
        logo: logo,
        title: '地学知识图谱服务平台(GKGS)', // 地学知识图谱管理系统
        menus: [
          {
            text: '知识管理',
            index: '1',
            icon: 'el-icon-menu'
            },
          {
            text: '知识图谱',
            index: '2',
            icon: 'el-icon-magic-stick'
            },
          {
            text: '智能问答',
            index: '3',
            icon: 'el-icon-microphone'
            },
          {
            text: '数据推荐',
            index: '4',
            icon: 'el-icon-s-opportunity'
            },
          {
            text: '领域共享',
            index: '5',
            icon: 'el-icon-share',
            children: [
              {text: '国土领域', index: '5-1', icon: 'el-icon-position'},
              {text: '国土领域2', index: '5-2', icon: 'el-icon-position'}]
            }
        ],
        dropdown: [
          // {
          //   text: '个人信息',
          //   command: 'info'
          // },
          // {
          //   text: '修改密码',
          //   command: 'password'
          // },
          {
            // divided: true,
            text: '注销登录',
            command: 'logout'
          }
        ],
        iframeKey: 1,
        firstTime: true
      }
    },
    computed: {
      colorTheme() {
        const {color, layout, skin} = this.setting
        const map = {
          simple: 'light',
          tech: 'dark',
          pro: 'black'
        }
        if (layout === 'sidebar') {
          return {
            sidebarTheme: map[color],
            navbarTheme: skin === 'dark' ? 'dark' : 'light'
          }
        }
        if (layout === 'navbar') {
          return {
            sidebarTheme: 'light',
            navbarTheme: map[color]
          }
        }

        if (layout === 'both') {
          return {
            navbarTheme: map[color],
            sidebarTheme: skin === 'dark' ? 'dark' : 'light'
          }
        }

        return {
          navbarTheme: 'light',
          sidebarTheme: 'light'
        }

      }
    },
    watch: {
      $route () {
        // console.log(this.$route.name, '$route')
        if (this.$route.name === 'iframe' && this.firstTime) {
            this.iframeKey = -this.iframeKey
            this.firstTime = false
        }
        
      }
    },
    methods: {
      // 页面标题构建函数，可根据匹配的路由返回响应的标题名称
      createDocumentTitle(matched) {
        return matched.meta.title
          ? `${matched.meta.title} - MyWeb 4.x`
          : 'MyWeb 4.x'
      },
      handleUserCommand(cmd) {
        switch (cmd) {
          case 'info':
            this.$router.push('/account/center')
            break
          case 'password':
            this.$router.push('/account/settings')
            break
          case 'logout':
            this.logout().then(r => {
              this.$access.logout()
            })
            break
        }
      },
      createBreadcrumb() {
        if (!this.setting.breadcrumb) return null
        return this.$route.matched
          .filter(n => n.meta.title)
          .map(n => {
            return {
              label: n.meta.title,
              to: n.path || '/'
            }
          })
      },
      createTab(fullPath, matched) {
        if (!this.setting.tab) return null
        if (fullPath && matched) {
          const {icon, title, tab} = matched.meta
          if (title || tab) {
            return {
              label: tab || title,
              value: fullPath,
              path: matched.path,
              icon: icon,
              closable: fullPath !== '/dashboard/analysis'
            }
          }
          return null
        } else {
          // 缺省首页
          return {
            label: '分析页',
            value: '/dashboard/analysis',
            closable: false
          }
        }
      },
      handleInfo() {
        // 退出登录功能
        window.sessionStorage.clear()
        this.$router.push('/login')
        // window.location.href = 'http://newgateway.gitee.io/my/'
      }
    },
    created() {
      this.getMenus().then(res => {
        this.menus = res
      })
    },
    // created()：在创建vue对象时，当html渲染之前就触发；但是注意，全局vue.js不强制刷新或者重启时只创建一次，也就是说，created()只会触发一次；
    // activated()：在vue对象存活的情况下，进入当前存在activated()函数的页面时，一进入页面就触发；可用于初始化页面数据等
    activated() {
      this.userInfo.name = window.localStorage.getItem('username')
    }
  }
</script>

