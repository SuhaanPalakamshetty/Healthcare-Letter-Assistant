# Healthcare Letter Assistant 🏥✉️

## Overview

Healthcare Letter Assistant is a Streamlit web application that helps healthcare providers generate professional and informal letters such as medical referrals, insurance appeals, and appointment reminders. Powered by OpenAI’s language model via the Groq API, it creates clear, well-structured letters customized by tone and recipient.

---

## Features

- Generate **Referral**, **Appeal**, and **Reminder** letters
- Choose between **Formal** and **Informal** tone
- Customize patient, sender, recipient info, reason, and appointment date
- Copy, view, and download generated letters easily
- Uses environment variables to securely handle API keys

---

## Try It Out:

- [here](https://healthcare-letter-assistanttabreadme-ov-file-kejgpazgbyot3ttip.streamlit.app/)

## Demo

![Video Demo](./demo/vid.mp4)  

---

## Getting Started

### Prerequisites

- Python 3.8 or later
- An OpenAI API key (Groq-compatible)
- Git (for cloning the repo)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/YOUR-USERNAME/healthcare-letter-assistant.git
   cd healthcare-letter-assistant

2. (Optional) Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate     # On Windows: venv\Scripts\activate

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   
4. Create a `.env` file in the root directory and add your API key:

   ```bash
   OPENAI_API_KEY=your-groq-api-key
## Usage:
1. Change your directory to your python environment

   ```bash
   cd C:\your\project\file\directory
2. Run the application

   ```bash
   python -m streamlit run main.py
## Contributing:
Contributions are welcome! Please open issues or submit pull requests on GitHub.
## License:
This project is licensed under the [MIT License](https://opensource.org/license/mit)
## Contact:
For questions, please reach out at kp7sun@gmail.com

### Thank you for using my Healthcare Letter Assistant!
