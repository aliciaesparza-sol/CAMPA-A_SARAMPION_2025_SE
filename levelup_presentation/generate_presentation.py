from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, ListFlowable, ListItem
from reportlab.lib.units import inch

def create_presentation():
    pdf_filename = "LEVEL_UP_Presentacion.pdf"
    doc = SimpleDocTemplate(
        pdf_filename,
        pagesize=letter,
        rightMargin=72,
        leftMargin=72,
        topMargin=72,
        bottomMargin=72
    )

    # Color Palette
    LEVEL_RED = colors.HexColor("#D32F2F")  # A professional dark red
    LEVEL_BLACK = colors.HexColor("#212121")
    LEVEL_GRAY = colors.HexColor("#757575")

    styles = getSampleStyleSheet()
    
    # Custom Styles
    title_style = ParagraphStyle(
        'LevelUpTitle',
        parent=styles['Title'],
        fontName='Helvetica-Bold',
        fontSize=36,
        leading=42,
        textColor=LEVEL_RED,
        alignment=TA_CENTER,
        spaceAfter=30
    )
    
    subtitle_style = ParagraphStyle(
        'LevelUpSubtitle',
        parent=styles['Heading2'],
        fontName='Helvetica',
        fontSize=18,
        leading=24,
        textColor=LEVEL_BLACK,
        alignment=TA_CENTER,
        spaceAfter=60
    )

    h1_style = ParagraphStyle(
        'LevelUpH1',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=20,
        leading=24,
        textColor=LEVEL_RED,
        spaceBefore=20,
        spaceAfter=10,
        borderPadding=(0, 0, 5, 0),
        borderWidth=0,
        borderColor=LEVEL_BLACK
    )

    h2_style = ParagraphStyle(
        'LevelUpH2',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=14,
        leading=18,
        textColor=LEVEL_BLACK,
        spaceBefore=12,
        spaceAfter=6
    )

    body_style = ParagraphStyle(
        'LevelUpBody',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=11,
        leading=14,
        textColor=LEVEL_BLACK,
        alignment=TA_JUSTIFY,
        spaceAfter=8
    )

    list_style = ParagraphStyle(
        'LevelUpList',
        parent=body_style,
        leftIndent=20,
        spaceAfter=4
    )
    
    centered_body_style = ParagraphStyle(
        'LevelUpBodyCentered',
        parent=body_style,
        alignment=TA_CENTER
    )
    
    price_style = ParagraphStyle(
        'LevelUpPrice',
        parent=h2_style,
        fontSize=16,
        textColor=LEVEL_RED,
        alignment=TA_LEFT
    )

    story = []

    # --- 1. Portada ---
    story.append(Spacer(1, 2*inch))
    story.append(Paragraph("LEVEL UP", title_style))
    story.append(Spacer(1, 0.5*inch))
    story.append(Paragraph("ORDEN. CONTINUIDAD. CONTROL. RESULTADOS.", subtitle_style))
    story.append(Spacer(1, 1*inch))
    story.append(Paragraph("Innovación y estrategia para el siguiente nivel de tu negocio.", centered_body_style))
    story.append(PageBreak())

    # --- 2. Introducción ---
    story.append(Paragraph("Introducción", h1_style))
    
    story.append(Paragraph("<b>Quién es Level Up</b>", h2_style))
    story.append(Paragraph("""
    Level Up es una empresa que innova y ayuda a los negocios a pasar al siguiente nivel, implementando estrategias integrales en uno de los sectores más importantes de cualquier local: el servicio al cliente.
    """, body_style))
    story.append(Paragraph("""
    A través de soluciones que optimizan la atención de llamadas y mejoran la experiencia de cada cliente, Level Up permite que los negocios ganen control, reduzcan estrés operativo y aumenten sus ventas, mientras enfocan su tiempo en crecer y destacar frente a la competencia.
    """, body_style))

    story.append(Paragraph("<b>Qué problema existe actualmente en los negocios</b>", h2_style))
    
    # Problem List Items
    story.append(Paragraph("<b>Alta demanda de atención telefónica</b>", body_style))
    story.append(ListFlowable([
        ListItem(Paragraph("Muchos negocios reciben más llamadas de las que pueden manejar.", list_style)),
        ListItem(Paragraph("Esto genera largas esperas, clientes frustrados y pérdida de ventas.", list_style)),
        ListItem(Paragraph("Consecuencia: La atención se vuelve inconsistente y puede dañar la reputación del negocio.", list_style)),
    ], bulletType='bullet', start='square'))

    story.append(Paragraph("<b>Logística de entrega deficiente o riesgosa</b>", body_style))
    story.append(ListFlowable([
         ListItem(Paragraph("El reparto puede ser lento, lo que provoca insatisfacción del cliente.", list_style)),
         ListItem(Paragraph("Riesgos físicos para repartidores o para los productos: accidentes, pérdida o daño de mercancía.", list_style)),
         ListItem(Paragraph("Esto también impacta en la percepción del negocio y aumenta costos por devoluciones o compensaciones.", list_style)),
    ], bulletType='bullet', start='square'))

    story.append(Paragraph("<b>Dependencia de aplicaciones externas de reparto</b>", body_style))
    story.append(ListFlowable([
         ListItem(Paragraph("Muchos locales no reciben suficientes pedidos directamente (por teléfono o propio canal digital).", list_style)),
         ListItem(Paragraph("Esto hace que dependan de apps de reparto que cobran altas comisiones.", list_style)),
         ListItem(Paragraph("Resultado: Pérdida de control sobre la relación con el cliente y reducción de márgenes de ganancia.", list_style)),
    ], bulletType='bullet', start='square'))

    story.append(Paragraph("<b>Impacto general de estos problemas</b>", body_style))
    story.append(ListFlowable([
         ListItem(Paragraph("Incapacidad de atender a todos los clientes con la misma eficacia.", list_style)),
         ListItem(Paragraph("Pérdida de clientes y oportunidades de ventas.", list_style)),
         ListItem(Paragraph("Aumento de costos operativos y reducción de rentabilidad.", list_style)),
    ], bulletType='bullet', start='square'))

    story.append(Paragraph("<b>Por qué la atención telefónica es crítica</b>", h2_style))
    story.append(Paragraph("""
    La atención telefónica resulta fundamental, ya que es el canal preferido principalmente por dos tipos de clientes: los habituales y los nuevos. La falta de atención adecuada al cliente habitual puede generar una pérdida de confianza en la marca, mientras que la deficiente atención al cliente nuevo representa la pérdida de una oportunidad de fidelización y disminuye la probabilidad de que regrese.
    """, body_style))
    
    story.append(PageBreak())

    # --- 3. La Problemática ---
    story.append(Paragraph("La Problemática", h1_style))
    story.append(Paragraph("""
    Los negocios pierden llamadas telefónicas no por negligencia, sino por carga operativa, estrés y falta de tiempo. Contestar el celular implica interrupciones constantes en la operación diaria.
    """, body_style))
    story.append(Paragraph("<b>Las llamadas perdidas significan ventas perdidas.</b>", ParagraphStyle('BoldRed', parent=body_style, textColor=LEVEL_RED, fontName='Helvetica-Bold')))

    # --- 4. La Solución Level Up ---
    story.append(Paragraph("La Solución Level Up", h1_style))
    story.append(Paragraph("Level Up centraliza y organiza la atención telefónica para garantizar resultados:", body_style))
    
    solution_items = [
        "Garantiza que todas las llamadas sean atendidas.",
        "Captura pedidos y datos completos.",
        "Envía la información directamente al negocio (WhatsApp u otro canal designado).",
        "Libera tiempo, reduce estrés y mejora el control operativo.",
        "Agiliza tiempos de entrega por pedido.",
        "Mejora la satisfacción general del cliente."
    ]
    
    list_items = [ListItem(Paragraph(item, list_style)) for item in solution_items]
    story.append(ListFlowable(list_items, bulletType='bullet', start='circle'))
    
    story.append(Spacer(1, 0.2*inch))
    story.append(Paragraph("<i>“Le quitamos el celular de las manos al negocio para que pueda enfocarse en lo importante.”</i>", 
                           ParagraphStyle('Quote', parent=body_style, alignment=TA_CENTER, fontSize=12, spaceBefore=10, spaceAfter=10)))

    # --- 5. Modelo de Trabajo ---
    story.append(Paragraph("Modelo de Trabajo", h1_style))
    story.append(Paragraph("Nuestro servicio se integra fluidamente en su operación:", body_style))
    model_items = [
        "<b>Implementación:</b> Configuramos el desvío de llamadas o línea dedicada.",
        "<b>Atención:</b> Nuestro equipo profesional atiende cada llamada con sus protocolos.",
        "<b>Gestión:</b> Capturamos la orden y los detalles del cliente.",
        "<b>Transmisión:</b> Enviamos la informacion procesada a su equipo listo para preparar.",
    ]
    story.append(ListFlowable([ListItem(Paragraph(item, list_style)) for item in model_items], bulletType='bullet'))
    
    story.append(PageBreak())

    # --- 6. Paquetes de Servicio ---
    story.append(Paragraph("Paquetes de Servicio", h1_style))

    # Level 1
    story.append(Paragraph("Paquete Level 1", h2_style))
    story.append(Paragraph("$1,000 MXN / Mensual", price_style))
    story.append(Paragraph("<b>Promoción: 1 semana gratis</b>", body_style))
    story.append(ListFlowable([
        ListItem(Paragraph("Atención total de llamadas", list_style)),
        ListItem(Paragraph("Captura de pedidos", list_style)),
        ListItem(Paragraph("Envío automático de comandas", list_style)),
        ListItem(Paragraph("Eliminación de la carga del celular", list_style)),
    ], bulletType='bullet'))

    # Level 2
    story.append(Paragraph("Paquete Level 2", h2_style))
    story.append(Paragraph("$2,000 MXN / Mensual", price_style))
    story.append(Paragraph("Incluye todo lo de Level 1, más:", body_style))
    story.append(ListFlowable([
        ListItem(Paragraph("Incremento del tráfico de llamadas", list_style)),
        ListItem(Paragraph("Publicidad y posicionamiento", list_style)),
        ListItem(Paragraph("Fotos, videos y publicaciones en redes sociales", list_style)),
    ], bulletType='bullet'))
    story.append(Paragraph("<i>Ideal para negocios que aún no reciben suficientes llamadas</i>", body_style))

    # Level 3
    story.append(Paragraph("Paquete Level 3", h2_style))
    story.append(Paragraph("Opción A: $20,000 MXN / Mensual", price_style))
    story.append(Paragraph("Opción B: $70 MXN / Envío", price_style))
    story.append(Paragraph("Incluye todo lo de Level 1 y 2, más:", body_style))
    story.append(ListFlowable([
        ListItem(Paragraph("Promociones exclusivas por llamada telefónica", list_style)),
        ListItem(Paragraph("Servicio de entrega con dron exclusivo de la marca Level Up", list_style)),
        ListItem(Paragraph("Dron proporcionado al firmar contrato", list_style)),
        ListItem(Paragraph("Instalación de área de aterrizaje para el dron", list_style)),
    ], bulletType='bullet'))
    
    story.append(PageBreak())

    # --- 7, 8, 9. Misión, Visión, Valores ---
    story.append(Paragraph("Nuestra Esencia", h1_style))
    
    story.append(Paragraph("Misión", h2_style))
    story.append(Paragraph("""
    Ayudar a los negocios a mantener el control total de su atención al cliente, asegurando que cada uno sea atendido de forma ordenada, continua y profesional, para evitar la pérdida de ventas, reducir la carga operativa y permitir un crecimiento estable y sostenible con un aire innovador.
    """, body_style))

    story.append(Paragraph("Visión", h2_style))
    story.append(Paragraph("""
    Establecer un nuevo estándar en la gestión de la atención al cliente, donde el orden, la continuidad y el control sean la base del crecimiento de los negocios.
    """, body_style))

    story.append(Paragraph("Valores Level Up", h2_style))
    values = [
        "<b>El cliente siempre es atendido:</b> Ninguna llamada se pierde.",
        "<b>Simplicidad operativa:</b> Hacemos fácil lo difícil.",
        "<b>El tiempo vale más que el dinero:</b> Optimizamos cada segundo.",
        "<b>Resultados medibles:</b> Datos reales para decisiones reales.",
        "<b>Innovación con propósito:</b> Tecnología al servicio del crecimiento.",
        "<b>Crecimiento compartido:</b> Si tú creces, nosotros crecemos."
    ]
    story.append(ListFlowable([ListItem(Paragraph(val, list_style)) for val in values], bulletType='bullet'))

    story.append(Spacer(1, 0.5*inch))

    # --- 10. Manifiesto de Marca ---
    story.append(Paragraph("Manifiesto de Marca", h1_style))
    story.append(Paragraph("""
    En Level Up creemos en el <b>Orden</b> sobre el caos. <br/>
    Creemos en la <b>Continuidad</b> de la excelencia, no en esfuerzos aislados. <br/>
    Creemos en el <b>Control</b> que libera, no que restringe. <br/>
    Brindamos <b>Atención Constante</b> porque cada cliente cuenta. <br/>
    Impulsamos un <b>Crecimiento sin caos</b>.
    """, body_style))

    # --- 11. Cierre Comercial ---
    story.append(Spacer(1, 1*inch))
    story.append(Paragraph("¿Listo para el siguiente nivel?", title_style))
    story.append(Paragraph("Recupera el control de tu negocio hoy mismo.", centered_body_style))
    story.append(Paragraph("Contáctanos para activar tu semana de prueba gratis.", centered_body_style))

    # Build PDF
    doc.build(story)
    print(f"PDF generado exitosamente: {pdf_filename}")

if __name__ == "__main__":
    create_presentation()
