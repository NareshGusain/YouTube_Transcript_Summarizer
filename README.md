# YouTube Transcript Summarizer

A modern web app to **instantly generate concise, AI-powered summaries from any YouTube video**.  
Paste a YouTube link, click summarize, and save time!

---

## 🚀 Features

- **Paste any YouTube link** and get a clean, readable transcript summary.
- **AI-powered transcript cleaning** for easy reading.
- **Modern, responsive UI** with a beautiful navbar and footer.
- **No sign-up required** – privacy-friendly and free.
- **Coming soon:** Chrome Extension, Android & iOS Apps!

---

## 🖥️ Demo

![Screenshot](static/demo_screenshot.png) <!-- Add your screenshot here -->

---

## ✨ How It Works

1. **Paste** a valid YouTube video link in the input box.
2. **Click** the "Summarize" button.
3. **Read** the AI-cleaned summary instantly on the page.

---

## 💡 How It Helps

- **Save time:** Read summaries instead of watching full videos.
- **Quick review:** Perfect for lectures, tutorials, and educational content.
- **Accessible:** Great for students, professionals, and lifelong learners.

---

## 🛠️ Tech Stack

- **Backend:** Django, Python
- **Frontend:** HTML, CSS (responsive, glassmorphism style)
- **Transcript Extraction:** [youtube-transcript-api](https://github.com/jdepoix/youtube-transcript-api)

---

## ⚡ Getting Started

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/yt-transcript-summarizer.git
    cd yt-transcript-summarizer
    ```

2. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the server:**
    ```bash
    python manage.py runserver
    ```

4. **Open in your browser:**
    ```
    http://127.0.0.1:8000/
    ```

---

## 📁 Project Structure

```
summarizeApp/
│
├── PyFunctions/
│   └── helper.py
├── templates/
│   └── index.html
├── static/
│   └── style.css
├── views.py
├── ...
```

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---
