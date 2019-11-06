# Router

### 설치

```bash
npm install vue-router
```

### 설정

- src폴더에 router.js 파일 만들고 다음과 같이 작성

  ```javascript
  import Vue from "vue";
  import Router from "vue-router";
  
  Vue.use(Router);
  
  const router = new Router({
  	mode: "history",
      base: process.env.BASE_URL,
      routes: [
          {
            path: "/경로",
            name: "이름",
            component: () => import("해당 component 파일 경로"),
            meta: { requiresAuth: true }
          },
      ]
  })
  export default router;
  ```

- main.js

  ```javascript
  // ...
  import router from './router'
  // ...
  new Vue({
    router, // 추가
    render: h => h(App),
  }).$mount('#app')
  ```

- App.vue

  ```html
  <template>
    <div id="app">
      <router-view></router-view> <!-- 추가 -->
    </div>
  </template>
  
  ```



### 궁금증

- router.js에서 mode: "history"하는 이유 [Link](<https://router.vuejs.org/kr/guide/essentials/history-mode.html>)

- router.js에서 base: process.env.BASE_URL하는 이유 [Link](<https://cli.vuejs.org/guide/mode-and-env.html#modes>)

