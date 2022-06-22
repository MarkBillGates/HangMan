import random # IMPORT RANDOM ĐỂ LẤY 1 TỪ NGẪU NHIÊN TRONG FILE WORD_LIST   
from words import word_list  # LẤY DATA WORDS TỪ FILE WORD_LIST 

def get_word():
    word = random.choice(word_list) # RANDOM  
    return word.upper() # CONVERT LOWERCASE TO UPPERCASE
# HAM RANDOM VA CHUYỂN ĐỔI CHỮ HOA THÀNH CHỮ THƯỜNG 

def play(word):
    word_completion = "_" * len(word) # TẠO MỘT CHUỖI TỪ ĐƯỢC TẠO BỞI USER CÓ ĐỘ DÀI BẰNG ĐỘ DÀI BẰNG TỪ ĐƯỢC RANDOM
    guessed = False # KHỞI TẠO BIẾN ĐOÁN MẶC ĐỊNH LÀ FALSE
    guessed_letters = [] # KHỞI TẠO MỘT CHUỖI CHỮ ĐÃ ĐƯỢC ĐOÁN SAU MỖI LƯỢT
    guessed_words = []  # KHỞI TẠO MỘT CHUỖI TỪ ĐÃ ĐƯỢC ĐOÁN SAU MỖI LƯỢT
    tries = 6 # KHỞI TẠO BIẾN TRIES ( SỐ LẦN ĐOÁN CHO PHÉP ) 
    print("Let's play Hangman!") # IN RA MÀN HÌNH 
    print(display_hangman(tries)) # IN RA MÀN HÌNH EMPTY STATE HANGMAN ( CHƯA SAI LẦN NÀO )
    print(word_completion) # IN RA MAN HINH CHUỖI ĐOÁN CẦN ĐƯỢC HOÀN THÀNH VỚI CÁC DẤU GẠCH NGANG DƯỚI 
    print("\n") # XUỐNG DÒNG 
    while not guessed and tries > 0: # LOOP VỚI ĐIỀU KIỆN ( GUESSED = TRUE AND TRIES > 0 )
        guess = input("Please guess a letter or word: ").upper() # YÊU CẦU NGƯỜI DÙNG NHẬP CHỮ HOẶC TỪ ĐOÁN ĐƯỢC VÀ BIẾN ĐỔI CHÚNG THÀNH CHỮ HOA ĐỂ SO SÁNH TOÁN TỬ VỚI TỪ ĐƯỢC RANDOM TRONG FILE WORD_LIST
        if len(guess) == 1 and guess.isalpha(): # NẾU USER NHẬP 1 CHỮ 
            if guess in guessed_letters: # NẾU CHỮ ĐOÁN ĐƯỢC NẰM TRONG CHUỖI CHỮ ĐÃ ĐOÁN  
                print("You already guessed the letter", guess)
            elif guess not in word: # NẾU CHỮ ĐOÁN ĐƯỢC KHÔNG NẰM TRONG CHUỖI CHỮ ĐÃ ĐOÁN 
                print(guess, "is not in the word.") 
                tries -= 1 # SỐ LẦN THỬ GIẢM XUỐNG 1 LẦN 
                guessed_letters.append(guess) # THÊM VÀO LIST TỪ ĐÃ ĐOÁN 
            else: # NẾU CHỮ ĐOÁN ĐƯỢC NẰM TRONG TỪ RANDOM 
                print("Good job,", guess, "is in the word!") 
                guessed_letters.append(guess) # THÊM VÀO LIST TỪ ĐÃ ĐOÁN  
                word_as_list = list(word_completion) # CHUYỂN ĐỔI CHUỖI SANG LIST
                indices = [i for i, letter in enumerate(word) if letter == guess] # KHỞI TẠO LIST INDEX ( CÁC CHỈ SỔ CỦA DẤU GẠCH NGANG VÀ CÁC CHỈ SỐ CỦA CÁC CHỮA VỪA ĐOÁN)
                for index in indices: 
                    word_as_list[index] = guess # GÁN CHỮ VỪA ĐOÁN VÀO LIST 
                word_completion = "".join(word_as_list) # CHUYỂN LIST VỪA GÁN THÀNH CHUỖI 
                if "_" not in word_completion: # NẾU '_' KHÔNG CÒN NẰM TRONG TỪ HOÀN THÀNH 
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha(): # NẾU ĐỘ DÀI CỦA TỪ VỪA ĐOÁN BẰNG ĐỘ DÀI CỦA TỪ RANDOM 
            if guess in guessed_words: # NẾU TỪ VỪA ĐOÀN NẰM TRONG TỪ ĐÃ ĐOÁN 
                print("You already guessed the word", guess)
            elif guess != word: # NẾU TỪ VỪA ĐOÁN KHÔNG PHẢI TỪ RANDOM
                print(guess, "is not the word.")
                tries -= 1 # SỐ LẦN THỬ GIẢM ĐI 1 LẦN 
                guessed_words.append(guess) # THÊM VÀO CHUỖI TỪ ĐÃ ĐOÁN 
            else: # NẾU ĐÚNG 
                guessed = True 
                word_completion = word
        else: # NẾU ĐỘ DÀI CHỮ HOẶC TỪ NHẬP VÀO KHÔNG BẰNG 1 HOẶC KHÁC ĐỘ DÀI TỪ RANDOM 
            print("Not a valid guess.")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed: # NẾU GUESSED ĐÚNG 
        print("Congrats, you guessed the word! You win!")
    else:
        print("Sorry, you ran out of tries. The word was " + word + ". Maybe next time!")


def display_hangman(tries):
    stages = [  # ĐẦU, THÂN, 2 TAY, 2 CHÂN ( HOÀN CHỈNH )
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # ĐẦU, THÂN, 2 TAY, 1 CHÂN
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # ĐẦU, THÂN, 2 TAY
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # ĐẦU , THÂN , 1 TAY
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # PHẦN ĐẦU
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # KHỞI TẠO BAN ĐẦU 
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries] # TRẢ VỀ DISPLAY VS GIÁ TRỊ TRÍE TƯƠNG ỨNG


def main(): # HÀM CHÍNH   
    word = get_word() # RANDOM TỪ 
    play(word) # CHƠI THÔI
    while input("Play Again? (Y/N) ").upper() == "Y": # TẠO VÒNG LẶP 
        word = get_word()
        play(word)


if __name__ == "__main__":
    main()
