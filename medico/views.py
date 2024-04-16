from django.http import HttpRequest
from django.shortcuts import redirect, render
from .models import DadosMedico, Especialidades, is_medico
from django.contrib.messages import constants, add_message


# Create your views here.
def cadastro_medico(request: HttpRequest):

    if is_medico(request.user):
        add_message(request, constants.WARNING, "Você já é médico")
        return redirect("/medicos/abrir_horario")


    if request.method == "GET":
        especialidades = Especialidades.objects.all()
        return render(request, 'cadastro_medico.html', { "especialidades": especialidades })
    

    elif request.method == "POST":
        crm = request.POST.get('crm')
        nome = request.POST.get('nome')
        cep = request.POST.get('cep')
        rua = request.POST.get('rua')
        bairro = request.POST.get('bairro')
        numero = request.POST.get('numero')

        cim = request.FILES.get('cim')
        rg = request.FILES.get('rg')
        foto = request.FILES.get('foto')

        especialidade = request.POST.get('especialidade')
        descricao = request.POST.get('descricao')
        valor_consulta = request.POST.get('valor_consulta')

        dados_medicos = DadosMedico(
            crm=crm,
            nome=nome,
            cep=cep,
            rua=rua,
            bairro=bairro,
            numero=numero,
            cedula_identidade_medica=cim,
            foto=foto,
            especialidade_id=especialidade,
            descricao=descricao,
            valor_consulta=valor_consulta,
            user=request.user
        )

        dados_medicos.save()

        add_message(request, constants.SUCCESS, "Caadastro médico realizado com sucesso")
        return redirect("/medicos/abrir_horario")