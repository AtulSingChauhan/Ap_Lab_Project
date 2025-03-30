import re
import pandas as pd

def preprocess_chat(chat_file):
    with open(chat_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    data = []
    
    # Updated regex pattern to match the new format
    pattern = r'\[(\d{1,2}/\d{1,2}/\d{2,4}), (\d{1,2}:\d{2}:\d{2} ?[APM]{2})\] (.+?): (.+)'
    
    for line in lines:
        match = re.match(pattern, line)
        if match:
            date, time, user, message = match.groups()
            full_datetime = f"{date}, {time}"
            data.append([full_datetime, user.strip(), message.strip()])

    if not data:
        print("⚠️ No chat messages extracted! Check the chat format.")

    df = pd.DataFrame(data, columns=['datetime', 'user', 'message'])
    
    # Convert datetime column to proper format
    df['datetime'] = pd.to_datetime(df['datetime'], format='%d/%m/%y, %I:%M:%S %p', errors='coerce')
    
    return df

# Run this manually to test:
if __name__ == "__main__":
    df = preprocess_chat("sample_chat.txt")
    print(df.head())  # Display extracted messages
