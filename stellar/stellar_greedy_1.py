# =============================================
# 별의 탐욕 알고리즘 - 핵융합 시각화
# 필요한 라이브러리: streamlit, matplotlib
# 설치 방법: pip install streamlit matplotlib
# 실행 방법: streamlit run stellar_greedy.py
# =============================================

import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# ── 1. 데이터 ──────────────────────────────
# (원자번호, 원소기호, 한글이름, 핵자당 결합에너지 MeV)
elements = [
    (1,  "H",  "수소",      1.11),
    (2,  "He", "헬륨",      7.07),
    (6,  "C",  "탄소",      7.68),
    (8,  "O",  "산소",      7.98),
    (10, "Ne", "네온",      8.03),
    (12, "Mg", "마그네슘",  8.26),
    (14, "Si", "규소",      8.45),
    (20, "Ca", "칼슘",      8.55),
    (24, "Cr", "크로뮴",    8.57),
    (26, "Fe", "철",        8.79),   # ← 여기서 탐색 종료
    (28, "Ni", "니켈",      8.73),
    (50, "Sn", "주석",      8.51),
    (79, "Au", "금",        7.92),
    (92, "U",  "우라늄",    7.59),
]

IRON_INDEX = 9  # 철은 리스트에서 10번째(인덱스 9)

# ── 2. 페이지 설정 ─────────────────────────
st.set_page_config(
    page_title="별의 탐욕 알고리즘",
    page_icon="⭐",
    layout="centered"
)

st.title("⭐ 별의 탐욕 알고리즘")
st.caption("핵융합은 매 순간 결합 에너지가 높아지는 원소로만 나아갑니다")

st.divider()

# ── 3. 슬라이더 (몇 단계까지 보여줄지) ────
step = st.slider(
    label="🔬 융합 단계 선택 (슬라이더를 움직여보세요!)",
    min_value=0,
    max_value=len(elements) - 1,
    value=0,
    step=1
)

# 현재 단계의 원소 정보
current = elements[step]
z, sym, name, be = current

# ── 4. 현재 원소 카드 ──────────────────────
col1, col2, col3 = st.columns(3)
col1.metric("현재 원소", f"{sym} ({name})")
col2.metric("원자번호 Z", z)
col3.metric("결합 에너지", f"{be:.2f} MeV")

# 철에 도달하면 경고 메시지
if step == IRON_INDEX:
    st.error("🔴 철(Fe)에 도달! 더 이상 에너지를 얻을 수 없습니다 → 별이 붕괴합니다 💥")
elif step > IRON_INDEX:
    st.warning("⚠️ 이 원소들은 핵융합으로 만들어지지 않습니다. 초신성 폭발(r-과정)로 생성됩니다.")
else:
    gain = be - elements[step - 1][3] if step > 0 else 0
    if step > 0:
        st.success(f"✅ 탐욕적 선택: {elements[step-1][1]} → {sym} | 에너지 +{gain:.2f} MeV 증가")

st.divider()

# ── 5. 그래프 그리기 ───────────────────────
fig, ax = plt.subplots(figsize=(9, 5))
fig.patch.set_facecolor("#0a0c18")
ax.set_facecolor("#0a0c18")

# 전체 곡선 (흐릿하게)
all_z  = [e[0] for e in elements]
all_be = [e[3] for e in elements]
ax.plot(all_z, all_be, color="#444466", linewidth=2, zorder=1)
ax.scatter(all_z, all_be, color="#333355", s=60, zorder=2)

# 탐색한 경로 (주황색)
visited_z  = [e[0] for e in elements[:step + 1]]
visited_be = [e[3] for e in elements[:step + 1]]
ax.plot(visited_z, visited_be, color="#ff7b2f", linewidth=3, zorder=3)
ax.scatter(visited_z, visited_be, color="#f5c842", s=80, zorder=4)

# 현재 위치 (강조)
ax.scatter([z], [be], color="#ff7b2f", s=220, zorder=5,
           edgecolors="white", linewidths=1.5)

# 철 기준선
ax.axvline(x=26, color="#a8b5c4", linestyle="--", linewidth=1.2, alpha=0.6)
ax.text(27, 1.5, "Fe (철)\n최대 안정점", color="#a8b5c4", fontsize=9)

# 원소 이름 표시
for i, (ez, esym, _, ebe) in enumerate(elements):
    color = "#f5c842" if i <= step else "#555577"
    ax.annotate(esym, (ez, ebe), textcoords="offset points",
                xytext=(0, 10), ha="center", fontsize=8.5,
                color=color, fontweight="bold")

# 축 설정
ax.set_xlabel("원자번호 (Z)", color="#aaaaaa", fontsize=11)
ax.set_ylabel("핵자당 결합 에너지 (MeV)", color="#aaaaaa", fontsize=11)
ax.set_title("결합 에너지 곡선과 탐욕적 탐색 경로", color="#f5c842", fontsize=13, pad=12)
ax.tick_params(colors="#666688")
for spine in ax.spines.values():
    spine.set_edgecolor("#222244")
ax.set_xlim(-2, 96)
ax.set_ylim(0, 10)
ax.grid(True, color="#1a1a2e", linewidth=0.8)

# 범례
orange_patch = mpatches.Patch(color="#ff7b2f", label="탐욕적 선택 경로")
gray_patch   = mpatches.Patch(color="#444466", label="미탐색 구간")
ax.legend(handles=[orange_patch, gray_patch],
          facecolor="#111122", labelcolor="white", fontsize=9)

st.pyplot(fig)

# ── 6. 설명 텍스트 ─────────────────────────
st.divider()
with st.expander("📖 탐욕 알고리즘이란?"):
    st.markdown("""
    **탐욕 알고리즘(Greedy Algorithm)**은 매 순간 **지금 당장 가장 좋은 선택**만 합니다.

    별의 핵융합도 마찬가지예요:
    - 수소 → 헬륨 → 탄소 → ... 결합 에너지가 증가하는 방향으로만 진행
    - **철(Fe)**에서 결합 에너지가 최대 → 더 이상 에너지 이득 없음 → 탐색 종료
    - 철보다 무거운 금, 우라늄은 **초신성 폭발** 때 만들어짐

    > 별은 의도 없이 물리 법칙을 따를 뿐이지만, 그 결과가 탐욕 알고리즘과 똑같습니다!
    """)
