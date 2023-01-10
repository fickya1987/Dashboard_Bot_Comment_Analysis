import time  # to simulate a real time data, time loop

import numpy as np  # np mean, np random
import pandas as pd  # read csv, df manipulation
import plotly.express as px  # interactive charts
import streamlit as st  # 🎈 data web app development

st.set_page_config(
    page_title="Dashboard Bot Analysis",
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
st.title("Reddit Brandmention Comment Analysis Dashboard")
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
    # create three columns
    kpi_totalComments, kpi_Accepted_Comments, kpi_Removed_Comments = st.columns(3)

    kpi_totalComments.metric(
        label="Comments by Bot",
        value=len(comment_status),
    )

    kpi_Accepted_Comments.metric(
        label="Accpeted Comments",
        value=accepted_comments,
    )

    kpi_Removed_Comments.metric(
        label="Removed Comments",
        value=removed_comments,
    )

    # kpi_claimed.metric(
    #     label="Total Gifts Claimed",
    #     value=total_claimed,
    # )
    #
    # kpi_claimed_percentage.metric(
    #     label="Gift Claim %",
    #     value=round((total_claimed/len(comment_status))*100),
    # )

    kpi_upvotes, kpi_downvotes, kpi_gift_claimed = st.columns(3)
    # fill in those three columns with respective metrics or KPIs
    kpi_upvotes.metric(
        label="Upvotes",
        value=np.sum(upvotes),
    )

    kpi_downvotes.metric(
        label="Downvotes",
        value=np.sum(downvotes),
    )

    kpi_gift_claimed.metric(
        label="Gifts Claimed",
        value=total_claimed,
    )

    # create two columns for charts

    fig_col1, fig_col2 = st.columns(2)
    # color_discrete_map = {"Removed": 'red', "Present": "green"}
    color_discrete_map = {"Removed": 'red', "Present": "green"}
    with fig_col1:
        st.markdown("### Comment status according to subreddit")

        with st.expander("See explanation"):
            st.write("This figure depicts the number of comments according to subreddit. Green color depicts comments "
                     "which are currently present and haven't been deleted and red color represents the comments which "
                     "got removed from respective subreddit")
            st.write(
                "Most of the brandmentions are made in Testosterone")
            st.write("PEDs and TransDIY are subreddits in which bot "
                "comments got removed ")

        fig = px.bar(data_frame=df, x="subreddit", color="status",
                     color_discrete_map=color_discrete_map)  # ,y="Status") #pie(df, values='Upvotes',names="Status")
        st.write(fig)

    with fig_col2:
        st.markdown("### Accepted vs Removed Comments Bar Chart")
        with st.expander("See explanation"):
            st.write("This figure depicts the overview of total comments made by bot on reddit. Green color depicts "
                     "those "
                     "comments \n which are accepted on subreddit and currently present in the thread and red color "
                     "depict the removed comments")
            st.write("We can analyze that out of 21 comments 16 comments were accepted in the subreddits and 5 "
                     "comments "
                     "were removed by mods")
        fig = px.bar(data_frame=df, x="status", color="status",
                     color_discrete_map=color_discrete_map)  # ,y="Status") #pie(df, values='Upvotes',names="Status")
        st.write(fig)

    fig_col1, fig_col2 = st.columns(2)
    color_discrete_map = {"Removed": 'red', "Present": "green"}
    with fig_col1:
        st.markdown("### Up votes Ratio in Comments(Present & Removed)")
        with st.expander("See explanation"):
            st.write("Pie chart represents the ratio of bot comments accordig to the Up votes")
            st.write("We can analyze from the figure that almost 87% of the bot comments got upvotes from the "
                     "redditors and 13% comments got upvotes but they were still removed from the threads")
        fig = px.pie(df, values='upvotes', names="status", color="status",
                     color_discrete_map={'Removed': 'red',
                                         'Present': 'green'}
                     )
        st.write(fig)

    with fig_col2:
        st.markdown("### Down votes Ratio in Comments(Present & Removed)")
        with st.expander("See explanation"):
            st.write("Pie chart represents the ratio of bot comments accordig to the down votes")
            st.write("We can analyze from the figure that all of the comment who got down votes were removed "
                     "from the subreddits")
        fig = px.pie(df, values='downvotes', names="status", color="status",
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
