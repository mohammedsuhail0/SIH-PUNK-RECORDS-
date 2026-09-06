import sys
import pptx
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

def populate_sih_template():
    template_path = r"C:\Users\Lenovo\Downloads\SIH2025-IDEA-Presentation-Format.pptx"
    prs = pptx.Presentation(template_path)

    # Color Palette
    C_NAVY = RGBColor(15, 23, 42)
    C_BLUE = RGBColor(2, 132, 199)
    C_TEAL = RGBColor(13, 148, 136)
    C_DARK = RGBColor(30, 41, 59)
    C_MUTED = RGBColor(71, 85, 105)
    C_GREEN = RGBColor(22, 163, 74)
    C_WHITE = RGBColor(255, 255, 255)

    # =========================================================================
    # SLIDE 1: TITLE PAGE
    # =========================================================================
    s1 = prs.slides[0]
    for shape in s1.shapes:
        if shape.has_text_frame:
            text = shape.text_frame.text
            if "Problem Statement ID" in text or "Problem Statement Title" in text:
                tf = shape.text_frame
                tf.clear()
                tf.word_wrap = True
                
                def add_meta_line(label, val, is_bold_val=True, color=C_DARK, size=11):
                    p = tf.add_paragraph()
                    p.space_after = Pt(4)
                    run1 = p.add_run()
                    run1.text = f"{label}: "
                    run1.font.bold = True
                    run1.font.size = Pt(size)
                    run1.font.color.rgb = C_BLUE
                    
                    run2 = p.add_run()
                    run2.text = val
                    run2.font.bold = is_bold_val
                    run2.font.size = Pt(size)
                    run2.font.color.rgb = color

                add_meta_line("Problem Statement ID", "26133", is_bold_val=True, size=13)
                add_meta_line("Problem Statement Title", "Accessibility and quality of public healthcare services, particularly in rural and underserved areas", is_bold_val=False, size=10.5)
                add_meta_line("Organization", "Government of Maharashtra (MSInS)", is_bold_val=True, size=11)
                add_meta_line("Theme", "MedTech / BioTech / HealthTech", is_bold_val=True, size=11)
                add_meta_line("Category", "Software Edition", is_bold_val=True, size=11)
                add_meta_line("Team Name", "ArogyaMitr", is_bold_val=True, color=C_GREEN, size=12)
                add_meta_line("Idea Title", "ArogyaMitr: Dual-Outlet Rural Healthcare Infrastructure & Voice-Guided Tele-Care Platform", is_bold_val=True, color=C_NAVY, size=11)

    # =========================================================================
    # SLIDE 2: PROPOSED SOLUTION (IDEA TITLE)
    # =========================================================================
    s2 = prs.slides[1]
    # Header
    for shape in s2.shapes:
        if shape.has_text_frame and "IDEA TITLE" in shape.text_frame.text:
            shape.text_frame.text = "PROPOSED SOLUTION: ArogyaMitr"
            shape.text_frame.paragraphs[0].font.size = Pt(20)
            shape.text_frame.paragraphs[0].font.bold = True
            shape.text_frame.paragraphs[0].font.color.rgb = C_NAVY
        elif shape.has_text_frame and "Proposed Solution" in shape.text_frame.text:
            tf = shape.text_frame
            tf.clear()
            tf.word_wrap = True
            
            def add_sec(title, bullets):
                p_head = tf.add_paragraph()
                p_head.space_before = Pt(4)
                p_head.space_after = Pt(2)
                r_head = p_head.add_run()
                r_head.text = title
                r_head.font.bold = True
                r_head.font.size = Pt(11)
                r_head.font.color.rgb = C_BLUE

                for b in bullets:
                    p_b = tf.add_paragraph()
                    p_b.space_after = Pt(2)
                    p_b.level = 0
                    r_b = p_b.add_run()
                    r_b.text = f"• {b}"
                    r_b.font.size = Pt(9.5)
                    r_b.font.color.rgb = C_DARK

            add_sec("1. Decentralized Physical Dual-Outlet Model", [
                "Outlet 1 (Gram Care Point - Inside Village): Gram Panchayat-based intake kiosk for daily patient queries, preliminary triage, basic vitals (BP/SpO2), and assisted digital check-ins by local health volunteers.",
                "Outlet 2 (Diagnostic & Supply Hub - Outskirts Junction): Strategic arterial hub serving 3–5 villages (5–7 km radius), operating as a quick-commerce healthcare dark store stocking cold-chain medicines and processing rapid lab tests."
            ])
            add_sec("2. Universal Voice-First & Illiterate-Friendly WebApp", [
                "100% Pictorial & Color-Coded UX: High-contrast visual icons (Heart, Pregnancy, Child, Fever, Emergency) eliminating reading/writing barriers.",
                "Regional Voice AI (Marathi/Hindi/Gondi): Natural spoken language intake with zero typing required.",
                "1-on-1 Guided Agent Support: Live human video/audio assistance guiding elderly/anxious villagers step-by-step.",
                "Direct 1-Touch 108 Emergency SOS: Instantly broadcasts patient GPS coordinates to nearby ambulances and staging hubs."
            ])
            add_sec("3. Instant Tele-Prescription to Medicine Dispensing Pipeline", [
                "Doctor tele-consultations auto-route digital prescriptions directly to the Outskirts Hub for rapid packing, eliminating 40–80 km city travel."
            ])

    # =========================================================================
    # SLIDE 3: TECHNICAL APPROACH
    # =========================================================================
    s3 = prs.slides[2]
    for shape in s3.shapes:
        if shape.has_text_frame and "TECHNICAL APPROACH" in shape.text_frame.text:
            shape.text_frame.paragraphs[0].font.size = Pt(20)
            shape.text_frame.paragraphs[0].font.bold = True
            shape.text_frame.paragraphs[0].font.color.rgb = C_NAVY
        elif shape.has_text_frame and "Technologies to be used" in shape.text_frame.text:
            tf = shape.text_frame
            tf.clear()
            tf.word_wrap = True

            def add_tech_layer(title, desc):
                p_head = tf.add_paragraph()
                p_head.space_before = Pt(4)
                p_head.space_after = Pt(2)
                r_head = p_head.add_run()
                r_head.text = title
                r_head.font.bold = True
                r_head.font.size = Pt(11)
                r_head.font.color.rgb = C_BLUE

                for d in desc:
                    p_d = tf.add_paragraph()
                    p_d.space_after = Pt(2)
                    r_d = p_d.add_run()
                    r_d.text = f"• {d}"
                    r_d.font.size = Pt(9.5)
                    r_d.font.color.rgb = C_DARK

            add_tech_layer("1. Frontend Client & Assistive Voice Engine", [
                "Cross-Platform PWA: React / Flutter PWA running on low-cost tablets and smartphones.",
                "Voice AI Integration: Bhashini Speech-to-Text & Text-to-Speech APIs for real-time Marathi, Gondi, and Hindi.",
                "Offline-First Data Layer: Embedded SQLite & WatermelonDB with Conflict-Free Replicated Data Types (CRDTs) to prevent data loss in 0G/2G dead zones."
            ])
            add_tech_layer("2. Telehealth, Media & Real-Time Gateway", [
                "Low-Bandwidth WebRTC: LiveKit WebRTC engine dynamically dropping to 15 kbps adaptive Opus audio during signal drops.",
                "Emergency SOS Broker: WebSocket-driven GPS dispatch engine connected to Maharashtra 108 Emergency network.",
                "Backend Architecture: High-throughput FastAPI (Python) & Node.js microservices with Redis queues."
            ])
            add_tech_layer("3. National Digital Health & Supply Chain Infrastructure", [
                "ABDM & FHIR Compliance: Interoperable HL7 / FHIR R4 clinical JSON schemas linked with Ayushman Bharat ABHA IDs.",
                "Inventory Ledger: Real-time PostgreSQL 16 + TimescaleDB tracking pharmaceutical stock levels and expiration alerts."
            ])

    # =========================================================================
    # SLIDE 4: FEASIBILITY AND VIABILITY
    # =========================================================================
    s4 = prs.slides[3]
    for shape in s4.shapes:
        if shape.has_text_frame and "FEASIBILITY AND VIABILITY" in shape.text_frame.text:
            shape.text_frame.paragraphs[0].font.size = Pt(20)
            shape.text_frame.paragraphs[0].font.bold = True
            shape.text_frame.paragraphs[0].font.color.rgb = C_NAVY
        elif shape.has_text_frame and "Analysis of the feasibility" in shape.text_frame.text:
            tf = shape.text_frame
            tf.clear()
            tf.word_wrap = True

            def add_feasibility_block(title, points):
                p_head = tf.add_paragraph()
                p_head.space_before = Pt(4)
                p_head.space_after = Pt(2)
                r_head = p_head.add_run()
                r_head.text = title
                r_head.font.bold = True
                r_head.font.size = Pt(11)
                r_head.font.color.rgb = C_BLUE

                for pt in points:
                    p_pt = tf.add_paragraph()
                    p_pt.space_after = Pt(2)
                    r_pt = p_pt.add_run()
                    r_pt.text = f"• {pt}"
                    r_pt.font.size = Pt(9.5)
                    r_pt.font.color.rgb = C_DARK

            add_feasibility_block("1. Operational & Economic Feasibility", [
                "Cost-Effective Micro-Hub Clustering: Setting up 1 Outskirts Diagnostic & Supply Hub for every 3–5 villages reduces infrastructure CapEx by 70% compared to building full pharmacies in every hamlet.",
                "Utilizes Existing Cadres: Leverages Gram Panchayat kiosks and existing ASHA / health volunteers for daily operation."
            ])
            add_feasibility_block("2. Potential Challenges & Risk Mitigation Strategies", [
                "Challenge: Poor/Zero Cellular Connectivity in Tribal Valleys (Gadchiroli/Melghat)\n  ➜ Mitigation: 100% Offline-First architecture; queue consultations locally and auto-sync on signal restoration.",
                "Challenge: High Digital & Language Illiteracy among Villagers\n  ➜ Mitigation: Zero-typing pictorial interface + regional voice prompts + 1-on-1 human agent guidance fallback.",
                "Challenge: Medicine Expiration & Cold-Chain Failure\n  ➜ Mitigation: Outskirts Hubs equipped with solar-backed refrigeration and real-time inventory telemetry to prevent stockouts."
            ])
            add_feasibility_block("3. Phased Rollout Roadmap", [
                "Phase 1 (M1-M3): Pilot 10 Villages + 2 Outskirts Hubs in Gadchiroli/Melghat | Phase 2 (M4-M8): Scale across 5 High-Priority Rural Districts | Phase 3 (M9-M12): Statewide 36-District Rollout."
            ])

    # =========================================================================
    # SLIDE 5: IMPACT AND BENEFITS
    # =========================================================================
    s5 = prs.slides[4]
    for shape in s5.shapes:
        if shape.has_text_frame and "IMPACT AND BENEFITS" in shape.text_frame.text:
            shape.text_frame.paragraphs[0].font.size = Pt(20)
            shape.text_frame.paragraphs[0].font.bold = True
            shape.text_frame.paragraphs[0].font.color.rgb = C_NAVY
        elif shape.has_text_frame and "Potential impact on the target audience" in shape.text_frame.text:
            tf = shape.text_frame
            tf.clear()
            tf.word_wrap = True

            def add_impact_block(title, points):
                p_head = tf.add_paragraph()
                p_head.space_before = Pt(4)
                p_head.space_after = Pt(2)
                r_head = p_head.add_run()
                r_head.text = title
                r_head.font.bold = True
                r_head.font.size = Pt(11)
                r_head.font.color.rgb = C_BLUE

                for pt in points:
                    p_pt = tf.add_paragraph()
                    p_pt.space_after = Pt(2)
                    r_pt = p_pt.add_run()
                    r_pt.text = f"• {pt}"
                    r_pt.font.size = Pt(9.5)
                    r_pt.font.color.rgb = C_DARK

            add_impact_block("1. Direct Quantitative Impact on Rural Beneficiaries", [
                "70% Reduction in Diagnostic Travel: Eliminates grueling 40–80 km journeys to city centers for basic diagnostic tests and pharmaceutical pickup.",
                "100% Inclusive for Illiterate Citizens: Spoken regional prompts and visual cues empower elderly and tribal citizens to access healthcare independently.",
                "< 15 Minute Emergency Response: Direct 1-touch SOS coordinates immediate ambulance and first-responder dispatch from the outskirts hub."
            ])
            add_impact_block("2. Broader Socio-Economic & Public Health Benefits", [
                "Zero Lost Prescriptions & Care Continuity: FHIR-compliant ABHA records ensure past test results and diagnoses travel seamlessly with the patient across facilities.",
                "Economic Protection: Saves rural families thousands in out-of-pocket transportation and wage losses from missed work days.",
                "Epidemic Early Warning: Aggregated diagnostic test data at cluster hubs provides automated spatial detection of malaria, dengue, and water-borne disease outbreaks."
            ])

    # =========================================================================
    # SLIDE 6: RESEARCH AND REFERENCES
    # =========================================================================
    s6 = prs.slides[5]
    for shape in s6.shapes:
        if shape.has_text_frame and "RESEARCH" in shape.text_frame.text:
            shape.text_frame.paragraphs[0].font.size = Pt(20)
            shape.text_frame.paragraphs[0].font.bold = True
            shape.text_frame.paragraphs[0].font.color.rgb = C_NAVY
        elif shape.has_text_frame and "Details / Links" in shape.text_frame.text:
            tf = shape.text_frame
            tf.clear()
            tf.word_wrap = True

            def add_ref_block(title, points):
                p_head = tf.add_paragraph()
                p_head.space_before = Pt(4)
                p_head.space_after = Pt(2)
                r_head = p_head.add_run()
                r_head.text = title
                r_head.font.bold = True
                r_head.font.size = Pt(11)
                r_head.font.color.rgb = C_BLUE

                for pt in points:
                    p_pt = tf.add_paragraph()
                    p_pt.space_after = Pt(2)
                    r_pt = p_pt.add_run()
                    r_pt.text = f"• {pt}"
                    r_pt.font.size = Pt(9.5)
                    r_pt.font.color.rgb = C_DARK

            add_ref_block("1. Government Health Data & Ground Reality Studies", [
                "National Family Health Survey (NFHS-5) Maharashtra: Data on rural maternal mortality, tribal access barriers in Gadchiroli/Nandurbar, and referral dropout rates.",
                "Rural Health Statistics (RHS 2022-23), Ministry of Health & Family Welfare (MoHFW): Analysis of sub-centre shortfalls and pharmaceutical supply chain bottlenecks.",
                "National Health Mission (NHM) Maharashtra: Guidelines on ASHA assisted care models and 108 Emergency Medical Services integration."
            ])
            add_ref_block("2. Technical Standards & Public Digital Infrastructure", [
                "Ayushman Bharat Digital Mission (ABDM): Guidelines for ABHA ID linkage, Health Information Exchange & Consent Manager (HIE-CM), and HL7 / FHIR R4 schema compliance.",
                "Bhashini (National Language Translation Mission): Technical specifications for open-source Indic speech-to-text and text-to-speech models.",
                "WHO Telemedicine & Digital Health Guidelines for Low-Resource Settings: Protocols for low-bitrate clinical audio triage and community health worker ergonomics."
            ])

    # Update Team Name Placeholder across slides 2-6
    for slide_idx in range(1, 6):
        slide = prs.slides[slide_idx]
        for shape in slide.shapes:
            if shape.has_text_frame and "Your Team Name" in shape.text_frame.text:
                shape.text_frame.text = "ArogyaMitr"
                shape.text_frame.paragraphs[0].font.size = Pt(10)
                shape.text_frame.paragraphs[0].font.bold = True
                shape.text_frame.paragraphs[0].font.color.rgb = C_BLUE

    # Remove Slide 7 (Instructions slide) if present so we keep exact 6 slides limit
    if len(prs.slides) > 6:
        rId = prs.slides._sldIdLst[6].rId
        prs.part.drop_rel(rId)
        del prs.slides._sldIdLst[6]
        print("Removed Slide 7 (Instruction slide) to comply with the 6-slide rule.")

    out_file = r"C:\Users\Lenovo\Downloads\ArogyaMitr_SIH2026_Idea_Presentation.pptx"
    prs.save(out_file)
    print(f"Successfully generated populated PPTX: {out_file}")

    scratch_file = r"C:\Users\Lenovo\.gemini\antigravity\scratch\mahahealth_connect\ArogyaMitr_SIH2026_Idea_Presentation.pptx"
    prs.save(scratch_file)

if __name__ == "__main__":
    populate_sih_template()
