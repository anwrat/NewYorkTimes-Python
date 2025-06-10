from datetime import datetime

def main():
    now = datetime.now()
    current_date = now.date()
    day = now.strftime("%A") # %A means weekday full version like Sunday, while %a means Sun (short version)
    print(f"{current_date} {day}")
    print("Hello this is New York Times")

if __name__ == '__main__':
    main()