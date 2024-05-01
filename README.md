# 🛠️ **[웹 프로젝트](https://github.com/leejinwon012/Sparta-Market)** 참조해 퓨어 장고 DRF 변환

이 프로젝트는 Django를 사용하여 사용자 및 상품을 관리하는 RESTful API를 구축한 것입니다. 사용자는 등록하고 로그인하여 개인 프로필을 관리하고, 상품은 등록하고 관리할 수 있습니다.

<br/>

## 프로젝트 일정 📅
개발 기간: 2024년 04월 29일(월) - 2024년 05월 02일(목)

<br/>

## 기능

### 사용자 등록 📝

사용자는 회원가입 양식을 통해 계정을 생성할 수 있습니다. 필수 정보로는 사용자 이름, 이메일, 비밀번호가 있습니다.

<br/>

### 사용자 로그인 🔐

등록한 계정으로 로그인하여 인증 토큰을 받습니다. 이 토큰을 사용하여 API 엔드포인트에 접근할 수 있습니다.

<br/>

### 사용자 관리 :scroll:

- **사용자 등록**: 사용자는 회원가입 양식을 통해 계정을 생성할 수 있습니다.
- **사용자 인증**: JWT(JSON Web Token)를 사용하여 사용자를 인증합니다.
- **사용자 프로필 조회 및 수정**: 인증된 사용자는 자신의 프로필을 조회하고 수정할 수 있습니다.

<br/>

### 상품 관리 📦

- **상품 등록**: 사용자는 상품의 제목, 내용, 이미지 등을 포함하여 새로운 상품을 등록할 수 있습니다.
- **상품 조회**: 등록된 상품 목록을 조회할 수 있습니다. 각 상품에는 제목, 내용, 이미지, 등록자 정보, 등록일시가 표시됩니다.
- **상품 수정 및 삭제**: 상품 등록자는 자신이 등록한 상품을 수정하거나 삭제할 수 있습니다.

<br/>

## 사용법 :page_with_curl:

1. **사용자 등록**: 회원가입 양식을 통해 계정을 생성합니다.
2. **사용자 인증**: 등록한 계정으로 로그인하여 인증 토큰을 받습니다.
3. **상품 등록**: 받은 토큰을 사용하여 상품을 등록합니다.
4. **상품 조회**: 등록된 상품 목록을 조회합니다.

<br/>

## API 엔드포인트 :pushpin:

- 사용자 등록(POST) : `/api/accounts/`
- 사용자 로그인(POST) : `/api/accounts/login/`
- 토큰 갱신(POST) : `/api/accounts/token/refresh/`
- 사용자 프로필 조회(GET) : `/api/accounts/<username>/`
- 상품 등록 및 조회(POST / GET) : `/api/products/`
- 상품 수정(PUT) : `/api/products/<productid>/`
- 상품 삭제(DEL) : `/api/products/<productid>/`

