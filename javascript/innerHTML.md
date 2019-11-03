# innerHTML

> 요소(element) 내에 포함 된 HTML 또는 XML 마크업을 가져오거나 설정합니다.

### 구문

```
element.innerHTML
```

### 사용법

```html
<button onclick="myFunction()">버튼</button>
<p id="check">first</p>
<script>
    function myFunction() {
        document.getElementById("check").innerHTML = 'second'
    }
</script>
```

<img width="636" alt="캡처" src="https://user-images.githubusercontent.com/45934117/68082628-80a41d80-fe62-11e9-9524-9d3ddf875dcc.PNG">

버튼 누른 후

<img width="618" alt="캡처" src="https://user-images.githubusercontent.com/45934117/68082617-62d6b880-fe62-11e9-841e-8c35500fbd82.PNG">

태그도 적용된다.

```html
<button onclick="myFunction()">버튼</button>
<p id="check">first</p>
<script>
    function myFunction() {
        document.getElementById("check").innerHTML = '<h1>second</h1>'
    }
</script>
```

<img width="690" alt="캡처" src="https://user-images.githubusercontent.com/45934117/68082850-2bb5d680-fe65-11e9-8fbc-62c4d756404c.PNG">

[innerHTML와innerText차이](./innerHTML와innerText차이.md)