# ⭐ 별의 핵융합과 탐욕 알고리즘

별의 핵융합 과정을 **탐욕 알고리즘(Greedy Algorithm)** 으로 시각화한 Streamlit 앱입니다.

핵융합은 매 순간 결합 에너지가 높아지는 원소로만 나아가기 때문에, 이는 탐욕 알고리즘의 특성과 동일합니다. 슬라이더를 조작하여 수소 → 철까지의 핵융합 과정을 단계별로 확인할 수 있습니다.

---

## 🚀 실행 방법

### 1. 저장소 클론
```bash
git clone https://github.com/your-username/stellar-greedy.git
cd stellar-greedy
```

### 2. 라이브러리 설치
```bash
pip install -r requirements.txt
```

### 3. 앱 실행
```bash
streamlit run stellar-greedy.py
```

---

## 📦 사용 라이브러리

| 라이브러리 | 용도 |
|---|---|
| `streamlit` | 웹 앱 UI |
| `matplotlib` | 결합 에너지 그래프 시각화 |

---

## 📖 주요 내용

- **탐욕 알고리즘**: 매 순간 최적의 선택(결합 에너지가 높은 원소)을 하는 알고리즘
- **결합 에너지 곡선**: 수소(1.11 MeV)부터 철(8.79 MeV)까지의 핵자당 결합 에너지 변화
- **철(Fe)**: 핵자당 결합 에너지가 가장 높아 별의 핵융합이 멈추는 지점
- **초신성 폭발**: 철 이후의 무거운 원소(금, 우라늄 등)가 만들어지는 과정
