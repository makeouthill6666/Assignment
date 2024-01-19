class Turtwig:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        damage = random.randint(1, self.attack_power)
        other.health -= damage
        return damage

class Chimchar:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        damage = random.randint(1, self.attack_power)
        other.health -= damage
        return damage

class Piplup:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        damage = random.randint(1, self.attack_power)
        other.health -= damage
        return damage


def main():
        print("포켓몬스터 PT 기라티나")

        print()

        input("PUSH ENTER BUTTON")

        print()

        print("흐음!! 잘 왔다!")

        input("")

        print("포켓몬스터의 세계에 온 것을 환영한다!")

        input("")

        print("내 이름은 마박사!")

        input("")

        print("모두가 포켓몬 박사님이라 부르고 있단다")

        input("")

        print("몬스터볼이다! 안에 포켓몬이 들어있다")

        input("")

        print("자! 어떤 포켓몬으로 할지 선택하거라")

        input("")

        starting = ''
        selected_pokemon = None
        while starting not in ['A', 'B', 'C']:
            starting = input(">A\n>B\n>C\n---->")
            print()

            if starting == 'A':
                print("어린잎포켓몬 모부기\n이 포켓몬으로 하겠느냐?")

                choice = input(">A 예\n>B 아니오\n---->")
                if choice == 'A':
                    print()
                    selected_pokemon = Turtwig("모부기", 55, 68)
                    print("모부기...\n역시! 좋은 포켓몬을 선택한 것 같구나")
                elif choice == 'B':
                    print("")
                    starting = ''
                else:
                    print("다시")

            elif starting == 'B':
                print("꼬마원숭이포켓몬 불꽃숭이\n이 포켓몬으로 선택하겠느냐?")

                choice = input(">A 예\n>B 아니오\n---->")
                if choice == 'A':
                    print()
                    selected_pokemon = Chimchar("불꽃숭이", 44, 58)
                    print("불꽃숭이...\n역시! 좋은 포켓몬을 선택한 것 같구나")
                elif choice == 'B':
                    print("")
                    starting = ''
                else:
                    print("다시")

            elif starting == 'C':
                print("펭귄포켓몬 팽도리\n이 포켓몬으로 정하겠느냐?")

                choice = input(">A예\n>B아니오\n---->")
                if choice == 'A':
                    print()
                    selected_pokemon = Piplup("팽도리", 53, 51)
                    print("팽도리\n역시! 좋은 포켓몬을 선택한 것 같구나")
                elif choice == 'B':
                    print("")
                    starting = ''
                else:
                    print("다시")

            else:
                starting = ''

        input("")

        print("알겠느냐!")

        input("")

        print("너에게 맡긴 포켓몬은 아직 밖의 세상을 모른다")

        input("")

        print("그런 의미로는 너희들이랑 닮았을지 모르겠구나")

        input("")

        print("으음! 닮은꼴끼리 잘 해보거라")

        input("")

        tutorial = ''

        while tutorial not in ['A', 'B', 'C']:
            tutorial = input(">A 풀숲에 들어간다\n>B 사람과 대화한다\n>C 종료\n---->")
            print()

            if tutorial == 'A':
                print("앗! 야생 피카츄가 튀어나왔다!")
                input("")
                print("가랏! 'pokemon'!")
                input("")
                print("'pokemon'은 무엇을 할까?")

                battle = ''
                while battle not in ['A', 'B']:
                    battle = input(">A 싸운다\n>B 도망친다\n---->")
                    print()

                    if battle == 'A':
                        print()
                        fight=''
                        while fight not in ['A','B','C']:
                            fight = input(">A 몸통박치기\n>B 째려보기\n>C 돌아가기\n---->")
                            print()

                            if fight == 'A':
                                pass

                            elif fight == 'B':
                                pass

                            elif fight == 'C':
                                battle = ''

                    elif battle == 'B':
                        print("무사히 도망쳤다!")
                        print()
                        tutorial = ''

                    else:
                        print("다시")
                        tutorial = ''

            if tutorial == 'B':
                print("광휘!!!\n포켓몬 승부다앗!")
                input("")
                print("포켓몬 트레이너 용식이 승부를 걸어왔다")
                input("")
                print("포켓몬 트레이너 용식은 (pokemon)를 내보냈다")
                input("")
                print("'pokemon'은 무엇을 할까?")

                battle = ''
                while battle not in ['A', 'B']:
                    battle = input(">A 싸운다\n>B 도망친다\n---->")
                    print()

                    if battle == 'A':
                        print()
                        fight = ''
                        while fight not in ['A', 'B', 'C']:
                            fight = input(">A 몸통박치기\n>B 째려보기\n>C 돌아가기\n---->")
                            print()

                            if fight == 'A':
                                pass

                            elif fight == 'B':
                                pass

                            elif fight == 'C':
                                battle = ''

                    elif battle == 'B':
                        print("도망칠 수 없다!")
                        print()
                        battle=''
                    else:
                        print("다시")
                        tutorial = ''


            if tutorial == 'C':
                print("여기까지의 활약을 포켓몬 레포트에 기록하겠습니까?")
                input("")
                choice = input(">A 예\n>B 아니오")
                if choice == 'A':
                    print(저장되었습니다)

                elif choice == 'B':
                    print("")
                    starting = ''


if __name__ == "__main__":
    main()
