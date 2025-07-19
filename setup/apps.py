from django.apps import AppConfig

class TarefasConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tarefas'
    verbose_name = 'Gerenciador de Tarefas'  # Optional: human-readable name for the app