# innerHTML와innerText차이

### innerHTML

```html
<p id="check"></p>
<script>
    document.getElementById("check").innerHTML = '<h1>second<h1>'
</script>
```

<img width="585" alt="캡처" src="https://user-images.githubusercontent.com/45934117/68082734-79314400-fe63-11e9-8590-e19b75f77c2c.PNG">

### innerText

```html
<p id="check"></p>
<script>
    document.getElementById("check").innerText = '<h1>second<h1>'
</script>
```

<img width="587" alt="캡처" src="https://user-images.githubusercontent.com/45934117/68082744-982fd600-fe63-11e9-8ba0-2652d25ba4dd.PNG">

결과

> innerHTML는 태그를 적용시키지만, innerText는 텍스트 그대로 출력시킴