from react_agent import run_agent

def main():
    user_input = input("Enter your request: ")
    response = run_agent(user_input)
    print("Agent:", response)

if __name__ == "__main__":
    main()
