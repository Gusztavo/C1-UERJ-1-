import streamlit as st
import math

def sum_points(point1, point2):
    """Soma dois pontos."""
    return (point1[0] + point2[0], point1[1] + point2[1])

def distance(point1, point2):
    """Calcula a distância euclidiana entre dois pontos."""
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

def main():
    st.title("Soma de Dois Pontos e Distância Entre Eles")

    # Entrada dos pontos
    st.subheader("Insira os pontos:")
    x1 = st.number_input("Ponto X1:", value=0)
    y1 = st.number_input("Ponto Y1:", value=0)
    x2 = st.number_input("Ponto X2:", value=0)
    y2 = st.number_input("Ponto Y2:", value=0)

    point1 = (x1, y1)
    point2 = (x2, y2)

    # Calcula a soma dos pontos
    result = sum_points(point1, point2)

    # Calcula a distância entre os pontos
    dist = distance(point1, point2)

    # Exibe o resultado
    st.subheader("Resultado:")
    st.write(f"A soma dos pontos ({point1}) e ({point2}) é: {result}")
    st.write(f"A distância entre os pontos ({point1}) e ({point2}) é: {dist}")

if __name__ == "__main__":
    main()