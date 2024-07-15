from django.shortcuts import render
from django.http import HttpResponse

def save_feedback_to_file(name, email, message, filename='feedback.txt'):
    with open(filename, 'a') as file:
        file.write(f"Name: {name}\n")
        file.write(f"Email: {email}\n")
        file.write(f"Message: {message}\n")
        file.write("="*40 + "\n")

def home(request):
    return render(request, 'home.html')

def contacts(request):
    if request.method == 'POST':
        # Получаем данные из формы
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        save_feedback_to_file(name, phone, message)

        # Обрабатываем данные (например, сохраняем их в базе данных, отправляем email и т.д.)
        # Здесь можно добавить код для обработки данных, например:
        # save_feedback_to_database(name, email, message)


        # Возвращаем ответ пользователю
        return HttpResponse("Спасибо, дорогой, за обратную связь!")

    # Если запрос GET, просто отображаем форму
    return render(request, 'contacts.html')
