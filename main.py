from lexer import lexer
import parser

# --- Default code samples ---
default_snippets = [
    "x=10",
    "if [ x > 0 ] then x=10 else x=20 fi",
    "for i in range do echo i done",
    "while [ x < 5 ] do x=x+1 done",
    "function test() { x=10 }"
]

def parse_input(code):
    parser.syntax_error = False
    parser.parser.parse(code,lexer=lexer)
    if parser.syntax_error:
        print("Rejected")
    else:
        print("Accepted")

def test_default_samples():
    for i, snippet in enumerate(default_snippets, start=1):
        print(f"\n--- Sample {i} ---")
        print("Code:", snippet)

        print("\nTokens:")
        lexer.input(snippet)
        for tok in lexer:
            print(tok)

        print("\nParsing Result:")
        parse_input(snippet)

def test_custom_input():
    while True:
        user_input = input("\nEnter shell-like code (or 'exit' to quit): ").strip()
        if user_input.lower() == "exit":
            break
        print("\nTokens:")
        lexer.input(user_input)
        for tok in lexer:
            print(tok)

        print("\nParsing Result:")
        parse_input(user_input)

if __name__ == "__main__":
    print("=== Testing default samples ===")
    test_default_samples()
    print("\n=== Enter your own input ===")
    test_custom_input()
