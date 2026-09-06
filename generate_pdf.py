import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch

def generate_pdf(output_path):
    doc = SimpleDocTemplate(
        output_path,
        pagesize=letter,
        leftMargin=0.5 * inch,
        rightMargin=0.5 * inch,
        topMargin=0.5 * inch,
        bottomMargin=0.5 * inch
    )

    styles = getSampleStyleSheet()

    c_primary = colors.HexColor("#0284c7")
    c_navy = colors.HexColor("#0f172a")
    c_teal = colors.HexColor("#0d9488")
    c_dark_text = colors.HexColor("#1e293b")
    c_muted = colors.HexColor("#64748b")
    c_light_bg = colors.HexColor("#f8fafc")
    c_border = colors.HexColor("#cbd5e1")
    c_red = colors.HexColor("#ef4444")

    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=19,
        leading=23,
        textColor=c_navy,
        spaceAfter=4
    )

    subtitle_style = ParagraphStyle(
        'DocSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=15,
        textColor=c_primary,
        spaceAfter=10
    )

    h1_style = ParagraphStyle(
        'SectionH1',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=12.5,
        leading=16,
        textColor=c_navy,
        spaceBefore=10,
        spaceAfter=5
    )

    h2_style = ParagraphStyle(
        'SectionH2',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10,
        leading=13,
        textColor=c_teal,
        spaceBefore=6,
        spaceAfter=3
    )

    body_style = ParagraphStyle(
        'BodyDark',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=12,
        textColor=c_dark_text,
        spaceAfter=5
    )

    bullet_style = ParagraphStyle(
        'BulletDark',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=11.5,
        textColor=c_dark_text,
        leftIndent=12,
        spaceAfter=3
    )

    table_cell = ParagraphStyle(
        'TableCell',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=7.8,
        leading=10.5,
        textColor=c_dark_text
    )

    table_header = ParagraphStyle(
        'TableHeader',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.2,
        leading=11,
        textColor=colors.white
    )

    story = []

    # Title & Metadata Banner
    story.append(Paragraph("SMART INDIA HACKATHON 2026 — TECHNICAL PROPOSAL", ParagraphStyle('PSTag', fontName='Helvetica-Bold', fontSize=8.5, textColor=c_primary, spaceAfter=2)))
    story.append(Paragraph("MahaHealth Connect: Dual-Outlet Rural Infrastructure & Voice-First WebApp", title_style))
    story.append(Paragraph("Problem Statement ID: 26133 | Organization: Government of Maharashtra | Theme: MedTech / BioTech / HealthTech", subtitle_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=c_primary, spaceBefore=2, spaceAfter=8))

    # Section 1
    story.append(Paragraph("1. Problem Context & Ground Realities in Rural Maharashtra", h1_style))
    story.append(Paragraph("In rural and tribal regions of Maharashtra (such as Gadchiroli, Melghat, and Nandurbar), healthcare delivery faces acute structural bottlenecks: high rates of digital illiteracy, massive travel burdens for diagnostics and medicines, and zero-connectivity isolation during medical emergencies.", body_style))
    
    story.append(Paragraph("• <b>Digital & Language Literacy Divide:</b> Over 45% of rural and tribal citizens cannot read or write complex English text or navigate standard telemedicine apps.", bullet_style))
    story.append(Paragraph("• <b>Separation of Consultation vs Supplies:</b> Even if a villager consults a doctor remotely, they still have to travel 40–80 km to town pharmacies and diagnostic labs to get prescribed medicines and blood tests.", bullet_style))
    story.append(Paragraph("• <b>Emergency Isolation:</b> In critical emergencies (e.g. snakebites, maternal complications), villagers panic without direct SOS connectivity or 1-on-1 human guidance to direct ambulances.", bullet_style))

    story.append(Spacer(1, 4))

    # Section 2
    story.append(Paragraph("2. Proposed Solution: Dual-Outlet Village Model + Multilingual Universal WebApp", h1_style))
    story.append(Paragraph("Our solution combines physical decentralized infrastructure with an ultra-accessible, voice-first digital platform:", body_style))

    # Table of Core Capabilities
    table_data = [
        [
            Paragraph("System Component", table_header),
            Paragraph("Physical / Digital Architecture", table_header),
            Paragraph("Key Functions & Village Impact", table_header)
        ],
        [
            Paragraph("<b>Outlet 1: Gram Care Point</b><br/><i>(Inside Village Core)</i>", table_cell),
            Paragraph("Located at Gram Panchayat / Community Hall, equipped with a touch-kiosk and assisted by a local health volunteer.", table_cell),
            Paragraph("Handles primary patient queries, assisted digital intake, preliminary vitals screening (BP, SpO2), and tele-doctor connect.", table_cell)
        ],
        [
            Paragraph("<b>Outlet 2: Diagnostic & Supply Hub</b><br/><i>(Outskirts Road Junction)</i>", table_cell),
            Paragraph("Situated on the main arterial road serving a cluster of 3–5 surrounding villages. Houses cold-chain pharma inventory and diagnostic gear.", table_cell),
            Paragraph("Dispenses prescribed medicines, collects lab test samples, prints/distributes diagnostic reports, and acts as 108 ambulance staging base.", table_cell)
        ],
        [
            Paragraph("<b>Universal WebApp</b><br/><i>(Illiterate-Friendly UX)</i>", table_cell),
            Paragraph("Progressive Web App (PWA) built with 100% pictorial icons, color-coded status, and voice assistance in Marathi, Gondi, and Hindi.", table_cell),
            Paragraph("Empowers illiterate users to speak or tap large symbols (Heart, Head, Pregnancy, Emergency) with zero typing required.", table_cell)
        ],
        [
            Paragraph("<b>1-on-1 Live Agent & SOS</b><br/><i>(Human-Guided Support)</i>", table_cell),
            Paragraph("One-Touch Emergency SOS button directly alerts nearby ambulances and outposts. Live WebRTC video/audio channel connects users 1-on-1 to trained agents.", table_cell),
            Paragraph("Provides reassuring, live human step-by-step guidance in their native dialect during medical anxiety or emergency triage.", table_cell)
        ]
    ]

    t1 = Table(table_data, colWidths=[1.8 * inch, 3.1 * inch, 2.6 * inch])
    t1.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), c_navy),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('GRID', (0, 0), (-1, -1), 0.5, c_border),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, c_light_bg]),
        ('TOPPADDING', (0, 0), (-1, -1), 4.5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4.5),
    ]))
    story.append(t1)

    story.append(Spacer(1, 6))

    # Section 3
    story.append(Paragraph("3. Technical Architecture & Data Standards", h1_style))
    story.append(Paragraph("• <b>Frontend & Voice Engine:</b> React / Flutter PWA integrated with Bhashini Speech-to-Text and Text-to-Speech APIs for natural spoken intake in Marathi, Hindi, and regional dialects. High-contrast icon layout for non-literate accessibility.", bullet_style))
    story.append(Paragraph("• <b>Telehealth & 1-on-1 Guided Video:</b> LiveKit WebRTC media server dynamically throttling audio to 15 kbps for uninterrupted voice calls over weak 2G signals.", bullet_style))
    story.append(Paragraph("• <b>Cloud Backend & Supply Ledger:</b> FastAPI (Python) backend with PostgreSQL 16 tracking real-time pharmaceutical inventory and diagnostic test orders between the Outskirts Hub and District Warehouse.", bullet_style))
    story.append(Paragraph("• <b>Emergency SOS Gateway:</b> WebSocket connection with GPS location broadcasting to the Maharashtra 108 Emergency Ambulance network and the nearest Outskirts Diagnostic Hub.", bullet_style))
    story.append(Paragraph("• <b>ABDM & Interoperability:</b> Adheres to HL7 / FHIR R4 electronic medical record schemas linked to citizen ABHA IDs, compliant with the DPDP Act 2023.", bullet_style))

    story.append(Spacer(1, 6))

    # Section 4
    story.append(Paragraph("4. Rollout Roadmap & Feasibility", h1_style))
    roadmap_data = [
        [
            Paragraph("Phase", table_header),
            Paragraph("Timeline", table_header),
            Paragraph("Target Scope & Key Deliverables", table_header)
        ],
        [
            Paragraph("<b>Phase 1: Pilot Cluster</b>", table_cell),
            Paragraph("Months 1 – 3", table_cell),
            Paragraph("Deploy in <b>10 Villages (Gadchiroli/Melghat)</b>: 10 Inner Village Care Points + 2 Outskirts Diagnostic & Supply Hubs. Onboard 30 village health agents.", table_cell)
        ],
        [
            Paragraph("<b>Phase 2: District Scaling</b>", table_cell),
            Paragraph("Months 4 – 8", table_cell),
            Paragraph("Scale across <b>5 High-Priority Rural Districts</b> with 100 Outskirts Logistics Hubs serving 400+ villages, integrating with 108 Emergency Medical Services.", table_cell)
        ],
        [
            Paragraph("<b>Phase 3: Statewide Rollout</b>", table_cell),
            Paragraph("Months 9 – 12+", table_cell),
            Paragraph("Statewide rollout across <b>all 36 districts of Maharashtra</b>, federating with the Ayushman Bharat Digital Mission (ABDM) and national supply chains.", table_cell)
        ]
    ]

    t2 = Table(roadmap_data, colWidths=[1.5 * inch, 1.2 * inch, 4.8 * inch])
    t2.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), c_teal),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('GRID', (0, 0), (-1, -1), 0.5, c_border),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, c_light_bg]),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
    ]))
    story.append(t2)

    story.append(Spacer(1, 6))

    # Section 5
    story.append(Paragraph("5. Measurable Impact & Key Differentiators", h1_style))
    story.append(Paragraph("• <b>70% Reduction in Diagnostic Travel:</b> Eliminates long bus journeys to city centers for basic diagnostic tests and pharmaceutical pickup.", bullet_style))
    story.append(Paragraph("• <b>100% Inclusion for Non-Literate Citizens:</b> Voice-first prompts and large pictorial cues ensure no villager is excluded due to illiteracy.", bullet_style))
    story.append(Paragraph("• <b>< 15 Minute Emergency Response:</b> Direct 1-touch SOS coordinates immediate ambulance dispatch from the Outskirts Hub staging area.", bullet_style))
    story.append(Paragraph("• <b>Prescription-to-Dispense Continuity:</b> Tele-doctor prescriptions are auto-routed to the Outskirts Supply Hub for immediate preparation.", bullet_style))

    story.append(Spacer(1, 6))
    story.append(HRFlowable(width="100%", thickness=1, color=c_border, spaceBefore=2, spaceAfter=6))
    story.append(Paragraph("<i>MahaHealth Connect — SIH 2026 Technical Submission | Government of Maharashtra | Maharashtra State Innovation Society</i>", ParagraphStyle('Footer', fontName='Helvetica-Oblique', fontSize=7.5, textColor=c_muted, alignment=1)))

    doc.build(story)
    print(f"PDF generated successfully at: {output_path}")

if __name__ == "__main__":
    out = r"C:\Users\Lenovo\Downloads\SIH2026_PS_26133_Comprehensive_Guide.pdf"
    generate_pdf(out)
    scratch_out = r"C:\Users\Lenovo\.gemini\antigravity\scratch\mahahealth_connect\SIH2026_PS_26133_Comprehensive_Guide.pdf"
    generate_pdf(scratch_out)
