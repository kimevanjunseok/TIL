# querySelector

> 제공한 선택자 또는 선택자 뭉치와 일치하는 문서 내 첫 번째 [`Element`](https://developer.mozilla.org/ko/docs/Web/API/Element)를 반환합니다. 일치하는 요소가 없으면 `null`을 반환합니다.

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

이렇게 출력한다.