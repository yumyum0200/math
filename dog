import streamlit as st

# 1. 페이지 설정
st.set_page_config(page_title="이차방정식 탐구 튜터", layout="wide")

# 2. 스타일링 (30px 폰트 및 디자인 요소)
st.markdown("""
    <style>
    .main { background-color: #ffffff; }
    [data-testid="column"] { min-width: 30% !important; }
    
    /* 문제 박스 스타일 (30px) */
    .problem-box {
        font-size: 30px !important;
        line-height: 1.8;
        padding: 2.5rem;
        background-color: #f0f7ff;
        border-radius: 25px;
        border-left: 15px solid #a2d2ff;
        color: #1e1e1e;
        margin-bottom: 20px;
    }
    
    /* 형광펜 효과 */
    .highlight {
        background-color: #fff3cd;
        font-weight: 900;
        padding: 0 5px;
        border-radius: 5px;
        color: #d63384;
    }

    /* 버튼 및 입력 요소 크기 */
    .stButton>button {
        width: 100%;
        height: 3.5em;
        font-size: 24px !important;
        font-weight: bold !important;
        border-radius: 15px;
    }
    
    /* 드롭다운 및 텍스트 폰트 조절 */
    .stSelectbox label, .stRadio label { font-size: 22px !important; font-weight: 600; }
    </style>
    """, unsafe_allow_html=True)

# 3. 세션 관리
if 'page' not in st.session_state:
    st.session_state.page = 1
if 'kw_on' not in st.session_state:
    st.session_state.kw_on = False

# 페이지 이동 함수
def move_page(delta):
    st.session_state.page += delta
    st.rerun()

# 공통 문제 텍스트
full_problem = "어느 유기견 보호소에서는 간식용 비스킷 90개를 전체 유기견에게 똑같이 나누어 주려고 한다. 유기견 한 마리 당 나누어 준 비스킷의 개수가 전체 유기견의 수보다 27만큼 작다고 할 때, 전체 유기견의 수를 구하시오."

# --- [1페이지] 도입: 문제 탐색 ---
if st.session_state.page == 1:
    st.title("🚀 오늘의 수학 탐구 미션")
    prob_display = full_problem
    if st.session_state.kw_on:
        prob_display = prob_display.replace("비스킷 90개", "<span class='highlight'>비스킷 90개</span>") \
                                   .replace("한 마리 당 나누어 준 비스킷의 개수가 전체 유기견의 수보다 27만큼 작다", "<span class='highlight'>한 마리 당 나누어 준 비스킷의 개수가 전체 유기견의 수보다 27만큼 작다</span>") \
                                   .replace("전체 유기견의 수", "<span class='highlight'>전체 유기견의 수</span>")

    col_txt, col_img = st.columns([7, 3])
    with col_txt:
        st.markdown(f'<div class="problem-box">{prob_display}</div>', unsafe_allow_html=True)
    with col_img:
        st.image("https://cdn-icons-png.flaticon.com/512/616/616408.png", width=120) # 강아지
        st.image("https://cdn-icons-png.flaticon.com/512/541/541732.png", width=100) # 비스킷
        if st.button("🖍️ Key Word"):
            st.session_state.kw_on = not st.session_state.kw_on
            st.rerun()

# --- [2페이지] Step 1. 구하려는 것 파악하기 ---
elif st.session_state.page == 2:
    col_l, col_r = st.columns([3, 7])
    with col_l:
        st.markdown("### 📋 문제")
        st.info(full_problem)
    with col_r:
        st.title("Step 1. 구하려는 것 파악하기")
        if st.button("💡 힌트 보기"):
            st.warning("문제를 꼼꼼하게 다시 읽어보세요! 문제 속에 답이 있어요")
        
        ans1 = st.selectbox("이 문제에서 구하려고 하는 것은?", ["선택하세요", "전체 비스킷 수", "전체 유기견의 수", "보호소의 크기"])
        if ans1 == "전체 유기견의 수":
            st.success("🎯 정답입니다! 유기견의 수를 x마리로 정하고 다음으로 넘어갑시다.")

