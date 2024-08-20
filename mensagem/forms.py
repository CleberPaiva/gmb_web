from django.forms import ModelForm
from .models import Mensagem


class MensagemForm(ModelForm):
    class Meta:
        model = Mensagem
        fields = [
            'nome',
            'email',
            'mural',
        ]
