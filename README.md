# 도마뱀 분양 거래 사이트를 참조해 퓨어 장고를 DRF 변환

이 프로젝트는 Django를 사용하여 사용자 및 상품을 관리하는 RESTful API를 구축한 것입니다. 사용자는 등록하고 로그인하여 개인 프로필을 관리하고, 상품은 등록하고 관리할 수 있습니다.

<br/>

## 기능

### 사용자 등록

사용자는 회원가입 양식을 통해 계정을 생성할 수 있습니다. 필수 정보로는 사용자 이름, 이메일, 비밀번호가 있습니다.

<br/>

### 사용자 로그인

등록한 계정으로 로그인하여 인증 토큰을 받습니다. 이 토큰을 사용하여 API 엔드포인트에 접근할 수 있습니다.

<br/>

### 사용자 관리

- **사용자 등록**: 사용자는 회원가입 양식을 통해 계정을 생성할 수 있습니다.
- **사용자 인증**: JWT(JSON Web Token)를 사용하여 사용자를 인증합니다.
- **사용자 프로필 조회 및 수정**: 인증된 사용자는 자신의 프로필을 조회하고 수정할 수 있습니다.

<br/>

### 상품 관리

- **상품 등록**: 사용자는 상품의 제목, 내용, 이미지 등을 포함하여 새로운 상품을 등록할 수 있습니다.
- **상품 조회**: 등록된 상품 목록을 조회할 수 있습니다. 각 상품에는 제목, 내용, 이미지, 등록자 정보, 등록일시가 표시됩니다.
- **상품 수정 및 삭제**: 상품 등록자는 자신이 등록한 상품을 수정하거나 삭제할 수 있습니다.

<br/>

## 사용법

1. **사용자 등록**: 회원가입 양식을 통해 계정을 생성합니다.
2. **사용자 인증**: 등록한 계정으로 로그인하여 인증 토큰을 받습니다.
3. **상품 등록**: 받은 토큰을 사용하여 상품을 등록합니다.
4. **상품 조회**: 등록된 상품 목록을 조회합니다.

<br/>

## API 엔드포인트

- 사용자 등록: `/`
- 사용자 로그인: `/login/`
- 토큰 갱신: `/token/refresh/`
- 사용자 프로필 조회: `/<username>/`
- 상품 등록 및 조회: `/products/`

