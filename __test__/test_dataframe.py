import pandas as pd

# Series와 dict 데이터를 활용한 DataFrame
d = {
    'one': pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'e']),
    'two': pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])}

# Basic : Full outer join
df = pd.DataFrame(d)
print(df)
print('------------------------------------------')


# dict list를 활용
d = [
    {'name': '둘리', 'age': 10, 'phone': '010-1111-1111'},
    {'name': '마이콜', 'age': 20, 'phone': '010-2222-2222'},
    {'name': '길동', 'age': 30, 'phone': '010-3333-3333'}]

df = pd.DataFrame(d)
print(df)
print('------------------------------------------')

# 원하는 컬럼명 선택
df2 = pd.DataFrame(d, columns=['name', 'phone'])
print(df2)
print('------------------------------------------')

# 데이터 추가(열 추가)
df2['height'] = [150, 160, 170]
print(df2)
print('------------------------------------------')

# 인덱스 선택 (기본값 : 0, 1, 2.. 숫자 인덱스)
df3 = df2.set_index('name')
print(df3)
print('------------------------------------------')

# 컬럼 선택
s = df2['name']
print(s)
print(type(s))
print('------------------------------------------')

# merge
df4 = pd.DataFrame([{'sido': '서울'}, {'sido': '부산'}, {'sido': '전주'}])
df5 = pd.merge(df2, df4, left_index=True, right_index=True)
print(df5)
print('------------------------------------------')

# merge & join
df1 = pd.DataFrame({
    '고객번호': [1001, 1002, 1003, 1004, 1005, 1006, 1007],
    '이름': ['둘리', '도우너', '또치', '길동', '희동', '마이콜', '영희']})

df2 = pd.DataFrame({
    '고객번호': [1001, 1001, 1005, 1006, 1008, 1001],
    '금액': [10000, 20000, 15000, 5000, 100000, 30000]})

# 공통 열인 고객번호 열을 기준으로 데이터를 찾아서 합친다.
# 이 때 기본적으로는 양쪽 데이터프레임에 모두 키가
# 존재하는 데이터만 보여주는(inner join 방식)

df3 = pd.merge(df1, df2)
print(df3)
print('------------------------------------------')

# outer join 방식은 키 값이 한쪽에만
# 있어도 양쪽 데이터를 모두 보여준다(full)
df3 = pd.merge(df1, df2, how='outer')
print(df3)
print('------------------------------------------')

# left, right 방식은 첫번째,
# 혹은 두번째 데이터프레임을 모두 보여준다
print(pd.merge(df1, df2, how='right'))
print('------------------------------------------')
print(pd.merge(df1, df2, how='left'))
print('------------------------------------------')


df1 = pd.DataFrame({'성별': ['남자', '남자', '여자'],
                    '연령': ['미성년자', '성인', '미성년자'],
                    '매출1': [1, 2, 3]})

df2 = pd.DataFrame({'성별': ['남자', '남자', '여자', '여자'],
                    '연령': ['미성년자', '미성년자', '미성년자', '성인'],
                    '매출2': [4, 5, 6, 7]})

# 기준 열은 on 인수로도 명시적 설정이 가능하다.
df3 = pd.merge(df1, df2) # 기본적으로 공통된 컬럼명인 성별, 연령이 on 된다
print(df3)
print('------------------------------------------')
df3 = pd.merge(df1, df2, on=['성별', '연령'])
print(df3)
print('------------------------------------------')
df3 = pd.merge(df1, df2, on=['성별']) # 결과물에 동일 속성명은 자동 변경되서 출력한다.
print(df3)
print('------------------------------------------')
df3 = pd.merge(df1, df2, on=['연령'])
print(df3)
print('------------------------------------------')


df1 = pd.DataFrame({'key1': ['foo', 'foo', 'bar'],
                    'key2': ['one', 'two', 'one'],
                    'lval': [1, 2, 3]})
df2 = pd.DataFrame({'k1': ['foo', 'foo', 'bar', 'bar'],
                    'k2': ['one', 'one', 'one', 'two'],
                    'rval': [4, 5, 6, 7]})
df3 = pd.merge(df1, df2, left_on='key1', right_on='k1')
print(df3)
print('------------------------------------------')

df1 = pd.DataFrame({'key': ['a', 'b', 'a', 'a', 'b', 'c'],  'value': range(6)})
df2 = pd.DataFrame({'group_val': [3.5, 7]}, index=['a', 'b'])
pd.merge(df1, df2, left_on='key', right_index=True)

df1 = pd.DataFrame([[1., 2.], [3., 4.], [5., 6.]], columns=['Ohio', 'Nevada'], index=['a', 'c', 'e'])
df2 = pd.DataFrame([[7., 8.], [9., 10.], [11., 12.], [13, 14]], columns=['Missouri', 'Alabama'], index=['b', 'c', 'd', 'e'])
print(df1)
print('------------------------------------------')
print(df2)
print('------------------------------------------')
print(pd.merge(df1, df2, left_index=True, right_index=True))

