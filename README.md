# Analysis_PublicData
---
> 공공 데이터 API를 활용한 데이터 기반 추천 프로그램입니다.
> API : [공공데이터 API](https://www.data.go.kr)
> Language : Python
> PythonLibary : Matlablib, scipy, pandas


***Analysis_PublicData*** 는 공공 데이터 API를 사용했습니다.
1. 출입국 관광 통계 서비스 
2. 관광 자원 통계 서비스 
> 두 데이터셋을 사용하여, 외국인의 입국 숫자에 따른 관광지 입장 수, 두 데이터간의 상관 관계를 분석할 것 입니다.
> matlablib를 이용해, 산점도 그래프 이미지 결과물을 생성하도록 했습니다.

# 시각화 결과
> 산점도 그래프- 나라별 입국자 수 & 관광지의 외국인 입장 수
---
<img src="https://github.com/twooopark/Analysis_PublicData/blob/master/__results__/visualization/graph_scatter.png" height="400px" />

> 바 그래프 - 나라별 입국자 수 & 관광지 별 외국인 입장 수
---
<img src="https://github.com/twooopark/Analysis_PublicData/blob/master/__results__/visualization/graph_bar.png" height="400px" />

# 상관분석
>상관관계
1. 두 변수 사이의 관계 및 성향을 파악하는 분석방법으로 예측, 추천등 많이 사용하는 분석 방법중 하나입니다. 예) 키가 크면 발이 크다.  교육 수준이 높을 수록 자녀의 대학 진학률이 높다 등
2. 산점도, 산포도라는 그래프를 통해 직관적으로 두 변수사이의 관계를 파악할 수 있습니다.            
3. 양의 상관관계 : x의 값이 증가에 따라 y의 값이 증가하는 상관관계
4. 음의 상관관계 : x의 값이 증가에 따라 y의 값이 감소하는 상관관계
5. 상관 관계가 없는 경우 : 전체적으로 흩뿌려져 있습니다.
6. 상관계수 (Correlation Coefficient)
- 서로 간의 데이터가 어느 정도의 근접도를 가지고 있는 지 표현합니다.
- 근접도를 표현하는 방법이  상관계수(r) 입니다.
- 상관계수는  -1 과 1 사이의 값을 가지며 0에 가까워 질수록  두 변수
  사이에는 아무런 관계가 없음을, -1에 가까워 질수록 음의 상관관계가
  1에 가까워 질수록 양의 상관관계가 크다고 봅니다.
  이 프로그램에서는 상관계수를 구하기 위해, scipy.stats.pearsonr함수를 사용했습니다.
