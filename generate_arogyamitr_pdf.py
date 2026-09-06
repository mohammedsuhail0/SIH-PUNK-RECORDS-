import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch

def generate_arogyamitr_pdf(output_path):
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
    c_green = colors.HexColor("#16a34a")

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
        fontSize=12,
        leading=15.5,
        textColor=c_navy,
        spaceBefore=10,
        spaceAfter=5
    )

    h2_style = ParagraphStyle(
        'SectionH2',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9.8,
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
    story.append(Paragraph("SMART INDIA HACKATHON 2026 — OFFICIAL TECHNICAL PROPOSAL", ParagraphStyle('PSTag', fontName='Helvetica-Bold', fontSize=8.5, textColor=c_primary, spaceAfter=2)))
    story.append(Paragraph("ArogyaMitr: Dual-Outlet Rural Healthcare Infrastructure & Voice-Guided Tele-Care Platform", title_style))
    story.append(Paragraph("Problem Statement ID: 26133 | Organization: Government of Maharashtra (MSInS) | Theme: MedTech / BioTech / HealthTech", subtitle_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=c_primary, spaceBefore=2, spaceAfter=8))

    # Executive Summary / 100-Word Description
    story.append(Paragraph("Executive Summary", h1_style))
    story.append(Paragraph("<b>ArogyaMitr</b> is a decentralized rural healthcare platform combining a physical dual-outlet infrastructure with a voice-guided, illiterate-friendly WebApp to bridge last-mile healthcare access. Our dual-outlet model establishes an <b>Inner-Village Care Point</b> for patient queries, basic triage, and assisted check-ins, supported by a shared <b>Outskirts Cluster Hub</b> that manages cold-chain medicine stock, diagnostic tests, and emergency logistics for 3–5 villages. The multilingual WebApp uses pictorial icons and regional voice prompts (Marathi/Hindi) for non-literate users. It enables direct doctor tele-consultations, instant prescription routing to the outskirts hub for rapid dispensing, 1-on-1 live human agent guidance, and one-touch 108 emergency SOS dispatch.", body_style))

    # Section 1: Problem Context
    story.append(Paragraph("1. Problem Analysis & Rural Ground Realities", h1_style))
    story.append(Paragraph("In rural and tribal regions of Maharashtra (including Gadchiroli, Melghat, and Nandurbar), healthcare delivery faces structural breakdowns across three dimensions:", body_style))
    story.append(Paragraph("• <b>The Digital Literacy Divide:</b> Over 45% of rural villagers cannot read or write complex English text or navigate standard telemedicine applications.", bullet_style))
    story.append(Paragraph("• <b>Travel Burden for Diagnostics & Drugs:</b> Even when villagers consult a doctor, they must travel 40–80 km to town centers simply to collect prescribed medicines and blood reports.", bullet_style))
    story.append(Paragraph("• <b>Emergency Isolation:</b> In acute emergencies (snakebites, cardiac distress, maternal complications), villagers lack one-touch panic connectivity or 1-on-1 human guidance to direct ambulances.", bullet_style))

    story.append(Spacer(1, 4))

    # Section 2: Proposed Solution Architecture
    story.append(Paragraph("2. Proposed Solution Architecture", h1_style))

    table_data = [
        [
            Paragraph("Component", table_header),
            Paragraph("Physical & Digital Architecture", table_header),
            Paragraph("Key Functions & Village Impact", table_header)
        ],
        [
            Paragraph("<b>Outlet 1: Gram Care Point</b><br/><i>(Inside Village Core)</i>", table_cell),
            Paragraph("Located at Gram Panchayat / Community Hall, equipped with a tablet kiosk and assisted by a local health volunteer.", table_cell),
            Paragraph("Handles daily patient queries, preliminary triage, basic vitals screening (BP, SpO2), and assisted digital onboarding.", table_cell)
        ],
        [
            Paragraph("<b>Outlet 2: Diagnostic & Supply Hub</b><br/><i>(Outskirts Cluster Junction)</i>", table_cell),
            Paragraph("Strategic highway facility serving a 3–5 village cluster (5–7 km radius), operating as a quick-commerce health micro-depot.", table_cell),
            Paragraph("Houses cold-chain medicines, processes rapid diagnostic tests, dispenses lab reports, and stages 108 emergency ambulances.", table_cell)
        ],
        [
            Paragraph("<b>Universal WebApp</b><br/><i>(Illiterate-Friendly UX)</i>", table_cell),
            Paragraph("Progressive Web App (PWA) with 100% pictorial icons, audio prompts in Marathi, Gondi, and Hindi, and zero-typing intake.", table_cell),
            Paragraph("Enables non-literate and elderly citizens to speak or tap large visual symbols (Heart, Head, Pregnancy, Emergency).", table_cell)
        ],
        [
            Paragraph("<b>1-on-1 Human Guide & SOS</b><br/><i>(Direct Tele-Care)</i>", table_cell),
            Paragraph("Live WebRTC video/audio channel to trained agents + One-Touch 108 Emergency SOS with GPS coordinate broadcasting.", table_cell),
            Paragraph("Provides reassuring, live step-by-step guidance in native dialects and dispatches nearby ambulances under 15 minutes.", table_cell)
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

    # Section 3: Technical Stack & Standards
    story.append(Paragraph("3. Technology Stack & Interoperability", h1_style))
    story.append(Paragraph("• <b>Frontend & Voice Engine:</b> React / Flutter PWA with Bhashini Speech-to-Text & Text-to-Speech APIs for natural spoken interactions in Marathi and Hindi. High-contrast icon layout for accessibility.", bullet_style))
    story.append(Paragraph("• <b>Telehealth & 1-on-1 Guidance:</b> LiveKit WebRTC media engine dynamically throttling audio down to 15 kbps for seamless calls over weak 2G/3G networks.", bullet_style))
    story.append(Paragraph("• <b>Micro-Fulfillment & Inventory Ledger:</b> FastAPI (Python) backend with PostgreSQL 16 tracking real-time pharmaceutical inventory and diagnostic test orders between the Outskirts Hub and District Warehouses.", bullet_style))
    story.append(Paragraph("• <b>National Digital Health Integration:</b> Compliant with Ayushman Bharat Digital Mission (ABDM) ABHA ID linkage and HL7 / FHIR R4 clinical JSON schemas; compliant with the DPDP Act 2023.", bullet_style))

    story.append(Spacer(1, 6))

    # Section 4: Implementation Roadmap
    story.append(Paragraph("4. Phased Implementation Roadmap", h1_style))
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
            Paragraph("<b>Phase 2: District Scale</b>", table_cell),
            Paragraph("Months 4 – 8", table_cell),
            Paragraph("Scale across <b>5 High-Priority Rural Districts</b> with 100 Outskirts Logistics Hubs serving 400+ villages; integrate with 108 Emergency Medical Services.", table_cell)
        ],
        [
            Paragraph("<b>Phase 3: Statewide Rollout</b>", table_cell),
            Paragraph("Months 9 – 12+", table_cell),
            Paragraph("Statewide deployment across <b>all 36 districts of Maharashtra</b>, federating with the Ayushman Bharat Digital Mission (ABDM) and national supply chains.", table_cell)
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

    # Section 5: Key Impacts
    story.append(Paragraph("5. Measurable Impact & Competitive Edge", h1_style))
    story.append(Paragraph("• <b>70% Reduction in Diagnostic Travel:</b> Eliminates long bus journeys to city centers for basic diagnostic tests and pharmaceutical pickup.", bullet_style))
    story.append(Paragraph("• <b>100% Inclusion for Non-Literate Citizens:</b> Voice-first prompts and large pictorial cues ensure no villager is excluded due to illiteracy.", bullet_style))
    story.append(Paragraph("• <b>< 15 Minute Emergency Response:</b> Direct 1-touch SOS coordinates immediate ambulance dispatch from the Outskirts Hub staging area.", bullet_style))
    story.append(Paragraph("• <b>Prescription-to-Dispense Continuity:</b> Tele-doctor prescriptions are auto-routed to the Outskirts Supply Hub for immediate preparation.", bullet_style))

    story.append(Spacer(1, 6))
    story.append(HRFlowable(width="100%", thickness=1, color=c_border, spaceBefore=2, spaceAfter=6))
    story.append(Paragraph("<i>ArogyaMitr — SIH 2026 Technical Submission | Government of Maharashtra | Maharashtra State Innovation Society</i>", ParagraphStyle('Footer', fontName='Helvetica-Oblique', fontSize=7.5, textColor=c_muted, alignment=1)))

    doc.build(story)
    print(f"PDF generated successfully at: {output_path}")

if __name__ == "__main__":
    out = r"C:\Users\Lenovo\Downloads\ArogyaMitr_SIH2026_PS26133_Solution_Proposal.pdf"
    generate_arogyamitr_pdf(out)
    scratch_out = r"C:\Users\Lenovo\.gemini\antigravity\scratch\mahahealth_connect\ArogyaMitr_SIH2026_PS26133_Solution_Proposal.pdf"
    generate_arogyamitr_pdf(scratch_out)
