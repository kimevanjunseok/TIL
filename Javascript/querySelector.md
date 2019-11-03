# querySelector

> 제공한 선택자 또는 선택자 뭉치와 일치하는 문서 내 첫 번째 [`Element`](https://developer.mozilla.org/ko/docs/Web/API/Element)를 반환합니다. 일치하는 요소가 없으면 `null`을 반환합니다.

### 구문

```
document.querySelector(selector)
```

### 사용법

```html
<div class="class-div">div</div>
<script>
    const click_button = document.querySelector('.class-div')
    console.log(click_button)
</script>
```

콘솔(click_button 값)

```html
<div class="class-div">div</div>
```

문서 내 첫 번째 `Element`를 반환한다는 뜻은

```html
<div class="class-div">div1</div>
<div class="class-div">div2</div>
<script>
    const click_button = document.querySelector('.class-div')
    console.log(click_button)
</script>
```

이런 경우 콘솔에서

```html
<div class="class-div">div1</div>
```

이렇게 출력된다.

### prepend

> javascript에서 추가할 수있다.

```html
<h1>prepend</h1>
<div class="add"></div>
<script>
    document.querySelector('.add').prepend('hi')
</script>
```

출력 결과

<img width="773" alt="캡처" src="https://user-images.githubusercontent.com/45934117/68082401-6ddc1980-fe5f-11e9-8f61-3f5b80e30ad9.PNG">

