# 🎯 Keylogger Control Panel – Projet pédagogique

> **⚠️ Usage strictement éducatif**  
> Ce projet est fourni uniquement dans un cadre d’étude ou de challenge contrôlé.  
> **N’utilisez jamais ce code pour surveiller une machine ou une personne sans consentement explicite et légal.**

---

## 📄 Présentation

Ce dépôt est un exemple pédagogique d’un système “keylogger + dashboard web” pour initier à la sécurité offensive/forensics :
- **Côté “VICTIME”** : un script Python enregistre les frappes clavier et les transmet à distance (TCP).
- **Côté “ATTAQUANT”** : un serveur reçoit, stocke et affiche via un dashboard web toutes les frappes reçues en temps réel.

---

## 📦 Structure du projet

```
keylogger/
├── ATTAQUANT/
│   ├── server_receiver.py      # Serveur TCP : reçoit et stocke les logs par UUID de victime
│   └── dashboard_simple.py     # Dashboard Flask : visualiser les logs reçus
├── VICTIME/
│   └── commande_client.py      # Script keylogger à lancer sur la machine cible
├── logs_keylogger/             # Dossier généré pour les logs (par uuid)
├── README.md
```

---

## 🚦 Fonctionnement détaillé

- Chaque victime s’identifie par un UUID unique, utilisé pour séparer les logs.
- Les frappes clavier sont enregistrées localement ET exfiltrées au serveur central via TCP.
- Le serveur stocke chaque frappe reçue dans un fichier dédié (`logs_keylogger/<uuid>_keylog.txt`).
- Un dashboard web (`dashboard_simple.py`) permet d’afficher en live chaque log reçu.

---

## 📋 Installation

### **Pré-requis**
- Python 3.8 ou plus
- pip
- Un navigateur web pour le dashboard

### **Clonage**
```bash
git clone https://github.com/votreuser/votre-repo-keylogger.git
cd votre-repo-keylogger
```

### **Dépendances**
```bash
pip install flask pynput
```
_`pynput` n'est requis que côté “victime”_

---

## 🛠️ Lancement

### 1️⃣ — **Démarrer le serveur collecteur (ATTAQUANT)**
```bash
cd ATTAQUANT
python3 server_receiver.py
```
- Le serveur reste en écoute sur `0.0.0.0:5001`.
- Les fichiers de logs seront créés automatiquement dans `../logs_keylogger/`.

### 2️⃣ — **Démarrer le dashboard web (ATTAQUANT)**
Dans un second terminal :
```bash
python3 dashboard_simple.py
```
- Ouvre [http://localhost:8080/](http://localhost:8080/) dans ton navigateur.

### 3️⃣ — **Lancer le keylogger sur la victime (VICTIME)**
- Installe la dépendance si nécessaire :
  ```
  pip install pynput
  ```
- Modifie l’IP du serveur (`SERVER_IP`) par celle de la machine “ATTAQUANT” dans `commande_client.py` :
  ```python
  SERVER_IP = "ip_de_la_machine_attaquante"
  ```
- Démarre la capture :
  ```bash
  python3 commande_client.py
  ```

---

## 🚨 Section Commandes et Automatisation

- Le script **client** (`commande_client.py`) démarre automatiquement la capture dès exécution.
- Pour stopper la capture : interrompre le script (Ctrl+C) ou le tuer côté système.
- Possibilité d’ajouter des commandes réseau “start/stop” centralisées (voir TODO dans le code pour extensions PRO).

---

## 🎨 Fonctionnalités

- Visualisation live des logs (dashboard Flask)
- Logs séparés par victime (UUID)
- Structure claire prête à étendre (multi-victimes, gestion avancée...)

---

## 🧑‍🎓 Exemple Type de log et arborescence

Une frappe envoyée par la victime :  
```json
{"uuid": "e4595c5c-2e2f-4867-a196-33e441a0e8f3", "key": "a"}
```
Se retrouve dans :
```
logs_keylogger/
└── e4595c5c-2e2f-4867-a196-33e441a0e8f3_keylog.txt
```

---

## 🛡️ Sécurité & Éthique

- **Usage réservé à l’apprentissage encadré/cours/lab.**
- **N’utilisez JAMAIS ce code à l’insu des utilisateurs !**
- Respectez toutes les lois locales sur le test d’intrusion, le consentement et la vie privée.
- Toute utilisation contraire à l’éthique, en production, ou dans le cadre d’une activité non autorisée est **strictement interdite**.

---

## 💡 Conseils pédagogiques / extensions

- Ajoutez une section multi-victimes sur le dashboard.
- Ajoutez un système d’envoi de commandes à distance (start/stop, etc.).
- Étendez pour supporter HTTP POST au lieu de TCP si besoin.
- Ajoutez l’enregistrement côté serveur des timestamps, IP publiques, etc.

---

## 📝 Licence

> **Projet à but strictement éducatif.**
>  
> Toute utilisation malveillante expose son auteur à des poursuites.  
>  
> © 2025, projet keylogger pédagogique – libre personnalisation, toute diffusion doit s’accompagner de ce présent avertissement.

---

## ❓ Contact / Contribuer

Pour toute question pédagogique ou suggestion, merci d’ouvrir une issue GitHub.

---

**On vous fait confiance : restez dans l’éthique et la légalité !**
