# vue-page-transition

## 사용 방법

#### npm install

```powershell
$ npm install vue-page-transition
```

#### 모든 router에 적용(App.vue)

```vue
<vue-page-transition name="fade-in-right">
    <router-view/>
</vue-page-transition>
```

#### 원하는 router에 적용(router.js)

```javascript
import Vue from "vue";
import Router from "vue-router";

Vue.use(Router);

const router = new Router({
  mode: "history",
  base: process.env.BASE_URL,
  routes: [
      // ...
    {
      path: "/",
      name: "Loading",
      component: () => import("./components/Loading/Loading.vue"),
      meta: { transition: 'fade-in-right' }
    },
      // ...
  ]
});
```



> fade-in-right 뿐만아니라 다양한 기능은 [vue-page-transition](<https://www.npmjs.com/package/vue-page-transition>) 참조

