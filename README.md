# Team-Techtonic-SIH

## 🔍 TAG & FIND — Campus Lost & Found Intelligence System

> **Smart India Hackathon 2026 (NITK Internal Selection)**  
> *Never lose what matters. Find what others lost.*

> **An open-source AI platform using CLIP computer vision to match lost items and verify ownership before revealing finder contact details—stopping fake claims and campus spam instantly.

## 📌 Problem & Hackathon Track
* **Track:** Campus-related Problem Statement
* **Problem Title:** Campus Lost-and-Found Intelligence System
* **Target Institution:** NITK Surathkal

## 🚨 The Problem
Every year on campus, 1,000+ items (laptops, student IDs, keys, electronics) are lost. Current recovery relies on chaotic WhatsApp groups, physical notice boards, or manual registers. This results in:
1. High risk of false/fraudulent claims.
2. Zero privacy protection for finders (spam calls & privacy risks).
3. Low recovery rate due to unstructured search.

## 💡 Our Solution
* **Finders** TAG an item with a photo and location.
* **Losers** FIND items via semantic search and prompt descriptions.
* **AI Engine** verifies ownership in real time before revealing finder contact info.

## ✨ Core Features

* 🤖 **AI Claim Verification:** CLIP multimodal model calculates semantic vector similarity between text descriptions and found images.
* 🚦 **Smart Risk Meter:**
  * 🟢 **LOW RISK (Cap, Bottle, Umbrella):** Direct claim access.
  * 🔴 **HIGH RISK (Laptop, Phone, Wallet, ID):** Requires a high AI match score + physical/ID verification proof.
* 🔒 **Privacy First:** Finder phone numbers remain hidden until AI verification succeeds.
* 📸 **Visual Feed:** Instagram-style scrollable catalog of found items on campus.

 ## 📌 System Flow 
 mermaid
 graph TD
    A[Upload Item] --> B[(Database)]
    B --> C[CLIP AI Matching]
    C --> D[Search / Claim]
    D --> E[Verification]
    E --> F[Safe Contact]
    F --> G[Generate QR Code]
    G --> H[Feedback and Suggestions]

├── frontend/     # User Interface & Visual Feed
├── backend/      # Users, Items & Claims Logic
├── ai/           # Matching & Similarity Score Algorithms
└── database/     # User & Item Information Storage

### Roles

HEMAN    - FRONT END DEVELOPER
AARUSH   - FRONT END DEVELOPER
BADHRISH - BACK END DEVELOPER
TRIJAL   - BACK END DEVELOPER
ANUSHKA  - PPT AND PRESENTATION
AYUSH    - PPT AND PRESENTATION
 



