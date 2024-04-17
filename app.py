import time  # to simulate a real time data, time loop

import numpy as np  # np mean, np random
import pandas as pd  # read csv, df manipulation
import plotly.express as px  # interactive charts
import streamlit as st  # 🎈 data web app development

st.set_page_config(
    page_title="Angkasa Pura 2 Sentiment Analysis Dashboard",
    page_icon="✅",
    layout="wide",
)

# read csv from a github repo
dataset_url = "data/Bot_Comments.csv"


# read csv from a URL
@st.experimental_memo
def get_data() -> pd.DataFrame:
    return pd.read_csv(dataset_url)


df = get_data()

# dashboard title
st.title("Angkasa Pura 2 Social media Sentiment Analysis Dashboard 01")
st.write("Date Range: 12/15/2022 - 01/06/2023")

# creating a single-element container
placeholder = st.empty()

upvotes = list(df.loc[:, 'upvotes'])
downvotes = list(df.loc[:, 'downvotes'])
comment_status = list(df.loc[:, "status"])
claimed_status = list(df.loc[:, "claimed"])
accepted_comments = 0
removed_comments = 0
total_claimed = 0

for status in comment_status:
    if status == "Present":
        accepted_comments = accepted_comments + 1
    else:
        removed_comments = removed_comments + 1

for status1 in claimed_status:
    if status1 == "Yes":
        total_claimed = total_claimed + 1
    # else:
    #     removed_comments = removed_comments + 1

with placeholder.container():
    # job_filter = st.selectbox("Select the Job", pd.unique(df["subreddit"]))
    # df_refined = df[["body"]]
    # for index, row in df_refined.iterrows():
    #     # print()
    #     with st.expander("See explanation"):
    #         st.write(row['body'])


    # create three columns
    kpi_totalComments, kpi_Accepted_Comments, kpi_Removed_Comments = st.columns(3)

    kpi_totalComments.metric(
        label="Total Comments for Angkasa Pura 2",
        value=len(comment_status),
    )

    kpi_Accepted_Comments.metric(
        label="Positive Sentiment Comments for AP2",
        value=accepted_comments,
    )

    kpi_Removed_Comments.metric(
        label="Negative Sentiment commentsfor AP2",
        value=removed_comments,
    )


    # create two columns for charts

    fig_col1, fig_col2 = st.columns(2)
    # color_discrete_map = {"Removed": 'red', "Present": "green"}
    color_discrete_map = {"Removed": 'red', "Present": "green"}
    with fig_col1:
        st.markdown("### Comment status according to Search Engine (Google, Bing,etc)")

        with st.expander("See explanation"):
            st.write("This figure depicts the number of people comments according to Search Engine.")
            st.write(
                "Those comments are all about Angkasa Pura 2 Services")


        fig = px.bar(data_frame=df, x="status", color="status",
                     color_discrete_map=color_discrete_map)  # ,y="Status") #pie(df, values='Upvotes',names="Status")
        st.write(fig)

    with fig_col2:
        st.markdown("### Comment Status from Social media (Tiktok, Youtube,etc)")
        with st.expander("See explanation"):
            st.write("This figure depicts the overview of total people comments made on social media regarding to Angkasa Pura 2 services.")

        fig = px.bar(data_frame=df, x="status", color="status",
                     color_discrete_map=color_discrete_map)  # ,y="Status") #pie(df, values='Upvotes',names="Status")
        st.write(fig)

    fig_col1, fig_col2 = st.columns(2)
    color_discrete_map = {"Removed": 'red', "Present": "green"}
    with fig_col1:
        st.markdown("### Soekarno-Hatta Airport services in Comments")
        with st.expander("See explanation"):
            st.write("Pie chart represents the ratio of people comments with regards to Soekarno Hatta Airport services")
            s
        fig = px.pie(df, values='upvotes', names="Comment status for Soekarno Hatta Airport", color="status",
                     color_discrete_map={'Removed': 'red',
                                         'Present': 'green'}
                     )
        st.write(fig)

    with fig_col2:
        st.markdown("### Kualanamu Airport services in Comments")
        with st.expander("See explanation"):
            st.write("Pie chart represents the ratio of people comments regarding to Kualanamu Airport services")
            s
        fig = px.pie(df, values='downvotes', names="Comment status for Kualanamu Airprot", color="status",
                     color_discrete_map={'Removed': 'red',
                                         'Present': 'green'}
                     )
        st.write(fig)

    # st.markdown("### Detailed Data View")
    # status_filter = st.sidebar.selectbox("View Dashboard According to", pd.unique(df["claimed"]))


    # status_filter = st.selectbox("Select status to view the data", pd.unique(df["status"]))
    # dataframe filter
    # df_refined = df[df["status"] == status_filter]
    # df_refined = df[["subreddit","offered_to","body","upvotes","downvotes","status","claimed"]]
    # st.dataframe(df_refined)

    # fig_col3, fig_col4 = st.columns(2)
    # # color_discrete_map = {"Removed": 'red', "Accepted": "green"}
    # with fig_col3:
    #     st.markdown("### First Chart")
    #     fig = px.pie(df, values=['Downvotes','Upvotes'])
    #     st.write(fig)
    #
    # color_discrete_map = {"Removed": 'red', "Accepted": "green"}
    # with fig_col4:
    #     st.markdown("### Second Chart")
    #     fig = px.bar(data_frame=df, x="subreddit", color="Status",
    #                  color_discrete_map=color_discrete_map)  # ,y="Status") #pie(df, values='Upvotes',names="Status")
    #     st.write(fig)

# top-level filters
# job_filter = st.selectbox("Select the Job", pd.unique(df["job"]))
#
# # creating a single-element container
# placeholder = st.empty()
#
# # dataframe filter
# df = df[df["job"] == job_filter]
