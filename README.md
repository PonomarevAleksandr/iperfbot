# 📡 Telegram Bot for Network Speed Testing (iperf3)

A powerful Telegram bot that allows users to test **network speed** using `iperf3` and receive results in **graphical or text format**.

---

## 📌 Features
✅ Run `iperf3` network speed tests directly from Telegram.  
✅ Choose output format: **graph 📈** or **text 📃**.  
✅ Fully **asynchronous** with `aiogram 3.x`.  
✅ Uses **FSM (Finite State Machine)** for smooth user interaction.  
✅ **Lightweight & optimized**, runs inside a Docker container.  

---

## 🚀 Setup & Installation

### 1️⃣ Clone the repository
```sh
git clone https://github.com/PonomarevAleksandr/iperfbot.git
cd your-repo
```

### 2️⃣ Create a `.env` file
Copy `.env.example` and rename it to `.env`, then set your bot token:
```sh
BOT_TOKEN=your-telegram-bot-token
```

### 3️⃣ Install dependencies
```sh
pip install -r requirements.txt
```

### 4️⃣ Run the bot
```sh
python main.py
```

---

## 🐳 Running with Docker
If you want to run the bot inside a **Docker container**, follow these steps:

### 1️⃣ Build the Docker image
```sh
docker build -t iperf3-bot .
```

### 2️⃣ Run the container
```sh
docker run -d --name iperf3-bot --env-file .env iperf3-bot
```

---

## 📜 Available Commands
| Command  | Description |
|----------|------------|
| `/start` | Start the bot and see welcome message |
| `/play`  | Start a new speed test session |
| `1. Graph 📈` | Choose graph format for results |
| `2. Text 📃`  | Choose text format for results |

---

## ⚙️ Project Structure
```
/src
 ├── handlers/         # Telegram command handlers
 │    ├── user.py      # User commands and FSM states
 │    ├── func.py      # Helper functions (iperf3 execution, graph generation)
 ├── keyboards/        # ReplyKeyboards for user input
 ├── shared/           # Global settings & configuration
 │    ├── fsm_state.py # FSM states definition
 │    ├── config.py    # Environment variable handling
 ├── main.py           # Main bot entry point
```

---

## 📡 How It Works
1️⃣ The user sends **`/play`**.  
2️⃣ The bot asks for **output format** (Graph 📈 or Text 📃).  
3️⃣ The user enters **test duration (seconds)**.  
4️⃣ The bot asks for the **IP address** of the `iperf3` server.  
5️⃣ The bot runs the `iperf3` test and **returns the result** in the chosen format.  

---

## 🛠 Requirements
- **Python 3.10+**
- `aiogram==3.2.0`
- `iperf3==0.1.11`
- `matplotlib==3.7.1`
- `pydantic-settings==2.0.3`
- `numpy<2`
- `aiohttp==3.9.3`
- `iperf3` installed on the system  

---

## 💡 Future Improvements
✅ Add support for **multiple concurrent tests**  
✅ Implement **logging and error tracking**  
✅ Add **custom bot commands for admins**  

---

## 💖 Credits
Developed by **[AiexCode](https://github.com/PonomarevAleksandr)**.  
If you found this project useful, **star 🌟 the repo!**  