# --- [3페이지] Step 2. 식 세우기 ---
elif st.session_state.page == 3:
    col_l, col_r = st.columns([3, 7])
    with col_l:
        st.markdown("### 📋 문제")
        st.info(full_problem)
    with col_r:
        st.title("Step 2. 식 세우기")
        st.subheader("2-(0) 문제 이해하기")
        q2_0 = st.selectbox("전체 유기견의 수가 40마리일 때, 한 마리당 비스킷 수는 몇 개일까?", ["선택하세요", "13개", "27개", "67개"])
        if q2_0 == "13개": st.success("맞았습니다! (40 - 27 = 13)")
        
        st.divider()
        st.subheader("2-(1) 문장 속 단서 찾기")
        q2_1 = st.selectbox("전체 유기견의 수가 x마리 일 때, 한 마리당 비스킷의 수를 x를 사용하여 나타내면?", ["선택하세요", "x + 27", "x - 27", "27 - x"])
        if q2_1 == "x - 27": st.info("💡 잘했습니다! (전체 수 - 27)만큼 비스킷을 받네요.")
        
        st.divider()
        st.subheader("2-(2) 식 세우기")
        q2_2 = st.selectbox("전체 비스킷 90개를 나타내는 올바른 식은?", ["선택하세요", "x + (x - 27) = 90", "x * (x - 27) = 90", "x / (x - 27) = 90"])
        if q2_2 == "x * (x - 27) = 90": st.success("👏 식이 완성되었습니다! x(x - 27) = 90")

# --- [4페이지] Step 3. 방정식 풀기 ---
elif st.session_state.page == 4:
    col_l, col_r = st.columns([3, 7])
    with col_l:
        st.markdown("### 📋 전개된 식")
        st.latex(r"x^2 - 27x - 90 = 0")
    with col_r:
        st.title("Step 3. 방정식 풀기")
        st.subheader("3-(1) 인수분해 하기")
        q3_1 = st.selectbox("위 식을 바르게 인수분해 한 것을 고르세요.", ["선택하세요", "(x - 3)(x + 30) = 0", "(x + 3)(x - 30) = 0", "(x - 9)(x - 10) = 0"])
        if q3_1 == "(x + 3)(x - 30) = 0":
            st.success("🎯 인수분해 성공!")
            st.divider()
            st.subheader("3-(2) 해 구하기")
            q3_2 = st.selectbox("인수분해 결과를 보고 해를 고르세요.", ["선택하세요", "x = 3 또는 x = -30", "x = -3 또는 x = 30", "x = 9 또는 x = 10"])
            if q3_2 == "x = -3 또는 x = 30":
                st.info("해를 찾았습니다!")
                st.divider()
                st.subheader("💡 생각하기")
                q3_3 = st.radio("왜 x = -3은 문제의 답이 될 수 없을까요?", ["유기견의 수가 너무 적어서", "유기견의 수는 자연수(양수)여야 하므로", "비스킷 개수가 음수가 되어버려서"], index=None)
                if q3_3 == "유기견의 수는 자연수(양수)여야 하므로":
                    st.success("정답입니다! 따라서 최종 답은 30마리입니다.")

# --- [5페이지] Step 4. 확인하기 ---
elif st.session_state.page == 5:
    st.title("Step 4. 확인하기")
    st.write("구한 답이 맞는지 직접 대입하여 확인해봅시다.")
    
    col1, col2 = st.columns(2)
    with col1:
        u_count = st.number_input("유기견의 수 (x)", min_value=0, step=1)
    with col2:
        b_count = st.number_input("한 마리당 비스킷 수 (x - 27)", min_value=0, step=1)
    
    total_val = u_count * b_count
    st.markdown(f"### 🧮 계산된 비스킷 수: {total_val}개")
    
    if total_val == 90 and u_count > 0:
        st.balloons()
        st.success("🎊 문제를 바르게 해결했습니다! 수고하셨습니다!")

# --- 하단 공통 네비게이션 ---
st.write("---")
b_col1, b_col2, b_col3 = st.columns([1, 8, 1])
with b_col1:
    if st.session_state.page > 1:
        if st.button("⬅️ 이전", key="prev"): move_page(-1)
with b_col3:
    if st.session_state.page < 5:
        if st.button("다음 ➡️", key="next"): move_page(1)
