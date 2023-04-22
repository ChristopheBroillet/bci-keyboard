from datetime import datetime

def test_to_send():
    now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    # now = now.strftime("%d/%m/%Y %H:%M:%S")
    return f"Message coming from the flask server {now}"
