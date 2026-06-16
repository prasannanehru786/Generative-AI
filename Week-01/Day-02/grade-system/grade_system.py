# grade_system.py

def calculate_grade(mark):
    """
    Returns the letter grade based on the mark.
    """

    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    elif mark >= 60:
        return "D"
    else:
        return "E"


def main():
    print("=" * 40)
    print("      Student Grade Calculator")
    print("=" * 40)

    try:
        # Get user input
        mark = float(input("Enter your mark (0-100): "))

        # Validate range
        if mark < 0 or mark > 100:
            print("\n❌ Error: Mark must be between 0 and 100.")
            return

        # Calculate grade
        grade = calculate_grade(mark)

        # Display result
        print("\n📊 Result")
        print("-" * 20)
        print(f"Mark  : {mark}")
        print(f"Grade : {grade}")

    except ValueError:
        print("\n❌ Error: Please enter a valid numeric value.")


if __name__ == "__main__":
    main()