from django.shortcuts import render


def informatii_view(request):
    informatii = {
        'title': 'Titlul postării',
        'content': 'Conținutul postării...',
        'date': '15 mai 2023',
        'image_url': '/images/image.png',

    }
    return render(request, 'informatii.html', {'informatii_content': informatii})


def get_details(request):
    return None
