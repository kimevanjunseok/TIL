# innerText

> 요소와 그 자손의 "렌더링"된 텍스트 콘텐츠를 나타냅니다.

### 구문

```
element.innerText
```

### 사용법

```html
<button onclick="myFunction()">버튼</button>
<p id="check">first</p>
<script>
    function myFunction() {
        document.getElementById("check").innerText = 'second'
    }
</script>
```

<img width="636" alt="캡처" src="https://user-images.githubusercontent.com/45934117/68082628-80a41d80-fe62-11e9-9524-9d3ddf875dcc.PNG">

버튼 누른 후

<img width="618" alt="캡처" src="https://user-images.githubusercontent.com/45934117/68082617-62d6b880-fe62-11e9-841e-8c35500fbd82.PNG">

[innerHTML와innerText차이](./innerHTML와innerText차이.md)