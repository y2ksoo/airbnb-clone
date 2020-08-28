# Django Study Note4

## TailwindCSS

- CSS framework

- node.js

  - 자바스크립트의 서버사이드 언어

  - npm(node package manager): node.js 기반 패키시 모듈 관리도구

- gulp

  - 자동화 빌드 시스템 : JS 또는 CSS의 반복작업을 처리해 줌

### 동작과정

```js
const css = () => {
  const postCSS = require("gulp-postcss");
  const sass = require("gulp-sass");
  const minify = require("gulp-csso");
  sass.compiler = require("node-sass");
  return gulp
#1    .src("assets/scss/styles.scss")
#2    .pipe(sass().on("error", sass.logError))
#3    .pipe(postCSS([require("tailwindcss"), require("autoprefixer")]))
#4    .pipe(minify())
#5    .pipe(gulp.dest("static/css"));
};
```

1. assets/scss/styles.scss 에 tailwind class를 이용해서 표현

2. sass를 css 파일로 변환

3. tailwind macro를 해석후 일반 css로 변화

4. 코드 정리

5. static/css 에 브라우저가 해석할 수 있는 일반 css 생성

- scss 파일만 수정하면 됨!!!

- scss 파일 수정 후 css 파일을 수정하기 위해 "npm run css" 실행

### rem 이란?

- em = font-size

  em은 가장 가까운 거리에 정의된 font-size를 기준으로 크기를 결정하는 단위이다

- root em

  root font-size와 관련됨.

  페이지에 설정된 기본 font-size에 의해 결정됨

### responsible design

- 화면 크기에 따라 변화하는 객체 만들기
