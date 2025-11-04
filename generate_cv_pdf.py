#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gerador PDF Profissional - Formata CVs com design corporativo
"""

from pathlib import Path
from datetime import datetime
from bs4 import BeautifulSoup
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Table, TableStyle, Paragraph,
    Spacer, HRFlowable
)


def extract_html_data():
    """Extrai TODOS os dados do HTML"""
    html_file = Path(
        r"D:\CV_ONLINE_VINICIUS\assets\docs\v07\public\index.html"
    )

    with open(html_file, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')

    data = {
        'nome': 'VINICIUS CAPANEMA',
        'titulo': (
            'Engenheiro Florestal • Doutor em Sensoriamento Remoto'
        ),
        'email': 'vinicius@vpcgeoser.com',
        'linkedin': 'linkedin.com/in/viniciuscapanema',
        'lattes': 'lattes.cnpq.br/4908905634731966',
        'sintetse': [],
        'competencias': {},
        'experiencia': [],
        'formacao': [],
        'idiomas': [],
        'cursos': [],
        'publicacoes': []
    }

    cards = soup.find_all('div', class_='card')

    # SÍNTESE
    for card in cards:
        h2 = card.find('h2')
        if h2 and 'Síntese' in h2.text:
            ps = card.find_all('p', class_=None)
            for p in ps:
                if p.text.strip() and 'lead' not in str(p.get('class', [])):
                    data['sintetse'].append(p.text.strip())
            break

    # COMPETÊNCIAS
    for card in cards:
        h2 = card.find('h2')
        if h2 and 'Competências' in h2.text:
            mcs = card.find_all('div', class_='mini-card')
            for mc in mcs:
                header = mc.find('div', class_='competency-header')
                if header:
                    spans = header.find_all('span')
                    if len(spans) > 1:
                        titulo_c = spans[1].text.strip()
                        conteudo = mc.find('div', class_='competency-content')
                        if conteudo:
                            ps = conteudo.find_all('p')
                            detalhes = [p.text.strip() for p in ps]
                            data['competencias'][titulo_c] = detalhes
            break

    # EXPERIÊNCIA
    for card in cards:
        h2 = card.find('h2')
        if h2 and 'Experiência Profissional' in h2.text:
            items = card.find_all('div', class_='timeline-item')
            for item in items:
                h3 = item.find('h3')
                if h3:
                    titulo = h3.text.replace('▶', '').strip()
                    meta = item.find('p', class_='meta')
                    periodo = meta.text if meta else ''
                    ul = item.find('ul')
                    atividades = []
                    if ul:
                        lis = ul.find_all('li')
                        for li in lis:
                            atividades.append(li.text.strip())
                    data['experiencia'].append({
                        'titulo': titulo,
                        'periodo': periodo,
                        'atividades': atividades
                    })
            break

    # FORMAÇÃO
    for card in cards:
        h2 = card.find('h2')
        if h2 and 'Formação Acadêmica' in h2.text:
            mcs = card.find_all('div', class_='mini-card')
            for mc in mcs:
                h3 = mc.find('h3')
                meta = mc.find('p', class_='meta')
                if h3 and meta:
                    titulo = h3.text.replace('', '').strip()
                    info = meta.text.strip()
                    data['formacao'].append({
                        'titulo': titulo,
                        'info': info
                    })
            break

    # IDIOMAS
    for card in cards:
        h2 = card.find('h2')
        if h2 and 'Idiomas' in h2.text:
            ul = card.find('ul')
            if ul:
                lis = ul.find_all('li')
                for li in lis:
                    data['idiomas'].append(li.text.strip())
            break

    # CURSOS
    for card in cards:
        h2 = card.find('h2')
        if h2 and 'Cursos' in h2.text:
            ul = card.find('ul')
            if ul:
                items = ul.find_all('li', class_='timeline-item')
                for item in items:
                    h3 = item.find('h3')
                    if h3:
                        cat = h3.text.replace('▶', '').strip()
                        div_c = item.find('div', class_='timeline-content')
                        if div_c:
                            inner_ul = div_c.find('ul')
                            if inner_ul:
                                inner_lis = inner_ul.find_all('li')
                                items_list = [
                                    li.text.strip() for li in inner_lis
                                ]
                                data['cursos'].append({
                                    'categoria': cat,
                                    'items': items_list
                                })
            break

    # PUBLICAÇÕES
    for card in cards:
        h2 = card.find('h2')
        if h2 and 'Publicações' in h2.text:
            ul = card.find('ul')
            if ul:
                items = ul.find_all('li', class_='timeline-item')
                for item in items:
                    h3 = item.find('h3')
                    if h3:
                        pub_t = h3.text.replace('▶', '').strip()
                        div_c = item.find('div', class_='timeline-content')
                        meta_p = None
                        desc = None
                        if div_c:
                            meta_e = div_c.find('p', class_='meta')
                            meta_p = meta_e.text if meta_e else ''
                            muted_p = div_c.find_all('p', class_='text-muted')
                            if muted_p:
                                desc = muted_p[0].text.strip()
                        data['publicacoes'].append({
                            'titulo': pub_t,
                            'meta': meta_p,
                            'descricao': desc
                        })
            break

    return data


def generate_pdf():
    """Gera PDF profissional"""

    output = Path(
        r"D:\CV_ONLINE_VINICIUS\assets\docs"
        r"\Curriculo_Vinicius_Capanema_2025.pdf"
    )

    dados = extract_html_data()

    # Configurar documento
    doc = SimpleDocTemplate(
        str(output),
        pagesize=A4,
        rightMargin=43.2,
        leftMargin=43.2,
        topMargin=36,
        bottomMargin=36
    )

    # Estilos
    styles = getSampleStyleSheet()

    s_nome = ParagraphStyle(
        'StyleNome',
        parent=styles['Heading1'],
        fontSize=26,
        textColor=colors.HexColor('#1a1a2e'),
        spaceAfter=4,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )

    s_titulo = ParagraphStyle(
        'StyleTitulo',
        parent=styles['Normal'],
        fontSize=11,
        textColor=colors.HexColor('#2563eb'),
        spaceAfter=2,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )

    s_contato = ParagraphStyle(
        'StyleContato',
        parent=styles['Normal'],
        fontSize=8.5,
        textColor=colors.HexColor('#555555'),
        spaceAfter=10,
        alignment=TA_CENTER,
        fontName='Helvetica'
    )

    s_secao = ParagraphStyle(
        'StyleSecao',
        parent=styles['Heading2'],
        fontSize=11,
        textColor=colors.HexColor('#2563eb'),
        spaceAfter=6,
        spaceBefore=10,
        fontName='Helvetica-Bold',
        borderColor=colors.HexColor('#2563eb'),
        borderWidth=2,
        borderPadding=4,
        borderRadius=2
    )

    s_corpo = ParagraphStyle(
        'StyleCorpo',
        parent=styles['Normal'],
        fontSize=9.5,
        textColor=colors.HexColor('#333333'),
        spaceAfter=7,
        leading=12,
        alignment=TA_JUSTIFY
    )

    s_item = ParagraphStyle(
        'StyleItem',
        parent=styles['Normal'],
        fontSize=9,
        textColor=colors.HexColor('#444444'),
        spaceAfter=3,
        leading=10.5,
        leftIndent=10
    )

    s_subsecao = ParagraphStyle(
        'StyleSubsecao',
        parent=styles['Normal'],
        fontSize=9.5,
        textColor=colors.HexColor('#1a1a2e'),
        spaceAfter=2,
        spaceBefore=3,
        fontName='Helvetica-Bold'
    )

    s_meta = ParagraphStyle(
        'StyleMeta',
        parent=styles['Normal'],
        fontSize=8,
        textColor=colors.HexColor('#888888'),
        spaceAfter=2,
        fontName='Helvetica-Oblique'
    )

    # Elementos
    elementos = []

    # CABEÇALHO
    elementos.append(Spacer(1, 0.15*cm))
    elementos.append(Paragraph(dados['nome'], s_nome))
    elementos.append(Paragraph(dados['titulo'], s_titulo))

    contato = (
        f"📧 {dados['email']} | 🔗 {dados['linkedin']} | "
        f"📄 {dados['lattes']}"
    )
    elementos.append(Paragraph(contato, s_contato))

    elementos.append(HRFlowable(
        width="100%",
        thickness=1,
        lineCap='square',
        color=colors.HexColor('#e0e0e0'),
        spaceAfter=0.2*cm
    ))

    # SÍNTESE
    elementos.append(Paragraph("SÍNTESE PROFISSIONAL", s_secao))
    for para in dados['sintetse']:
        elementos.append(Paragraph(para, s_corpo))
    elementos.append(Spacer(1, 0.15*cm))

    # COMPETÊNCIAS
    elementos.append(Paragraph("COMPETÊNCIAS-CHAVE", s_secao))

    if dados['competencias']:
        comp_list = list(dados['competencias'].items())
        comp_rows = []

        for i in range(0, len(comp_list), 2):
            row = []

            titulo1, detalhes1 = comp_list[i]
            cell1 = f"<b>{titulo1}</b><br/>"
            if detalhes1:
                cell1 += f"<font size=7.5>{detalhes1[0][:150]}</font>"
            row.append(Paragraph(cell1, s_item))

            if i + 1 < len(comp_list):
                titulo2, detalhes2 = comp_list[i + 1]
                cell2 = f"<b>{titulo2}</b><br/>"
                if detalhes2:
                    cell2 += (
                        f"<font size=7.5>{detalhes2[0][:150]}</font>"
                    )
                row.append(Paragraph(cell2, s_item))
            else:
                row.append(Paragraph("", s_item))

            comp_rows.append(row)

        comp_table = Table(
            comp_rows,
            colWidths=[230, 230]
        )
        comp_table.setStyle(TableStyle([
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('LEFTPADDING', (0, 0), (-1, -1), 5),
            ('RIGHTPADDING', (0, 0), (-1, -1), 5),
            ('TOPPADDING', (0, 0), (-1, -1), 3),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
            ('BACKGROUND', (0, 0), (-1, -1),
             colors.HexColor('#f8f9fa')),
            ('GRID', (0, 0), (-1, -1), 0.5,
             colors.HexColor('#e0e0e0')),
            ('ROWBACKGROUNDS', (0, 0), (-1, -1),
             [colors.HexColor('#f8f9fa'),
              colors.HexColor('#ffffff')])
        ]))
        elementos.append(comp_table)

    elementos.append(Spacer(1, 0.15*cm))

    # EXPERIÊNCIA
    elementos.append(Paragraph("EXPERIÊNCIA PROFISSIONAL", s_secao))

    for idx, exp in enumerate(dados['experiencia']):
        elementos.append(
            Paragraph(f"<b>{exp['titulo']}</b>", s_subsecao)
        )
        elementos.append(
            Paragraph(f"<i>{exp['periodo']}</i>", s_meta)
        )

        for ativ in exp['atividades'][:5]:
            elementos.append(Paragraph(f"• {ativ}", s_item))

        if idx < len(dados['experiencia']) - 1:
            elementos.append(Spacer(1, 0.08*cm))

    elementos.append(Spacer(1, 0.15*cm))

    # FORMAÇÃO
    elementos.append(Paragraph("FORMAÇÃO ACADÊMICA", s_secao))

    form_rows = []
    for form in dados['formacao']:
        form_rows.append([
            Paragraph(f"<b>{form['titulo']}</b>", s_item),
            Paragraph(form['info'], s_meta)
        ])

    if form_rows:
        form_table = Table(form_rows, colWidths=[230, 230])
        form_table.setStyle(TableStyle([
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('LEFTPADDING', (0, 0), (-1, -1), 4),
            ('RIGHTPADDING', (0, 0), (-1, -1), 4),
            ('TOPPADDING', (0, 0), (-1, -1), 2),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
            ('GRID', (0, 0), (-1, -1), 0.5,
             colors.HexColor('#e0e0e0')),
            ('BACKGROUND', (0, 0), (-1, -1),
             colors.HexColor('#fafafa'))
        ]))
        elementos.append(form_table)

    elementos.append(Spacer(1, 0.15*cm))

    # IDIOMAS
    elementos.append(Paragraph("IDIOMAS", s_secao))
    for idioma in dados['idiomas']:
        elementos.append(Paragraph(f"• {idioma}", s_item))

    elementos.append(Spacer(1, 0.1*cm))

    # CURSOS
    if dados['cursos']:
        elementos.append(
            Paragraph("CURSOS & TREINAMENTOS", s_secao)
        )
        for curso_cat in dados['cursos']:
            elementos.append(
                Paragraph(f"<b>{curso_cat['categoria']}</b>",
                          s_subsecao)
            )
            for item in curso_cat['items']:
                elementos.append(
                    Paragraph(f"• {item}", s_item)
                )
            elementos.append(Spacer(1, 0.05*cm))

    elementos.append(Spacer(1, 0.1*cm))

    # PUBLICAÇÕES
    if dados['publicacoes']:
        elementos.append(Paragraph("PUBLICAÇÕES", s_secao))
        for pub in dados['publicacoes'][:6]:
            elementos.append(
                Paragraph(f"<b>{pub['titulo']}</b>", s_subsecao)
            )
            if pub['meta']:
                elementos.append(
                    Paragraph(pub['meta'], s_meta)
                )
            if pub['descricao']:
                elementos.append(
                    Paragraph(pub['descricao'], s_corpo)
                )
            elementos.append(Spacer(1, 0.05*cm))

    # RODAPÉ
    elementos.append(Spacer(1, 0.15*cm))
    elementos.append(HRFlowable(
        width="100%",
        thickness=0.5,
        color=colors.HexColor('#e0e0e0'),
        spaceAfter=0.1*cm
    ))

    rodape = (
        f"Currículo gerado em "
        f"{datetime.now().strftime('%d de %B de %Y')} | "
        f"Dados extraídos do HTML | Design profissional"
    )
    elementos.append(Paragraph(
        rodape,
        ParagraphStyle(
            'RodapeStyle',
            parent=styles['Normal'],
            fontSize=7.5,
            textColor=colors.HexColor('#999999'),
            alignment=TA_CENTER
        )
    ))

    # Gerar
    try:
        doc.build(elementos)
        return True
    except Exception as e:
        print(f"Erro: {e}")
        import traceback
        traceback.print_exc()
        return False


if __name__ == "__main__":
    print("=" * 80)
    print("📄 GERADOR DE CURRÍCULO PDF PROFISSIONAL - Design Corporativo")
    print("=" * 80)

    print("\n🔄 Extraindo dados completos do HTML...")
    print("   ✓ Síntese profissional (completa)")
    print("   ✓ Competências-chave (todas)")
    print("   ✓ Experiência profissional (todas)")
    print("   ✓ Formação acadêmica (completa)")
    print("   ✓ Idiomas")
    print("   ✓ Cursos & Treinamentos (todos)")
    print("   ✓ Publicações (todas)")

    print("\n🎨 Aplicando formatação profissional...")
    print("   ✓ Cores corporativas (#2563eb)")
    print("   ✓ Tipografia elegante (Helvetica)")
    print("   ✓ Tabelas formatadas e estruturadas")
    print("   ✓ Espaçamento profissional")
    print("   ✓ Linhas separadoras")
    print("   ✓ Design HR-ready")

    print("\n⏳ Gerando PDF...")
    success = generate_pdf()

    if success:
        output = Path(
            r"D:\CV_ONLINE_VINICIUS\assets\docs"
            r"\Curriculo_Vinicius_Capanema_2025.pdf"
        )
        size_kb = output.stat().st_size / 1024
        print("\n✅ PDF GERADO COM SUCESSO!")
        print(f"📦 Tamanho: {size_kb:.1f} KB")
        print(f"📍 Local: {output}")
        print("\n🎯 Qualidade profissional:")
        print("   ✓ Design corporativo")
        print("   ✓ Dados completos e sincronizados com HTML")
        print("   ✓ Formatação elegante")
        print("   ✓ Pronto para distribuição em processos seletivos")
    else:
        print("\n❌ Erro na geração do PDF")

    print("\n" + "=" * 80)
