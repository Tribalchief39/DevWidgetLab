import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="Pie Chart Generator", layout="wide")

st.title("Pie Chart Generator")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Chart Controls")

    labels_input = st.text_input(
        "Enter Categories (comma separated)",
        "Food,Rent,Transport,Entertainment"
    )

    values_input = st.text_input(
        "Enter Values (comma separated)",
        "300,500,150,200"
    )

    show_percent = st.checkbox("Show Percentages", True)

with col2:
    st.subheader("Preview")

    try:
        labels = [x.strip() for x in labels_input.split(",")]
        values = [float(x.strip()) for x in values_input.split(",")]

        fig, ax = plt.subplots()

        if show_percent:
            ax.pie(values, labels=labels, autopct='%1.1f%%')
        else:
            ax.pie(values, labels=labels)

        ax.set_title("Pie Chart")

        st.pyplot(fig)

        # Download button
        fig.savefig("pie_chart.png")
        with open("pie_chart.png", "rb") as file:
            st.download_button(
                label="Download Chart",
                data=file,
                file_name="pie_chart.png",
                mime="image/png"
            )

    except:
        st.warning("Please make sure the number of labels and values match.")