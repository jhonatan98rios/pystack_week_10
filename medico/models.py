from django.db.models import Model, CharField, IntegerField, FloatField, ImageField, TextField, ForeignKey, DO_NOTHING
from django.contrib.auth.models import User

def is_medico(user):
    return DadosMedico.objects.filter(user=user).exists()

# Create your models here.
class Especialidades(Model):
    especialidade = CharField(max_length=100)

    def __str__(self) -> str:
        return self.especialidade
    

class DadosMedico(Model):
    crm = CharField(max_length=30)
    nome = CharField(max_length=100)
    cep = CharField(max_length=15)
    rua = CharField(max_length=100)
    bairro = CharField(max_length=100)
    numero = IntegerField()
    rg = ImageField(upload_to='rgs')
    cedula_identidade_medica = ImageField(upload_to='cim')
    foto = ImageField(upload_to='foto_perfil')
    descricao = TextField()
    valor_consulta = FloatField(default=100)
    user = ForeignKey(User, on_delete=DO_NOTHING)
    especialidade = ForeignKey(Especialidades, on_delete=DO_NOTHING)

    def __str__(self) -> str:
        return self.user.username