import streamlit as st
import random

# 1. 어플 기본 설정 (제목, 아이콘)
st.set_page_config(page_title="보드게임 필승기", page_icon="🎲")

st.title("🏆 보드게임 필승 조합 생성기")
st.write("지난 판 번호를 넣고 버튼을 누르세요! (띄어쓰기만 해도 자동 인식됩니다)")

# 2. 입력칸 설정 (예시 번호를 띄어쓰기 형식으로 변경)
last_input = st.text_input("지난 판 번호 6개 (예: 1 5 12 23 35 41)", "1 5 12 23 35 41")

# 3. 번호 생성 로직 (콤마와 띄어쓰기 모두 지원)
def generate_lucky_sets(input_str):
    try:
        # 콤마(,)를 공백으로 바꾸고, 공백을 기준으로 숫자를 나눕니다.
        num_list = input_str.replace(',', ' ').split() 
        last_wins = [int(x) for x in num_list]
        
        # 입력된 숫자가 정확히 6개인지 확인
        if len(last_wins) != 6:
            return "숫자 6개를 정확히 입력해주세요. (예: 1 5 12 23 35 41)"
        
        results = []
        attempts = 0
        # 최대 1000번 시도하여 조건에 맞는 조합 5세트 생성
        while len(results) < 5 and attempts < 1000:
            attempts += 1
            # 이월수 전략: 지난 번호 중 1~2개 포함
            co = random.sample(last_wins, random.randint(1, 2))
            # 제외수 전략: 지난 번호를 제외한 나머지 번호들
            pool = [n for n in range(1, 46) if n not in last_wins]
            others = random.sample(pool, 6 - len(co))
            final = sorted(co + others)
            
            # 필터링 조건 (합계: 121~160, 홀짝 비율: 2:4 ~ 4:2)
            odd_count = len([n for n in final if n % 2 != 0])
            if (121 <= sum(final) <= 160) and (2 <= odd_count <= 4):
                results.append({"nums": final, "sum": sum(final), "co": co})
        return results
    except Exception as e:
        return f"입력 형식을 확인해주세요! (숫자만 입력 가능합니다)"

# 4. 실행 버튼 및 결과 출력
if st.button("🚀 이번 판 승리 번호 뽑기"):
    data = generate_lucky_sets(last_input)
    
    # 결과가 리스트(정상)인 경우 출력
    if isinstance(data, list):
        for i, item in enumerate(data, 1):
            st.success(f"**세트 {i}:** {item['nums']}")
            st.caption(f"이월수: {item['co']} | 합계: {item['sum']}")
        st.balloons() # 성공 축하 풍선 효과!
    # 에러 메시지인 경우 출력
    else:
        st.error(data)
