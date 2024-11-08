from dataclasses import dataclass
from typing import Optional
from uuid import UUID
from datetime import date

@dataclass
class NFModelSaida:
    recnum: Optional[int] = None
    filial: Optional[int] = None
    nota_fiscal: Optional[int] = None
    modelo: Optional[str] = None
    serie: Optional[str] = None
    serie_nf: Optional[str] = None
    cancelada: Optional[str] = None
    complementar: Optional[str] = None
    fatura: Optional[str] = None
    nf_devolucao: Optional[int] = None
    nf_modelodev: Optional[str] = None
    conhecimento: Optional[int] = None
    dtemissao: Optional[date] = None
    dtsaida: Optional[date] = None
    horario_saida: Optional[str] = None
    operacao: Optional[int] = None
    cfop01: Optional[int] = None
    cfop02: Optional[int] = None
    cfop03: Optional[int] = None
    cfop04: Optional[int] = None
    natureza_ope: Optional[str] = None
    insc_est_subs: Optional[str] = None
    vr_servico: Optional[float] = None
    vr_descontoos: Optional[float] = None
    vr_baseiss: Optional[float] = None
    perc_iss: Optional[float] = None
    vr_iss: Optional[float] = None
    vr_irrf: Optional[float] = None
    vr_inss: Optional[float] = None
    vr_desconto: Optional[float] = None
    vr_reducaoicms: Optional[float] = None
    vr_baseicms: Optional[float] = None
    vr_icms: Optional[float] = None
    vr_basesubst: Optional[float] = None
    vr_subst: Optional[float] = None
    vr_produtos: Optional[float] = None
    vr_frete: Optional[float] = None
    vr_seguro: Optional[float] = None
    vr_encargos: Optional[float] = None
    vr_ipi: Optional[float] = None
    vr_total: Optional[float] = None
    cliente: Optional[int] = None
    nome: Optional[str] = None
    endereco: Optional[str] = None
    bairro: Optional[str] = None
    cidade: Optional[str] = None
    estado: Optional[str] = None
    cep: Optional[str] = None
    fone: Optional[str] = None
    referencia: Optional[str] = None
    cpf: Optional[str] = None
    identidade: Optional[str] = None
    insc_produtor: Optional[str] = None
    qtd_volumes: Optional[int] = None
    numero: Optional[int] = None
    especie: Optional[str] = None
    marca: Optional[str] = None
    peso_bruto: Optional[float] = None
    peso_liquido: Optional[float] = None
    obs_operacao: Optional[str] = None
    observacao01: Optional[str] = None
    observacao02: Optional[str] = None
    observacao03: Optional[str] = None
    observacao04: Optional[str] = None
    observacao05: Optional[str] = None
    observacao06: Optional[str] = None
    observacao07: Optional[str] = None
    observacao08: Optional[str] = None
    texto01: Optional[str] = None
    texto02: Optional[str] = None
    texto03: Optional[str] = None
    texto04: Optional[str] = None
    texto05: Optional[str] = None
    formadoc01: Optional[str] = None
    formavlr01: Optional[float] = None
    formadt01: Optional[date] = None
    formadoc02: Optional[str] = None
    formavlr02: Optional[float] = None
    formadt02: Optional[date] = None
    formadoc03: Optional[str] = None
    formavlr03: Optional[float] = None
    formadt03: Optional[date] = None
    formadoc04: Optional[str] = None
    formavlr04: Optional[float] = None
    formadt04: Optional[date] = None
    formadoc05: Optional[str] = None
    formavlr05: Optional[float] = None
    formadt05: Optional[date] = None
    formadoc06: Optional[str] = None
    formavlr06: Optional[float] = None
    formadt06: Optional[date] = None
    formadoc07: Optional[str] = None
    formavlr07: Optional[float] = None
    formadt07: Optional[date] = None
    formadoc08: Optional[str] = None
    formavlr08: Optional[float] = None
    formadt08: Optional[date] = None
    formadoc09: Optional[str] = None
    formavlr09: Optional[float] = None
    formadt09: Optional[date] = None
    itens: Optional[int] = None
    data_inc: Optional[date] = None
    hora_inc: Optional[str] = None
    usu_inc: Optional[int] = None
    maq_inc: Optional[str] = None
    data_alt: Optional[date] = None
    hora_alt: Optional[str] = None
    usu_alt: Optional[int] = None
    maq_alt: Optional[str] = None
    data_exc: Optional[date] = None
    hora_exc: Optional[str] = None
    usu_exc: Optional[int] = None
    maq_exc: Optional[str] = None
    envia_pocket: Optional[str] = None
    dtexportacao: Optional[date] = None
    desconto_icms: Optional[float] = None
    forma_emissao: Optional[str] = None
    vr_ii: Optional[float] = None
    vr_pis: Optional[float] = None
    vr_cofins: Optional[float] = None
    vr_pis_serv: Optional[float] = None
    vr_cofins_serv: Optional[float] = None
    chave_nfe: Optional[str] = None
    seq_cce: Optional[int] = None
    situacao_cce: Optional[str] = None
    fl_conting_paf: Optional[str] = None
    vr_retencaop: Optional[float] = None
    vr_retencaos: Optional[float] = None
    celular: Optional[str] = None
    id: Optional[UUID] = None
    vr_credito: Optional[float] = None
    ddd_celular: Optional[str] = None
    nf_origem: Optional[int] = None
    seq_nf_origem: Optional[int] = None
    nf_substituta: Optional[int] = None
    seq_nf_substituta: Optional[int] = None
    cnpj_ret: Optional[str] = None
    razao_ret: Optional[str] = None
    endereco_ret: Optional[str] = None
    numero_ret: Optional[str] = None
    referencia_ret: Optional[str] = None
    bairro_ret: Optional[str] = None
    cidade_ret: Optional[str] = None
    uf_ret: Optional[str] = None
    cep_ret: Optional[str] = None
    fone_ret: Optional[str] = None
    email_ret: Optional[str] = None
    ie_ret: Optional[str] = None
    cnpj_entrega: Optional[str] = None
    razao_entrega: Optional[str] = None
    endereco_entrega: Optional[str] = None
    numero_entrega: Optional[str] = None
    referencia_entrega: Optional[str] = None
    bairro_entrega: Optional[str] = None
    cidade_entrega: Optional[str] = None
    uf_entrega: Optional[str] = None
    cep_entrega: Optional[str] = None
    fone_entrega: Optional[str] = None
    email_entrega: Optional[str] = None
    ie_entrega: Optional[str] = None
    vr_fcp_st: Optional[float] = None
    intermediador_nfe: Optional[str] = None
    meiopagamento: Optional[str] = None
    ind_presenca: Optional[str] = None

    @classmethod
    def from_raw_data(cls, file: dict):
        return cls(
            recnum = file.get("recnum"),
            filial = file.get("filial"),
            nota_fiscal = file.get("nota_fiscal"),
            modelo = file.get("modelo"),
            serie = file.get("serie"),
            serie_nf = file.get("serie_nf"),
            cancelada = file.get("cancelada"),
            complementar = file.get("complementar"),
            fatura = file.get("fatura"),
            nf_devolucao = file.get("nf_devolucao"),
            nf_modelodev = file.get("nf_modelodev"),
            conhecimento = file.get("conhecimento"),
            dtemissao = file.get("dtemissao"),
            dtsaida = file.get("dtsaida"),
            horario_saida = file.get("horario_saida"),
            operacao = file.get("operacao"),
            cfop01 = file.get("cfop01"),
            cfop02 = file.get("cfop02"),
            cfop03 = file.get("cfop03"),
            cfop04 = file.get("cfop04"),
            natureza_ope = file.get("natureza_ope"),
            insc_est_subs = file.get("insc_est_subs"),
            vr_servico = file.get("vr_servico"),
            vr_descontoos = file.get("vr_descontoos"),
            vr_baseiss = file.get("vr_baseiss"),
            perc_iss = file.get("perc_iss"),
            vr_iss = file.get("vr_iss"),
            vr_irrf = file.get("vr_irrf"),
            vr_inss = file.get("vr_inss"),
            vr_desconto = file.get("vr_desconto"),
            vr_reducaoicms = file.get("vr_reducaoicms"),
            vr_baseicms = file.get("vr_baseicms"),
            vr_icms = file.get("vr_icms"),
            vr_basesubst = file.get("vr_basesubst"),
            vr_subst = file.get("vr_subst"),
            vr_produtos = file.get("vr_produtos"),
            vr_frete = file.get("vr_frete"),
            vr_seguro = file.get("vr_seguro"),
            vr_encargos = file.get("vr_encargos"),
            vr_ipi = file.get("vr_ipi"),
            vr_total = file.get("vr_total"),
            cliente = file.get("cliente"),
            nome = file.get("nome"),
            endereco = file.get("endereco"),
            bairro = file.get("bairro"),
            cidade = file.get("cidade"),
            estado = file.get("estado"),
            cep = file.get("cep"),
            fone = file.get("fone"),
            referencia = file.get("referencia"),
            cpf = file.get("cpf"),
            identidade = file.get("identidade"),
            insc_produtor = file.get("insc_produtor"),
            qtd_volumes = file.get("qtd_volumes"),
            numero = file.get("numero"),
            especie = file.get("especie"),
            marca = file.get("marca"),
            peso_bruto = file.get("peso_bruto"),
            peso_liquido = file.get("peso_liquido"),
            obs_operacao = file.get("obs_operacao"),
            observacao01 = file.get("observacao01"),
            observacao02 = file.get("observacao02"),
            observacao03 = file.get("observacao03"),
            observacao04 = file.get("observacao04"),
            observacao05 = file.get("observacao05"),
            observacao06 = file.get("observacao06"),
            observacao07 = file.get("observacao07"),
            observacao08 = file.get("observacao08"),
            texto01 = file.get("texto01"),
            texto02 = file.get("texto02"),
            texto03 = file.get("texto03"),
            texto04 = file.get("texto04"),
            texto05 = file.get("texto05"),
            formadoc01 = file.get("formadoc01"),
            formavlr01 = file.get("formavlr01"),
            formadt01 = file.get("formadt01"),
            formadoc02 = file.get("formadoc02"),
            formavlr02 = file.get("formavlr02"),
            formadt02 = file.get("formadt02"),
            formadoc03 = file.get("formadoc03"),
            formavlr03 = file.get("formavlr03"),
            formadt03 = file.get("formadt03"),
            formadoc04 = file.get("formadoc04"),
            formavlr04 = file.get("formavlr04"),
            formadt04 = file.get("formadt04"),
            formadoc05 = file.get("formadoc05"),
            formavlr05 = file.get("formavlr05"),
            formadt05 = file.get("formadt05"),
            formadoc06 = file.get("formadoc06"),
            formavlr06 = file.get("formavlr06"),
            formadt06 = file.get("formadt06"),
            formadoc07 = file.get("formadoc07"),
            formavlr07 = file.get("formavlr07"),
            formadt07 = file.get("formadt07"),
            formadoc08 = file.get("formadoc08"),
            formavlr08 = file.get("formavlr08"),
            formadt08 = file.get("formadt08"),
            formadoc09 = file.get("formadoc09"),
            formavlr09 = file.get("formavlr09"),
            formadt09 = file.get("formadt09"),
            itens = file.get("itens"),
            data_inc = file.get("data_inc"),
            hora_inc = file.get("hora_inc"),
            usu_inc = file.get("usu_inc"),
            maq_inc = file.get("maq_inc"),
            data_alt = file.get("data_alt"),
            hora_alt = file.get("hora_alt"),
            usu_alt = file.get("usu_alt"),
            maq_alt = file.get("maq_alt"),
            data_exc = file.get("data_exc"),
            hora_exc = file.get("hora_exc"),
            usu_exc = file.get("usu_exc"),
            maq_exc = file.get("maq_exc"),
            envia_pocket = file.get("envia_pocket"),
            dtexportacao = file.get("dtexportacao"),
            desconto_icms = file.get("desconto_icms"),
            forma_emissao = file.get("forma_emissao"),
            vr_ii = file.get("vr_ii"),
            vr_pis = file.get("vr_pis"),
            vr_cofins = file.get("vr_cofins"),
            vr_pis_serv = file.get("vr_pis_serv"),
            vr_cofins_serv = file.get("vr_cofins_serv"),
            chave_nfe = file.get("chave_nfe"),
            seq_cce = file.get("seq_cce"),
            situacao_cce = file.get("situacao_cce"),
            fl_conting_paf = file.get("fl_conting_paf"),
            vr_retencaop = file.get("vr_retencaop"),
            vr_retencaos = file.get("vr_retencaos"),
            celular = file.get("celular"),
            id = file.get("id"),
            vr_credito = file.get("vr_credito"),
            ddd_celular = file.get("ddd_celular"),
            nf_origem = file.get("nf_origem"),
            seq_nf_origem = file.get("seq_nf_origem"),
            nf_substituta = file.get("nf_substituta"),
            seq_nf_substituta = file.get("seq_nf_substituta"),
            cnpj_ret = file.get("cnpj_ret"),
            razao_ret = file.get("razao_ret"),
            endereco_ret = file.get("endereco_ret"),
            numero_ret = file.get("numero_ret"),
            referencia_ret = file.get("referencia_ret"),
            bairro_ret = file.get("bairro_ret"),
            cidade_ret = file.get("cidade_ret"),
            uf_ret = file.get("uf_ret"),
            cep_ret = file.get("cep_ret"),
            fone_ret = file.get("fone_ret"),
            email_ret = file.get("email_ret"),
            ie_ret = file.get("ie_ret"),
            cnpj_entrega = file.get("cnpj_entrega"),
            razao_entrega = file.get("razao_entrega"),
            endereco_entrega = file.get("endereco_entrega"),
            numero_entrega = file.get("numero_entrega"),
            referencia_entrega = file.get("referencia_entrega"),
            bairro_entrega = file.get("bairro_entrega"),
            cidade_entrega = file.get("cidade_entrega"),
            uf_entrega = file.get("uf_entrega"),
            cep_entrega = file.get("cep_entrega"),
            fone_entrega = file.get("fone_entrega"),
            email_entrega = file.get("email_entrega"),
            ie_entrega = file.get("ie_entrega"),
            vr_fcp_st = file.get("vr_fcp_st"),
            intermediador_nfe = file.get("intermediador_nfe"),
            meiopagamento = file.get("meiopagamento"),
            ind_presenca = file.get("ind_presenca")

        )
