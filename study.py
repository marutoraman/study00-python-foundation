# if文の使い方
def study_if():
    name="ライオン"

    if name=="パンダ":
        print("パンダは動物です")
        print("ifなか")
    print("ifそと")

# forの使い方
def study_for():
    for i in range(20):
        if i%2==1:
            print("{}は奇数です".format(i))
        else:
            print("{}は偶数です".format(i))

# Listの使い方
def study_list():
    name_list=["ぱんだ","らいおん","いるか","にんげん"]    
    animal_list=["ぱんだ","らいおん"]
    print(name_list)
    
    for name in name_list:
        if name in animal_list:
            print("{}は動物です。".format(name))
        else:
            print("{}は動物ではありません。".format(name))
            
# Ductの使い方
def study_dict():
    name_list=[{"name":"パンダ",
           "color":"白黒",
           "weight":"１００kg"},
          {"name":"ライオン",
           "color":"金色",
           "weight":"１５０kg"}]
    
    for name in name_list:
        print(name["name"])
    
# 関数の使い方
def view_animal(name_list):
    for name in name_list:
        print(name["name"])
    
    return len(name_list) 
    
def main():
    name_list=[{"name":"パンダ",
            "color":"白黒",
            "weight":"１００kg"},
            {"name":"ライオン",
            "color":"金色",
            "weight":"１５０kg"}]
    len_name_list=view_animal(name_list)
    print("{}匹でした".format(len_name_list))
    
if __name__ == "__main__":
    main()


