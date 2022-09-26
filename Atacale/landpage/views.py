from django.shortcuts import render, redirect
from landpage.models import registerCandidate
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.core.mail import send_mail

def land(request):
    
    if(request.method == "POST"):
        
        cargoInput = request.POST['cargo']
        nome_completoInput = request.POST['nome_completo']
        sexoInput = request.POST['sexo']
        naturalidadeInput = request.POST['naturalidade']
        nacionalidadeInput = request.POST['nacionalidade']
        alturaInput = request.POST['altura']
        pesoInput = request.POST['peso']
        data_aniversarioInput = request.POST['data_aniversario']
        idadeInput = request.POST['idade']
        celularInput = request.POST['celular']
        nome_paiInput = request.POST['nome_pai']
        nome_maeInput = request.POST['nome_mae']
        enderecoInput = request.POST['endereco']
        bairroInput = request.POST['bairro']
        cepInput = request.POST['cep']
        necessidade_especialInput = request.POST['necessidade_especial']
        necessidade_especial_descricaoInput = request.POST['necessidade_especial_descricao']
        
        habilitacaoInput = request.POST['habilitacao']
        categoria_habilitacaoInput = request.POST['categoria_habilitacao']
        reservistaInput = request.POST['reservista']
        cpfInput = request.POST['cpf']
        rgInput = request.POST['rg']
        orgao_expedidorInput = request.POST['orgao_expedidor']
        ufInput = request.POST['uf']
        escolaridadeInput = request.POST['escolaridade']
        status_escolaridadeInput = request.POST['status_escolaridade']
        data_conclusao_escolaridadeInput = request.POST['data_conclusao_escolaridade']
        instituicaoInput = request.POST['instituicao']
        estado_civilInput = request.POST['estado_civil']
        estado_civil_conjulgueInput = request.POST['estado_civil_conjulgue']
        filhosInput = request.POST['filhos']
        
        if request.POST['filhos_quantidade'] == '':
            filhos_quantidadeInput = None
        else:     
            filhos_quantidadeInput = request.POST['filhos_quantidade']
       
        if request.POST['filhos_moram'] == '':
            filhos_moramInput = None
        else:     
            filhos_moramInput = request.POST['filhos_moram']
        
        if request.POST['filhos_maior_idade'] == '':
            filhos_maior_idadeInput = None
        else:     
            filhos_maior_idadeInput = request.POST['filhos_maior_idade']
        
        instagramInput = request.POST['instagram']
        facebookInput = request.POST['facebook']
        linkedInInput = request.POST['linkedIn']
        
        if request.POST['rendas'] == '':
            rendasInInput = None
        else:     
            rendasInInput = request.POST['rendas']
        conta_em_bancoInInput = request.POST['conta_em_banco']
        bancosInInput = request.POST['bancos']
        imovelInput = request.POST['imovel']
        residenciaInput = request.POST['residencia']
        transporteInput = request.POST['transporte']
        transporte_descricaoInput = request.POST['transporte_descricao']
        parentesInput = request.POST['parentes']
        parentes_descricaoInput = request.POST['parentes_descricao']
        cursosInput = request.POST['cursos']
        cursos_descricaoInput = request.POST['cursos_descricao']
        
        primeiro_empregoInput = request.POST['primeiro_emprego']
        nome_ultima_empresaInput = request.POST['nome_ultima_empresa']
        responsavel_ultima_empresaInput = request.POST['responsavel_ultima_empresa']
        endereco_ultima_empresaInput = request.POST['endereco_ultima_empresa']
        telefone_ultima_empresaInput = request.POST['telefone_ultima_empresa']
        cargo_ultima_empresaInput = request.POST['cargo_ultima_empresa']    
            
        if request.POST['ultimo_salario_ultima_empresa'] == '':
            ultimo_salario_ultima_empresaInput = None
        else:
            ultimo_salario_ultima_empresaInput = request.POST['ultimo_salario_ultima_empresa']
        ctps_assinada_ultima_empresaInput = request.POST['ctps_assinada_ultima_empresa']
        motivo_saida_ultima_empresaInput = request.POST['motivo_saida_ultima_empresa']
        
        if request.POST['data_admisao_ultima_empresa'] == '':
            data_admisao_ultima_empresaInput = None
        else:
            data_admisao_ultima_empresaInput = request.POST['data_admisao_ultima_empresa']
            
        emprego_atual_ultima_empresaInput = request.POST['emprego_atual_ultima_empresa']
        
        if request.POST['data_demissao_ultima_empresa'] == '':
            data_demissao_ultima_empresaInput = None
        else:
            data_demissao_ultima_empresaInput = request.POST['data_demissao_ultima_empresa']
            
        atividade_ultima_empresaInput = request.POST['atividade_ultima_empresa']
        outro_empregoInput = request.POST['outro_emprego']
        nome_penultima_empresaInput = request.POST['nome_penultima_empresa']
        responsavel_penultima_empresaInput = request.POST['responsavel_penultima_empresa']
        endereco_penultima_empresaInput = request.POST['endereco_penultima_empresa']
        telefone_penultima_empresaInput = request.POST['telefone_penultima_empresa']
        cargo_penultima_empresaInput = request.POST['cargo_penultima_empresa']
        if request.POST['ultimo_salario_penultima_empresa'] == '':
            ultimo_salario_penultima_empresaInput = None
        else:
            ultimo_salario_penultima_empresaInput = request.POST['ultimo_salario_penultima_empresa']
        ctps_assinada_penultima_empresaInput = request.POST['ctps_assinada_penultima_empresa']
        motivo_saida_penultima_empresaInput = request.POST['motivo_saida_penultima_empresa']
        
        if request.POST['data_admisao_penultima_empresa'] == '':
            data_admisao_penultima_empresaInput = None
        else:
            data_admisao_penultima_empresaInput = request.POST['data_admisao_penultima_empresa']
        
        if request.POST['data_demissao_penultima_empresa'] == '':
            data_demissao_penultima_empresaInput = None
        else:
            data_demissao_penultima_empresaInput = request.POST['data_demissao_penultima_empresa']
            
        atividade_penultima_empresaInput = request.POST['atividade_penultima_empresa']
        empresa_destaqueInput = request.POST['empresa_destaque']
        curriculoInput = request.POST['curriculo']
        fotoInput = request.POST['foto']

        candidate = registerCandidate.objects.create(cargo = cargoInput,
                                            nome_completo = nome_completoInput,
                                            sexo = sexoInput,
                                            naturalidade = naturalidadeInput,
                                            nacionalidade = nacionalidadeInput,
                                            altura = alturaInput,
                                            peso = pesoInput,
                                            data_aniversario = data_aniversarioInput,
                                            idade = idadeInput,
                                            celular = celularInput,
                                            nome_pai = nome_paiInput,
                                            nome_mae = nome_maeInput,
                                            endereco = enderecoInput,
                                            bairro = bairroInput,
                                            cep = cepInput,
                                            necessidade_especial = necessidade_especialInput,
                                            necessidade_especial_descricao = necessidade_especial_descricaoInput,
                                            habilitacao = habilitacaoInput,
                                            categoria_habilitacao = categoria_habilitacaoInput,
                                            reservista = reservistaInput,
                                            cpf = cpfInput,
                                            rg = rgInput,
                                            orgao_expedidor = orgao_expedidorInput,
                                            uf = ufInput,
                                            escolaridade = escolaridadeInput,
                                            status_escolaridade = status_escolaridadeInput,
                                            data_conclusao_escolaridade = data_conclusao_escolaridadeInput,
                                            instituicao = instituicaoInput,
                                            estado_civil = estado_civilInput,
                                            estado_civil_conjulgue = estado_civil_conjulgueInput,
                                            filhos = filhosInput,
                                            filhos_quantidade = filhos_quantidadeInput,
                                            filhos_moram = filhos_moramInput,
                                            filhos_maior_idade = filhos_maior_idadeInput,
                                            instagram = instagramInput,
                                            facebook = facebookInput,
                                            linkedIn = linkedInInput,
                                            rendas = rendasInInput,
                                            conta_em_banco = conta_em_bancoInInput,
                                            bancos = bancosInInput,
                                            imovel = imovelInput,
                                            residencia = residenciaInput,
                                            transporte = transporteInput,
                                            transporte_descricao = transporte_descricaoInput,
                                            parentes = parentesInput,
                                            parentes_descricao = parentes_descricaoInput,
                                            cursos = cursosInput,
                                            cursos_descricao = cursos_descricaoInput,
                                            primeiro_emprego = primeiro_empregoInput,
                                            nome_ultima_empresa = nome_ultima_empresaInput,
                                            responsavel_ultima_empresa = responsavel_ultima_empresaInput,
                                            endereco_ultima_empresa = endereco_ultima_empresaInput,
                                            telefone_ultima_empresa = telefone_ultima_empresaInput,
                                            cargo_ultima_empresa = cargo_ultima_empresaInput,
                                            ultimo_salario_ultima_empresa = ultimo_salario_ultima_empresaInput,
                                            ctps_assinada_ultima_empresa = ctps_assinada_ultima_empresaInput,
                                            motivo_saida_ultima_empresa = motivo_saida_ultima_empresaInput,
                                            data_admisao_ultima_empresa = data_admisao_ultima_empresaInput,
                                            emprego_atual_ultima_empresa = emprego_atual_ultima_empresaInput,
                                            data_demissao_ultima_empresa = data_demissao_ultima_empresaInput,
                                            atividade_ultima_empresa = atividade_ultima_empresaInput,
                                            outro_emprego = outro_empregoInput,
                                            nome_penultima_empresa = nome_penultima_empresaInput,
                                            responsavel_penultima_empresa = responsavel_penultima_empresaInput,
                                            endereco_penultima_empresa = endereco_penultima_empresaInput,
                                            telefone_penultima_empresa = telefone_penultima_empresaInput,
                                            cargo_penultima_empresa = cargo_penultima_empresaInput,
                                            ultimo_salario_penultima_empresa = ultimo_salario_penultima_empresaInput,
                                            ctps_assinada_penultima_empresa = ctps_assinada_penultima_empresaInput,
                                            motivo_saida_penultima_empresa = motivo_saida_penultima_empresaInput,
                                            data_admisao_penultima_empresa = data_admisao_penultima_empresaInput,
                                            data_demissao_penultima_empresa = data_demissao_penultima_empresaInput,
                                            atividade_penultima_empresa = atividade_penultima_empresaInput,
                                            empresa_destaque = empresa_destaqueInput,
                                            
                                            curriculo = curriculoInput,
                                            foto = fotoInput,)
        print(fotoInput)
        print(curriculoInput) 
        #candidate.save()
        return redirect('/')
    
    return render(request, 'landpage/index.html',{})

def my_callback(sender, **kwargs):
    print("testando")
    subject = kwargs.get('instance').cargo
    email_template_name = "landpage/NewCandidate.txt"
    c = {
    "cargo": kwargs.get('instance').cargo,
    'nome_completo': kwargs.get('instance').nome_completo,
    'idade': kwargs.get('instance').idade,
    'altura': kwargs.get('instance').altura,
    'peso': kwargs.get('instance').peso,
    'sexo': kwargs.get('instance').sexo,
    'naturalidade': kwargs.get('instance').naturalidade,
    'uf': kwargs.get('instance').uf,
    'endereco': kwargs.get('instance').endereco,
    'bairro': kwargs.get('instance').bairro,
    'cep': kwargs.get('instance').cep,
    'celular': kwargs.get('instance').celular,
    }
    email = render_to_string(email_template_name, c)
    send_mail(subject, email, 'admin@example.com',
                ['brunomaya10@hotmail.com'], fail_silently=False)

post_save.connect(my_callback, registerCandidate, dispatch_uid="landpage")