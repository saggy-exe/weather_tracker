from api import fetch_weather
from database import WeatherDB
from datetime import datetime


def display_weather(result):
    print(f"City: {result['city']}")
    print(f"Temperature: {result['temperature']}°C")
    print(f"Description: {result['description']}")
    print(f"Humidity: {result['humidity']}%")
    print(f"Fetched at: {result['fetched_at']}")


def display_history(rows):
    if not rows:
        print("No history found.")
        return

    print("\n" + "="*100)
    print(f"{'ID':<5} {'City':<15} {'Temp (°C)':<10} {'Humidity':<10} {'Time':<20} {'Description'}")
    print("="*100)

    for row in rows:
        id_, city, temp, desc, humidity, ts = row

        time_str = datetime.fromtimestamp(ts).strftime("%Y-%m-%d %H:%M:%S")

        print(f"{id_:<5} {city:<15} {temp:<10.2f} {humidity:<10} {time_str:<20} {desc}")

    print("="*100)


def display_stats(stats):
    if stats[0] is None:
        print("No data available.")
        return

    avg, max_t, min_t = stats
    print(f"Average Temp: {avg:.2f}°C")
    print(f"Max Temp: {max_t}°C")
    print(f"Min Temp: {min_t}°C")


def main():
    db = WeatherDB()

    while True:
        print("\n1. Fetch Weather")
        print("2. View History")
        print("3. City Stats")
        print("4. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            city = input("Enter city: ").lower()

            try:
                result = fetch_weather(city)

                if not result:
                    print("City not found.")
                    continue

                display_weather(result)
                db.insert_weather(result)

            except PermissionError as e:
                print(f"Error: {e}")
            except Exception as e:
                print(f"Something went wrong: {e}")

        elif choice == "2":
            city = input("Enter city: ").lower()
            rows = db.view_history(city)
            display_history(rows)

        elif choice == "3":
            city = input("Enter city: ").lower()
            stats = db.city_stats(city)
            display_stats(stats)

        elif choice == "4":
            db.close()
            print("Goodbye 👋")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()