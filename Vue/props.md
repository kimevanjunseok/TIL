# props

### 데이터 전달하기

- 데이터를 보내는 component

  ```vue
  <template>
    <VueCheck msg="Welcome to Your Vue.js App"/> // msg라는 변수로 전달
  </template>
  <script>
  import VueCheck from './components/VueCheck.vue'
  
  export default {
    name: 'Send',
    components: {
      VueCheck
    }
  }
  </script>
  ```

- 데이터를 받는component

  ```vue
  <template>
    <div>
      {{msg}}
    </div>
  </template>
  
  <script>
  export default {
    name: 'VueCheck',
    props: {msg: String} // String, Number, Boolean, Array ...
  }
  </script>
  ```

  or

  ```vue
  <template>
    <div>
      {{msg}}
    </div>
  </template>
  
  <script>
  export default {
    name: 'VueCheck',
    props: ['msg']
  }
  </script>
  ```

  

### data() 에 저장되있는 데이터 보내기

- 데이터를 보내는 component

  ```vue
  <template>
    <VueCheck v-bind:info="array"/>
    // or
    <VueCheck :info="array"/>
  </template>
  <script>
  import VueCheck from './components/VueCheck.vue'
  
  export default {
    name: 'Send',
    components: {
      VueCheck
    },
    data() {
      return {
        array: [1, 2, 3, 4]
      }
    }
  }
  </script>
  ```

- 데이터를 받는component

  ```vue
  <template>
    <div>
      {{ list }}
    </div>
  </template>
  
  <script>
  export default {
    name: 'VueCheck',
    props: ['info'],
    data() {
      return {
        list: this.info //해당 component의 data 변수에 저장할 수 있다
      }
    },
  }
  </script>
  ```

###### 참고 문서 [Link](<https://kr.vuejs.org/v2/guide/components-props.html>)

