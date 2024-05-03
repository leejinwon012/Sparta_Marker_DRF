# 🛠️ **[Django 프로젝트](https://github.com/leejinwon012/Sparta-Market)** 참조해 퓨어 장고 DRF 변환

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

- **사용자 등록(POST)** : `/api/accounts/`
- **사용자 로그인(POST)** : `/api/accounts/login/`
- **토큰 갱신(POST)** : `/api/accounts/token/refresh/`
- **사용자 프로필 조회(GET**) : `/api/accounts/<username>/`
- **상품 등록 및 조회(POST / GET)** : `/api/products/`
- **상품 수정(PUT)** : `/api/products/<productid>/`
- **상품 삭제(DEL)** : `/api/products/<productid>/`

<br/>


## ERD 💾

<div align="center">
  <img src="https://github.com/leejinwon012/Sparta_Marker_DRF/assets/78424970/c61b2733-ad3c-4ca0-b3a1-3686f7169a68" alt="ERD" width="700" height="500">
</div>

<br/>



## POSTMAN 기능 점검 🌐

- POSTMAN을 활용해서 각 기능들을 점검한 결과입니다.

<br/>

## 회원가입

<div align="center">
  <img src="https://github.com/leejinwon012/Sparta_Marker_DRF/assets/78424970/ab94a367-8633-4873-b7f5-89dd191bde15" alt="회원가입" width="550">
</div>

회원가입 기능을 통해 새로운 사용자를 등록할 수 있습니다.

---

<br/>

## 로그인

<div align="center">
  <img src="https://github.com/leejinwon012/Sparta_Marker_DRF/assets/78424970/da5f4c7a-e8ba-40cf-8adb-c453643d34ac" alt="로그인" width="550">
</div>

회원가입한 사용자로 로그인할 수 있습니다.

---

<br/>

## 로그인 토큰 재발급

<div align="center">
  <img src="https://github.com/leejinwon012/Sparta_Marker_DRF/assets/78424970/188c0ba0-3b46-4ad4-842f-8093e0169dfd" alt="로그인 토큰 재발급" width="550">
</div>

로그인 토큰을 재발급받을 수 있습니다.

---

<br/>

## 프로필 조회

<div align="center">
  <img src="https://github.com/leejinwon012/Sparta_Marker_DRF/assets/78424970/306e0186-3c07-4493-8e48-d8b0412e5f97" alt="프로필 조회" width="550">
</div>

사용자의 프로필을 조회할 수 있습니다.

---

<br/>

## 상품 등록 전 토큰

<div align="center">
  <img src="https://github.com/leejinwon012/Sparta_Marker_DRF/assets/78424970/f9b951d1-bdd3-4380-a34b-508d08c23102" alt="상품 등록 전 토큰" width="550">
</div>

상품을 등록하기 위해 필요한 토큰입니다. 이에 따라 회원가입을 한 유저만 상품 등록이 가능함을 의미합니다.

---

<br/>

## 상품 등록

<div align="center">
  <img src="https://github.com/leejinwon012/Sparta_Marker_DRF/assets/78424970/ce5273d1-6bb3-4ff2-8fe8-49427eddcf29" alt="상품 등록" width="550">
</div>

새로운 상품을 등록할 수 있습니다.

---

<br/>

## 상품 목록 조회

<div align="center">
  <img src="https://github.com/leejinwon012/Sparta_Marker_DRF/assets/78424970/ac4fd2cc-887d-4bcc-af80-b56071d53ebd" alt="상품 목록 조회" width="550">
</div>

등록된 상품 목록을 3개씩 조회할 수 있습니다. POSTMAN의 PAGE의 VALUE 값인 페이지 번호를 변경해서 주면 다음 페이지의 항목을 볼 수 있습니다.

---

<br/>

## 상품 목록 검색

<div align="center">
  <img src="https://github.com/leejinwon012/Sparta_Marker_DRF/assets/78424970/800b9918-04ac-47c8-94ae-61c245e090cc" alt="상품 목록 검색" width="550">
</div>

상품 목록을 검색할 수 있습니다.

---

<br/>

## 상품 수정 전 토큰

<div align="center">
  <img src="https://github.com/leejinwon012/Sparta_Marker_DRF/assets/78424970/4f9facbb-4e95-4096-8557-e91ea265d858" alt="상품 수정 전 토큰" width="550">
</div>

상품을 수정하기 위해 필요한 토큰입니다. 상품을 등록한 유저만 자신의 게시글을 수정 가능함을 의미합니다.

---

<br/>

## 상품 수정

<div align="center">
  <img src="https://github.com/leejinwon012/Sparta_Marker_DRF/assets/78424970/35d8fbba-492a-443d-902c-c80981bc3dc0" alt="상품 수정" width="550">
</div>

등록된 상품을 수정할 수 있습니다.

---

<br/>

## 상품 삭제

<div align="center">
  <img src="https://github.com/leejinwon012/Sparta_Marker_DRF/assets/78424970/cfa39748-6dc2-4809-a31f-9013ea8f6295" alt="상품 삭제" width="550">
</div>

등록된 상품을 삭제할 수 있습니다.




