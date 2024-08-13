import streamlit as st
import preprocess
import helper
import matplotlib.pyplot as plt
import seaborn as sns
st.sidebar.title("Whatsapp chat analyzer")
uploaded_file=st.sidebar.file_uploader("Choose a file")
if uploaded_file is not None:
    btyes_data=uploaded_file.getvalue()
    data=btyes_data.decode("utf-8")
    # st.text(data)
    df=preprocess.preprocess(data)
    st.dataframe(df)

    # fetch unique user

    user_list=df['Sender'].unique().tolist()
    # user_list.remove("OG'S")
    user_list.sort()
    user_list.insert(0,'Overall')
    selected_user=st.sidebar.selectbox('Show analysis wrt',user_list)

    if st.sidebar.button("Show Analysis"):
        num_messages,words,num_media_messages,num_of_links=helper.fetch_stats(selected_user,df)
        col1,col2,col3,col4=st.columns(4)
        with col1:
            st.header('Total Messages')
            st.title(num_messages)
        with col2:
            st.header('Total Words')
            st.title(len(words))
        with col3:
            st.header('Total Media')
            st.title(num_media_messages)
        with col4:
            st.header('Total Links Shared')
            st.title(num_of_links)
        if selected_user=='Overall':
            st.title('Most busy users')
            col1,col2=st.columns(2)
            X,new_df=helper.get_busy_user(df)
            fig,ax=plt.subplots()
            with col1:
                ax.bar(X.index,X.values)
                st.pyplot(fig)
                plt.xticks(rotation=45)
                plt.show()
            with col2:
                st.title('Each Percentage')
                st.dataframe(new_df)
        # word cloud
        st.title("Word Cloud")
        df_wc=helper.create_word_cloud(selected_user,df)
        fig,ax=plt.subplots()
        ax.imshow(df_wc)
        st.pyplot(fig)

        # most common 
        st.title('Most Common words')
        return_df=helper.most_common_words(selected_user,df)
        st.dataframe(return_df)