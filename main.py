import time
from colorama import Fore, Style, init
import json
import csv

init(autoreset=True)

current_user = None
current_choice = None
current_health = 100
saves = []


def colored_print(text, color):
    print(f"{color}{text}{Style.RESET_ALL}")


def save_game():
    global current_user
    global current_choice
    global current_health
    global saves
    save_data = {
        "user": current_user,
        "choice": current_choice,
        "health": current_health,
    }
    saves.append(save_data)
    with open("saves.json", "w") as save_file:
        json.dump(saves, save_file)


def load_game():
    global current_user
    global current_choice
    global current_health
    global saves
    try:
        with open("saves.json", "r") as save_file:
            saves = json.load(save_file)
        if saves:
            current_save = saves[-1]
            current_user = current_save["user"]
            current_choice = current_save.get("choice", None)
            current_health = current_save.get("health", 100)
    except FileNotFoundError:
        print("Сохранения не найдены.")


def delete_save():
    global saves
    if saves:
        print("Выберите сохранение для удаления:")
        for i, save in enumerate(saves, 1):
            print(f"{i}. {save['user']} - {save['choice']}")
        try:
            choice = int(input("Введите номер сохранения для удаления: "))
            if 1 <= choice <= len(saves):
                deleted_save = saves.pop(choice - 1)
                print(f"Сохранение {deleted_save['user']} удалено.")
                with open("saves.json", "w") as save_file:
                    json.dump(saves, save_file)
            else:
                print("Некорректный выбор.")
        except ValueError:
            print("Введите число.")
    else:
        print("Нет сохранений для удаления.")


def game_over():
    global current_user
    global current_choice
    global current_health
    global saves
    colored_print("Игра окончена. Хотите сыграть еще раз? (да/нет)", Fore.RED)
    choice = input().lower()
    if choice == "да":
        start_game()
    else:
        with open("game_data.csv", "a", newline="") as csv_file:
            csv_writer = csv.writer(csv_file)
            for save in saves:
                csv_writer.writerow([current_user, save.get("choice", None), save.get("health", 100)])
        colored_print("Спасибо за игру! До свидания!", Fore.YELLOW)


def start_game():
    load_game()
    print("Вы находитесь в темном лесу.")
    time.sleep(1)
    print("Вы можете пойти влево, вправо, прямо или назад.")
    choice = input().lower()
    if choice == "влево":
        print("Вы находите заброшенный замок.")
        time.sleep(1)
        print("1. Исследовать замок")
        print("2. Пройти мимо")
        choice = input("Выберите действие: ")
        if choice == "1":
            print("Вы находите магический артефакт внутри замка.")
            time.sleep(1)
            print("Артефакт придает вам силу.")
            time.sleep(1)
            ancient_temple()
        elif choice == "2":
            print("Вы решаете не рисковать и идете дальше.")
            time.sleep(1)
            ancient_temple()
        else:
            print("Неверный выбор. Вы проигрываете.")
            game_over()
    elif choice == "вправо":
        print("Вы натыкаетесь на стаю волков.")
        time.sleep(1)
        print("1. Попытаться уйти")
        print("2. Сразиться с волками")
        choice = input("Выберите действие: ")
        if choice == "1":
            print("Вы уходите, но вас настигает волк.")
            time.sleep(1)
            battle()
        elif choice == "2":
            print("Вы сражаетесь с волками.")
            time.sleep(1)
            battle()
        else:
            print("Неверный выбор. Вы проигрываете.")
            game_over()
    elif choice == "прямо":
        print("Вы видите загадочный свет впереди.")
        time.sleep(1)
        print("1. Подойти ближе")
        print("2. Обойти стороной")
        choice = input("Выберите действие: ")
        if choice == "1":
            print("Вы подходите ближе и обнаруживаете магическую фонтанку.")
            time.sleep(1)
            print("Фонтанка возвращает вам здоровье и силы.")
            time.sleep(1)
            forest()
        elif choice == "2":
            print("Вы решаете обойти и идете дальше.")
            time.sleep(1)
            forest()
        else:
            print("Неверный выбор. Вы проигрываете.")
            game_over()
    elif choice == "назад":
        print("Вы решаете вернуться на своей пути.")
        time.sleep(1)
        underwater_cave()
    else:
        print("Неверный выбор. Вы проигрываете.")
        game_over()


