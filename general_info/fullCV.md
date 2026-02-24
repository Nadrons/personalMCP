
# Nadrons – Data Scientist – Physics MSci (Hons)
**Location:** UK
**LinkedIn:** -

---
## Personal Statement

Data Engineer and Data Scientist with expertise in building scalable Azure and Databricks data platforms, MLOps infrastructure, and end-to-end reporting solutions. Proven track record delivering complex projects from concept to production, with focus on self-service analytics, data governance, and LLM-powered applications. I have extensive experience with stakeholder communication, project management and self-directed working to transform “it would be nice if…” conversations into actionable products.

  

---

  

## Education

  

| Period | Institution | Qualification |
|--------|-------------|---------------|
| 2012 – 2016 | University of Nottingham | MSci Hons Physics – *First Class Honours* |
| 2011 – 2012 | University of Nottingham | Engineering Foundation Degree – *2:1* |
---

  

## Relevant Employment

  

### 2022 – Present: Black Duck – Staff Data Scientist / Data Engineer


*Black Duck is a cyber-security firm focused on application security. I fill a dual role, building enterprise-scale data infrastructure and implementing ML solutions.*

#### Key Projects & Achievements


**DuckBI: Building An Enterprise Data Lakehouse & Agentic Analytics Platform**

Led the architecture and implementation of an enterprise-scale data lakehouse in response to a CPTO mandate to consolidate siloed data across seven product lines (SAST and DAST tools) within a three-month deadline. As part of a three-person data science team, delivered a production system 30 days ahead of schedule with all stretch goals completed. The lakehouse now serves C-suite executives and dozens of daily users for critical business intelligence.

*Data Infrastructure & Integration:*
-   Designed and implemented medallion architecture (bronze/silver/gold) using Databricks Unity Catalog with Azure storage backend.
-   Integrated data from seven main product lines, federating sensitive (Salesforce) and prohibitively large datasets (scan request/response pairs) from existing Snowflake and MongoDB instances.
-   Built automated validation pipelines with Kubernetes-based Airflow for data egress from secure, VPN-walled environments.
-   Developed automated validation system allowing prepped data with correct backlog entries to be processed without new pipeline development.

*Data Governance & Security:*
-   Collaborated with security, legal, and DBA teams to establish comprehensive "Data Mobility Policy" defining data classification framework (Public/Internal/Confidential/Restricted).
-   Implemented data governance ensuring compliance and appropriate access controls across cross-functional stakeholders.

*Data Products & Analytics:*
-   Architected three-tier DBT data product hierarchy implemented as scheduled jobs:
    -   **Level 0:** Product-specific tables with cross-product nomenclature and data definitions
    -   **Level 1:** Cross-product unified tables enabling portfolio-wide analysis
    -   **Level 2:** Bespoke analytics tables for specialized business and technical questions
-   Worked directly with stakeholders and data stewards from various product lines to build out data products.

*LLM-Powered Analytics & User Enablement:*
-   Built LLM-powered Teams chatbot (@DuckBI) using Copilot Studio and custom MCP server for natural language queries against data products.
-   Deployed MCP server within Innovation Zone (Kubernetes service) with Databricks service principal access to data products and glossary.
-   Integrated bot with Black Duck documentation via company website for comprehensive context.
-   Established and documented "public" Databricks workspace accessible to all business users.
-   Designed and delivered workshops training users on data exploration and dashboarding capabilities.


**Telemetry Self-Service Portal**

As a complement to DuckBI, I built an end-to-end self-service platform enabling users within the business to post and manage their own datasets. Users could register against our portal app with their EntraIDs, generate API keys and begin posting data immediately.

-   Architected serverless Azure pipeline: APIM (user auth/rate limiting), Functions (for initial data enrichment), Event Hubs (stream ingestion), Stream Analytics (filtering), Databricks (processing to catalog)
-   Developed OAuth-protected Flask app for self-registration, schema management, payload validation, and real-time monitoring
-   Created governance model, defining data owner rights and change management.
-   Achieved zero-touch onboarding for most users; currently supporting active users across departments with data integrated into retention analytics.
    

**MLOps & LLM Implementation**

-   Replaced legacy NLP models with fine-tuned transformers model trained on decades of scan data
-   Implemented automated retraining pipeline as new data becomes available or drift is detected
---

### 2016 – 2022: Weatherford International Ltd. - Research Physicist / Data Analyst

  
Oilfield services company specializing in oil well exploration. Applied data science and signal processing to well logging data, managing interdepartmental R&D projects from conception to field deployment.

#### Key Responsibilities

-   Designed signal processing and ML pipelines for multi-sensor well logging systems (could be 20+ concurrent devices).
-   Implemented CNNs and LSTMs to aggregate measured signals into descriptive geological models.
-   Led data archaeology project: aggregated and cleaned legacy datasets from early 2000s for holistic analysis.

#### Relevant Training

- MathWorks Deep Learning with MATLAB
- PRINCE2 Project Management
- Writing Point scientific writing

  

---
## Technical Skills


| | |
|---|---|
| **Data Engineering & Infrastructure**<br>• Azure: Event Hubs, Stream Analytics, Functions, APIM<br>• Databricks: Unity Catalog, Spark SQL, Delta Lake<br>• Orchestration: Airflow, Kubernetes, DBT<br>• Platforms: Snowflake, MongoDB (federation)<br>• Patterns: Medallion architecture, data lakehouse, federated systems | **Machine Learning & AI**<br>• LLM fine-tuning, deployment, and MLOps<br>• Deep learning: CNNs, LSTMs (time-series, NLP)<br>• Automated model lifecycle management <br>• Model serving via AzureML and Databricks |
| **Development & DevOps**<br>• Languages: Python, SQL, MATLAB<br>• Frameworks: Flask, Copilot Studio, MCP servers<br>• CI/CD, Linux, Windows | **Data Governance & Security**<br>• Data classification and compliance<br>• OAuth, API key management<br>• Cross-functional collaboration |
| **Soft Skills**<br>• Experienced in technical writing and presentation<br>• Project leadership under tight deadlines<br>• Regularly responding to PR requests<br>• Experienced user of Claude and pals| |

  

---
## Further Information and Interests

| **Professional** | **Personal** |
|------------------|--------------|
| • Published author in *SPE Journal*<br>• Full UK driving license | • DIY enthusiast<br>• Squash player, regular gym-goer |
---

  
## Referees
  
References available on request.