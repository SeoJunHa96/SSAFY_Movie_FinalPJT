# SSAFY_Movie_FinalPJT

# 프로젝트명

<h4>RE: MOVIE</h4>

Remind / Recommend / Review
</br>
RE는 기억, 추천, 리뷰를 의미하며 해당 웹 서비스의 주요 기능들을 나타냈습니다.
</br>
또한, 댓글 형태의 이름를 통해
</br>
댓글처럼 가볍게 다른 사람들과 의견을 공유할 수 있는
</br>
'영화 커뮤니티 사이트'를 지향함을 표현했습니다.


---

### 프로젝트 기간 : 2023-11-13 ~ 2023-11-24

---

### 역할 분담 및 기술 스택

- 정세진
  - 백엔드 (파이썬, Django)
- 서준하
  - 프론트엔드 (자바스크립트, Vue3, css)

이렇게 계획하고 시작했으나, 나중에는 기능별 구현을 위해 역할이 섞임.

---

### 프로젝트 LOGO
#### <초기 로고>
<img src="https://github.com/SeoJunHa96/SSAFY_Movie_FinalPJT/blob/main/img/RE_%20MOVIE-logo.png" width="200" height="150">

#### <최종 로고>
<img src="https://github.com/SeoJunHa96/SSAFY_Movie_FinalPJT/blob/main/final-pjt-front/src/assets/logo.png" width="200" height="150">
(로고 삽입을 위해 배경을 지운 상태라 이상하게 보임)


---

### 프로젝트 요구사항

  - 영화 데이터(50개 이상, fixtures)
  - 영화 추천 알고리즘
  - API 사용
  - 커뮤니티
  - README(팀원 정보, 역할 분담, ERD, 목표 서비스, 구현 정도, 영화추천 알고리즘에 대한 기술적 설명, 서비스 대표 기능 설명, 배포 URL, etc)

---

### 일정

|      일정       |                           내용                           |
| :-------------: | :------------------------------------------------------: |
| ~ 11월 15일(수) |             git 생성, 프로젝트 구상 및 기획              |
|  11월 16일(목)  |               ERD 작성, 기본적인 구조 생성               |
|  11월 17일(금)  | 필요 API 가져오기, 영화 정보 JSON 생성, 프론트 개발 시작 |
|  11월 18일(토)  |                     핵심 기능 구현                     |
|  11월 19일(일)  |         1차 중간 점검(디버깅 및 보안 사항 확인)          |
|  11월 20일(월)  |                     인증 관련 구현                        |
|  11월 21일(화)  |                      미구현 부분 구현                        |
|  11월 22일(수)  |                  배포, 디자인 마무리, 디버깅                  |
|  11월 23일(목)  |                  최종 마무리, 발표 준비                  |



---

### 와이어 프레임

메인 페이지<br><img src="https://github.com/SeoJunHa96/SSAFY_Movie_FinalPJT/blob/main/img/%EC%99%80%EC%9D%B4%EC%96%B4%ED%94%84%EB%A0%88%EC%9E%841%20-%20%EB%A9%94%EC%9D%B8%20%ED%8E%98%EC%9D%B4%EC%A7%80.png" width="400" height="500"> <br><br>
로그인 관련<br><img src="https://github.com/SeoJunHa96/SSAFY_Movie_FinalPJT/blob/main/img/%EC%99%80%EC%9D%B4%EC%96%B4%ED%94%84%EB%A0%88%EC%9E%842%20-%20account.png" width="600" height="400"><br><br>
프로필<br><img src="https://github.com/SeoJunHa96/SSAFY_Movie_FinalPJT/blob/main/img/%EC%99%80%EC%9D%B4%EC%96%B4%ED%94%84%EB%A0%88%EC%9E%843%20-%ED%94%84%EB%A1%9C%ED%95%84.png" width="450" height="400"><br><br>
영화 추천 관련<br><img src="https://github.com/SeoJunHa96/SSAFY_Movie_FinalPJT/blob/main/img/%EC%99%80%EC%9D%B4%EC%96%B4%ED%94%84%EB%A0%88%EC%9E%844%20-%20%EC%98%81%ED%99%94%EC%B6%94%EC%B2%9C(movie).png" width="550" height="600"><br><br>
커뮤니티 관련<br><img src="https://github.com/SeoJunHa96/SSAFY_Movie_FinalPJT/blob/main/img/%EC%99%80%EC%9D%B4%EC%96%B4%ED%94%84%EB%A0%88%EC%9E%845%20-%20%EB%A6%AC%EB%B7%B0%20%EA%B2%8C%EC%8B%9C%ED%8C%90.png" width="700" height="350"><br>

---

### ERD
<img src="https://github.com/SeoJunHa96/SSAFY_Movie_FinalPJT/blob/main/img/ERD.png" width="700" height="700"><br>
---

### 기능 구현 (상세 페이지)

---
### 영화 추천 알고리즘

초기 사용자의 경우 장르별 최다 관객수를 기준으로 10개를 추천
1개 이상의 영화를 좋아요 누른 경우 영화의 장르와 유사도가 가장 높은 영화 10개 임의 추천.

---

### 최종 진행 과정

모델링 작업 실패로 인해 게시글과 유저 관련 기능들(팔로우, 팔로잉, 댓글 등)은 구현하지 못했지만
영화 API를 받아와서 정보를 띄우는 것은 생각보다 깔끔하게 구현되었다.


---

### 후기

서준하:
“개발자는 실패가 일상인 직업이다.”
이걸 이해하고 받아드리려고 노력했던 프로젝트였다.

정세진:
<br/>
수업만 듣다가 프로젝트를 진행하며 직접 적용하고 응용하려니 마음대로 되지 않아 속상할 때가 많았다.
복습도 하고 없는 자료를 찾아가는 과정이 고통스럽긴 했지만 기능이 제대로 동작하게 되면 많은 쾌감도 얻었다.
많은 도움을 주고 함께 해준 팀원이 정말 고맙고 2주 동안 정신없었지만 배운 것이 많아 정말 좋은 시간이었다.