def ancient_temple():
    print("Вы обнаруживаете древний храм в лесу.")
    time.sleep(1)
    print("Храм полон загадок и опасностей.")
    time.sleep(1)
    print("1. Исследовать храм")
    print("2. Пойти в другую сторону")
    choice = input("Выберите действие: ")
    if choice == "1":
        print("Вы входите в храм и сталкиваетесь с первой загадкой.")
        time.sleep(1)
        print("Решив ее, вы продвигаетесь дальше, но опасности только увеличиваются.")
        time.sleep(1)
        print("В конце храма вас ждет великое испытание.")
        time.sleep(1)
        battle()
    elif choice == "2":
        print("Вы решаете не рисковать и идете дальше в поисках других приключений.")
        time.sleep(1)
        forest()
    else:
        print("Неверный выбор. Вы проигрываете.")
        game_over()


def forest():
    print("Вы идете глубже в лес и натыкаетесь на странного волшебника.")
    time.sleep(1)
    print("Волшебник предлагает вам помощь в обмен на выполнение задания.")
    time.sleep(1)
    print("1. Согласиться на задание")
    print("2. Отказаться и продолжить свой путь")
    choice = input("Выберите действие: ")
    if choice == "1":
        print("Вы соглашаетесь выполнить задание волшебника.")
        time.sleep(1)
        print("Волшебник дарует вам магический посох.")
        time.sleep(1)
        print("Теперь у вас есть магическая сила.")
        time.sleep(1)
        mystical_cave()
    elif choice == "2":
        print("Вы решаете не связываться с волшебником и идете дальше.")
        time.sleep(1)
        mystical_cave()
    else:
        print("Неверный выбор. Вы проигрываете.")
        game_over()


def mystical_cave():
    print("Вы приходите к загадочной пещере.")
    time.sleep(1)
    print("1. Войти в пещеру")
    print("2. Пройти мимо")
    choice = input("Выберите действие: ")
    if choice == "1":
        print("Вы входите в пещеру и находите древние артефакты.")
        time.sleep(1)
        print("Артефакты придают вам магические способности.")
        time.sleep(1)
        print("Теперь вы можете использовать магию в битве.")
        time.sleep(1)
        continue_game()
    elif choice == "2":
        print("Вы решаете не рисковать и идете дальше.")
        time.sleep(1)
        continue_game()
    else:
        print("Неверный выбор. Вы проигрываете.")
        game_over()


def underwater_cave():
    print("Вы обнаруживаете вход в подводную пещеру.")
    time.sleep(1)
    print("1. Войти в пещеру")
    print("2. Пройти мимо")
    choice = input("Выберите действие: ")
    if choice == "1":
        print("Вы входите в пещеру и обнаруживаете потопленный корабль.")
        time.sleep(1)
        print("Исследуя корабль, вы находите сокровища и сундук с картой сокровищ.")
        time.sleep(1)
        print("1. Открыть сундук")
        print("2. Следовать по карте")
        choice = input("Выберите действие: ")
        if choice == "1":
            print("Вы открываете сундук и находите драгоценности.")
            time.sleep(1)
            print("С сокровищами в кармане вы возвращаетесь на берег.")
            time.sleep(1)
            continue_game()
        elif choice == "2":
            print("Вы следуете по карте и приходите к другой части пещеры.")
            time.sleep(1)
            print("Там вас ждет новая загадка.")
            time.sleep(1)
            print("1. Решить загадку")
            print("2. Вернуться обратно")
            choice = input("Выберите действие: ")
            if choice == "1":
                print("Вы решаете загадку и продвигаетесь дальше.")
                time.sleep(1)
                print("Вас ждет еще одно испытание.")
                time.sleep(1)
                battle()
            elif choice == "2":
                print("Вы решаете вернуться обратно.")
                time.sleep(1)
                continue_game()
            else:
                print("Неверный выбор. Вы проигрываете.")
                game_over()
        else:
            print("Неверный выбор. Вы проигрываете.")
            game_over()
    elif choice == "2":
        print("Вы решаете не рисковать и идете дальше.")
        time.sleep(1)
        continue_game()
    else:
        print("Неверный выбор. Вы проигрываете.")
        game_over()


def continue_game():
    print("Вы продолжаете свой путь и натыкаетесь на деревню.")
    time.sleep(1)
    print("Деревня - ваш следующий этап приключений.")
    save_game()
