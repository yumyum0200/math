import streamlit as st

# 1. 페이지 설정
st.set_page_config(page_title="이차방정식 탐구 튜터", layout="wide")

# 2. 태블릿 가로 분할 유지 CSS
st.markdown("""
    <style>
    [data-testid="column"] { min-width: 30% !important; }
    .stAlert { padding: 1rem; }
    </style>
    """, unsafe_allow_html=True)

# 3. 화면 분할 (3:7 비율)
col_problem, col_activity = st.columns([3, 7], gap="large")

# --- 왼쪽: 문제 상황 고정 영역 ---
with col_problem:
    st.markdown("### 📋 오늘의 문제")
    st.info("""
    **비스킷 90개**를 유기견들에게 똑같이 나누어 주려고 한다. 
    
    **한 마리당 비스킷 개수**가 **전체 유기견의 수**보다 **27만큼 작다**고 할 때, 전체 유기견의 수를 구하시오.
    """)
    st.write("---")
    st.success("🔍 **힌트 확인**\n1. 구하려는 것($x$) 확인\n2. '1마리당 개수'를 $x$로 표현\n3. '전체 개수' 식 세우기")

# --- 오른쪽: 학생 탐구 활동 영역 ---
with col_activity:
    st.title("🐶 유기견 문제 해결 가이드")
    
    # [1단계] 구하려는 것 파악하기
    st.header("1단계: 구하려는 것 파악하기")
    step1_choice = st.radio(
        "이 문제에서 미지수 $x$로 놓을 것은?",
        ["전체 비스킷의 수", "전체 유기견의 수", "강아지의 몸무게"],
        index=None, key="step1"
    )

    if step1_choice == "전체 유기견의 수":
        st.success("🎯 **성공!** 전체 유기견의 수를 **$x$마리**라고 합시다.")
        st.divider()

        # [2단계] 문제의 뜻에 맞는 식 세우기
        st.header("2단계: 문제의 뜻에 맞는 식 세우기")
        
        # 2-(1) 문장 속 단서 찾기
        st.subheader("2-(1) 문장 속 단서 찾기")
        st.write("'한 마리당 비스킷 개수'를 $x$를 사용하여 나타내면?")
        clue = st.selectbox(
            "알맞은 식을 고르세요.",
            ["x + 27", "x - 27", "27 - x", "90 / x"],
            index=None, key="clue"
        )

        if clue == "x - 27":
            st.success("💡 **맞아요!** 한 마리당 비스킷은 **($x - 27$)개**입니다.")
            
            # 2-(2) 수식 완성하기
            st.subheader("2-(2) 수식 완성하기")
            st.write("전체 비스킷이 90개가 되는 방정식을 완성하세요.")
            
            col_eq1, col_eq2, col_eq3 = st.columns([2, 1, 2])
            with col_eq1:
                st.write(" ( 유기견 수 ) ")
                st.latex(r"x")
            with col_eq2:
                st.write(" × ")
                st.write(" ") # 줄맞춤용
            with col_eq3:
                st.write(" ( 1마리당 개수 ) ")
                st.latex(r"(x - 27)")
            
            st.write("이 식의 결과가 **90**이 되어야 합니다.")
            st.latex(r"x(x - 27) = 90")
            
            if st.checkbox("식 세우기 완료! 이제 답을 찾아볼까요?", key="confirm_eq"):
                st.divider()

                # [3단계] 방정식 풀기 및 탐구
                st.header("3단계: 조건에 맞는 x 찾기")
                st.write("슬라이더를 움직여 식이 참이 되는 $x$를 찾아보세요.")
                
                x_val = st.slider("유기견의 수($x$)", 28, 50, 28)
                result = x_val * (x_val - 27)
                
                st.metric("계산된 비스킷 총합", f"{result}개", delta=int(result-90), delta_color="inverse")
                
                if result == 90:
                    st.balloons()
                    st.success(f"🎊 찾았습니다! 유기견 수는 **{x_val}마리**입니다.")
                    
                    with st.expander("4단계: 해의 확인 (중요!)"):
                        st.markdown("""
                        **구한 값이 문제의 뜻에 맞는지 확인합시다.**
                        - $x = 30$일 때, 한 마리당 비스킷은 $30 - 27 = 3$(개)
                        - 전체 비스킷은 $30 \\times 3 = 90$(개)
                        - 또한 마릿수는 양수여야 하므로 $x=30$이 적절합니다.
                        """)
        elif clue is not None:
            st.error("문제를 다시 보세요. '유기견 수($x$)보다 27만큼 작다'고 했습니다.")

    elif step1_choice is not None:
        st.error("우리가 최종적으로 알고 싶은 대상을 미지수로 정해야 해요.")
