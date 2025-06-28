from urlextract import URLExtract
from wordcloud import WordCloud
import pandas as pd
from collections import Counter
import emoji


extract=URLExtract()

def fetch_stats(selected_user,df):


        if selected_user != 'Overall':
            df = df[df['user'] == selected_user]

        #1.fetch number of messages
        num_messages = df.shape[0]

        #2. number of words
        words=[]
        for message in df['message']:
             words.extend(message.split())

        #3.fetch number of media messages
        num_media_messages = df[df['message'].str.contains('omitted', case=False, na=False)].shape[0]


        #4.fetch number of links shared
        links=[]
        for message in df['message']:
            links.extend(extract.find_urls(message))

        return num_messages,len(words),num_media_messages,len(links)


def most_busy_users(df):
    x = df['user'].value_counts().head()
    df=round((df['user'].value_counts()/df.shape[0])*100,2).reset_index().rename(columns={'user':'name','count':'percent'})
    return x,df



def create_word_cloud(selected_user, df):
    # Filter messages
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    df = df[df['message'].notnull()]
    df = df[~df['message'].str.contains('omitted', case=False, na=False)]
    df['message'] = df['message'].str.replace('<This message was edited>', '', case=False, regex=False)

    # Load stop words properly
    with open('stop_hinglish.txt', 'r') as f:
        stop_words = f.read().splitlines()

    # Function to remove stop words
    def remove_stop_words(message):
        words = []
        for word in message.lower().split():
            if word not in stop_words:
                words.append(word)
        return " ".join(words)

    # Apply to messages and join text
    cleaned_text = df['message'].apply(remove_stop_words).str.cat(sep=" ")

    # Generate word cloud
    wc = WordCloud(width=500, height=500, min_font_size=10, background_color='white')
    wordcloud = wc.generate(cleaned_text)
    return wordcloud



def most_common_words(selected_user,df):

    f=open('stop_hinglish.txt','r')
    stop_words=f.read()

    if selected_user != 'Overall':
        df=df[df['user'] == selected_user]

    df = df[df['message'].notnull()]
    df = df[~df['message'].str.contains('omitted', case=False, na=False)]
    df['message'] = df['message'].str.replace('<This message was edited>', '', case=False, regex=False)

    words = []

    for message in df['message']:
        for word in message.lower().split():  # converting all words to lowercase
            if word and word.strip() not in stop_words:
                words.append(word.strip())
        words.extend(message.split())

    most_common_df = pd.DataFrame(Counter(words).most_common(20))
    return most_common_df

def emoji_helper(selected_user,df):

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    emojis = []

    for message in df['message']:
        emojis.extend([c for c in message if c in emoji.EMOJI_DATA])

    emoji_df=pd.DataFrame(Counter(emojis).most_common(len(Counter(emojis))))
    return emoji_df


def monthly_timeline(selected_user,df):

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    timeline = df.groupby(['year', 'month_num', 'month']).count()['message'].reset_index()
    time = []
    for i in range(timeline.shape[0]):
        time.append(timeline['month'][i] + "-" + str(timeline['year'][i]))

    timeline['time'] = time

    return timeline


def daily_timeline(selected_user,df):

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    df['only_date'] = df['date'].dt.date
    daily_timeline = df.groupby('only_date').count()['message'].reset_index()

    return daily_timeline


def week_activity_map(selected_user,df):

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    return df['day_name'].value_counts()


def month_activity_map(selected_user,df):

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    return df['month'].value_counts()


def activity_map(selected_user,df):

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    user_heatmap=df.pivot_table(index='day_name', columns='period', values='message', aggfunc='count').fillna(0)

    return user_heatmap



