import random

# 掛け算の処理
def same_tens_times(tens):
    count = 1
    while True:
        #　片方の数が11,片方が10の位の数の掛け算の問題作成処理
        if tens == 11:
            li = [tens, random.randint(10, 19)]
            random.shuffle(li)
            x = li[0]
            y = li[1]

        # 十の位が同じで1の位の合計が10の数の掛け算の問題作成処理
        elif tens == 10:
            tens_value = random.randint(1, 9) * tens
            first_ones_value = random.randint(1, 9)
            second_ones_value = 10 - first_ones_value
            x = tens_value + first_ones_value
            y = tens_value + second_ones_value
            
        # 十の位が同じ数同士の掛け算の問題作成処理
        else:               
            x = random.randint(tens * 10, tens * 10 + 9)
            y = random.randint(tens * 10, tens * 10 + 9)

        #上記で作成した問題の表示と正誤判定処理
        print(f"""{count}問目
{x}×{y}=""")
        correct_answer = x * y
        my_answer = input()

        try:
            if int(my_answer) == correct_answer:
                print("正解！")
            else:
                print(f"不正解！正解は{correct_answer}です。")
        except ValueError:
            print(f"不正解!正解は{correct_answer}です。")
                  
        print("続ける→Enter モード選択に戻る→b")
        command = input()
        if command == "b" or command == "ｂ":
            print()
            return

        count += 1

#　＝＝メイン画面＝＝
another = ""

print("""---インド式計算のかけ算編---
始めるにはEnterを押してください。""")
input()

while True:
    try:
        print(f"""{another}数値を入力して計算するモードを選択してください。
１～９・・・１０の位が１～９同士の掛け算　例 １３×１５など
１０・・・１０の位が同じで１の位の合計が１０の数の掛け算　例 ２３×２７など
１１・・・片方が１１，片方が１０の位の数の掛け算　例　１１×１５など""")

        tens = int(input()) 
        if tens in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]:
            print()
            same_tens_times(tens)
            another = ""
            continue

        else:
            print("そのモードは存在しません。")


    except ValueError:
        print("数値を入力してください。")

    print()
    another = "もう一度"
    continue
