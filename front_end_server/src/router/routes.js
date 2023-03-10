import _login from '../views/_login.vue'
import _layout from '../views/_layout.vue'
import cardlist from '../views/list/card.vue'
import guotu from '../components/guotu.vue'
import guotu2 from '../components/guotu2.vue'
import tongyongkg from '../components/tongyongkg'
import qarobot from '../components/qarobot'
// import kgmanage from '../components/kgmanage'
import kgmanage from '../components/kgmanage_self.vue'
import welcome from '../components/welcome'
export default function ({get}) {
  return [
    {
      path: '/',
      redirect: '/login',
      meta: {keepAlive: false }
    },
    {
      path: '/login',
      component: _login,
      meta: {keepAlive: false },
      props: true
    }, 
    {
      path: '/layout',
      component: _layout,
      redirect: '/welcome',
      meta: {
        title: '知识管理主页',
        keepAlive: true // 需要缓存
      },
      props: true,
      children: [
        { path: '/welcome', component: welcome, meta: {keepAlive: true } },
        { path: '/1', component: kgmanage, meta: {keepAlive: true } },
        { path: '/2', name: 'iframe', component: tongyongkg, meta: {keepAlive: true }},
        { path: '/3', component: qarobot, meta: {keepAlive: true } },
        { path: '/4', component: cardlist, meta: {keepAlive: true } },
        { path: '/5-1', component: guotu, meta: {keepAlive: true } },
        { path: '/5-2', component: guotu2, meta: {keepAlive: true } }
      ]
    }
  ]
}
