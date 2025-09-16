
alphabetSize: int = 26


def clearLastLine(count: int = 1) -> None:
    for _ in range(count):
        #? ANSI escape codes
        #? \x1b : escape char
        #? [1A  : move cursor up 1 line
        #? [2K  : nukes the current line
        #? \r   : puts the cursor in col 0
        print("\x1b[1A\x1b[2K\r", end="")


def isIntString(text: str) -> bool:
    #? just changes negative numbers into postives
    #? checks if the string is a digit
    return text.lstrip("-").isdigit()


def shiftCharacters(char: str, shift: int) -> str:
    #? ord turns a character into its unicode version so i can do math on it
    #? chr does the oppsite and turns the unicode into a char
    if "a" <= char <= "z":
        base: int = ord("a")
        return chr((ord(char) - base + shift) % alphabetSize + base)
    
    elif "A" <= char <= "Z":
        base: int = ord("A")
        return chr((ord(char) - base + shift) % alphabetSize + base)
    
    else: 
        return char
    
def applyCipher(text: str, shift: int) -> str:
    result: str = ""
    for char in text:
        result += shiftCharacters(char, shift)
    return result


def askalphabetSizee() -> str:
    while True:
        userAnswer: str = input("Encode or Decode: (e/d): ").strip().lower()
        if userAnswer in ("e", "d"):
            return userAnswer
        clearLastLine(1)

def askDecodeMethod() -> str:
    while True:
        userAnswer: str = input("Known offset or Brute force: (k/b): ").strip().lower()
        if userAnswer in ("k", "b"):
            return userAnswer
        clearLastLine(1)

def askOffset(prompt: str) -> int:
    while True:
        rawInputText: str = input(prompt).strip()
        if isIntString(rawInputText):
            return int(rawInputText) % alphabetSize
        clearLastLine



def main() -> None:
    print("==Caesar Cipher==")

    alphabetSizee: str = askalphabetSizee()

    if alphabetSizee == "e":
        rotationOffset: int = askOffset("Rotation/Offset: ")
        enteredText: str = input("Text to encode: ")
        print("\nEncoded:\n" + applyCipher(enteredText, rotationOffset))
    else: 
        decodeMethod: str = askDecodeMethod()
        if decodeMethod == "k":
            knownOffset: int = askOffset("Known offset: ")
            cipherText: str = input("Text to decode: ")
            print("\nDecoded:\n" + applyCipher(cipherText, (-knownOffset) % alphabetSize))
        
        else:
            cipherText: str = input("Text to brute force: ")
            print("\nTrying all 26 offsets:\n")
            for offsetValue in range(alphabetSize):
                attempt: str = applyCipher(cipherText, (-offsetValue) % alphabetSize)
                print(f"{offsetValue:2d}: {attempt}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nBye :(")
