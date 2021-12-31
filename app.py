import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import joblib

filename = 'random_forest.sav'
loaded_model = joblib.load(filename)
df = pd.read_csv("customer_final.csv")
st.set_option('deprecation.showPyplotGlobalUse', False)

st.markdown('<style>body{background-color: Blue;}</style>',unsafe_allow_html=True)
st.title("Customer Segment Prediction")

with st.form("my_form"):
    balance=st.number_input(label='Balance',step=0.001,format="%.6f")
    purchases=st.number_input(label='Purchases',step=0.01,format="%.1f")
    cash_advance=st.number_input(label='Cash Advance',step=0.01,format="%.1f")
    purchases_frequency=st.number_input(label='Purchases Frequency',step=0.01,format="%.6f")
    oneoff_purchases_frequency=st.number_input(label='OneOff Purchases Frequency',step=0.1,format="%.6f")
    purchases_installment_frequency=st.number_input(label='Purchases Installments Freqency',step=0.1,format="%.6f")
    cash_advance_frequency=st.number_input(label='Cash Advance Frequency',step=0.1,format="%.6f")
    cash_advance_trx=st.number_input(label='Cash Advance Trx',step=1)
    purchases_trx=st.number_input(label='Purchases TRX',step=1)
    credit_limit=st.number_input(label='Credit Limit',step=0.1,format="%.2f")

    data=[[balance,purchases,cash_advance,purchases_frequency,
           oneoff_purchases_frequency,purchases_installment_frequency,cash_advance_frequency,cash_advance_trx,purchases_trx,
           credit_limit]]

    submitted = st.form_submit_button("Submit")

if submitted:
    cluster=loaded_model.predict(data)[0]
    print('Este cliente pertence ao grupo: ',cluster)

    cluster_df = df[df['CLUSTER']==cluster]
    plt.rcParams["figure.figsize"] = (10,3)
    for cluster in cluster_df.drop(['CLUSTER'],axis=1):
        fig, ax = plt.subplots()
        grid= sns.FacetGrid(cluster_df, col='CLUSTER')
        grid= grid.map(plt.hist, cluster)
        plt.show()
        st.pyplot(figsize=(5, 5))