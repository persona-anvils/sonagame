import streamlit as st
import random

# 어플 기본 설정
st.set_page_config(page_title="보드게임 필승기", page_icon="🎲")

st.title("🏆 보드게임 필승 조합 생성기")
st.write("지난 판 번호를 넣고 버튼을 누르세요!")

# 입력칸
last_input = st.text_input("지난 판 번호 6개 (예: 1, 5, 12, 23, 35, 41)", "1, 5, 12, 23, 35, 41")

# 번호 생성 로직
def generate_lucky_sets(input_str):
    try:
        # 쉼표로 나누고 숫자로 변환
        last_wins = [int(x.strip()) for x in input_str.split(",")]
        if len(last_wins) != 6:
            return "6개의 숫자를 정확히 입력해주세요."
        
        results = []
        # 안전을 위해 최대 1000번까지만 계산 시도
        attempts = 0
        while len(results) < 5 and attempts < 1000:
            attempts += 1
            co = random.sample(last_wins, random.randint(1, 2))
            pool = [n for n in range(1, 46) if n not in last_wins]
            others = random.sample(pool, 6 - len(co))
            final = sorted(co + others)
            
            # 필터링 조건
            if (121 <= sum(final) <= 160) and (2 <= len([n for n in final if n % 2 != 0]) <= 4):
                results.append({"nums": final, "sum": sum(final), "co": co})
        return results
    except Exception as e:
        return f"에러 발생: {e}"

# 버튼 클릭
if st.button("🚀 이번 판 승리 번호 뽑기"):
    data = generate_lucky_sets(last_input)
    if isinstance(data, list):
        for i, item in enumerate(data, 1):
            st.success(f"**세트 {i}:** {item['nums']}")
            st.caption(f"이월수: {item['co']} | 합계: {item['sum']}")
    else:
        st.error(data)
