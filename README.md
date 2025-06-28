# 📊 WhatsApp Chat Analyzer

**WhatsApp Chat Analyzer** is a Streamlit-based interactive web app that provides powerful insights into WhatsApp group or personal chat exports. Upload your chat `.txt` file and explore message patterns, media sharing, emoji usage, and most frequently used words — all visualized beautifully using charts and word clouds.

---

## 🚀 Features

- 📥 Upload WhatsApp chat exports (`.txt` format)
- 👥 Analyze activity by individual users or overall
- 📊 Chat statistics:
  - Total messages
  - Word count
  - Media messages shared
  - Links shared
- 🧑‍💬 Identify most active users
- 🌥️ Generate word clouds of common words
- 📈 Timeline graphs (daily & monthly message trends)
- 📅 Weekly and monthly activity maps
- 🔥 Hourly heatmap to visualize active time slots
- 🧾 Most common words (excluding stopwords)
- 😂 Emoji usage breakdown with pie chart
- 📎 Link extraction using `urlextract`

---

## 📁 File Structure

```

whatsapp-chat-analyzer/
│
├── app.py                # Main Streamlit app UI
├── helper.py             # All backend analysis functions
├── preprocessor.py       # Preprocessing of raw chat data
├── stop\_hinglish.txt     # Custom stopwords list (Hindi + English)
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation

````

---

## 📦 Requirements

Install all dependencies using:

```bash
pip install -r requirements.txt
````

Contents of `requirements.txt`:

```
streamlit
pandas
matplotlib
seaborn
wordcloud
urlextract
emoji
```

---

## 🛠️ How to Run

1. Clone the repo:

   ```bash
   git clone https://github.com/your-username/whatsapp-chat-analyzer.git
   cd whatsapp-chat-analyzer
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Launch the app:

   ```bash
   streamlit run app.py
   ```

4. Upload your exported `WhatsApp Chat.txt` file (without media) in the sidebar and start analyzing!

---

## 🧠 How It Works

* `preprocessor.py` parses the raw WhatsApp chat using regex and converts it into a clean DataFrame.
* `helper.py` contains functions to extract stats, count emojis, generate word clouds, most common words, and visual timelines.
* `app.py` provides a user-friendly interface using Streamlit widgets to control what data gets displayed.

---

## 📝 Future Improvements

* Sentiment analysis of messages
* Emoji categorization (happy, angry, sad, etc.)
* Network graphs showing user interactions
* Export charts/data to PDF/CSV
* Support for multilingual chats

---

## 👩‍💻 Developed By

**Varri Navya**
Feel free to connect on [GitHub](https://github.com/Navyavarri10) 😊

---
