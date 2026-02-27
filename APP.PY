import streamlit as st
import random

st.set_page_config(page_title="보드게임 필승기", page_icon="🎲")

st.title("🏆 보드게임 필승 조합 생성기")
st.markdown("---")

# 입력 섹션
st.subheader("1. 지난 판 당첨 번호 입력")
last_input = st.text_input("숫자 6개를 쉼표(,)로 구분해서 적어주세요.", "1, 5, 12, 23, 35, 41")

# 생성 함수
def generate_lucky_sets(input_str):
    try:
        last_wins = [int(x.strip()) for x in input_str.split(",")]
        if len(last_wins) != 6: return None
        
        results = []
        while len(results) < 5:
            co = random.sample(last_wins, random.randint(1, 2))
            pool = [n for n in range(1, 46) if n not in last_wins]
            others = random.sample(pool, 6 - len(co))
            final = sorted(co + others)
            
            if (121 <= sum(final) <= 160) and (2 <= len([n for n in final if n % 2 != 0]) <= 4):
                results.append({"nums": final, "sum": sum(final), "co": co})
        return results
    except:
        return None

# 실행 버튼
if st.button("🚀 이번 판 승리 번호 뽑기"):
    data = generate_lucky_sets(last_input)
    if data:
        for i, item in enumerate(data, 1):
            st.info(f"**세트 {i}:** {item['nums']}")
            st.caption(f"이월수: {item['co']} | 합계: {item['sum']}")
    else:
        st.error("입력 형식이 잘못되었습니다. (예: 1, 5, 12, 23, 35, 41)")
