questions = ["My name __ Vova", "I __ a coder", "I live __ Kazakhstan"]
answers = ["is", "am", "in"]

def points_word(total_points):
    last_digit = total_points % 10
    last_two_digits = total_points % 100
    
    return "балл" if last_digit == 1 and last_two_digits != 11 else \
           "балла" if 2 <= last_digit <= 4 and not (12 <= last_two_digits <= 14) else \
           "баллов"

def ask_question(question, answer):
    for attempts in range(3, 0, -1): 
        print(question)
        if input() == answer:
            print("Ответ верный!")
            return 4 - attempts
        if attempts != 1:
            print(f"Осталось попыток: {attempts-1}, попробуйте еще раз!")
    print(f"Увы, но нет. Верный ответ: {answer}")
    return 0

def main():
    if input('Привет! Предлагаю проверить свои знания английского! Наберите "ready", чтобы начать!\n').lower() == "ready":
        total_points = sum(ask_question(q, a) for q, a in zip(questions, answers))
        word = points_word(total_points)
        print(f"Вот и все! Вы ответили на {total_points//3} вопросов из {len(questions)} верно, вы набрали {total_points} {word}.")
    else:
        print("Кажется, вы не хотите играть. Очень жаль.")

if __name__ == "__main__":
    main()
