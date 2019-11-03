# addEventListener

> 지정한 이벤트가 대상에 전달될 때마다 호출할 함수를 설정합니다.

### 구문

```html
target.addEventListener(type, listener[, options])
```

### 사용법

```html
<div class="class-div">div</div>
<script>
    const click_button = document.querySelector('.class-div')
    function clickfunc() {
        console.log(1)
    }
    click_button.addEventListener('click', clickfunc)
</script>
```

콘솔에서

```
1
```

클릭할 때마다 함수가 실행된다.

```html
<button class="class-btn">div</button>
<div class="div-cnt"></div>
<script>
    const click_button = document.querySelector('.class-btn')
    const div_cnt = document.querySelector('.div-cnt')
    let cnt = 0
    click_button.addEventListener('click', event => {
        cnt += 1
        div_cnt.innerHTML = cnt
    })
</script>
```

클릭 할때마다 cnt가 증가한다.