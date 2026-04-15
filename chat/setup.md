```
python3 -m venv chat
source chat/bin/activate
pip install -r requirements.txt
```

```
# Basic usage
python chat.py --message "Hi, who are you?" --user-id "ricardo_test_1"

# Using short flags
python chat.py -m "What is LangGraph?" -u "ricardo_123"

# See full JSON output
python chat.py -m "Hello" -v
```