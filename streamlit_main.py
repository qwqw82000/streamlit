import streamlit as st

st.title("안녕하세요")
st.header("header")
st.subheader("subheader")
st.text("이것은 일반 텍스트")

st.markdown("""
# h1 tag
## h2 tag
### h3 tag

큰 제목
====================

중간 제목
---------------------

:moon:

:sunglasses:

** 볼드체 **

_ 이탤릭체 _

1. 첫 번째
2. 두 번째
3. 세 번째
""")

st.latex(r'''a + ar + a r^2 + a r^3 + \cdots +  a r^{n-1} =
\sum_{k=0}^{n-1} ar^k =
a \left(\frac{1-r^{n}}{1-r}\right)
''')

d = {
    "name": "김영하", 
    "language": "Python",
    "topic": "NLP"
}

st.write(d)
