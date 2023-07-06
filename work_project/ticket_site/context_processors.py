from user.models import User


def get_all_users(request):
    students = User.objects.all()  # interoghez tabela student_student pentru a lua toti studentii
    return {'get_users': User}

# STEP1: Definim un fisier nou in djangoProject numit context_processors in care definim o functie ce va returna un dictionar
# cu toti studenti

# STEP2: In djangoProject in fisierul settings.py mergeti catre variabila Templates unde veti gasi lista numita
# context_processors unde veti adauga calea catre functia implementa in fisieru context_processors ('djangoProject.context_processors.get_all_students')

# STEP3: Accesam o pagina.html unde vrem sa afisam datele din functia scrisa in fisierul context_processors
