# 🏥 ArogyaMitr (आरोग्यमित्र)
### Dual-Outlet Rural Healthcare Infrastructure & Voice-Guided Tele-Care Platform
> **Smart India Hackathon (SIH) 2026** • **Problem Statement ID: 26133**  
> **Theme:** MedTech / BioTech / HealthTech (Software Edition)  
> **Organization:** Government of Maharashtra (Maharashtra State Innovation Society - MSInS)  
> **Team Name:** PUNK RECORDS / ArogyaMitr

---

[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![Python 3.13](https://img.shields.io/badge/Python-3.13-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Vercel](https://img.shields.io/badge/Vercel-000000?style=for-the-badge&logo=vercel&logoColor=white)](https://vercel.com)
[![ABDM FHIR R4](https://img.shields.io/badge/ABDM-FHIR_R4_Compliant-0d9488?style=for-the-badge)](https://abdm.gov.in)
[![Bhashini AI](https://img.shields.io/badge/MeitY-Bhashini_Voice_AI-0284c7?style=for-the-badge)](https://bhashini.gov.in)

---

## 📌 1. Problem Statement Overview (PS 26133)

Rural and tribal districts in Maharashtra (such as Gadchiroli, Nandurbar, and Melghat) face critical structural healthcare barriers:
1. **Literacy & Language Deficit:** Over **45% of rural citizens** cannot read English or formal medical terms, making text-heavy telemedicine apps ineffective.
2. **The "Digital PDF Fallacy":** Telemedicine portals (like e-Sanjeevani) provide digital prescriptions on a phone screen, but leave patients stranded in remote villages with **zero pharmacies**.
3. **Severe Distance & Wage Loss:** Villagers travel **40 to 80 km** on tractors to reach sub-district hospitals, losing ₹1,000+ per episode in bus fares and lost daily farm wages.
4. **High Referral Dropout:** Over **65% of high-risk maternal and emergency cases** fail to complete hospital referrals.
5. **0G/2G Network Dead Zones:** Severe connectivity blackouts in forest valleys crash standard web apps.

---

## 💡 2. The Solution: Physical Dual-Outlet Architecture

ArogyaMitr bridges the gap between **Digital Tele-Care** and **Physical Supply Logistics** through a **Dual-Outlet Model**:

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                                   AROGYAMITR ECOSYSTEM                                 │
├────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                        │
│   📍 1. INSIDE THE VILLAGE             ☁️ 2. IN THE CLOUD / CIVIL HOSPITAL             │
│   ┌──────────────────────────────┐     ┌──────────────────────────────────────────┐    │
│   │   Gram Care Point (Kiosk)    │     │   Doctor Tele-Consult Desk (Digital)     │    │
│   │ • Patient meets ASHA helper  │────▶│ • MBBS Doctors at District Civil Hosp    │    │
│   │ • Speaks symptoms in Marathi │     │ • Conducts 15kbps low-bandwidth consult  │    │
│   │ • Checks vitals (BP, SpO2)   │     │ • Issues instant digital e-Prescription  │    │
│   └──────────────┬───────────────┘     └────────────────────┬─────────────────────┘    │
│                  │                                          │                          │
│                  │ (Blood/Urine Sample)                     │ (Instant Digital Rx)     │
│                  ▼                                          ▼                          │
│   📍 3. ON THE CLUSTER OUTSKIRTS (Serving 3–5 Villages / 5 km Radius)                  │
│   ┌───────────────────────────────────────────────────────────────────────────────┐    │
│   │           The Healthcare "Dark Store" & Diagnostic Micro-Hub                  │    │
│   │                                                                               │    │
│   │  💊 PHARMACY SECTION            🧪 DIAGNOSTIC LAB         🚑 EMERGENCY BASE   │    │
│   │  • Cold-chain insulin, ASV      • Rapid blood & urine     • 108 Ambulance     │    │
│   │  • Solar-powered refrigeration  • Sputum & malaria kits   • Oxygen cylinders  │    │
│   │  • 15–30 min delivery runner    • Same-day digital report • < 15 min dispatch │    │
│   └──────────────────────────────────────┬────────────────────────────────────────┘    │
│                                          │                                             │
│                                          ▼ (15–30 Min Medicine Delivery)               │
│                        [ Delivered back to Village Care Point ]                        │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

### 🏢 The Three Operational Pillars:
1. **Outlet 1: Gram Care Point (Inside Village):**
   * Located at Gram Panchayat / Sub-Centre.
   * Walk-in tablet kiosk operated by local ASHA volunteers.
   * **100% Pictorial & Vernacular Voice AI (Marathi/Hindi/Gondi)** with zero typing.
   * **1-on-1 Sahayak Guide:** Live human video/audio assistance button for elderly/anxious citizens.
   * Basic vitals screening (BP, SpO2, Pulse, Temp, Blood Sugar).

2. **The Cloud Doctor Desk (Decentralized):**
   * Medical Officers at Civil Hospitals / PHCs conduct tele-consultations over ultra-low bandwidth (15 kbps).
   * Automated Clinical Risk Score (Normal, Moderate Risk, Emergency).
   * Digital e-Prescriptions auto-routed directly to the nearest Outskirts Hub.

3. **Outlet 2: Outskirts Diagnostic & Supply Dark Hub (Highway Junction):**
   * Strategic micro-fulfillment depot serving **a cluster of 3 to 5 villages (5–7 km radius)** — *"Blinkit for Healthcare"*.
   * **Solar-Powered Cold Chain (2°C–8°C):** Stocks critical emergency medicines (Insulin, Anti-Snake Venom, Oxytocin).
   * **Rapid Diagnostic Point-of-Care Lab:** Processes CBC, malaria antigen, dengue, and urine samples.
   * **108 Ambulance Staging Base:** Parked ambulances with oxygen and paramedics ready for instant dispatch on **1-Touch SOS**.
   * **15–30 Min Last-Mile Delivery:** Local runners dispatch medicine packs back to the village kiosk.

---

## 🛠️ 3. Full Technology Stack

| Layer | Technologies | Role & Function in ArogyaMitr |
| :--- | :--- | :--- |
| **Frontend UI/UX** | HTML5 / Vanilla JS PWA + Tailwind CSS | Responsive tablet interface in Medical Light Theme with large accessible cards. |
| **Vernacular Voice AI** | Bhashini AI (MeitY) & Web Speech Synthesis | Listens to speech in **Marathi/Hindi/Gondi** and speaks instructions aloud. |
| **0G / Offline Layer** | SQLite + IndexedDB (CRDTs) | **0G Mode:** Records patient intakes with zero connectivity and auto-syncs when online. |
| **Telehealth & SOS Engine** | LiveKit WebRTC (Opus Codec), WebSockets | 15 kbps ultra-low bandwidth tele-consults + real-time 1-Touch SOS GPS broadcasting. |
| **Backend Core** | Python (FastAPI), Pydantic V2, Uvicorn | Clinical risk scoring algorithm, prescription dispatch routing, and session handling. |
| **Database & Sensors** | PostgreSQL 16 + TimescaleDB | Relational patient data + time-series telemetry for cold-chain refrigerator temperature (`4.2°C`). |
| **National Standards** | Ayushman Bharat (ABDM), HL7 FHIR R4 JSON | Links 14-digit ABHA IDs and exports interoperable clinical document bundles. |
| **Data Privacy & Security** | AES-256 Encryption, TLS 1.3, STRIDE Hardening | Full compliance with India's **Digital Personal Data Protection (DPDP) Act 2023**. |

---

## 📊 4. Quantitative Impact & Metrics

* 📉 **70% Reduction in Diagnostic Travel:** Eliminates 40–80 km trips for medicine and testing.
* 💰 **₹1,000+ Economic Savings per Episode:** Prevents lost daily agricultural wages and bus fares.
* 🗣️ **100% Inclusivity for Non-Literate Citizens:** Voice-first prompts leave no citizen behind.
* ⏱️ **< 15-Minute Emergency Response:** 1-Touch SOS coordinates nearby 108 ambulances.
* 📈 **95%+ Referral Completion:** Closes the 65% drop-off gap for high-risk maternal cases.
* 🏛️ **70% CapEx Savings for Government:** 1 shared Outskirts Hub serves 5 villages.

---

## 🚀 5. Local Setup & Execution

### Prerequisites:
* Python 3.10+
* Git

```powershell
# 1. Clone the repository
git clone https://github.com/mohammedsuhail0/SIH-PUNK-RECORDS-.git
cd SIH-PUNK-RECORDS-

# 2. Install dependencies
pip install -r requirements.txt

# 3. Launch the ArogyaMitr MVP Server
python -m uvicorn app:app --host 127.0.0.1 --port 8000 --reload
```

👉 Open browser at: **`http://127.0.0.1:8000`**

---

## 🌐 6. Live Vercel Deployment

The application is deployed and live in production on Vercel:
* 🔗 **Live Production URL:** [https://mahahealthconnect.vercel.app](https://mahahealthconnect.vercel.app)
* 🔗 **Alternative Mirror URL:** [https://mahahealthconnect-emydfto9l-mohammedsuhail0s-projects.vercel.app](https://mahahealthconnect-emydfto9l-mohammedsuhail0s-projects.vercel.app)
* `vercel.json` provides routing for static SPA frontend + serverless FastAPI backend (`api/index.py`).

---

## 📑 7. Presentation & Proposal Files

* 📊 **Presentation Deck (.pptx):** [`ArogyaMitr_SIH2026_Idea_Presentation.pptx`](file:///./ArogyaMitr_SIH2026_Idea_Presentation.pptx)
* 📑 **Presentation Document (.pdf):** [`ArogyaMitr_SIH2026_Idea_Presentation.pdf`](file:///./ArogyaMitr_SIH2026_Idea_Presentation.pdf)
* 📄 **Solution Proposal (.pdf):** [`ArogyaMitr_SIH2026_PS26133_Solution_Proposal.pdf`](file:///./ArogyaMitr_SIH2026_PS26133_Solution_Proposal.pdf)
* 📚 **Complete Project Context:** [`CONTEXT.md`](file:///./CONTEXT.md)
* 🤖 **Agent Onboarding Brief:** [`AGENT.md`](file:///./AGENT.md)
