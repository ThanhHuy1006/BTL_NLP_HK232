import io
import sys
import nltk
from nltk import CFG, ChartParser

# Đặt mã hóa mặc định cho stdout là UTF-8
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Định nghĩa ngữ pháp
grammar = CFG.fromstring("""
  S -> POSITIVE | NEGATIVE
  POSITIVE -> REQUEST_MORE_INFO | EXPRESS_INTEREST | ASK_DETAIL
  NEGATIVE -> EXCUSE | REJECT_OFFER | STATE_UNINTEREST
  REQUEST_MORE_INFO -> "tell" "me" "more" | "can" "you" "give" "me" "more" "details"
  EXPRESS_INTEREST -> "I'm" "interested" "in" "this" "product" | "this" "sounds" "interesting"
  ASK_DETAIL -> "can" "this" "product" "help" "me" "save" "costs"
  EXCUSE -> "I'm" "not" "free" "at" "the" "moment" | "I" "can't" "talk" "right" "now"
  REJECT_OFFER -> "no" "thanks" | "I'm" "not" "interested" "in" "it"
  STATE_UNINTEREST -> "I" "don't" "buy" "things" "from" "unsolicited" "calls"
""")
parser = ChartParser(grammar)

# Danh sách các câu thử nghiệm
test_sentences = {  
    "Tell me more": "POSITIVE",
    "Can this product help me save costs?": "POSITIVE",
    "No thanks": "NEGATIVE",
    "This sounds interesting": "POSITIVE",
    "Can you give me more details": "POSITIVE",

}

# Thực hiện phân tích cú pháp và phân loại
for sentence, expected in test_sentences.items():
    # Chuẩn hóa câu về chữ thường và tách từ, loại bỏ dấu câu
    words = sentence.lower().translate(str.maketrans('', '', ',.?')).split()
    parses = list(parser.parse(words))
    actual = "INVALID" if not parses else ("POSITIVE" if 'POSITIVE' in str(parses[0]) else "NEGATIVE")
    print(f"Testing: {sentence}")
    print(f"Expected: {expected}, Actual: {actual}")
    print("Result:", "PASS" if expected == actual else "FAIL")
    if parses:
        for tree in parses:
            tree.pretty_print()
    print("-" * 50)  # In dòng phân cách
