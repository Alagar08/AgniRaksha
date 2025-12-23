
# 🔥 AgniRaksha  
### Edge AI & IoT-Powered Predictive Safety Platform for Fireworks MSMEs  
**“Seconds that save lives.”**

AgniRaksha is a solar-powered, edge-AI enabled safety system designed
to **predict fire and explosion risks before they occur** in rural
firecracker MSMEs. Unlike traditional alarms, AgniRaksha acts **before
disaster**, giving workers precious seconds to escape and automatically
calling emergency services.

---

## 🚨 Problem Statement

Small fireworks MSMEs face severe safety issues:
- Fire alarms react **after** fire starts
- No operation during power cuts
- No automatic emergency calling
- Imported SCADA systems are expensive
- No AI-based prediction for rural industries

---

## 💡 Solution Overview

AgniRaksha combines:
- Low-cost industrial sensors  
- Edge AI for **early risk prediction**  
- Solar power for uninterrupted operation  
- LoRa + GSM for offline-first communication  

### Key Actions When Risk Is High:
- 🔊 Sirens warn workers instantly  
- 📱 SMS alerts to owners (local language)  
- 📞 Auto-call to nearby fire station & police  
- 📊 Live risk dashboard for owners  

---

## 🧠 System Architecture

**Sensors → ESP32 → LoRa → Edge AI (Jetson/RPi) → Alerts + Dashboard**

Sensors monitored:
- Temperature
- Gas (flammable gases)
- Humidity

---

## ✨ Unique Features

- Predicts danger **before fire**
- Works during power cuts (solar powered)
- Auto emergency calling (fire & police)
- Local-language alerts
- Affordable for rural MSMEs
- Offline-first design

---

## 🛠️ Technology Stack

| Layer | Technology |
|-----|-----------|
| Sensors | Temperature, Gas, Humidity |
| MCU | ESP32 |
| Communication | LoRa, GSM |
| Edge AI | Python, Scikit-Learn |
| Dashboard | Flask |
| Power | Solar + Battery |

---

## 📂 Repository Structure

Refer to project folders:
- `firmware/` – ESP32 & LoRa code  
- `edge_ai/` – AI model training & inference  
- `communication/` – GSM, siren logic  
- `dashboard/` – Web UI  
- `docs/` – Diagrams & proposal  

---

## 🚀 Deployment (Quick Start)

```bash
git clone https://github.com/yourusername/AgniRaksha.git
cd AgniRaksha
python3 dashboard/app.py
