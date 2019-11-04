# How to get current name of route in Vue

### watch 사용

> component 이동할때마다 값을 저장(Redirect X)

```javascript
// ...
data() {
    return {
        urldata: "",
    }
},
watch: {
    '$route': function(route){
        this.urldata = route.name // 해당 component의 name를 출력한다
    } 
}
// ...
```

### created or mounted 사용

> component가 redirect 될 때 저장

```javascript
// ...
data() {
    return {
        urldata: "",
    }
},
created() {
    this.urldata = window.location.pathname // router에 설정한 path를 출력한다
},
// or
mounted() {
    this.urldata = window.location.pathname // router에 설정한 path를 출력한다
},
// ...
```