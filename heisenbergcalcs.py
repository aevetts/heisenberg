import streamlit as st
from sympy import ImmutableMatrix, latex

a = ImmutableMatrix([[1, 0, 0], [0, 1, 1], [0, 0, 1]])
b = ImmutableMatrix([[1, 1, 0], [0, 1, 0], [0, 0, 1]])
c = ImmutableMatrix([[1, 0, 1], [0, 1, 0], [0, 0, 1]])
gen_dict = {'a': a, 'b': b, 'c': c, 'A': a**-1, 'B': b**-1, 'C': c**-1}

def wordToMatrix(word):
    result = ImmutableMatrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    for char in word:
        result = result * gen_dict[char]
    return result

st.header('Heisenberg normal form calculator')
st.markdown(r'Find the normal form of a word in the Heisenberg group $\langle a,b,c\mid [b,a]=c, [c,a]=[c,b]=1\rangle$.') 
# st.latex(r'\langle a,b,c\mid [b,a]=c, [c,a]=[c,b]=1\rangle')
st.markdown('This tool uses capitals to denote inverses, and the convention for commutators is that $[x,y]=xyXY$.')
st.markdown('Enter a word in $\{a,b,c,A,B,C\}^*$.')
word = st.text_input(label='Input word')

#add some validation
inputvalid = True
for char in word:
        if char not in gen_dict.keys():
            inputvalid = False

if inputvalid == False:
    st.markdown('INVALID INPUT')

if word and inputvalid:
    for char in word:
        if char not in gen_dict.keys():
            st.text('Invalid input')

    mat = wordToMatrix(word)

    # st.subheader('Malcev normal form')
    
    if mat[1,2]==0:
        apower=''
    elif mat[1,2] == 1:
        apower='a'
    elif mat[1,2] == -1:
        apower='A'
    elif mat[1,2] < 0:
        apower=f'A^{{{-mat[1,2]}}}'
    else:
        apower=f'a^{{{mat[1,2]}}}'

    if mat[0,1]==0:
        bpower=''
    elif mat[0,1] == 1:
        bpower='b'
    elif mat[0,1] == -1:
        bpower='B'
    elif mat[0,1] < 0:
        bpower=f'B^{{{-mat[0,1]}}}'
    else:
        bpower=f'b^{{{mat[0,1]}}}'

    if mat[0,2]==0:
        cpower = ''
    elif mat[0,2] == 1:
        cpower = 'c'
    elif mat[0,2] == -1:
        cpower = 'C'
    elif mat[0,2]<0:
        cpower = f'C^{{{-mat[0,2]}}}'
    else:
        cpower = f'c^{{{mat[0,2]}}}'
    
    if apower+bpower+cpower=='':
        nf='1'
    else:
        nf=apower+bpower+cpower
  
    st.markdown(f'Normal form: ${nf}$')
    