def continue_after_market():
    print("Вы решаете идти дальше после посещения рынка.")
    time.sleep(1)
    print("1. Пойти в лес")
    print("2. Пойти к реке")
    choice = input("Выберите действие: ")

    if choice == "1":
        print("Вы направляетесь в лес в поисках новых приключений.")
        time.sleep(1)
        ancient_temple()
    elif choice == "2":
        print("Вы направляетесь к реке, где вас ждут новые загадки.")
        time.sleep(1)
        underwater_cave()
    else:
        print("Неверный выбор. Вы проигрываете.")
        game_over()


def continue_in_village():
    print("Вы решаете исследовать деревню дальше.")
    time.sleep(1)
    print("1. Посетить лавку заклинаний")
    print("2. Обратиться к деревенскому старейшине")
    choice = input("Выберите действие: ")

    if choice == "1":
        print("Вы посещаете лавку заклинаний и находите магические предметы.")
        time.sleep(1)
        print("1. Купить магический свиток")
        print("2. Разговор с владельцем лавки")
        choice = input("Выберите действие: ")
        if choice == "1":
            print("Вы покупаете магический свиток и получаете новые заклинания.")
            time.sleep(1)
            print("Теперь у вас есть дополнительные возможности.")
            save_game()
        elif choice == "2":
            print("Вы разговариваете с владельцем лавки и узнаете интересные факты.")
            time.sleep(1)
            save_game()
        else:
            print("Неверный выбор. Вы проигрываете.")
            game_over()

    elif choice == "2":
        print("Вы обращаетесь к деревенскому старейшине.")
        time.sleep(1)
        print("1. Просить совет")
        print("2. Разговор о прошлых приключениях")
        choice = input("Выберите действие: ")
        if choice == "1":
            print("Старейшина дает вам мудрый совет.")
            time.sleep(1)
            save_game()
        elif choice == "2":
            print("Вы рассказываете старейшине о ваших прошлых приключениях.")
            time.sleep(1)
            save_game()
        else:
            print("Неверный выбор. Вы проигрываете.")
            game_over()

    else:
        print("Неверный выбор. Вы проигрываете.")
        game_over()


# ... (остальной код)

def continue_game():
    print("Вы продолжаете свой путь и натыкаетесь на деревню.")
    time.sleep(1)
    print("Деревня - ваш следующий этап приключений.")
    print("1. Посетить таверну")
    print("2. Обследовать рынок")
    print("3. Поговорить с местными жителями")
    choice = input("Выберите действие: ")

    if choice == "1":
        print("Вы заходите в таверну и узнаете интересные слухи.")
        time.sleep(1)
        print("1. Присоединиться к разговору")
        print("2. Пойти дальше")
        choice = input("Выберите действие: ")
        if choice == "1":
            print("Вы присоединяетесь к разговору и получаете новую информацию.")
            time.sleep(1)
            print("Таверна оказалась источником полезных подсказок.")
            save_game()
        elif choice == "2":
            print("Вы решаете пойти дальше.")
            continue_after_market()
        else:
            print("Неверный выбор. Вы проигрываете.")
            game_over()

    elif choice == "2":
        print("Вы обследуете рынок и находите несколько интересных предметов.")
        time.sleep(1)
        print("1. Купить что-то")
        print("2. Пройти мимо")
        choice = input("Выберите действие: ")
        if choice == "1":
            print("Вы покупаете предмет и получаете дополнительные ресурсы.")
            time.sleep(1)
            print("Теперь у вас есть новые возможности.")
            continue_in_village()
        elif choice == "2":
            print("Вы решаете пройти мимо и идти дальше.")
            save_game()
        else:
            print("Неверный выбор. Вы проигрываете.")
            game_over()

    elif choice == "3":
        print("Вы разговариваете с местными жителями, узнаете о местных проблемах и легендах.")
        time.sleep(1)
        print("1. Помочь решить проблему")
        print("2. Пройти мимо")
        choice = input("Выберите действие: ")
        if choice == "1":
            print("Вы решаете помочь местным жителям и получаете благословение.")
            time.sleep(1)
            print("Теперь у вас есть поддержка деревенских жителей.")
            save_game()
        elif choice == "2":
            print("Вы решаете пройти мимо и идти дальше.")
            save_game()
        else:
            print("Неверный выбор. Вы проигрываете.")
            game_over()

    else:
        print("Неверный выбор. Вы проигрываете.")
        game_over()

start_game()
